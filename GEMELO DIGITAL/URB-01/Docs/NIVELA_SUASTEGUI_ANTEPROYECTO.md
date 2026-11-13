# UNIVERSIDAD DE GUAYAQUIL
## FACULTAD DE INGENIERÍA INDUSTRIAL

# ANTEPROYECTO DE TRABAJO DE TITULACIÓN

## MODELO DE DATOS MULTIMODAL PARA RIESGO URBANO EN UN GEMELO DIGITAL

**SUSTENTANTE(S):**
Nivela Mejía José Andrés
Suastegui Naranjo Luis Josué

**DOCENTE TUTOR/REVISOR:** Katty Lino

**GUAYAQUIL, 26 agosto de 2026**

---

## DATOS GENERALES

| | |
|---|---|
| **CARRERA** | Sistemas de la Información |
| **FECHA** | 18/08/2026 |

| | Apellidos | Nombres |
|---|---|---|
| **ESTUDIANTE 1** | Nivela Mejía | José Andrés |
| **ESTUDIANTE 2** | Suastegui Naranjo | Luis Josué |

**Correo institucional y personal:**

- luis.suasteguin@ug.edu.ec
- luisjosuesuastegui@gmail.com
- jose.nivelam@ug.edu.ec
- joseandresnivela@hotmail.com

**Teléfono:** 0987492152 / 0978821289

## TEMA

Modelo de datos multimodal para riesgo urbano en un gemelo digital

### Línea de Investigación

- [ ] Sostenibilidad, derechos y tecnologías en el ordenamiento territorial, ambiente de la construcción y arquitectura.
- [ ] Desarrollo local y emprendimiento socio económico sostenible.
- [x] Ciencias básicas, bioconocimiento y desarrollo industrial.
- [ ] Salud humana, animal y del ambiente.
- [ ] Tecnologías agrícolas y de la agricultura.
- [ ] Entornos virtuales de aprendizaje y tecnologías educativas.

### Cobertura

- [ ] Nacional
- [ ] Provincial
- [x] Local
- [ ] Otros

---

# CONTENIDO

## 1. PLANTEAMIENTO Y FORMULACIÓN DEL PROBLEMA

### 1.1 Antecedentes

Los gemelos digitales urbanos se han consolidado en los últimos años como una herramienta para la gestión inteligente de ciudades, integrando datos geoespaciales, viales y de infraestructura en representaciones virtuales que permiten monitorear, analizar y simular el comportamiento del entorno físico. La literatura reciente evidencia un crecimiento sostenido de investigaciones sobre gemelos digitales urbanos orientados a resiliencia, seguridad vial y gestión del riesgo (Mazzetto, 2024; Wang et al., 2024), así como marcos de referencia para estandarizar la integración de datos multimodales (geoespaciales, viales, contextuales y operativos) en plataformas del tipo CityGML y bases de datos geoespaciales como PostGIS (ISPRS Archives, 2024; Buildings, 2024).

Sin embargo, persisten desafíos relacionados con la heterogeneidad de las fuentes de datos urbanos (open data municipal, OpenStreetMap, sensores, incidentes), evidenciada incluso entre fuentes abiertas ampliamente usadas (Mara et al., 2025), la falta de modelos de datos reutilizables entre módulos analíticos, y la ausencia de mecanismos de calidad y trazabilidad que permitan que otros componentes de un gemelo digital (grafos de conectividad, índices de criticidad, modelos de IA y simulación de escenarios) se apoyen en una única fuente de verdad consistente (Jeddoub et al., 2024).

Este anteproyecto se enmarca en el proyecto FCI RISKTWIN, una iniciativa multi-tesis orientada a construir un gemelo digital multimodal urbano-industrial para la gestión del riesgo, del cual el presente trabajo (código interno URB-01) constituye la capa base de datos urbanos que alimentará los módulos de grafos (URB-02), índice de criticidad (URB-03), inteligencia artificial (URB-04), simulación (URB-05) y la API integradora (SIS-API-01).

### 1.2 Planteamiento del Problema

Actualmente no existe un modelo de datos urbano unificado que permita integrar de forma consistente las capas geoespaciales, la red vial, los puntos de interés, las zonas de análisis, los aforos y las variables contextuales necesarias para alimentar un gemelo digital urbano orientado a la gestión del riesgo. Esta carencia obliga a que cada módulo analítico (grafos, índices, modelos de IA, simulaciones) trabaje con estructuras de datos distintas, sin trazabilidad de fuente ni reglas de calidad comunes, lo que dificulta la interoperabilidad, incrementa el riesgo de inconsistencias y limita la escalabilidad del sistema.

