# IND-SIS-02 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/NB3_Dashboard_UX_Riesgos_Reyes_Garcia_2.0_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/NB3_Dashboard_UX_Riesgos_Reyes_Garcia_2.0.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| Requisitos no presentados como entregable | **5 requisitos funcionales** (RF-01…RF-05), cada uno con historia, criterio de aceptación y prioridad MoSCoW |
| Faltan criterios de usabilidad | **5 criterios medibles** (UX-01…UX-05) con métrica, umbral e instrumento |
| Faltan dos wireframes explícitos | **W1, mapa de zonas críticas**, y **W2, detalle H–E–V de una zona**, anotados con los RF que cubren |
| Perfiles dispersos en el texto | **2 perfiles** (técnico y operativo) en una ficha comparable; matriz de trazabilidad |
| Severidad 1–5 distinta del resto | Propuesta de armonización a 1–4 (contrato común) |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/NB3_Dashboard_UX_Riesgos_Reyes_Garcia_2.0_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/IND-SIS-02/src"
pip install pandas matplotlib
jupyter lab NB3_Dashboard_UX_Riesgos_Reyes_Garcia_2.0_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`pandas matplotlib` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- Ninguna externa

## Salidas (en `src/salidas_complementarias/`)

- `indsis02_perfiles_usuario.csv`
- `indsis02_requisitos_funcionales.csv`
- `indsis02_criterios_usabilidad.csv`
- `indsis02_wireframe_W1_mapa_zonas_criticas.png`, `indsis02_wireframe_W2_detalle_hev_zona.png`
- `indsis02_trazabilidad.csv`, `indsis02_armonizacion_severidad.csv`

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] 2 perfiles, 5 RF, 5 criterios y 2 wireframes exportados
- [x] Cada RF trazado a un perfil, un criterio y un elemento de wireframe
- [x] Los wireframes muestran la etiqueta de datos de prueba (RF-05)

## Limitaciones

- Los wireframes son de baja fidelidad y sus valores son ilustrativos.
- Los umbrales de usabilidad son metas que deben validarse con usuarios de planta.
- La armonización de severidad es una propuesta para acordar con SI-01.

## Relación con el notebook original

La Parte B (dashboard Plotly interactivo, heurísticas de Nielsen, experimento A/B, SUS) se conserva y es la base para la versión de alta fidelidad.

**Ajustes puntuales en la copia (Parte B):**

* Parámetros de datos: nota de armonización de la severidad **1–5 → 1–4** y de las zonas `Z0# → IND-Z0#`. El código no se cambió, para no romper la Parte B.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
