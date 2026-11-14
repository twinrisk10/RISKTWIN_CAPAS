# Notebooks complementarios · auditoría de noviembre de 2026

Cada proyecto tiene una **copia complementaria** de su notebook principal (`*_COMPLEMENTARIO.ipynb`) y un `README_COMPLEMENTARIO.md`. **Los notebooks originales no se modificaron.**

Cada copia tiene dos partes:
- **Parte C:** bloque nuevo, autocontenido y ya ejecutado como evidencia.
- **Parte B:** el original como referencia, con ajustes puntuales marcados `# [AJUSTE AUDITORÍA]`.

La base compartida (zonas, contrato H–E–V y matriz de variables) está en [`COMUN/`](COMUN/README.md).

| Proyecto | Notebook complementario | README | Entrega mínima cubierta |
|---|---|---|---|
| URB-01 | `URB-01/src/URB01_notebook_piloto_COMPLEMENTARIO.ipynb` | [README](URB-01/README_COMPLEMENTARIO.md) | Zona Perimetral (12 zonas `PER-Z##`), matriz de 19 variables H–E–V, catálogo de fuentes, esquema espacio-temporal, muestra GeoJSON/CSV |
| URB-02 | `URB-02/src/URB02_prueba_piloto_COMPLEMENTARIO.ipynb` | [README](URB-02/README_COMPLEMENTARIO.md) | Intersección piloto `PER-Z04`, modelo nodo–arista–atributos, grafo de 8 nodos y 9 tramos, intermediación y pérdida de eficiencia |
| URB-03 | `URB-03/src/Indice_criticidad_urbana_Guayaquil_piloto_COMPLEMENTARIO.ipynb` | [README](URB-03/README_COMPLEMENTARIO.md) | Fórmula H–E–V de 3 riesgos, agregación aditiva y multiplicativa, 2 normalizaciones, 12 zonas sintéticas, sensibilidad ±10/20/30 % |
| URB-04 | `URB-04/src/URB04_patrones_riesgo_urbano_piloto_COMPLEMENTARIO.ipynb` | [README](URB-04/README_COMPLEMENTARIO.md) | Ficha de objetivo (ocurrencia semanal), 3 algoritmos y 2 líneas base, protocolo temporal con prueba reservada |
| URB-05 | `URB-05/src/URB05_notebook_piloto_2.0_COMPLEMENTARIO.ipynb` | [README](URB-05/README_COMPLEMENTARIO.md) | Exactamente 3 escenarios (base, reducción de velocidad, separación de flujos), supuestos S1–S7, Monte Carlo, prototipo JSON |
| SIS-API-01 | `SIS-API-01/src/NB2_georisk_twin_Libreria_API_Chango_Zambrano_2.0_COMPLEMENTARIO.ipynb` | [README](SIS-API-01/README_COMPLEMENTARIO.md) | Contratos Pydantic, JSON Schema, paquete `georisk_twin_hev`, 3 endpoints con 7 pruebas que pasan |
| IND-SIS-01 | `IND-SIS-01/src/NB1_RISKTWIN_Arquitectura_Integracion_Delgado_Vargas_2.0_COMPLEMENTARIO.ipynb` | [README](IND-SIS-01/README_COMPLEMENTARIO.md) | Diagrama de componentes, ER ejecutado en SQLite, contratos de entrada y salida, interfaz con el núcleo, dataset sintético |
| IND-SIS-02 | `IND-SIS-02/src/NB3_Dashboard_UX_Riesgos_Reyes_Garcia_2.0_COMPLEMENTARIO.ipynb` | [README](IND-SIS-02/README_COMPLEMENTARIO.md) | 2 perfiles, 5 requisitos funcionales, 5 criterios de usabilidad, wireframes W1 (mapa) y W2 (detalle H–E–V) |

## Respuesta a los cuatro hallazgos críticos

1. **Territorio:** todos los proyectos urbanos usan la misma delimitación del corredor de la Perimetral y el identificador `PER-Z01…Z12`. Los industriales usan `IND-Z01…Z06`.
2. **Tres indicadores:** las inundaciones están en la matriz y en el índice, pero **siempre marcadas como sintéticas**. No hay registros reales por zona y no se inventaron.
3. **Contratos:** `COMUN/contrato_hev_v1.json`, implementado en Pydantic por SIS-API-01. La severidad común es 1–4 (IND-SIS-02 tiene una propuesta de armonización desde 1–5).
4. **Evidencia:** las 8 Partes C se ejecutaron el 14-11-2026 sin errores. Las salidas quedaron en cada notebook y en `src/salidas_complementarias/`, con chequeos automáticos (`assert`) y distinción explícita entre `real` y `sintetico`.

## Hallazgo adicional: siniestros ATM duplicados

`URB-04/test_Data/siniestros_via_perimetral_guayaquil.csv` tiene **1 973 filas, pero solo 534 siniestros únicos** (1 080 duplicados exactos y 359 filas que repiten el código con otros vehículos). Los complementarios deduplican por código.

**Conviene recalcular** cualquier resultado anterior basado en filas, en particular `SIS-API-01/test_Data/risktwin_urb04_output.json`.

## Resultados que conviene conocer antes de presentar

- **URB-04:** en la prueba reservada (2026), la regresión logística obtiene PR-AUC 0,48 (IC 95 % 0,33–0,64) y la mejor línea base 0,37 (0,24–0,52). Los intervalos se solapan: **no hay un ganador claro** y debe presentarse como evaluación exploratoria.
- **URB-03:** con datos sintéticos, el ranking es estable ante cambios de pesos de ±30 % (Spearman ≥ 0,94; el top-3 se conserva siempre).
- **URB-05:** la reducción de velocidad baja la criticidad de la zona de influencia alrededor de un 12 % y la separación de flujos alrededor de un 7 %. Esta última traslada parte del conflicto a tramos vecinos. Los flujos son sintéticos: muestran el comportamiento del modelo, no un efecto real.