Este problema es particularmente crítico para la gestión del riesgo: cuando las coordenadas geográficas presentan inconsistencias (por ejemplo, sistemas de referencia espacial distintos o errores de georreferenciación) o cuando existen registros duplicados entre fuentes, la incertidumbre se traslada directamente a los módulos que dependen de esos datos. Un grafo de conectividad construido sobre coordenadas inconsistentes puede generar adyacencias erróneas entre nodos; un índice de criticidad calculado sobre registros duplicados puede sobreestimar o subestimar el nivel de exposición de una zona; y un simulador de escenarios que reciba datos con baja trazabilidad puede producir resultados poco confiables.

Contar con un modelo de datos consistente y validado es, por tanto, una condición necesaria para que la gestión del riesgo dentro del gemelo digital urbano se sustente en información confiable al momento de simular escenarios o calcular índices de criticidad.

### 1.3 Causas

- Heterogeneidad de fuentes urbanas abiertas (OpenStreetMap, datos municipales, POI, incidentes) sin un esquema común de integración.
- Ausencia de un diccionario de datos y de un modelo lógico compartido entre los distintos módulos del gemelo digital.
- Falta de reglas de limpieza, validación geográfica y control de calidad aplicadas de forma sistemática a los datos urbanos.
- Carencia de plantillas de carga reutilizables que permitan a otros equipos alimentar el sistema sin reconstruir el pipeline de datos.
- Inconsistencias en los Sistemas de Referencia Espacial (CRS/proyecciones) y falta de estandarización en los formatos de origen (GeoJSON, Shapefile, CSV, APIs REST) empleados por las distintas fuentes urbanas.

### 1.4 Consecuencias

- Inconsistencias geográficas y temporales que afectan la confiabilidad de los módulos que dependen del dataset urbano: coordenadas con distinto sistema de referencia o mal geocodificadas distorsionan las relaciones de adyacencia usadas por el módulo de grafos, introducen ruido en el cálculo del índice de criticidad, y reducen la precisión de los modelos de IA y de los algoritmos de simulación de escenarios de riesgo, que dependen de series espacio-temporales limpias y comparables.
- Duplicidad de esfuerzos entre los equipos del proyecto RISKTWIN al no contar con una estructura de datos reutilizable.
- Dificultad para escalar el gemelo digital a nuevas zonas urbanas por falta de trazabilidad de fuente y documentación.
- Baja interoperabilidad con la API integradora (SIS-API-01), lo que retrasa la conexión entre módulos y, en consecuencia, demora la disponibilidad de información actualizada para la toma de decisiones en gestión del riesgo por parte de los equipos y autoridades involucradas.

### 1.5 Formulación del Problema

¿Cómo estructurar e integrar datos multimodales geoespaciales, viales, contextuales y operativos para un gemelo digital urbano orientado a la gestión del riesgo, de manera que sean reutilizables, trazables y de calidad verificable para su utilización por los diferentes módulos analíticos del sistema?

## 2. ALCANCE

El proyecto comprende el diseño e implementación de un modelo de datos urbano multimodal que integre información geoespacial, vial, puntos de interés (POI), zonas de análisis, aforos, incidentes y variables contextuales, dentro del ámbito del proyecto FCI RISKTWIN. El diseño incluye la elaboración de un diccionario de datos, un modelo lógico, un catálogo de fuentes abiertas, reglas de limpieza y validación geográfica, plantillas de carga reutilizables y un dataset urbano de prueba (v0.1) documentado, construido a partir de una zona urbana seleccionada de Guayaquil. El desarrollo se ejecutará mediante scripts ETL en Python (GeoPandas, PostGIS/GeoPackage) durante el periodo de 16 semanas.

El proyecto NO incluye:

- El desarrollo de los módulos de grafos urbanos (URB-02), índice de criticidad (URB-03), modelos de inteligencia artificial (URB-04) ni el simulador de escenarios (URB-05), que corresponden a tesis independientes dentro de RISKTWIN.
- La implementación completa de la API/plataforma integradora (SIS-API-01); este trabajo entregará la estructura y el dataset que dicha API consumirá.
- La recolección de datos sensibles de identificación personal; solo se emplearán fuentes abiertas y datos simulados/documentados cuando no existan datos reales disponibles.

