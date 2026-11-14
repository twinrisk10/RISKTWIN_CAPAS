# URB-05 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/URB05_notebook_piloto_2.0_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/URB05_notebook_piloto_2.0.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| El catálogo no tiene exactamente los tres escenarios exigidos | **Exactamente tres escenarios:** Base, Reducción de velocidad (90 → 60 km/h, modelo de potencia) y Separación de flujos |
| Variables modificables y supuestos no explícitos | Tabla de variables modificables por escenario y 7 supuestos (S1–S7) con su fuente y su control |
| Falta la comparación cuantitativa | Monte Carlo de 200 réplicas con números aleatorios comunes, IC 95 %, prueba pareada de Wilcoxon, mapa de diferencias y sensibilidad de los supuestos |
| Falta el prototipo | Motor `simulation_v02.py` (compatible con v0.1.0; 7 pruebas que pasan) y contrato JSON de entrada y salida para la API |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/URB05_notebook_piloto_2.0_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/URB-05/src"
pip install numpy pandas scipy matplotlib
jupyter lab URB05_notebook_piloto_2.0_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas scipy matplotlib` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- `SIS-API-01/test_Data/geoJsonPerimetral.geojson` (geometría real)
- Siniestros ATM (proporción de atropellos por zona como proxy de exposición peatonal)
- Celda `%%writefile simulation_v02.py`: el motor original más las dos intervenciones nuevas

## Salidas (en `src/salidas_complementarias/`)

- `urb05_catalogo_tres_escenarios.csv`
- `urb05_comparacion_tres_escenarios.csv` / `.png`, `urb05_mapa_delta_escenarios.png`
- `urb05_sensibilidad_supuestos.csv`, `urb05_pruebas_motor_v02.csv`
- `urb05_insumo_perimetral.csv`, `urb05_payload_ejemplo.json`, `urb05_resultados_api.json`
- `src/simulation_v02.py` (lo escribe el notebook)

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] El JSON de resultados contiene exactamente {Base, Reducción de velocidad, Separación de flujos}
- [x] Las 7 pruebas del motor pasan (incluida la compatibilidad con v0.1.0)
- [x] Comparación cuantitativa con IC 95 % y efectos sobre los tramos vecinos
- [x] Los supuestos están documentados y tienen análisis de sensibilidad

## Limitaciones

- Flujos, deterioro y buena parte de la exposición peatonal son sintéticos: los porcentajes muestran cómo responde el modelo, no el efecto real esperado.
- El efecto de la separación de flujos (S4) no tiene calibración local.
- La red solo incluye la capa "Vía Perimetral".

## Relación con el notebook original

La Parte B se conserva completa (catálogo exploratorio de 5 intervenciones, ANOVA, tablero Plotly, Supabase). La sección 7 se marcó como **exploratoria** y no como entrega.

**Ajustes puntuales en la copia (Parte B):**

* `generar_insumo_sintetico`: el centro por defecto pasa del centro de Guayaquil a **PER-Z04 (Perimetral)**.
* Sección 7: se marca el catálogo original de 5 intervenciones como **exploratorio**. Los tres escenarios exigidos están en la Parte C.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
