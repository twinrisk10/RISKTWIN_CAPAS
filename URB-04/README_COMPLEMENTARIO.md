# URB-04 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/URB04_patrones_riesgo_urbano_piloto_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/URB04_patrones_riesgo_urbano_piloto.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| No se fija qué se predice | **Ocurrencia** de ≥ 1 siniestro con víctimas en la zona `PER-Z##` en la **semana siguiente** (horizonte de 1 semana), con ficha de la variable objetivo |
| Falta comparación de tres algoritmos con protocolo | Regresión logística, Random Forest y XGBoost frente a dos líneas base, con partición temporal, validación con origen móvil, prueba reservada única e IC bootstrap |
| `MIN_EVENTOS_REALES = 500` sin justificación | Se reemplaza por el criterio **EPV ≥ 10** (eventos por variable), que se cumple con 13,0; el umbral 500 se documenta como decisión de diseño |
| Riesgo de presentar resultados simulados como validación | Se usan solo datos reales y la parte **se detiene** si faltan (no cambia a datos sintéticos en silencio). Los resultados se rotulan como evaluación retrospectiva exploratoria |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/URB04_patrones_riesgo_urbano_piloto_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/URB-04/src"
pip install numpy pandas scikit-learn xgboost matplotlib
jupyter lab URB04_patrones_riesgo_urbano_piloto_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas scikit-learn xgboost matplotlib` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- Siniestros ATM y homicidios (`URB-04/test_Data`, reales), deduplicados con el cargador común
- `COMUN/zonas_perimetral.csv` (atributos estáticos de la zona)

## Salidas (en `src/salidas_complementarias/`)

- `urb04_ficha_variable_objetivo.csv`: ficha
- `urb04_tabla_comparativa_modelos.csv` y `urb04_curvas_pr_importancia.png`: comparación
- `urb04_protocolo_particion.csv` y `urb04_validacion_cruzada_temporal.csv`: protocolo
- `urb04_dataset_zona_semana.csv`: dataset analítico (1 356 filas)

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] Variable objetivo, unidad y horizonte definidos sin ambigüedad
- [x] Ninguna característica usa información posterior a la semana w
- [x] Tres algoritmos y dos líneas base evaluados con el mismo protocolo
- [x] La prueba reservada (2026) se usa una sola vez; se reporta la PR-AUC con IC 95 %
- [x] EPV ≥ 10 en entrenamiento

## Limitaciones

- Evaluación retrospectiva sobre un solo corredor y unas 21 semanas de prueba. Los IC de los modelos se solapan con los de la línea base: **no hay un ganador claro**.
- Los resultados del notebook original y de `SIS-API-01/test_Data/risktwin_urb04_output.json` se calcularon sobre filas duplicadas y deben recalcularse.
- No hay TPDA, clima diario ni inundaciones reales como predictores.

## Relación con el notebook original

La Parte B (Supabase, GCN/GraphSAGE con `torch`, SHAP, clustering) se conserva. Se acotó el `BBOX` y se documentó el umbral `MIN_EVENTOS_REALES`.

**Ajustes puntuales en la copia (Parte B):**

* Celda de parámetros: `BBOX_POR_DEFECTO` acotado al **corredor de la Perimetral**. Se añade la justificación de `MIN_EVENTOS_REALES = 500` (decisión de diseño, no requisito estadístico; la Parte C usa EPV ≥ 10) y la advertencia sobre las filas duplicadas del CSV ATM.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
