# URB-02 · Notebook complementario (auditoría, noviembre 2026)

**Notebook:** `src/URB02_prueba_piloto_COMPLEMENTARIO.ipynb`  
**Copia de:** `src/URB02_prueba_piloto.ipynb` (el original **no se modificó**)  
**Salidas:** `src/salidas_complementarias/`

## Qué cambia respecto al original

| Hallazgo de la auditoría | Cambio en el notebook complementario |
|---|---|
| No hay una intersección piloto de la Perimetral | Intersección piloto = intercambiador de la zona `PER-Z04`, elegido con un criterio explícito (tabla de candidatos) |
| El modelo nodo–arista–atributos no está explícito | Diagrama del modelo y tablas de nodos y aristas con sus atributos |
| Faltan dos métricas justificadas | **Intermediación** ponderada por longitud (exposición) y **pérdida de eficiencia global** al cerrar un nodo (vulnerabilidad), con su justificación |

## Estructura del notebook

| Parte | Contenido | ¿Se ejecuta? |
|---|---|---|
| Parte C | Bloque nuevo y autocontenido con los ajustes de la auditoría (C.0 = base común, idéntica en todos los proyectos) | **Sí**, es la entrega |
| Parte B | Copia del notebook original con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]` | No es necesaria (referencia) |

## Cómo ejecutar

### En Google Colab
1. Abrir el notebook `src/URB02_prueba_piloto_COMPLEMENTARIO.ipynb` desde GitHub (*Archivo → Abrir cuaderno → GitHub*, repositorio `AaronTech24/Gemelos_Digitales`).
2. En la celda **C.0**, cambiar `CLONAR_REPO = True`. Así se descargan `COMUN/` y los datos de prueba del repositorio.
3. Ejecutar en orden las celdas de la **Parte C** (de C.0 hasta el final de la Parte C). **No hace falta ejecutar la Parte B.**

### En local (Jupyter / VS Code)
```bash
git clone https://github.com/AaronTech24/Gemelos_Digitales.git
cd "Gemelos_Digitales/GEMELO DIGITAL/URB-02/src"
pip install numpy pandas matplotlib networkx scipy
jupyter lab URB02_prueba_piloto_COMPLEMENTARIO.ipynb
```
Ejecutar la Parte C de arriba abajo. La celda C.0 encuentra sola la carpeta `GEMELO DIGITAL/` y `COMUN/`.

> **Evidencia incluida en el repositorio:** la Parte C ya se ejecutó el 14-11-2026 (Python 3.13). Las salidas de las celdas quedaron guardadas en el notebook y los archivos en `src/salidas_complementarias/`. La Parte B (original) **no** se ejecutó.

## Dependencias

`numpy pandas matplotlib networkx scipy` (Python ≥ 3.10). La Parte B tiene las dependencias del original.

## Entradas

- `SIS-API-01/test_Data/geoJsonPerimetral.geojson` (OSM, real)
- `COMUN/zonas_perimetral.csv`
- Siniestros ATM (mediante el cargador común) para asociarlos a los tramos

## Salidas (en `src/salidas_complementarias/`)

- `urb02_diagrama_modelo_grafo.png`: modelo nodo–arista–atributos
- `urb02_mapa_grafo_piloto.png` y `urb02_grafo_piloto.geojson`: mapa piloto
- `urb02_nodos.csv`, `urb02_aristas.csv`, `urb02_grafo_piloto.graphml`: tablas y grafo con las dos métricas

## Criterios de aceptación

Se verifican en el propio notebook con `assert` o tablas de chequeo. En la ejecución del 14-11-2026 **se cumplieron todos**.

- [x] Grafo pequeño (8 nodos, 9 tramos) con al menos una intersección de grado ≥ 3
- [x] Dos métricas calculadas y en [0, 1]
- [x] Aristas apuntan a nodos existentes; longitudes positivas; resultado reproducible

## Limitaciones

- La capa del repositorio solo tiene las vías llamadas "Vía Perimetral" (sin calles transversales). Para la red completa, ejecutar la Parte B en Colab (OSMnx).
- Grafo no dirigido: sirve para la conectividad estructural, no para la asignación de tráfico.
- La correlación entre intermediación y siniestros se calcula con n = 6 tramos: es solo exploratoria.

## Relación con el notebook original

La Parte B descarga la red con `ox.graph_from_point`. Su celda de parámetros ya está centrada en `PER-Z04`, con radio de 800 m.

**Ajustes puntuales en la copia (Parte B):**

* Celda de parámetros: zona **Guasmo → intercambiador de la Vía Perimetral en PER-Z04**, radio 1 500 → 800 m.

Para integrar los cambios al original, basta con copiar las celdas de la Parte C. Son autocontenidas y no dependen de la Parte B.
