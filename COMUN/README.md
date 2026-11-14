# COMUN · Base compartida de los notebooks complementarios

Esta carpeta reúne lo que **todos** los equipos deben usar igual. Responde a los hallazgos críticos 1 (territorio) y 3 (contratos de datos) de la auditoría de noviembre de 2026.

| Archivo | Qué es | Quién lo produce / usa |
|---|---|---|
| `zonas_perimetral.geojson` / `.csv` | 12 zonas comunes `PER-Z01…PER-Z12` del corredor de la Vía Perimetral | Lo generan `generar_zonas_perimetral.py`. Lo usan URB-01…05 y SIS-API-01 |
| `generar_zonas_perimetral.py` | Script reproducible de la delimitación (`pip install shapely pyproj`) | — |
| `contrato_hev_v1.json` | Contrato común: identificadores, CRS, tiempo, riesgos, componentes H–E–V, niveles, `tipo_dato` y entidades `zona`, `evento`, `observacion`, `indicador_zona` | Todos. SIS-API-01 lo implementa en Pydantic |
| `matriz_variables_hev.csv` | Matriz de 19 variables H–E–V para los tres riesgos (exportada por URB-01) | URB-01 la produce; URB-03 y SIS-API-01 la consumen |

## Regla territorial (v1)

1. **Eje:** vías OSM con `name = "Vía Perimetral"` (`SIS-API-01/test_Data/geoJsonPerimetral.geojson`, extracción del 09-11-2026).
2. **Corredor:** 200 m a cada lado del eje. Es el mismo umbral de los CSV de siniestros y homicidios de `URB-04/test_Data`.
3. **Zonas:** 12 franjas de igual amplitud en latitud entre −2,0730 y −2,2425, numeradas de norte (Z01) a sur (Z12).
4. **Asignación de un evento:** `k = floor((−2,0730 − lat) / ((−2,0730 + 2,2425) / 12))` y `id_zona = PER-Z{k+1:02d}`.

Las zonas industriales usan el prefijo `IND-Z##` para no confundirse con las urbanas.

## Calidad de datos: deduplicación de siniestros ATM

`URB-04/test_Data/siniestros_via_perimetral_guayaquil.csv` tiene **1 973 filas, pero solo 534 siniestros distintos** (código `SINIESTROS`):

- 1 080 filas son duplicados exactos.
- 359 filas repiten el código y solo cambian las columnas de vehículos.

Los notebooks complementarios cuentan **códigos únicos** con la función común `cargar_eventos_reales()` (celda C.0). Los análisis anteriores que contaron filas (incluido `risktwin_urb04_output.json`) sobrestiman los siniestros y las víctimas en un factor de alrededor de 3,7.

## Estado

Es una **propuesta** que deben acordar los equipos y el tutor. Cualquier cambio de versión debe actualizar el campo `version` del contrato y la tabla embebida de la celda C.0 de cada notebook.