## 3. JUSTIFICACIÓN DE LA INVESTIGACIÓN

El carácter multimodal del modelo propuesto responde a la naturaleza del riesgo urbano: los fenómenos que se busca representar y simular (congestión vial, exposición a incidentes, criticidad de infraestructura) no pueden explicarse a partir de un único tipo de dato, sino que emergen de la combinación de información geoespacial (capas, límites, coordenadas), vial (red de tránsito, conectividad), de puntos de interés y aforos (uso y ocupación del espacio), y contextual/operativa (incidentes, sensores, condiciones temporales). Integrar estas modalidades bajo un modelo de datos común permite que los módulos de grafos, índice de criticidad, IA y simulación trabajen sobre una representación coherente del territorio, en lugar de reconciliar fuentes heterogéneas de manera independiente en cada módulo.

### 3.1 Justificación Teórica

El proyecto aporta al cuerpo de conocimiento sobre gemelos digitales urbanos multimodales, un campo en expansión respaldado por revisiones recientes sobre integración de gemelos digitales urbanos en el desarrollo de ciudades inteligentes (Mazzetto, 2024), sobre la resiliencia urbana mediante el ciclo entre el espacio virtual y el mundo real (Wang et al., 2024) y sobre la integración de IoT, IA y gemelos digitales en ciudades inteligentes (Sacoto-Cabrera et al., 2025). El diseño de un modelo de datos reutilizable contribuye además a la discusión metodológica sobre interoperabilidad de datos urbanos mediante grafos de conocimiento (Ding et al., 2023) y estándares como CityGML aplicados a grandes volúmenes de datos geoespaciales (ISPRS Archives, 2024).

### 3.2 Justificación Práctica

El modelo de datos resultante beneficia directamente a los cuatro módulos posteriores del proyecto RISKTWIN (grafos, índice de criticidad, IA y simulación), al proveerles una estructura de datos común, documentada y con criterios de calidad verificada. A nivel institucional, sienta las bases técnicas para que la Carrera de Sistemas de la Información cuente con un caso de estudio integrador de gemelos digitales urbanos aplicables a la gestión del riesgo, con posibilidad de ser replicado en otras zonas de la ciudad.

### 3.3 Justificación Metodológica

Se adopta el enfoque de Design Science Research (DSR), por ser el más adecuado para proyectos que requieren diseñar y evaluar un artefacto de forma iterativa, con criterios de aceptación verificables. La investigación seguirá las fases propias de DSR: (1) identificación del problema, correspondiente a la ausencia de un modelo de datos urbano unificado y trazable; (2) definición de objetivos, orientados a un modelo de datos multimodal reutilizable, trazable y de calidad verificable; (3) diseño del artefacto, mediante la elaboración del diccionario de datos, el modelo lógico y las reglas de calidad; (4) implementación, a través del pipeline ETL en Python (GeoPandas, PostGIS/GeoPackage); (5) demostración, mediante la construcción del dataset urbano de prueba (v0.1) sobre una zona piloto de Guayaquil; (6) evaluación, verificando las métricas de calidad de datos y la interoperabilidad con el módulo de grafos (URB-02); y (7) comunicación, mediante la documentación técnica y el reporte de calidad entregados al proyecto RISKTWIN. El artefacto de esta investigación queda así identificado como el modelo de datos multimodal, el dataset urbano de prueba (v0.1) y los mecanismos de transformación y validación (pipeline ETL y reglas de calidad) que lo acompañan.

## 4. OBJETIVO GENERAL

Diseñar un modelo de datos urbano multimodal que integre y organice fuentes geoespaciales, viales, contextuales y operativas garantizando su reutilización, trazabilidad y calidad verificable para soportar los módulos analíticos de un gemelo digital urbano gestión de riesgo.

## 5. OBJETIVOS ESPECÍFICOS

- Elaborar un inventario de fuentes de datos urbanos abiertas (OpenStreetMap, datos municipales, POI, incidentes) y estructurar un diccionario de datos aplicando el estándar de metadatos geográficos ISO 19115 para documentar rigurosamente las entidades, variables, atributos y la trazabilidad del modelo.
- Diseñar el modelo lógico de datos urbano aplicando la metodología MDA (Model-Driven Architecture) en sus niveles de abstracción, garantizando la estructuración del componente espacial mediante el cumplimiento de los lineamientos del OGC (Open Geospatial Consortium) y los Principios FAIR (Encontrable, Accesible, Interoperable y Reutilizable).
- Definir un modelo de evaluación y métricas de calidad espacial (completitud, consistencia geográfica, ausencia de duplicados y validez del sistema de referencia espacial) que deberá cumplir el dataset, estableciendo para cada regla un umbral de aceptación técnico y verificable.
- Construir y documentar un dataset urbano de prueba (v0.1) sobre una zona piloto de Guayaquil, verificando su interoperabilidad y precisión con los módulos de grafos e indicadores del proyecto RISKTWIN mediante la aplicación del modelo de evaluación definido y pruebas conjuntas de carga con los equipos responsables.

