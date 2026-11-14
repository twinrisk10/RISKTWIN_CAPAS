# IND-SIS-01 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/NB1_RISKTWIN_Arquitectura_Integracion_Delgado_Vargas_2.0_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/NB1_RISKTWIN_Arquitectura_Integracion_Delgado_Vargas_2.0.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| El diagrama entidad-relación no está consolidado | ER con 5 entidades (figura + Mermaid + DDL), **ejecutado** en SQLite con pruebas de integridad |
| Esquemas de entrada y salida no consolidados | Contratos Pydantic de entrada (SI-02, SI-01) y de salida (dashboard, evento común) → JSON Schema |
| Interfaces con el núcleo común no definidas | Tabla de correspondencia INCIDENTE → `evento` y INDICADOR → `observacion` H–E–V; zonas `Z0#` → `IND-Z0#` |
| Falta un dataset pequeño exportable | 120 incidentes, 48 indicadores y 6 zonas (CSV, JSON y SQLite), validados contra los contratos |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/NB1_RISKTWIN_Arquitectura_Integracion_Delgado_Vargas_2.0_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/IND-SIS-01/src"
pip install numpy pandas matplotlib "pydantic>=2"
jupyter lab NB1_RISKTWIN_Arquitectura_Integracion_Delgado_Vargas_2.0_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas matplotlib "pydantic>=2"` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- Ninguna externa: el dataset se genera con semilla 42

## Salidas (en `src/salidas_complementarias/`)

- `indsis01_diagrama_componentes.png`, `indsis01_tecnologias.csv`
- `indsis01_diagrama_entidad_relacion.png`, `indsis01_esquema.sql`
- `indsis01_contratos_entrada_salida.schema.json`, `indsis01_interfaz_nucleo_comun.csv`, `indsis01_ejemplo_salida_api.json`
- `indsis01_dataset_*.csv`, `indsis01_dataset_sintetico.json`, `indsis01_piloto.db`

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] El DDL crea las 5 tablas sin errores
- [x] Las restricciones rechazan zona inexistente, severidad 5, código antiguo `Z01` y periodo duplicado
- [x] El dataset cumple los contratos de entrada (0 errores)
- [x] La consulta de salida cumple el contrato `SalidaIndicadoresZona`

## Limitaciones

- El dataset es sintético.
- SI-01 y SI-02 aún no entregan datos reales: los contratos de entrada son una propuesta que deben confirmar.
- `indice_gravedad` se usa como proxy de vulnerabilidad; debe confirmarlo SI-01.

## Relación con el notebook original

La Parte B (ETL de datos sucios, SQLAlchemy, FastAPI con uvicorn, pruebas de rendimiento) se conserva. El catálogo de zonas lleva la equivalencia `Z0# → IND-Z0#`.

**Ajustes puntuales en la copia (Parte B):**

* Catálogo de zonas: nota de equivalencia `Z0# → IND-Z0#` según el contrato común. El código original no se cambió, para no romper la Parte B.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
