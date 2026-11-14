# URB-01 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/URB01_notebook_piloto_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/URB01_notebook_piloto.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| La zona piloto es el centro de Guayaquil (radio 1 000 m) | Zona piloto = corredor de la Vía Perimetral, 200 m a cada lado del eje, dividido en 12 zonas comunes `PER-Z01…Z12` (`COMUN/`) |
| Faltan al menos 15 variables H–E–V | Matriz de **19 variables** (3 riesgos × H, E, V), con sentido, unidad, fuente y tipo de dato |
| Faltan fuentes para cada riesgo | Catálogo de 11 fuentes (F01–F10, F99) con su estado de disponibilidad |
| Falta la muestra GeoJSON/CSV con zonas | 995 eventos reales (534 siniestros ATM + 461 homicidios) con `id_zona`; GeoJSON de muestra y GeoJSON de zonas con variables |
| — | **Hallazgo nuevo:** el CSV ATM de la Perimetral tiene 1 973 filas pero solo 534 siniestros únicos. Se deduplica por código |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/URB01_notebook_piloto_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/URB-01/src"
pip install numpy pandas matplotlib
jupyter lab URB01_notebook_piloto_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas matplotlib` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- `COMUN/zonas_perimetral.csv` y `.geojson` (zonas comunes)
- `COMUN/contrato_hev_v1.json` (diccionario del intercambio)
- `URB-04/test_Data/siniestros_via_perimetral_guayaquil.csv` (ATM, real)
- `URB-04/test_Data/homicidios_via_perimetral.csv` (real)

## Salidas (en `src/salidas_complementarias/`)

- `urb01_matriz_variables_hev.csv`: matriz de 19 variables (copiada también en `COMUN/matriz_variables_hev.csv`)
- `urb01_catalogo_fuentes.csv`: catálogo de fuentes
- `urb01_diccionario_intercambio.csv`: esquema espacial-temporal del contrato
- `urb01_eventos_perimetral.csv` y `urb01_eventos_muestra.geojson`: eventos con zona identificada
- `urb01_observaciones_zona.csv` (formato largo del contrato), `_ancha.csv` y `urb01_zonas_perimetral_hev.geojson`
- `urb01_mapa_zonas_perimetral.png`, `urb01_mapa_peligrosidad_real.png`, `urb01_validacion_contrato.csv`

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] Zona piloto ubicada en la Vía Perimetral, con identificador común
- [x] ≥ 15 variables, y cada riesgo con al menos una H, una E y una V
- [x] Cada variable tiene fuente y `tipo_dato`; las inundaciones no usan datos reales inventados
- [x] Muestra GeoJSON/CSV con `id_zona` válido (`PER-Z##`)
- [x] Los 10 chequeos de `urb01_validacion_contrato.csv` en verdadero

## Limitaciones

- 13 de 19 variables son sintéticas o pendientes (todas las de inundaciones).
- Las franjas de los extremos (Z01 y Z12) contienen más kilómetros de vía porque allí la vía gira; las tasas se calculan por km o km².
- La seguridad urbana solo usa homicidios (no hay robos por zona). La procedencia de la base de homicidios debe confirmarse.

## Relación con el notebook original

La Parte B descarga la red OSM y los POI con OSMnx (necesita Internet) y usa Supabase y la API de LLM de forma opcional. Su celda de parámetros ya apunta a la zona `PER-Z05` de la Perimetral.

**Ajustes puntuales en la copia (Parte B):**

* Celda de parámetros: zona piloto **Centro de Guayaquil → Vía Perimetral, zona PER-Z05** (centroide de COMUN) e identificador `Z01 → PER-Z05`.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
