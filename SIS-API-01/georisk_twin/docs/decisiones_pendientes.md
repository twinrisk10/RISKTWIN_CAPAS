# Decisiones pendientes y puntos a confirmar

Detectados al contrastar la matriz de interfaces con los entregables del 18/11.

| # | Tema | Qué se observó | Propuesta de v0 | Con quién confirmar |
|---|---|---|---|---|
| 1 | Nombre del paquete | El planteamiento dice `georisk_twin`; la lámina de entregables dice `RISKTWIN` | Se usa `georisk_twin` como nombre de importación | Tutor / equipo |
| 2 | Límite entre IND-SIS-01 y SIS-API-01 | IND-SIS-02 espera que IND-SIS-01 le dé «arquitectura y API para consultar datos» y pregunta qué endpoints proporcionará IND-SIS-01 | SIS-API-01 es el núcleo común; IND-SIS-01 define la integración de datos industriales sobre ese núcleo | IND-SIS-01, IND-SIS-02, tutor |
| 3 | Identificador | URB-01 y URB-05 usan `tramo_id`; URB-04 usa `id`; la entrega pide esquema de «zona» | `zona_id` canónico; `tramo_id` e `id` aceptados como alias de entrada | URB-01, URB-04, URB-05 |
| 4 | Sistema de coordenadas | URB-01 intercambia GeoJSON en WGS 84; URB-02 declara EPSG:32717 en sus salidas | API en EPSG:4326; las capas que entreguen en 32717 convierten en su adaptador (por ejemplo con `pyproj`) | URB-01, URB-02 |
| 5 | Catálogo de variables | SI-01 (mínimo 12) y URB-01 (mínimo 15) aún no entregan la lista definitiva | Catálogo sintético mínimo de 9 variables | SI-01, URB-01 |
| 6 | Quién normaliza y con qué orientación | No está definido | `valor_normalizado` en [0, 1], 1 = mayor riesgo; el método lo define URB-03 | URB-03, SI-01 |
| 7 | Taxonomía y severidad de eventos | SI-02 aún no la entrega | 3 tipos del enunciado y severidad 1 a 5 provisional | SI-02 |
| 8 | URB-05: ¿bajo demanda o precalculado? (pregunta de URB-05 a SIS-API-01) | Sin definir | v0: **precalculado**; URB-05 entrega CSV con los campos de la matriz y la API los sirve. Ejecución bajo demanda en una versión posterior | URB-05 |
| 9 | URB-04: estructura y frecuencia | Preguntan qué estructura necesita SIS-API-01 y cada cuánto se actualizan los datos | Contrato borrador `ResultadoPrediccion`; frecuencia por definir | URB-04 |
| 10 | Plantillas de carga | URB-01 pide a SIS-API-01 los requisitos de las plantillas de carga | `POST /v1/observaciones` define el formato; falta una plantilla CSV equivalente | URB-01 |
| 11 | Formatos de intercambio | GraphML (URB-02), GeoPackage/PostGIS (URB-01), CSV/XLSX (varios), JSON (URB-04) | v0 solo JSON; adaptadores por formato en versiones siguientes | Todos |
| 12 | Datos reales | SI-02 debe confirmar con Cristian y Eugenia si hay registros reales | Todo es sintético y está marcado con `sintetico=true` | SI-02 |
