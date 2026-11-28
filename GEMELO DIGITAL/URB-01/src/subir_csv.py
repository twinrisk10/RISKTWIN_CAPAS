import csv
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
CARPETA_DATOS = Path(__file__).parent / "datasets"

# Orden de carga respetando llaves foráneas (prediccion depende de modelo_riesgo)
LOTE_BASE = [
    ("modelo_riesgo", "modelo_riesgo_rows.csv"),
    ("clima_diario",  "clima_diario_rows.csv"),
    ("feriado",       "feriado_rows.csv"),
    ("prediccion",    "prediccion_rows.csv"),
]

# Cambia a True SOLO si quieres crear/cargar también las vistas como tablas de respaldo (stg_...)
CARGAR_STAGING_VISTAS = False
LOTE_STAGING = [
    ("stg_v_panel_semanal_zona", "v_panel_semanal_zona_rows.csv"),
    ("stg_v_prediccion_zona",    "v_prediccion_zona_rows.csv"),
]


def obtener_pk(cur, nombre_tabla: str) -> list[str]:
    cur.execute(
        """
        SELECT kcu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
          ON tc.constraint_name = kcu.constraint_name
         AND tc.table_schema = kcu.table_schema
        WHERE tc.constraint_type = 'PRIMARY KEY'
          AND tc.table_schema = current_schema()
          AND tc.table_name = %s
        ORDER BY kcu.ordinal_position;
        """,
        (nombre_tabla,),
    )
    return [fila[0] for fila in cur.fetchall()]


def tiene_identity_always(cur, nombre_tabla: str) -> bool:
    cur.execute(
        """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.columns
            WHERE table_schema = current_schema()
              AND table_name = %s
              AND identity_generation = 'ALWAYS'
        );
        """,
        (nombre_tabla,),
    )
    return bool(cur.fetchone()[0])


def sincronizar_secuencia(cur, nombre_tabla: str, pk_cols: list[str]) -> None:
    if len(pk_cols) != 1:
        return
    pk = pk_cols[0]
    cur.execute("SELECT pg_get_serial_sequence(%s, %s);", (nombre_tabla, pk))
    seq = cur.fetchone()[0]
    if seq:
        cur.execute(
            sql.SQL("SELECT setval(%s, COALESCE((SELECT MAX({}) FROM {}), 1));").format(
                sql.Identifier(pk),
                sql.Identifier(nombre_tabla),
            ),
            (seq,),
        )


def cargar_csv_upsert(cur, nombre_tabla: str, ruta_csv: Path) -> None:
    if not ruta_csv.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    with ruta_csv.open("r", encoding="utf-8") as f:
        columnas = next(csv.reader(f))
        f.seek(0)

        tabla_id = sql.Identifier(nombre_tabla)
        cols_id = sql.SQL(", ").join(map(sql.Identifier, columnas))

        cur.execute("DROP TABLE IF EXISTS pg_temp.tmp_carga;")
        cur.execute(
            sql.SQL(
                "CREATE TEMP TABLE tmp_carga ON COMMIT DROP AS SELECT {} FROM {} WITH NO DATA;"
            ).format(cols_id, tabla_id)
        )

        copy_sql = sql.SQL(
            "COPY tmp_carga ({}) FROM STDIN WITH (FORMAT csv, HEADER true, NULL '', ENCODING 'UTF8')"
        ).format(cols_id)
        cur.copy_expert(copy_sql.as_string(cur), f)

    pk_cols = obtener_pk(cur, nombre_tabla)
    overriding = sql.SQL("OVERRIDING SYSTEM VALUE ") if tiene_identity_always(cur, nombre_tabla) else sql.SQL("")

    if pk_cols:
        pk_id = sql.SQL(", ").join(map(sql.Identifier, pk_cols))
        update_cols = [c for c in columnas if c not in pk_cols]

        if update_cols:
            set_clause = sql.SQL(", ").join(
                sql.SQL("{} = EXCLUDED.{}").format(sql.Identifier(c), sql.Identifier(c))
                for c in update_cols
            )
            conflict_sql = sql.SQL("ON CONFLICT ({}) DO UPDATE SET {}").format(pk_id, set_clause)
        else:
            conflict_sql = sql.SQL("ON CONFLICT ({}) DO NOTHING").format(pk_id)
    else:
        conflict_sql = sql.SQL("")

    upsert_sql = sql.SQL("INSERT INTO {} ({}) {}SELECT {} FROM tmp_carga {};").format(
        tabla_id, cols_id, overriding, cols_id, conflict_sql
    )
    cur.execute(upsert_sql)
    filas = cur.rowcount

    sincronizar_secuencia(cur, nombre_tabla, pk_cols)
    cur.execute("DROP TABLE IF EXISTS pg_temp.tmp_carga;")

    print(f"[OK] {nombre_tabla} <- {ruta_csv.name} ({filas} filas procesadas)")


def ejecutar_lote(crear_tablas: bool = False) -> None:
    lote = LOTE_BASE + (LOTE_STAGING if CARGAR_STAGING_VISTAS else [])
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            ruta_sql = CARPETA_DATOS / "carga_postgresql_supabase.sql"
            if (crear_tablas or CARGAR_STAGING_VISTAS) and ruta_sql.exists():
                cur.execute(ruta_sql.read_text(encoding="utf-8"))
                print(f"[OK] Esquema verificado con {ruta_sql.name}")

            for tabla, archivo in lote:
                cargar_csv_upsert(cur, tabla, CARPETA_DATOS / archivo)

    print("Carga completada correctamente.")


def cargar_archivo_unico(nombre_tabla: str, ruta_archivo: str) -> None:
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cargar_csv_upsert(cur, nombre_tabla, Path(ruta_archivo))
    print("Archivo cargado correctamente.")


if __name__ == "__main__":
    if not DATABASE_URL:
        sys.exit("Error: falta definir DATABASE_URL en el archivo .env")

    if len(sys.argv) == 3:
        cargar_archivo_unico(sys.argv[1], sys.argv[2])
    else:
        ejecutar_lote(crear_tablas=False)