## 6. HIPÓTESIS DE INVESTIGACIÓN

No aplica una hipótesis estadística contrastable. El presente anteproyecto corresponde a un desarrollo de tipo aplicado orientado a la construcción de un artefacto (modelo de datos y dataset urbano), enmarcado en Design Science Research (DSR), enfoque en el que la validez del trabajo no se establece mediante la comprobación de una hipótesis, sino mediante la evaluación del artefacto frente a criterios de aceptación verificables. En este proyecto, el artefacto se evaluará mediante: (a) métricas de calidad de datos (completitud, consistencia geográfica, tasa de duplicados y trazabilidad de fuente) medidas sobre el dataset urbano de prueba (v0.1); y (b) una prueba de integración en la zona piloto que verifique la interoperabilidad del dataset con el módulo de grafos (URB-02) del proyecto RISKTWIN. El cumplimiento de estos criterios de aceptación constituirá la evidencia de que el artefacto resuelve el problema planteado.

## 7. MARCO TEÓRICO Y REFERENCIAL

### 7.1 Gemelos digitales urbanos

Un gemelo digital urbano es una representación virtual dinámica de un entorno urbano que integra datos geoespaciales, de infraestructura y contextuales para apoyar la toma de decisiones. (Mazzetto, 2024) identifica los principales retos de integración de estos sistemas en el desarrollo de ciudades inteligentes, mientras que Wang et al. (2024) describen el ciclo de retroalimentación entre el espacio virtual y el mundo físico como elemento central para mejorar la resiliencia urbana. Estos referentes sustentan la necesidad de un modelo de datos base robusto como el propuesto.

### 7.2 Riesgo urbano y gestión del riesgo

La gestión del riesgo urbano se apoya cada vez más en gemelos digitales para anticipar y responder a eventos que afectan la seguridad y funcionalidad de la ciudad, mediante la construcción de índices de criticidad y la simulación de escenarios sobre la infraestructura vial y de servicios (Costa, 2024).

La calidad de los datos geoespaciales que alimentan estos modelos resulta un insumo crítico: solo un dataset urbano consistente, trazable y con reglas de calidad verificables permite que los índices de criticidad y las simulaciones de riesgo reflejen con precisión las condiciones reales del territorio, en lugar de propagar errores heredados de los datos de origen.

### 7.3 Modelos de datos multimodales y estándares geoespaciales

La representación de datos urbanos multimodales requiere combinar estándares como CityGML con bases de datos geoespaciales (PostGIS/GeoPackage) y fuentes abiertas como OpenStreetMap. Trabajos recientes abordan entornos multi-base de datos adaptados a grandes volúmenes de geodatos (ISPRS Archives, 2024) y la construcción de modelos de datos de gemelos digitales a partir de datos públicos (Buildings, 2024), lo que orienta las decisiones de diseño del diccionario de datos y el modelo lógico de este proyecto, permitiendo unificar redes viales, puntos de interés, datos operativos y zonas de análisis.

### 7.4 Metadatos, trazabilidad y calidad de datos

El procesamiento de grandes volúmenes de geodatos urbanos (Big Geodata) impone desafíos significativos de almacenamiento, indexación y estandarización. Para abordar esta complejidad, la comunidad científica aboga por entornos multi-base de datos espacialmente habilitadas (como PostGIS o GeoPackage) que se alineen con estándares internacionales de representación semántica.

Investigaciones recientes profundizan en la adaptación de estándares como CityGML a entornos de bases de datos distribuidas para resolver los problemas inherentes al manejo masivo de geodatos en gemelos digitales (ISPRS Archives, 2024). Adoptar estos estándares garantiza que las geometrías y atributos de las entidades urbanas posean una semántica clara y universalmente comprensible por distintos motores de procesamiento.

### 7.5 Grafos de conocimiento e interoperabilidad

