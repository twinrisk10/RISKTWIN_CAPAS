# URB-03 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/Indice_criticidad_urbana_Guayaquil_piloto_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/Indice_criticidad_urbana_Guayaquil_piloto.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| Falta una formulación H–E–V inequívoca | Fórmula escrita en notación matemática (C.1) y exportada como `urb03_formulacion_hev.md` |
| Faltan dos alternativas de agregación documentadas | A, aditiva ponderada (compensatoria), y B, multiplicativa geométrica (no compensatoria), con dos normalizaciones (min-max y z-score con Φ) |
| Faltan los tres indicadores | Accidentes viales, seguridad urbana e **inundaciones**, con las 19 variables de URB-01 |
| Faltan resultados sobre ≥ 5 zonas sintéticas | 12 zonas sintéticas (`PER-Z01…Z12`) con generador de semilla fija; sensibilidad de ±10/20/30 % |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/Indice_criticidad_urbana_Guayaquil_piloto_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/URB-03/src"
pip install numpy pandas scipy matplotlib
jupyter lab Indice_criticidad_urbana_Guayaquil_piloto_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas scipy matplotlib` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- `COMUN/matriz_variables_hev.csv` (si no está, se usa una copia embebida)
- Opcional: `ORIGEN_DATOS = "urb01"` usa las observaciones de URB-01

## Salidas (en `src/salidas_complementarias/`)

- `urb03_formulacion_hev.md`: documento matemático
- `urb03_tabla_pesos.csv`: tabla de pesos
- `urb03_indicadores_zona.csv`: indicadores en formato del contrato; `urb03_ranking_comparado.csv`
- `urb03_sensibilidad_resumen.csv`, `_detalle.csv`, `urb03_sensibilidad_pesos.png`
- `urb03_componentes_hev.png`, `urb03_indice_global_comparacion.png`

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] ≥ 5 zonas
- [x] Los 3 riesgos incluidos
- [x] Dos agregaciones y dos normalizaciones comparadas (Spearman)
- [x] Sensibilidad con ±10/20/30 % por peso
- [x] Índices en [0, 1] y resultados marcados como sintéticos

## Limitaciones

- Los valores son sintéticos: los rankings verifican la fórmula, no priorizan zonas reales.
- Los pesos base (1/3) son neutrales y provisionales; falta ponderación experta (AHP o Delphi).
- Con pocas zonas, min-max es sensible a los extremos (por eso se compara con z-score).

## Relación con el notebook original

La Parte B usa una cuadrícula de 500 m, Supabase opcional, `esda`/`libpysal` para autocorrelación espacial y un LLM opcional. Su `BBOX` se acotó al corredor de la Perimetral.

**Ajustes puntuales en la copia (Parte B):**

* Celda de parámetros: `BBOX` pasa del área amplia de Guayaquil al **corredor de la Vía Perimetral**. La fórmula oficial de tres riesgos está en la Parte C.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
