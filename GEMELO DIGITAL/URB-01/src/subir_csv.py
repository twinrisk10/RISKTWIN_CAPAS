import csv
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
CARPETA_DATOS = Path(__file__).parent / "datos"

# Orden de carga respetando llaves foráneas (prediccion depende de modelo_riesgo)
LOTE_BASE = [
    ("modelo_riesgo", "modelo_riesgo_rows.csv"),
    ("clima_diario",  "clima_diario_rows.csv"),
    ("feriado",       "feriado_rows.csv"),
    ("prediccion",    "prediccion_rows.csv"),
]

# Cambia a True solo si también quieres materializar las vistas como tablas de staging
CARGAR_STAGING_VISTAS = False
LOTE_STAGING = [
    ("stg_v_panel_semanal_zona", "v_panel_semanal_zona_rows.csv"),
    ("stg_v_prediccion_zona",    "v_prediccion_zona_rows.csv"),
]


def cargar_csv(cur, nombre_tabla: str, ruta_csv: Path) -> None:
    if not ruta_csv.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    with ruta_csv.open("r", encoding="utf-8") as f:
        columnas = next(csv.reader(f))
        f.seek(0)
        consulta = sql.SQL(
            "COPY {} ({}) FROM STDIN WITH (FORMAT csv, HEADER true, NULL '', ENCODING 'UTF8')"
        ).format(
            sql.Identifier(nombre_tabla),
            sql.SQL(", ").join(map(sql.Identifier, columnas)),
        )
        cur.copy_expert(consulta.as_string(cur), f)

    print(f"[OK] {nombre_tabla} <- {ruta_csv.name}")


def ejecutar_lote(crear_tablas: bool = True) -> None:
    lote = LOTE_BASE + (LOTE_STAGING if CARGAR_STAGING_VISTAS else [])
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            if crear_tablas:
                ruta_sql = CARPETA_DATOS / "carga_postgresql_supabase.sql"
                cur.execute(ruta_sql.read_text(encoding="utf-8"))
                print(f"[OK] Esquema verificado con {ruta_sql.name}")

            for tabla, archivo in lote:
                cargar_csv(cur, tabla, CARPETA_DATOS / archivo)

    print("Carga completada correctamente.")


def cargar_archivo_unico(nombre_tabla: str, ruta_archivo: str) -> None:
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cargar_csv(cur, nombre_tabla, Path(ruta_archivo))
    print("Archivo cargado correctamente.")


if __name__ == "__main__":
    if not DATABASE_URL:
        sys.exit("Error: falta definir DATABASE_URL en el archivo .env")

    # Uso 1 (lote completo): python subir_csv.py
    # Uso 2 (cualquier archivo futuro): python subir_csv.py nombre_tabla datos/archivo.csv
    if len(sys.argv) == 3:
        cargar_archivo_unico(sys.argv[1], sys.argv[2])
    else:
        ejecutar_lote(crear_tablas=True)
        