La interoperabilidad entre módulos de un gemelo digital urbano puede reforzarse mediante grafos de conocimiento que integren datos 3D de la ciudad (Ding et al., 2023). Este enfoque es relevante como referencia conceptual, dado que el dataset urbano producido en este trabajo deberá ser consumido posteriormente por el módulo de grafos urbanos (URB-02) del proyecto RISKTWIN. La trazabilidad permite auditar el ciclo de vida de cada registro espacial hasta su fuente original. Estudios comparativos sobre fuentes abiertas de uso masivo, como OpenStreetMap y Google Maps, evidencian divergencias espaciales y temporales significativas en cuanto a la cobertura y actualización de las amenidades urbanas (Mara et al., 2025).

Esta heterogeneidad refuerza el imperativo de implementar reglas explícitas de validación topológica, completitud de atributos y control de duplicados dentro del pipeline de procesamiento propuesto, asegurando la consistencia del modelo final.

### 7.6 Interoperabilidad y estándares

La interoperabilidad semántica y sintáctica es el pilar que permite la sinergia entre los múltiples módulos independientes de un gemelo digital. Para evitar los silos de información, la literatura propone el uso de grafos de conocimiento como mecanismo para integrar y enriquecer los datos tridimensionales y bidimensionales de la ciudad (Ding et al., 2023). Este enfoque de interoperabilidad es fundamental como referencia conceptual para este anteproyecto, dado que el modelo de datos estructurado y el dataset resultante deberán ser consumidos eficientemente por algoritmos de enrutamiento y conectividad en el módulo posterior de grafos urbanos (URB-02) del ecosistema RISKTWIN.

### 7.7 Integración y procesos ETL de datos geoespaciales

La orquestación de datos provenientes de repositorios heterogéneos (GeoJSON, Shapefiles, archivos planos CSV y APIs REST) demanda la implementación de flujos de trabajo ETL (Extracción, Transformación y Carga) especializados en el dominio geoespacial. Revisiones exhaustivas sobre la integración de datos a lo largo de todo el ciclo de vida de los gemelos digitales urbanos identifican la carencia de procesos ETL estandarizados y automatizables como una de las principales barreras tecnológicas para la consolidación de datasets interoperables (Jeddoub et al., 2024). El diseño de scripts ETL robustos utilizando librerías de manipulación de datos como GeoPandas integradas con PostGIS permite la homologación de sistemas de referencia espacial y la limpieza sistemática, constituyendo el núcleo operativo de la presente investigación.

### 7.8 IoT, IA y ciudades inteligentes

La convergencia tecnológica entre el Internet de las Cosas (IoT), la Inteligencia Artificial (IA) y los gemelos digitales está redefiniendo el paradigma de las ciudades inteligentes. La revisión sistemática desarrollada por Sacoto-Cabrera et al. (2025) mapea las trayectorias de investigación actuales, demostrando cómo los sensores distribuidos y los modelos predictivos dependen críticamente de infraestructuras de datos subyacentes.

Esta relación evidencia que un dataset urbano multivariable, limpio y bien estructurado no es un fin en sí mismo, sino un medio indispensable; actuará como el sustrato vital (ground truth) para el entrenamiento de los algoritmos de IA y los motores de simulación (módulos URB-04 y URB-05) que dotarán de inteligencia predictiva al gemelo digital.

### 7.9 Artículos científicos similares al tema

El desarrollo metodológico y técnico de esta propuesta de investigación se sustenta en el análisis de trabajos previos que abordan problemáticas equivalentes en la estructuración de información urbana:

- **Benchmark Datasets Multimodales (Wysocki et al., 2026):** En su introducción del conjunto de datos TUM2TWIN, los autores presentan un benchmark a gran escala para gemelos digitales urbanos. Este trabajo valida empíricamente la necesidad crítica de construir conjuntos de datos estandarizados que sirvan de línea base para simulaciones complejas e integración multisensorial. El enfoque metodológico de TUM2TWIN sirve como molde referencial para el diseño del modelo lógico (URB-01) en la zona piloto de Guayaquil.
- **Revisión de Iniciativas de Integración (Jeddoub et al., 2024):** Su investigación evalúa de manera integral el ciclo de vida de los datos en los gemelos digitales, destacando los cuellos de botella en la asimilación de formatos divergentes. Este artículo justifica la necesidad de desplazar el esfuerzo manual hacia pipelines ETL programáticos, validando la aproximación de emplear entornos en Python para automatizar la transformación geométrica y semántica de las fuentes abiertas.
- **Entornos Multi-Base de Datos (ISPRS Archives, 2024):** El estudi aborda los retos arquitectónicos de adaptar estándares semánticos a las demandas del big geodata urbano. Las conclusiones de este trabajo respaldan las decisiones arquitectónicas, específicamente la necesidad de separar las reglas de calidad y trazabilidad de la capa de visualización.

