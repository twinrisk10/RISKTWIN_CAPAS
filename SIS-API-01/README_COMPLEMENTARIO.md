# SIS-API-01 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/NB2_georisk_twin_Libreria_API_Chango_Zambrano_2.0_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/NB2_georisk_twin_Libreria_API_Chango_Zambrano_2.0.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| No hay contrato H–E–V común | Modelos Pydantic `Zona`, `Evento`, `Observacion`, `IndicadorZona` (y solicitudes y respuestas), exportados como JSON Schema |
| Falta el esquema zona/evento/observación | Se implementa el esquema de `COMUN/contrato_hev_v1.json`, con validaciones cruzadas (p. ej. `id_variable` coherente con riesgo y componente) |
| Hay que elegir tres endpoints | `POST /datos/validar` → `POST /indicadores/calcular` → `POST /analitico/priorizar` |
| Falta evidencia de ejecución funcional | 7 pruebas `pytest` con `TestClient` que pasan; pares solicitud/respuesta guardados en `evidencia/` |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/NB2_georisk_twin_Libreria_API_Chango_Zambrano_2.0_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Instalar dependencias si faltan: `!pip install -q fastapi httpx pytest`. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/SIS-API-01/src"
pip install fastapi "pydantic>=2" httpx pytest pandas numpy
jupyter lab NB2_georisk_twin_Libreria_API_Chango_Zambrano_2.0_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`fastapi "pydantic>=2" httpx pytest pandas numpy` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- `URB-01/src/salidas_complementarias/urb01_observaciones_zona.csv` (si no está, se genera una muestra sintética mínima)

## Salidas (en `src/salidas_complementarias/`)

- `salidas_complementarias/georisk_twin_hev/`: paquete (`pyproject.toml`, `src/`, `tests/`, `README.md`)
- `.../contrato/contrato_hev_v1.schema.json`: contrato JSON
- `.../evidencia/reporte_pytest.txt` y `*.json`: evidencia de prueba

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] El paquete se instala con `pip install -e .`
- [x] El OpenAPI documenta los 3 endpoints
- [x] Validar rechaza los 4 tipos de error de contrato con un mensaje por campo
- [x] Calcular devuelve índices en [0, 1] con ambas agregaciones
- [x] Priorizar devuelve un top-k ordenado y una advertencia si los datos no son reales

## Limitaciones

- Sin persistencia: los datos llegan en la solicitud (la conexión con Supabase del original no se incluyó).
- La normalización min-max es relativa a las zonas enviadas en cada solicitud.

## Relación con el notebook original

La Parte B (paquete `georisk_twin` v0.5, CI, benchmark y Supabase) se conserva. `Incidente.zona` lleva una nota sobre el identificador común.

**Ajustes puntuales en la copia (Parte B):**

* `schemas.py`: nota en `Incidente.zona`. El contrato común usa los identificadores `PER-Z##` / `IND-Z##`; la severidad 1–4 ya era compatible. Los contratos nuevos están en la Parte C.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