## 8. MARCO METODOLÓGICO

### 8.1 Tipo de Investigación

La investigación es de tipo aplicada y descriptiva, orientada al diseño de un artefacto tecnológico (modelo de datos y dataset urbano) que resuelve una necesidad concreta de integración de datos dentro del proyecto RISKTWIN. Se justifica por la necesidad de producir un resultado utilizable (dataset y documentación) más que de generalizar teóricamente.

### 8.2 Enfoque y Modalidad de Investigación

El enfoque es predominantemente cuantitativo, dado que se trabajará con métricas de calidad de datos (completitud, consistencia geográfica, duplicados, cobertura espacial). La modalidad es de tipo proyecto de desarrollo tecnológico con validación de campo mediante una prueba de integración en una zona urbana piloto.

### 8.3 Fuentes, Técnicas e Instrumentos para la Recolección de Datos

| Tipo de Fuente | Fuente | Técnica | Instrumento |
|---|---|---|---|
| Secundaria | OpenStreetMap | Extracción ETL (API/descarga) | Scripts Python (OSMnx/GeoPandas) |
| Secundaria | Datos municipales abiertos | Descarga y normalización | Scripts ETL Python |
| Secundaria | Puntos de interés (POI) y siniestros/incidentes abiertos | Extracción y geocodificación | GeoPandas / PostGIS |
| Primaria (simulada/documentada) | Aforos simulados o levantados | Simulación documentada o levantamiento de campo | Plantillas de carga / hojas de registro |

### 8.4 Población y Muestra

La población objeto de estudio corresponde al conjunto de capas de datos urbanos disponibles para la zona piloto seleccionada. La muestra estará conformada por los registros geoespaciales, viales, de POI, aforos e incidentes correspondientes a dicha zona piloto, seleccionados mediante muestreo no probabilístico intencional.

### 8.5 Análisis y Tratamiento de la Información

Los datos serán procesados mediante un pipeline ETL en Python (GeoPandas, PostGIS/GeoPackage), aplicando normalización espacio-temporal, validación de coordenadas y reglas de limpieza documentadas. Los resultados se analizarán mediante métricas de calidad de datos (completitud, consistencia geográfica, duplicados, cobertura espacial, trazabilidad de fuente), presentadas en un reporte de calidad y un notebook reproducible.

### 8.6 Matriz de Operacionalización de Variables

| Variable | Dimensión | Indicador | Técnica | Instrumento |
|---|---|---|---|---|
| Calidad del dataset urbano | Completitud | % de campos completos por capa | Análisis descriptivo | Script de validación (Python) |
| Calidad del dataset urbano | Consistencia geográfica | % de registros con coordenadas válidas dentro de la zona piloto | Validación geoespacial | GeoPandas / PostGIS |
| Calidad del dataset urbano | Duplicados | Tasa de registros duplicados detectados | Deduplicación automatizada | Script Python |
| Interoperabilidad | Cobertura espacial | N.º de capas integradas / capas planificadas | Verificación de esquema | Diccionario de datos |
| Interoperabilidad | Trazabilidad de fuente | % de registros con fuente documentada | Auditoría de metadatos | Catálogo de fuentes |

## 9. METODOLOGÍA DE DESARROLLO A EMPLEAR

### 9.1 Justificación de la Metodología

Se propone el uso de la metodología MDA (Model-Driven Architecture), definida por el Object Management Group (OMG). Esta elección se justifica por la naturaleza estructural y la complejidad de los datos que maneja el proyecto dentro del gemelo digital RISKTWIN. Al tratar con el procesamiento espacial de exposición a amenazas, vulnerabilidades y procesos ETL geoespaciales, MDA permite separar la conceptualización del entorno urbano (la lógica y los indicadores) de la infraestructura tecnológica subyacente.

La dependencia de este proyecto con los demás módulos (URB-02 a URB-05) requiere un modelo lógico robusto, estandarizado y altamente interoperable. Utilizar el enfoque guiado por modelos (a través de sus fases CIM, PIM y PSM) asegura que el diccionario de datos y los esquemas espaciales se definan cumpliendo con estándares internacionales (ISO 19115 y OGC) antes de su implementación técnica, garantizando entregas estructuradas (datasets v0.1, documentación, scripts de carga) que sean escalables e independientes de plataformas específicas.

### 9.2 Prácticas Aplicadas

- **Diseño estructurado por niveles de abstracción:** Construcción incremental del sistema transitando por el Modelo Independiente de Computación (CIM) para entender el entorno, el Modelo Independiente de Plataforma (PIM) para estructurar el modelo lógico y diccionario de datos, y el Modelo Específico de Plataforma (PSM) para el diseño final del pipeline ETL y bases de datos.
- **Revisiones y validación de modelos:** Revisiones periódicas de los artefactos de modelado con el tutor líder (Katty) para validar el diseño conceptual y lógico, asegurando un alineamiento exacto del componente espacial con los requerimientos de los módulos URB-02 a URB-05.
- **Gestión de configuración y versiones:** Control de versiones estricto de los modelos de arquitectura, diccionarios de datos y código (scripts ETL) mediante un repositorio Git compartido con todo el proyecto RISKTWIN.
- **Validación geoespacial y aseguramiento de calidad:** Pruebas de validación espacial ejecutadas sobre cada versión del dataset (v0.1, etc.), garantizando que la estructura resultante cumpla con los principios FAIR (Encontrable, Accesible, Interoperable y Reutilizable) y las métricas de evaluación definidas.

### 9.4 Historias de Usuario / Requisitos

| ID | Historia de Usuario | Prioridad | Iteración |
|---|---|---|---|
| HU-01 | Como equipo del módulo de grafos (URB-02), quiero consumir un dataset urbano documentado y validado, para construir el grafo de conectividad sin reprocesar los datos. | Alta | |
| HU-02 | Como investigador del proyecto, quiero un diccionario de datos claro, para entender el significado y origen de cada variable urbana. | Alta | |
| HU-03 | Como desarrollador del pipeline ETL, quiero reglas de limpieza y validación geográfica documentadas, para garantizar la calidad del dataset. | Media | |
| HU-04 | Como equipo de la API integradora (SIS-API-01), quiero plantillas de carga reutilizables, para conectar el dataset urbano al sistema sin trabajo adicional | Media | |

## 10. CRONOGRAMA DE ACTIVIDADES

| Actividad | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|:-:|:-:|:-:|:-:|
| Inventario de fuentes y diccionario de datos | X | | | |
| Diseño del modelo lógico y reglas de calidad | X | X | | |
| Implementación del pipeline ETL (GeoPandas/PostGIS) | | X | X | |
| Construcción y validación del dataset urbano v0.1 (zona piloto) | | | X | X |
| Documentación final y prueba de integración con URB-02 | | | | X |

## 11. PRESUPUESTO Y FINANCIAMIENTO

| Rubro | Descripción | Costo (USD) |
|---|---|---|
| Infraestructura | Hosting/almacenamiento para dataset y base de datos geoespacial | |
| Software | Herramientas y librerías (mayoritariamente open source: Python, GeoPandas, PostGIS) | |
| Otros | | |
| **TOTAL** | | institucional |

*(Los costos están en blanco en el original; la celda del total dice "institucional".)*

## 12. BENEFICIOS ESPERADOS DEL PROYECTO

- Provee a los módulos de grafos, índice de criticidad, IA y simulación del proyecto RISKTWIN un dataset urbano común, documentado y de calidad verificada, reduciendo duplicidad de esfuerzos entre equipos.
- Aporta a la Carrera de Sistemas de la Información un caso de estudio aplicado de integración de datos multimodales para gemelos digitales urbanos, con potencial de reutilización en futuros proyectos de titulación.
- Sienta una base técnica escalable a otras zonas urbanas, favoreciendo la gestión preventiva del riesgo a nivel local.

## 13. DERECHOS DE PROPIEDAD INTELECTUAL

El desarrollo de este trabajo de tesis contempla la generación de resultados susceptibles de protección por Propiedad Intelectual (derechos de autor, patentes, programa de computador).

¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [x] Software (scripts ETL y pipeline de procesamiento de datos)
- [x] Modelo/algoritmo (modelo lógico de datos urbano)
- [x] Manual/documentación técnica (diccionario de datos y catálogo de fuentes)
- [ ] No aplica

## 14. Referencias Bibliográficas

Archives., I. (2024). *Towards a multi-database CityGML environment adapted to big geodata issues of urban digital twins.* Obtenido de https://doi.org/10.5194/isprs-archives-XLVIII-4-W10-2024-101-2024

Buildings. (2024). *Building Digital Twin Data Model Based on Public Data.* Obtenido de https://doi.org/10.3390/buildings14092911

Chen, W. (2025). *Digital Twin-Assisted Urban Resilience: A Data-Driven Framework. Urban Science, 9(1), 33.* Obtenido de https://doi.org/10.3390/urbansci9010033

Costa, D. G. (2024). *Achieving sustainable smart cities through geospatial data-driven approaches.* Obtenido de https://doi.org/10.3390/su16020640

Ding, W. e. (2023). *Integrating 3D City Data through Knowledge Graphs. arXiv.* Obtenido de https://arxiv.org/abs/2310.11555

García, S. (2024). *Enhancing Urban Resilience: Smart City Data Analyses, Forecasts, and Digital Twins. Future Internet, 16(2), 47.* Obtenido de https://doi.org/10.3390/fi16020047

Jeddoub, I. N.-A. (2024). *Data integration across urban digital twin lifecycle: A comprehensive review of current initiatives. Annals of GIS.* Obtenido de https://doi.org/10.1080/19475683.2024.2416135

Mara, F. A. (2025). *The divergent geographies of urban amenities: A data comparison between OpenStreetMap and Google Maps.* Obtenido de https://doi.org/10.3390/su17209016

Mazzetto, S. (2024). *A Review of Urban Digital Twins Integration, Challenges, and Future Directions in Smart City Development. Sustainability.* Obtenido de https://doi.org/10.3390/su16198337

Moreno, L. (2024). *Spatiotemporal Data Integration for Smart City Infrastructure: An ETL Pipeline Approach. Journal of Urban Technology, 31(4), 112-128.* Obtenido de https://doi.org/10.1080/10630732.2024.2198453

Noguera, R.-Z. (2024). *Interoperability in Urban Digital Twins: Semantic Modeling and Geospatial Databases. IEEE Access, 12, 45102-45115.* Obtenido de https://doi.org/10.1109/ACCESS.2024.3351098

Sacoto-Cabrera, e. a. (2025). *AI, and Digital Twins in Smart Cities: A Systematic Review for a Thematic Mapping and Research Agenda. Smart Cities.* Obtenido de https://doi.org/10.3390/smartcities8050175

Wang, e. a. (2024). *Digital twin approach for enhancing urban resilience: A cycle between virtual space and the real world.* Obtenido de https://doi.org/10.1016/j.rcns.2024.06.002

Wysocki, O. e. (2026). *TUM2TWIN: Introducing the large-scale multimodal urban digital twin benchmark dataset. ISPRS Journal of Photogrammetry and Remote Sensing, 232, 810–830.* Obtenido de https://doi.org/10.1016/j.isprsjprs.2025.12.013

---

## RÚBRICA DE EVALUACIÓN

> **Nota:** página escaneada con anotaciones manuscritas; transcripción aproximada.

| Criterio | Nota evaluador | Nota máxima |
|---|:-:|:-:|
| Planteamiento y formulación del problema; Innovación (aporte novedoso o mejora significativa) | 1 | 1 |
| Alcance / Justificación | 1 | 1 |
| Objetivos (General y Específicos) coherentes | 0.8 | 1 |
| Marco Teórico / Marco Metodológico / Referencias Bibliográficas | 0.8 | 1 |
| Metodología de Desarrollo | 0.8 | 1 |
| *(Subtotal Estructura)* | | 5 |
| Cronograma / Presupuesto | 1 | 1 |
| Manejo claro de las ideas / Beneficios esperados del proyecto | 1 | 1 |
| Claridad y coherencia en la redacción | 1 | 1 |
| Referentes teóricos sustentados | 1 | 1 |
| Argumentos para una propuesta | 1 | 1 |
| *(Subtotal Aspectos de Fondo)* | | 5 |
| **NOTA SOBRE 10** | **9.6** | **10** |

## FIRMAS

| Nombre del estudiante | C.I. |
|---|---|
| Nivela Mejía José Andrés | 0930832522 |
| Suastegui Josué | 0924998974 |

Los campos "Nombre Docente Revisor Anteproyecto" y su C.I. aparecen en blanco. Al pie hay firmas manuscritas de los dos estudiantes y de dos docentes (PhD. Juan Carlos García y LSI. Katty Lino).
