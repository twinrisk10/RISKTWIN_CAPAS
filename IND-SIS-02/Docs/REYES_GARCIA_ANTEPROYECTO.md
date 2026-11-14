# UNIVERSIDAD DE GUAYAQUIL
## FACULTAD DE INGENIERÍA INDUSTRIAL

# ANTEPROYECTO DE TRABAJO DE TITULACIÓN

## Datos Generales

| | |
|---|---|
| **CARRERA** | Sistemas de la Información |
| **FECHA** | 26/08/2026 |

| | Apellidos | Nombres |
|---|---|---|
| **ESTUDIANTE 1** | Reyes Salinas | Alberto Renan |
| **ESTUDIANTE 2** | García Anzules | Suanny Nayely |

**Correo electrónico institucional y personal:**

- alberto.reyess@ug.edu.ec
- Theromilju_renan@hotmail.com
- suanny.garciaa@ug.edu.ec
- sgarciaanzules@gmail.com

**Teléfono:** 0996474673 / 0967693238

## Tema

**TEMA:** Dashboard UX para priorización de riesgos industriales y toma de decisiones preventivas

**LÍNEA DE INVESTIGACIÓN:**

- [ ] Sostenibilidad, derechos y tecnologías en el ordenamiento territorial, ambiente de la construcción y arquitectura.
- [ ] Desarrollo local y emprendimiento socio económico sostenible.
- [x] Ciencias básicas, bioconocimiento y desarrollo industrial. *(resaltado en amarillo)*
- [ ] Salud humana, animal y del ambiente.
- [ ] Tecnologías agrícolas y de la agricultura.
- [ ] Entornos virtuales de aprendizaje y tecnologías educativas.

**COBERTURA:**

- [ ] Nacional
- [ ] Provincial
- [x] Local *(resaltado en amarillo)*
- [ ] Otros

---

## 1. PLANTEAMIENTO Y FORMULACIÓN DEL PROBLEMA

### 1.1. Antecedentes

La transformación digital en el sector industrial ha favorecido la incorporación de sistemas capaces de recopilar, procesar y representar grandes volúmenes de información relacionada con procesos, equipos, eventos e indicadores de seguridad. En este escenario, los dashboards se han consolidado como herramientas de apoyo para presentar datos relevantes de manera estructurada y facilitar su interpretación. No obstante, su utilidad no depende únicamente de la cantidad de información disponible, sino también de la forma en que esta se organiza visualmente y de la facilidad con la que los usuarios pueden identificar situaciones que requieren atención. Por ello, los enfoques centrados en el usuario han adquirido importancia en el desarrollo de soluciones digitales aplicadas a entornos industriales (Asad et al., 2023).

Los avances vinculados con los gemelos digitales también han impulsado nuevas formas de interacción entre los sistemas tecnológicos y las personas encargadas de supervisar los procesos industriales. Krupas et al. (2024) sostienen que las soluciones orientadas a la colaboración entre humanos y sistemas digitales deben incorporar mecanismos de interacción comprensibles, accesibles y adaptados a las necesidades de los usuarios. Desde esta perspectiva, la efectividad de una herramienta industrial no se limita a la precisión de los datos procesados, sino que también depende de la capacidad del usuario para comprenderlos y utilizarlos oportunamente durante la toma de decisiones.

En el ámbito de la visualización industrial, un estudio publicado en Computers y Industrial Engineering en 2024 presentó el diseño de un dashboard basado en gemelos digitales para una línea de ensamblaje flexible. La propuesta permitió integrar información procedente de diferentes componentes del sistema productivo y representarla mediante una interfaz centralizada para facilitar el seguimiento de las operaciones.

Este antecedente demuestra que los dashboards pueden contribuir a sintetizar información compleja y apoyar el monitoreo industrial. Sin embargo, su orientación se concentra principalmente en el seguimiento del funcionamiento del sistema y no específicamente en determinar qué recursos visuales permiten establecer prioridades entre diferentes niveles de riesgo.

La usabilidad constituye otro componente relevante dentro del diseño de dashboards. Almasi et al. (2023), mediante una revisión sistemática, analizaron distintos métodos utilizados para evaluar este tipo de interfaces e identificaron criterios relacionados con facilidad de uso, utilidad, aprendizaje, satisfacción y desempeño durante las tareas. Entre los instrumentos utilizados se encuentra la System Usability Scale (SUS), que permite obtener una valoración general de la experiencia de interacción. Estos aportes evidencian que la evaluación de un dashboard debe considerar no solo su funcionamiento técnico, sino también la capacidad de los usuarios para interpretar la información, completar tareas y reconocer correctamente los elementos que requieren una respuesta.

De manera complementaria, Chen et al. (2024) desarrollaron un dashboard geoespacial integrado con tecnologías de gemelo digital para representar vulnerabilidades y condiciones de riesgo. La integración de distintas capas de información permitió visualizar zonas con diferentes niveles de afectación y apoyar procesos de análisis y planificación. Este antecedente demuestra la utilidad de las representaciones visuales para comprender escenarios complejos; sin embargo, todavía resulta necesario profundizar en la manera en que elementos como mapas de zonas críticas, indicadores de frecuencia, severidad, niveles de exposición y alertas visuales pueden influir en la capacidad de los usuarios para establecer prioridades dentro de un contexto industrial.

A partir de los antecedentes revisados, se identifica que la literatura ha avanzado en el desarrollo de dashboards, gemelos digitales, interfaces de visualización y métodos para evaluar su usabilidad.

No obstante, persiste un vacío relacionado con la identificación de qué visualizaciones facilitan de manera más clara la priorización de riesgos industriales por parte de usuarios técnicos y operativos. En particular, se requiere analizar si determinadas formas de presentar zonas críticas, frecuencia y severidad de eventos, indicadores de exposición y recomendaciones preventivas permiten reducir el tiempo de interpretación, disminuir errores y mejorar la claridad al establecer prioridades. Frente a esta necesidad, el anteproyecto plantea el diseño y evaluación de un dashboard UX orientado a facilitar la interpretación de riesgos y fortalecer la toma de decisiones preventivas en entornos industriales.

### 1.2. Planteamiento del problema

En los entornos industriales se generan datos relacionados con eventos de seguridad, niveles de exposición, frecuencia de incidentes, severidad de consecuencias y condiciones asociadas a distintas zonas operativas. Aunque esta información resulta relevante para la gestión preventiva, su disponibilidad no garantiza que los usuarios puedan interpretarla con rapidez ni establecer correctamente cuáles riesgos requieren atención prioritaria. Cuando los datos se presentan de manera dispersa, poco jerarquizada o mediante visualizaciones que no responden a las necesidades de los usuarios, aumenta la dificultad para reconocer situaciones críticas y tomar decisiones oportunas.

Los usuarios técnicos y operativos requieren identificar, dentro de un conjunto amplio de información, qué eventos representan una mayor amenaza, dónde se concentran las condiciones críticas y qué acciones preventivas deben considerarse. Sin embargo, los dashboards industriales pueden priorizar la cantidad de indicadores mostrados sobre la claridad de la información, lo que dificulta distinguir los elementos realmente relevantes para una determinada tarea. Esta situación puede generar mayores tiempos de interpretación, errores durante la identificación de prioridades y dificultades para comprender la relación entre frecuencia, severidad, exposición y nivel de riesgo.

El problema central se relaciona, por tanto, con la falta de claridad respecto a qué tipos de visualizaciones permiten a los usuarios técnicos y operativos interpretar y priorizar de manera más efectiva los riesgos industriales. La presentación de información mediante mapas de zonas críticas, indicadores, alertas, niveles de severidad u otros recursos visuales puede influir en la rapidez y precisión con que se reconocen las condiciones que requieren intervención. Por esta razón, el diseño de la interfaz debe considerar no solo la representación de los datos, sino también criterios de experiencia de usuario, usabilidad y utilidad operativa.

Abordar esta problemática resulta relevante porque una adecuada priorización permite dirigir la atención hacia los riesgos que requieren una respuesta preventiva con mayor urgencia. En este contexto, el desarrollo y evaluación de un dashboard UX permitirá analizar la claridad de diferentes visualizaciones y determinar su utilidad para apoyar la interpretación de riesgos y la toma de decisiones preventivas dentro del entorno industrial.

### 1.3. Causas

- Presentación dispersa o poco jerarquizada de la información relacionada con los riesgos industriales.
- Uso de visualizaciones que no siempre responden a las necesidades de usuarios técnicos y operativos.
- Dificultad para integrar en una misma interfaz información sobre frecuencia, severidad, exposición y zonas críticas.
- Falta de criterios de experiencia de usuario orientados específicamente a facilitar la priorización de riesgos.
- Escasa evaluación de la usabilidad y utilidad operativa de los dashboards empleados para apoyar decisiones preventivas.

### 1.4. Consecuencias

- Mayor tiempo requerido para identificar los riesgos que necesitan atención prioritaria.
- Posibilidad de cometer errores durante la interpretación y clasificación de situaciones críticas.
- Dificultad para reconocer zonas, eventos o condiciones con mayores niveles de riesgo.
- Sobrecarga de información para usuarios técnicos y operativos durante el análisis de datos.
- Limitaciones para utilizar la información disponible como apoyo oportuno en la toma de decisiones preventivas.

### 1.5. Formulación del problema

¿Qué visualizaciones facilitan la priorización de riesgos industriales por parte de usuarios técnicos y operativos?

## 2. ALCANCE

El proyecto comprende el diseño, implementación y evaluación de un dashboard UX orientado a la visualización y priorización de riesgos industriales. La solución integrará información relacionada con zonas críticas, frecuencia y severidad de eventos, indicadores de exposición y recomendaciones preventivas, con el propósito de facilitar la interpretación de los riesgos por parte de usuarios técnicos y operativos.

Para su desarrollo se elaborarán requisitos de usuario, wireframes, mapa de navegación y un prototipo interactivo, que posteriormente servirán como base para la construcción del dashboard funcional.

El dashboard utilizará como insumos el dataset SI-02, los indicadores SI-01, información proveniente de la arquitectura IND-SIS-01, mapas o planos por zonas y catálogos de riesgos disponibles. La evaluación se realizará mediante tareas representativas con usuarios técnicos u operativos, considerando métricas como tiempo de ejecución, tasa de éxito, errores, satisfacción, utilidad percibida y claridad de priorización. Asimismo, se emplearán instrumentos de evaluación de usabilidad como SUS o UEQ. El proyecto se desarrollará durante el período académico establecido para la ejecución del anteproyecto y culminará con una versión funcional del dashboard, un reporte de evaluación UX y recomendaciones de rediseño basadas en los resultados obtenidos.

**El proyecto NO incluye:**

- El desarrollo de nuevos sensores, dispositivos de adquisición de datos o sistemas físicos destinados a la detección de riesgos industriales.
- La construcción desde cero de la arquitectura, API o fuentes de datos utilizadas por el dashboard, debido a que estas serán consumidas como insumos del sistema.
- La implementación de modelos predictivos destinados a anticipar accidentes o eventos industriales futuros.
- La sustitución de los procedimientos, protocolos o decisiones de seguridad establecidos por las organizaciones industriales.
- El despliegue definitivo del dashboard como sistema institucional de producción, debido a que el alcance se concentra en el diseño, prototipado, implementación funcional y evaluación con usuarios.

## 3. JUSTIFICACIÓN DE LA INVESTIGACIÓN

### 3.1. Justificación teórica

La investigación se justifica teóricamente por la necesidad de profundizar en la relación entre la experiencia de usuario, la visualización de información y la priorización de riesgos dentro de entornos industriales.

Los estudios relacionados con tecnologías industriales centradas en las personas señalan que la interacción entre el usuario y los sistemas digitales constituye un elemento relevante para facilitar la interpretación de información compleja y apoyar actividades operativas (Asad et al., 2023). Desde esta perspectiva, un dashboard no debe limitarse a presentar indicadores, sino que debe organizar la información de acuerdo con las necesidades cognitivas y operativas de quienes deben utilizarla.

De igual manera, la evaluación de la usabilidad permite determinar si una interfaz facilita el cumplimiento de tareas y la comprensión de la información presentada. Almasi et al. (2023) identificaron que los dashboards pueden evaluarse mediante criterios relacionados con facilidad de uso, utilidad, satisfacción y desempeño del usuario. En consecuencia, el proyecto aportará conocimiento sobre la manera en que diferentes recursos visuales, como zonas críticas, niveles de severidad, frecuencia de eventos e indicadores de exposición, pueden contribuir a establecer prioridades entre distintos riesgos industriales.

En este contexto, los gemelos digitales constituyen un referente teórico relevante debido a que permiten representar digitalmente sistemas, procesos o activos físicos y vincularlos con información procedente del entorno industrial. Su desarrollo ha fortalecido la integración entre datos operativos, modelos digitales e interfaces orientadas al usuario, favoreciendo nuevas formas de supervisión y análisis de los procesos. Krupas et al. (2024) señalan que los enfoques de gemelos digitales centrados en las personas requieren mecanismos de interacción que faciliten la comprensión y utilización de la información. Esta perspectiva sustenta el desarrollo de un dashboard UX capaz de transformar datos industriales en visualizaciones útiles para la identificación y priorización de riesgos.

### 3.2. Justificación práctica

Desde una perspectiva práctica, el proyecto busca proporcionar a usuarios técnicos y operativos una herramienta que facilite la identificación de situaciones que requieren atención prioritaria. La concentración de información sobre riesgos dentro de una interfaz estructurada puede reducir el esfuerzo necesario para consultar diferentes fuentes y favorecer una interpretación más rápida de las condiciones presentes en las distintas zonas de operación.

El dashboard permitirá representar de manera integrada los principales indicadores asociados con los riesgos y presentar recomendaciones preventivas que sirvan como apoyo para la toma de decisiones. Su evaluación con usuarios permitirá identificar dificultades de interacción, errores de interpretación y elementos visuales que requieran mejoras. De esta manera, los resultados podrán contribuir al desarrollo de interfaces industriales más comprensibles y orientadas a las necesidades reales de quienes participan en actividades de supervisión y prevención.

Desde su aplicación industrial, la integración de información asociada con gemelos digitales permite disponer de representaciones actualizadas de procesos y condiciones operativas que pueden ser utilizadas mediante dashboards para apoyar actividades de supervisión. Wang y Lee (2024) demostraron que un dashboard basado en gemelo digital puede centralizar y representar información procedente de una línea de ensamblaje flexible, facilitando el seguimiento de sus operaciones. En el presente proyecto, este enfoque permitirá aprovechar datos e indicadores provenientes de los sistemas relacionados para presentar zonas críticas, niveles de severidad, frecuencia de eventos y exposición, proporcionando a los usuarios una visión organizada que favorezca decisiones preventivas más oportunas.

### 3.3. Justificación metodológica

La investigación utilizará una combinación de Design Science Research, Human-Centred Design y evaluación de usabilidad, debido a que el proyecto requiere tanto la construcción de una solución tecnológica como su valoración mediante la interacción con usuarios. Design Science Research permitirá orientar el proceso de creación y evaluación del dashboard como una solución destinada a responder al problema identificado, mientras que Human-Centred Design permitirá incorporar las necesidades de usuarios técnicos y operativos durante el diseño de la interfaz.

La evaluación combinará información cuantitativa y cualitativa mediante pruebas basadas en tareas, instrumentos SUS o UEQ y métricas como tiempo de ejecución, tasa de éxito, errores, satisfacción, utilidad percibida y claridad de priorización. Este enfoque permitirá valorar el funcionamiento del dashboard desde diferentes dimensiones y generar recomendaciones de rediseño sustentadas en evidencia obtenida durante las pruebas con usuarios.

Metodológicamente, la vinculación con los gemelos digitales industriales permitirá trabajar con información proveniente de fuentes y componentes relacionados con la representación digital del entorno operativo, sin que el proyecto tenga como finalidad desarrollar un gemelo digital desde cero. Asad et al. (2023) destacan que los sistemas industriales centrados en las personas requieren integrar tecnología, datos e interacción humana para generar soluciones que respondan a las necesidades reales de los usuarios. Por ello, el dashboard será diseñado como una capa de interacción que utilizará los datos disponibles para construir visualizaciones y posteriormente evaluar, mediante tareas controladas, la capacidad de los usuarios para identificar, interpretar y priorizar los riesgos presentados.

## 4. OBJETIVO GENERAL

Diseñar y evaluar un dashboard industrial para visualizar, interpretar y priorizar riesgos con enfoque de utilidad operativa.

## 5. OBJETIVOS ESPECÍFICOS

- Identificar los requisitos de usuarios técnicos y operativos y los criterios de visualización necesarios para representar zonas críticas, frecuencia, severidad e indicadores de exposición asociados con riesgos industriales.
- Diseñar e implementar un dashboard UX funcional que integre información sobre riesgos industriales mediante visualizaciones orientadas a facilitar su interpretación, priorización y la presentación de recomendaciones preventivas.
- Evaluar la usabilidad y utilidad operativa del dashboard mediante pruebas con usuarios, considerando métricas de tiempo de tarea, tasa de éxito, errores, satisfacción y claridad de priorización, con el fin de establecer recomendaciones de mejora.

## 6. HIPÓTESIS DE INVESTIGACIÓN

No aplica. La investigación se orienta al diseño y evaluación de un dashboard UX para la priorización de riesgos industriales, mediante pruebas de usabilidad con usuarios técnicos y operativos. El estudio busca determinar qué visualizaciones facilitan la interpretación y priorización de riesgos a partir de métricas de desempeño, usabilidad y utilidad percibida.

Debido a que no se parte de evidencias obtenidas previamente en un lugar específico que permitan establecer y contrastar una relación causal entre variables, no se plantea una hipótesis de investigación.

## 7. MARCO TEÓRICO Y REFERENCIAL REDUCIDO

### 7.1. Dashboards industriales y visualización de datos

Los dashboards industriales son interfaces digitales diseñadas para integrar, sintetizar y representar información procedente de procesos, equipos y sistemas de producción. Su propósito consiste en transformar datos operativos en representaciones visuales que permitan reconocer tendencias, anomalías y condiciones que requieren atención. En este sentido, el dashboard funciona como un punto de interacción entre los datos generados por el entorno industrial y los usuarios responsables de supervisarlos. Wang y Lee (2024) desarrollaron un dashboard basado en gemelo digital para una línea de ensamblaje flexible, demostrando que la integración de datos dentro de una interfaz centralizada puede favorecer el seguimiento y análisis de las operaciones industriales.

La eficacia de un dashboard depende en gran medida de la forma en que se estructura y presenta la información. Elementos como gráficos, mapas, indicadores, tablas, alertas y escalas visuales deben organizarse de acuerdo con la importancia de los datos y las tareas que realiza el usuario. Liu (2025) destaca que los elementos de diseño visual influyen en la evaluación de las interfaces digitalizadas, debido a que aspectos como la organización, jerarquía y representación de la información condicionan la manera en que esta puede ser interpretada. Por esta razón, el diseño visual debe responder a criterios funcionales y no únicamente estéticos, especialmente cuando la información presentada sirve de apoyo para decisiones relacionadas con situaciones de riesgo.

En el contexto del presente proyecto, la visualización adquiere especial importancia debido a que el dashboard deberá representar zonas críticas, frecuencia y severidad de eventos, indicadores de exposición y recomendaciones preventivas. Chen et al. (2024) demostraron que la integración de dashboards geoespaciales con diferentes capas de información permite representar vulnerabilidades y favorecer la comprensión de escenarios de riesgo. A partir de este enfoque, la visualización industrial puede utilizarse para organizar la información según su nivel de criticidad, facilitando que los usuarios técnicos y operativos identifiquen las condiciones que requieren una intervención prioritaria.

Elhabashy et al. (2026) plantean que la visualización de datos en entornos de Industria 4.0 permite transformar grandes volúmenes de información de producción en elementos comprensibles que apoyan el análisis y la toma de decisiones. En su estudio desarrollado en una empresa fabricante de neumáticos, los autores implementaron un marco de visualización basado en dashboards para analizar indicadores de eficiencia de los equipos, identificar pérdidas operativas y facilitar intervenciones correctivas. Estos resultados evidencian que la organización adecuada de los datos mediante recursos gráficos puede reducir el riesgo de que información relevante pase desapercibida y favorecer una interpretación más directa de las condiciones operativas, principio que resulta aplicable a un dashboard destinado a identificar y priorizar riesgos industriales.

Por otra parte, Lin et al. (2025) destacan que los dashboards de desempeño constituyen un recurso importante para comunicar datos y supervisar el funcionamiento de organizaciones y entornos industriales. A partir del análisis de 114 dashboards y de la participación de expertos de la industria, los autores identificaron patrones de diseño orientados a mejorar la creación y adaptación de estas interfaces según las necesidades de los usuarios. Este planteamiento refuerza la importancia de considerar no solamente los datos que serán representados, sino también la estructura visual, la distribución de componentes y la facilidad para modificar la interfaz de acuerdo con el contexto de uso. En el presente proyecto, estos criterios resultan relevantes para diseñar visualizaciones que permitan distinguir con claridad los riesgos que requieren atención prioritaria.

### 7.2. Experiencia de usuario (UX) en sistemas industriales

La experiencia de usuario comprende las percepciones, respuestas y valoraciones que se generan durante la interacción de una persona con un producto o sistema digital. En los entornos industriales, este concepto adquiere características particulares, debido a que las interfaces se utilizan para ejecutar tareas relacionadas con monitoreo, supervisión y toma de decisiones. Asad et al. (2023) señalan que los sistemas industriales centrados en las personas deben considerar las necesidades, capacidades y condiciones de interacción de los usuarios. Esta perspectiva resulta fundamental para evitar que el avance tecnológico incremente innecesariamente la complejidad de las tareas realizadas por operadores y personal técnico.

La incorporación de principios de UX en sistemas industriales implica diseñar interfaces comprensibles, accesibles y coherentes con el contexto en el que serán utilizadas. Krupas et al. (2024) destacan que la evolución hacia una industria centrada en las personas requiere fortalecer los mecanismos de interacción entre usuarios y sistemas digitales. Esto supone considerar no solamente la disponibilidad de información, sino también cómo se comunica, qué acciones permite realizar y qué esfuerzo demanda su interpretación. Una interfaz industrial que presenta datos sin una estructura adecuada puede aumentar la carga cognitiva del usuario y dificultar la identificación de información relevante durante situaciones que requieren respuestas oportunas.

Los estudios recientes sobre interacción humano-computador en contextos industriales continúan reforzando esta orientación. Hamdani et al. (2025) proponen un enfoque adaptativo de interacción para el contexto de Industria 5.0 en el que la experiencia del usuario constituye una dimensión relevante para adaptar los sistemas a diferentes condiciones operativas. Para el dashboard planteado en esta investigación, la UX permitirá orientar decisiones sobre jerarquía de información, navegación, distribución de indicadores y presentación de alertas. De esta manera, el diseño buscará que usuarios técnicos y operativos puedan localizar e interpretar los riesgos con el menor esfuerzo posible y con una estructura acorde con las tareas que deben realizar.

### 7.3. Visual Analytics aplicado a la gestión de riesgos

Visual Analytics integra técnicas de análisis de datos con representaciones visuales interactivas para facilitar la exploración, interpretación y comprensión de información compleja. Su utilidad radica en que permite combinar la capacidad de procesamiento de los sistemas informáticos con la capacidad humana para identificar patrones, relaciones y anomalías. Dentro de un entorno industrial, este enfoque puede utilizarse para analizar eventos, indicadores de exposición, condiciones operativas y niveles de severidad, presentando los resultados mediante recursos gráficos que faciliten su comprensión. De esta manera, la información deja de observarse como registros aislados y pasa a formar parte de una estructura visual orientada al análisis.

El desarrollo reciente de Visual Analytics en aplicaciones industriales muestra una tendencia hacia interfaces que mantienen al usuario dentro del proceso de interpretación. Kucher (2025) señala que las herramientas de Visual Analytics pueden apoyar la comprensión de resultados obtenidos mediante sistemas inteligentes y permitir evaluaciones centradas en la interacción humana. Esta característica resulta relevante cuando la información es compleja o cuando existen diferentes factores que deben considerarse simultáneamente. Por ello, un dashboard orientado a riesgos industriales puede utilizar filtros, gráficos comparativos, mapas, indicadores de criticidad y mecanismos interactivos para permitir que el usuario explore los datos antes de establecer una prioridad.

La aplicación de Visual Analytics también permite integrar componentes espaciales y temporales dentro del análisis de riesgos. Chen et al. (2024) utilizaron un dashboard geoespacial para representar vulnerabilidades de infraestructura en diferentes escalas, facilitando una visión conjunta de las condiciones analizadas. En el presente proyecto, este principio puede trasladarse al contexto industrial mediante la representación de zonas críticas y su relación con frecuencia, severidad y exposición. La combinación de estos elementos permitirá analizar no solamente la existencia de un riesgo, sino también su ubicación y nivel de importancia, proporcionando una base visual para establecer prioridades preventivas.

### 7.4. Priorización y gestión de riesgos industriales

La gestión de riesgos industriales comprende procesos destinados a identificar, analizar, valorar y tratar situaciones capaces de afectar a personas, instalaciones, procesos o recursos de una organización. Dentro de este proceso, la priorización permite establecer qué riesgos requieren una intervención más inmediata en función de factores como frecuencia, severidad y exposición. Cuando existen numerosos eventos o indicadores, resulta necesario establecer mecanismos que permitan diferenciar las situaciones críticas de aquellas que presentan menor nivel de urgencia. Por esta razón, la calidad de la información y su forma de representación constituyen elementos importantes dentro del proceso de valoración y toma de decisiones.

Los dashboards pueden apoyar este proceso mediante recursos visuales que destaquen diferencias entre niveles de riesgo. Liu (2025) plantea que la evaluación de interfaces de visualización debe considerar la importancia relativa de sus elementos y la forma en que estos permiten organizar la información. Aplicado a la gestión de riesgos, este principio implica evitar que todos los indicadores tengan el mismo peso visual, debido a que una presentación sin jerarquías puede dificultar la identificación de situaciones prioritarias. El empleo de escalas de severidad, ordenamiento por criticidad, mapas de zonas y alertas puede contribuir a orientar la atención hacia aquellos eventos que requieren una revisión inmediata.

La priorización no debe depender exclusivamente de algoritmos o de una clasificación automática, puesto que los usuarios técnicos y operativos mantienen un papel relevante en la interpretación del contexto. Asad et al. (2023) sostienen que los enfoques industriales centrados en las personas buscan integrar las capacidades tecnológicas con la experiencia y conocimiento de los usuarios. En consecuencia, el dashboard propuesto actuará como una herramienta de apoyo y no como un sustituto de la decisión humana. Su propósito será organizar la información de riesgos de forma comprensible, permitiendo que el usuario determine qué situaciones requieren mayor atención y utilice las recomendaciones preventivas como apoyo para definir posibles acciones.

### 7.5. Usabilidad y toma de decisiones preventivas

La usabilidad permite evaluar en qué medida una interfaz puede ser utilizada para alcanzar determinados objetivos de manera efectiva, eficiente y satisfactoria. En los dashboards, esta característica es especialmente importante porque una interfaz puede disponer de información técnicamente correcta y, aun así, presentar dificultades para su interpretación. Almasi et al. (2023), mediante una revisión sistemática, identificaron distintos instrumentos y criterios utilizados para evaluar dashboards, incluyendo dimensiones relacionadas con utilidad, facilidad de uso, aprendizaje y satisfacción. También identificaron el empleo de instrumentos estandarizados como la System Usability Scale para valorar la percepción del usuario respecto a una interfaz.

La evaluación de la usabilidad debe complementarse con métricas obtenidas durante la realización de tareas. El tiempo requerido, la tasa de éxito, los errores cometidos y la capacidad para localizar información permiten determinar si una determinada estructura visual facilita o dificulta el trabajo del usuario. Almasi et al. (2023) señalan que la evaluación de dashboards requiere seleccionar instrumentos adecuados según las características y objetivos de la interfaz analizada. En el presente proyecto, estas mediciones permitirán comparar el desempeño de los usuarios frente a las visualizaciones utilizadas y determinar si el dashboard facilita realmente la identificación y priorización de riesgos industriales.

La relación entre usabilidad y toma de decisiones preventivas se encuentra en la capacidad de la interfaz para transformar información disponible en elementos que puedan ser comprendidos y utilizados oportunamente. Krupas et al. (2024) destacan la necesidad de fortalecer la interacción entre las personas y los sistemas digitales dentro de entornos industriales centrados en el ser humano. Por esta razón, el dashboard será evaluado no solamente por su funcionamiento técnico, sino también por la utilidad percibida y la claridad con que permite establecer prioridades. Los resultados de estas pruebas servirán para identificar dificultades de interacción y formular recomendaciones de rediseño orientadas a mejorar el apoyo que la interfaz proporciona durante la toma de decisiones preventivas.

La usabilidad constituye un componente esencial en el diseño de dashboards, debido a que permite determinar si una interfaz puede ser utilizada de manera efectiva, eficiente y satisfactoria para alcanzar determinados objetivos. En sistemas donde se presentan grandes cantidades de información, una adecuada organización visual puede facilitar la localización de datos relevantes y disminuir dificultades durante la interacción. Almasi et al. (2023) identificaron que la evaluación de dashboards debe considerar aspectos como facilidad de uso, utilidad, capacidad de aprendizaje, adecuación a las tareas, satisfacción y características de la interfaz. Por esta razón, la usabilidad del dashboard industrial debe analizarse considerando tanto la percepción de los usuarios como su capacidad para interpretar correctamente los indicadores de riesgo y completar las tareas propuestas.

La usabilidad mantiene una relación directa con la experiencia de usuario (UX), debido a que la interacción no depende únicamente del funcionamiento técnico del sistema, sino también de la manera en que las personas perciben, comprenden y utilizan la información presentada. Hjelle et al. (2024), mediante un estudio experimental con visualizaciones de dashboards, determinaron que características de la información como su formato, actualidad y completitud influyen en la satisfacción del usuario y en la complejidad percibida de las tareas, factores que posteriormente repercuten en la calidad de las decisiones. En un contexto de riesgos industriales, estos hallazgos adquieren relevancia porque la claridad de las visualizaciones puede favorecer que el usuario diferencie condiciones críticas, interprete los niveles de riesgo y establezca prioridades con mayor precisión.

En los sistemas industriales, la relación entre UX y toma de decisiones preventivas adquiere mayor importancia debido a que los operadores interactúan con información compleja en escenarios donde pueden existir implicaciones relacionadas con seguridad, continuidad operacional y desempeño. Kant et al. (2025) sostienen que el diseño de interfaces humano-máquina para manufactura inteligente debe considerar la experiencia del operador, la complejidad de la información y procesos de diseño centrados en las personas para contribuir a la confiabilidad, mantenibilidad, disponibilidad y seguridad de los sistemas. En consecuencia, el dashboard propuesto deberá procurar que los usuarios identifiquen rápidamente zonas críticas, niveles de severidad, frecuencia de eventos e indicadores de exposición, de manera que la interfaz funcione como apoyo para la toma de decisiones preventivas y no como una fuente adicional de complejidad.

### 7.6. Diseño Centrado en el Usuario (UCD) aplicado a interfaces industriales

El Diseño Centrado en el Usuario, denominado UCD por sus siglas en inglés, constituye un enfoque en el cual las características, necesidades, tareas y contexto de los usuarios se consideran durante las diferentes etapas del desarrollo de un sistema. En entornos industriales, su aplicación resulta relevante porque los usuarios técnicos y operativos presentan conocimientos, responsabilidades y necesidades de información que pueden diferir de las consideradas inicialmente por los desarrolladores. Nunes et al. (2024) demostraron que el diseño de soluciones para sistemas de control industrial requiere comprender de manera explícita a los usuarios y sus procesos de decisión, incorporando su participación mediante entrevistas, definición de perfiles, elaboración de personas y desarrollo iterativo de wireframes. Este enfoque permite reducir el riesgo de construir interfaces técnicamente funcionales que no respondan adecuadamente a las condiciones reales de operación.

La aplicación del UCD se desarrolla mediante un proceso iterativo en el que los prototipos son revisados y modificados a partir de la retroalimentación obtenida de los usuarios y expertos. Dougherty et al. (2025) utilizaron sesiones de diseño centrado en el usuario para desarrollar un dashboard electrónico y posteriormente complementaron el proceso con evaluaciones de expertos y análisis heurísticos de usabilidad. Los resultados permitieron realizar modificaciones relacionadas con diseño visual, navegación, filtros, clasificación de información y correspondencia entre la interfaz y el contexto real de uso. Este antecedente evidencia que involucrar a los usuarios durante el diseño permite identificar problemas antes de implementar una versión definitiva y favorece la construcción de dashboards ajustados a las tareas que deben realizarse.

En el presente proyecto, el UCD permitirá orientar el desarrollo del dashboard desde la identificación inicial de requisitos hasta la evaluación del prototipo funcional. Se deberán considerar las necesidades de usuarios técnicos y operativos para definir la estructura de navegación, jerarquía de indicadores, representación de zonas críticas, niveles de severidad y mecanismos para mostrar recomendaciones preventivas. Nunes et al. (2024) señalan que la iteración entre expertos y desarrolladores permite capturar progresivamente las necesidades reales de quienes utilizarán una solución industrial y transformar esa información en elementos visuales y funcionales pertinentes. Por esta razón, los wireframes, el prototipo interactivo y el dashboard funcional deberán revisarse de manera progresiva antes de efectuar la evaluación final con usuarios.

### 7.7. Heurísticas de Nielsen para la evaluación de interfaces

Las heurísticas de Nielsen constituyen principios ampliamente utilizados para detectar problemas de usabilidad en interfaces digitales. Estas consideran aspectos como visibilidad del estado del sistema, correspondencia entre el sistema y el mundo real, control y libertad del usuario, consistencia, prevención de errores, reconocimiento antes que recuerdo, flexibilidad, diseño estético y minimalista, recuperación ante errores y ayuda disponible. Liu y Yang (2025) integraron los principios de Nielsen dentro de un modelo sistemático para evaluar visualizaciones y demostraron que estas heurísticas continúan siendo pertinentes para analizar interfaces caracterizadas por grandes volúmenes de información y elevados niveles de interacción. Su utilización permite valorar la interfaz desde criterios definidos y reconocer aquellos componentes que podrían dificultar la comprensión o el uso del sistema.

La evaluación heurística resulta particularmente útil durante el desarrollo de dashboards porque permite identificar deficiencias antes de realizar pruebas completas con los usuarios finales. Dougherty et al. (2025) emplearon una lista de evaluación basada en las diez heurísticas de Nielsen para analizar un dashboard y clasificar los problemas encontrados según su nivel de severidad. Entre los aspectos evaluados se consideraron la correspondencia entre el sistema y el mundo real, la organización espacial, la codificación de información y otros criterios de interacción. Este procedimiento permitió introducir modificaciones de diseño de manera iterativa, lo que demuestra que la evaluación heurística puede complementar las pruebas realizadas posteriormente con usuarios y contribuir a mejorar la calidad de una interfaz antes de su implementación definitiva.

La aplicación de estas heurísticas dentro del dashboard de riesgos industriales permitirá revisar aspectos directamente relacionados con la interpretación y priorización de información. Se deberá verificar que los indicadores sean comprensibles, que exista consistencia entre las diferentes pantallas, que las alertas y niveles de riesgo resulten reconocibles, que las acciones del usuario generen retroalimentación y que se evite la incorporación de elementos visuales innecesarios. Gonzalez Capdevila et al. (2025) destacan que la evaluación heurística continúa siendo una técnica relevante tanto en investigación como en entornos profesionales y proponen mecanismos para hacer más objetiva la valoración de los problemas identificados por diferentes evaluadores. En consecuencia, este procedimiento permitirá detectar y corregir dificultades de usabilidad antes de comparar el desempeño de los usuarios durante las tareas de priorización de riesgos.

## 8. MARCO METODOLÓGICO

### 8.1. Tipo de investigación

La investigación será de tipo aplicada, debido a que se orientará al diseño y evaluación de una solución tecnológica dirigida a una necesidad concreta: facilitar la visualización, interpretación y priorización de riesgos industriales. A partir de información relacionada con zonas críticas, frecuencia y severidad de eventos e indicadores de exposición, se desarrollará un dashboard UX que permita presentar los riesgos de manera estructurada y comprensible para usuarios técnicos y operativos.

Asimismo, tendrá un alcance descriptivo y evaluativo. Será descriptivo porque permitirá identificar las necesidades de los usuarios, las características de las visualizaciones y los criterios requeridos para representar los riesgos industriales. Será evaluativo porque se analizará el desempeño del dashboard mediante tareas de uso, considerando métricas de usabilidad, tiempo de ejecución, tasa de éxito, errores, satisfacción, utilidad percibida y claridad para establecer prioridades.

El desarrollo de la solución seguirá los principios de Design Science Research, orientados a la construcción y evaluación de un artefacto tecnológico, complementados con Human-Centred Design, con el propósito de incorporar las necesidades de los usuarios durante el diseño de la interfaz. Esta combinación permitirá desarrollar el dashboard de manera iterativa y generar recomendaciones de mejora a partir de los resultados obtenidos durante su evaluación.

### 8.2. Enfoque y modalidad de investigación

La investigación adoptará un enfoque mixto, debido a que integrará información cuantitativa y cualitativa durante la evaluación del dashboard. El componente cuantitativo permitirá analizar métricas como tiempo de ejecución de las tareas, tasa de éxito, número de errores y resultados obtenidos mediante instrumentos de usabilidad como SUS o UEQ. Estos datos permitirán valorar el desempeño de los usuarios durante la interacción con las visualizaciones propuestas.

El componente cualitativo permitirá conocer las percepciones de los participantes respecto a la claridad de la información, facilidad de interpretación, utilidad de las visualizaciones y dificultades encontradas durante las tareas. Esta información complementará los resultados cuantitativos y permitirá identificar aspectos de la interfaz que requieran ajustes o rediseño a partir de la experiencia manifestada por los usuarios técnicos y operativos.

La modalidad combinará investigación documental, desarrollo tecnológico y trabajo de campo. La revisión documental permitirá establecer criterios de diseño, visualización y usabilidad; el desarrollo tecnológico comprenderá la elaboración de wireframes, prototipo interactivo y dashboard funcional; mientras que el trabajo de campo estará constituido por las pruebas realizadas con usuarios técnicos y operativos *[en]* condiciones controladas. *(En el PDF original falta la palabra "en".)*

Para la fase de evaluación se empleará un diseño experimental A/B, mediante la comparación de un grupo control, que realizará tareas de identificación y priorización de riesgos sin utilizar el dashboard, y un grupo tratamiento, que efectuará las mismas tareas con apoyo del dashboard desarrollado. Esta comparación permitirá determinar si el uso de la interfaz genera diferencias en el tiempo de ejecución, tasa de error y precisión en la identificación de zonas críticas, proporcionando evidencia cuantitativa sobre su utilidad para apoyar la priorización de riesgos industriales y la toma de decisiones preventivas.

### 8.3. Fuentes, técnicas e instrumentos para la recolección de datos

| Tipo de fuente | Fuente | Técnica | Instrumento |
|---|---|---|---|
| Primaria | Usuarios técnicos y operativos | Observación durante pruebas de usabilidad | Guion de tareas y ficha de observación |
| Primaria | Usuarios técnicos y operativos | Encuesta de usabilidad | System Usability Scale (SUS) |
| Primaria | Usuarios técnicos y operativos | Evaluación de experiencia de usuario | User Experience Questionnaire (UEQ) |
| Primaria | Usuarios técnicos y operativos | Registro de desempeño | Matriz de tiempo de tarea, tasa de éxito y errores |
| Primaria | Usuarios técnicos y operativos | Prueba de identificación y priorización de riesgos | Matriz de precisión en la identificación de zonas críticas |
| Primaria | Usuarios técnicos y operativos | Retroalimentación posterior a las pruebas | Cuestionario de satisfacción y utilidad percibida |
| Secundaria | Dataset SI-02 e indicadores SI-01 | Análisis de datos | Matriz de indicadores de riesgo |
| Secundaria | API y arquitectura IND-SIS-01 | Revisión técnica | Registro de estructura e integración de datos |
| Secundaria | Mapas, planos por zonas y catálogos de riesgos | Análisis documental | Matriz de zonas, eventos y niveles de riesgo |
| Secundaria | Literatura científica sobre UX, dashboards y riesgos industriales | Revisión documental | Ficha bibliográfica |

### 8.4. Población y muestra de la investigación

La población estará constituida por usuarios técnicos y operativos vinculados con procesos industriales, cuya actividad requiera interpretar información relacionada con condiciones de operación, eventos, indicadores o riesgos. La selección de este grupo responde a que constituye la población objetivo del dashboard y posee características acordes con las tareas que serán evaluadas durante las pruebas de usabilidad.

Se utilizará un muestreo no probabilístico intencional, mediante el cual se seleccionarán participantes que cumplan con el perfil técnico u operativo requerido y tengan disponibilidad para participar en el estudio. Una vez seleccionados, los participantes serán distribuidos en dos grupos para desarrollar la evaluación A/B: un grupo control, que realizará las tareas de identificación y priorización de riesgos sin utilizar el dashboard, y un grupo tratamiento, que ejecutará las mismas tareas con apoyo del dashboard desarrollado. Se procurará mantener una distribución equilibrada entre ambos grupos para facilitar la comparación de los resultados.

El número definitivo de participantes dependerá de la disponibilidad y acceso a usuarios del entorno industrial. En caso de contar con una muestra limitada, se complementará la evaluación mediante pruebas formativas, valoración de usuarios o expertos internos y triangulación de métricas como tiempo de tarea, tasa de error, precisión en la identificación de zonas críticas y puntuación de usabilidad. Los resultados serán interpretados dentro del alcance de la muestra disponible, evitando generalizaciones estadísticas que excedan las características del estudio.

### 8.5. Análisis y tratamiento de la información

Los datos obtenidos durante las pruebas serán organizados y procesados mediante una matriz de resultados. Las métricas cuantitativas incluirán tiempo de ejecución por tarea, tasa de éxito, tasa de error, precisión en la identificación de zonas críticas, puntuación de usabilidad SUS, satisfacción y utilidad percibida. En una primera etapa se aplicará estadística descriptiva mediante frecuencias, porcentajes, promedios y medidas de tendencia central, según las características de los datos obtenidos.

Para comparar los resultados entre el grupo control y el grupo tratamiento se aplicarán pruebas estadísticas inferenciales. Cuando los datos cumplan los supuestos correspondientes, se empleará la prueba t de Student para determinar la existencia de diferencias entre ambos grupos. En caso de que la muestra sea reducida o los datos no presenten una distribución adecuada para pruebas paramétricas, se utilizará una prueba de Wilcoxon como alternativa no paramétrica. La comparación permitirá establecer si el uso del dashboard produce diferencias en variables como tiempo de tarea, errores y precisión para identificar zonas críticas.

Además de determinar la significancia estadística de las diferencias observadas, se calculará el tamaño del efecto mediante Cohen's d, con el propósito de establecer la magnitud de las diferencias entre las condiciones evaluadas. Este análisis permitirá conocer si los cambios asociados con el uso del dashboard presentan una relevancia práctica, evitando que la interpretación se limite únicamente a la existencia o ausencia de significancia estadística. En caso de que durante el estudio se evalúen múltiples versiones del dashboard con los mismos participantes, se podrá emplear un ANOVA de medidas repetidas para comparar el desempeño obtenido en las distintas versiones.

Las respuestas cualitativas y observaciones realizadas durante las pruebas serán clasificadas de acuerdo con aspectos como dificultades de navegación, comprensión de indicadores, identificación de zonas críticas, interpretación de niveles de severidad y claridad de las recomendaciones preventivas. Finalmente, se realizará una triangulación entre las métricas de desempeño, los instrumentos de usabilidad y las percepciones de los participantes, con la finalidad de determinar qué visualizaciones facilitan en mayor medida la priorización de riesgos industriales y formular recomendaciones de rediseño orientadas a mejorar la claridad, usabilidad y utilidad operativa del dashboard.

### 8.6. Matriz de operacionalización de variables

| Variable | Dimensión | Indicador | Técnica | Instrumento |
|---|---|---|---|---|
| Dashboard UX para visualización de riesgos industriales | Usabilidad | Puntuación de usabilidad | Encuesta | SUS |
| Dashboard UX para visualización de riesgos industriales | Experiencia de usuario | Satisfacción y percepción de la interacción | Encuesta | UEQ |
| Dashboard UX para visualización de riesgos industriales | Eficiencia | Tiempo requerido para completar tareas | Prueba de usabilidad | Guion de tareas y registro de tiempos |
| Dashboard UX para visualización de riesgos industriales | Efectividad | Tasa de tareas completadas correctamente | Prueba de usabilidad | Matriz de tasa de éxito |
| Dashboard UX para visualización de riesgos industriales | Facilidad de interacción | Número y tipo de errores durante las tareas | Observación | Ficha de observación |
| Priorización de riesgos industriales | Claridad de priorización | Identificación correcta del riesgo prioritario | Prueba basada en tareas | Guion de tareas |
| Priorización de riesgos industriales | Interpretación del riesgo | Comprensión de frecuencia, severidad y exposición | Prueba de usabilidad | Matriz de resultados |
| Priorización de riesgos industriales | Reconocimiento espacial | Identificación de zonas críticas | Prueba basada en tareas | Dashboard y guion de tareas |
| Priorización de riesgos industriales | Utilidad operativa | Percepción de utilidad para apoyar decisiones preventivas | Encuesta | Cuestionario de utilidad percibida |
| Priorización de riesgos industriales | Apoyo preventivo | Comprensión de recomendaciones preventivas presentadas | Encuesta y observación | Cuestionario y ficha de observación |

## 9. METODOLOGÍA DE DESARROLLO A EMPLEAR

### 9.1. Justificación de la metodología

Para el desarrollo del proyecto se empleará una metodología ágil, específicamente Scrum, debido a que permite organizar el trabajo en iteraciones cortas, facilitar la retroalimentación continua y realizar ajustes progresivos durante la construcción del dashboard. Esta elección resulta pertinente porque el proyecto no solo implica desarrollar un producto funcional, sino también validar su utilidad y usabilidad con usuarios técnicos y operativos. En ese sentido, la naturaleza iterativa de Scrum favorece la mejora continua de la interfaz a partir de los hallazgos obtenidos en cada fase.

La selección de Scrum también responde al tamaño del equipo de trabajo, conformado por dos estudiantes con responsabilidades diferenciadas, pero complementarias. Mientras un integrante se enfoca en los aspectos de experiencia de usuario, instrumentos y pruebas, el otro se orienta a la implementación funcional, conexión de datos y análisis de resultados. Esta organización permite distribuir tareas por sprint, revisar avances periódicamente y mantener una coordinación clara entre diseño, desarrollo y evaluación.

Además, Scrum es compatible con el enfoque metodológico del proyecto, ya que puede integrarse con Design Science Research y Human-Centred Design. De esta manera, cada iteración permitirá identificar necesidades, diseñar propuestas, implementar mejoras y evaluar resultados con usuarios. Por ello, la metodología ágil contribuirá a obtener un dashboard funcional, usable y alineado con el propósito de apoyar la priorización de riesgos industriales y la toma de decisiones preventivas.

### 9.2. Herramientas de planificación (opcional)

Como herramientas de planificación se utilizarán el Product Backlog y el Sprint Backlog, con el fin de organizar las funcionalidades, tareas y entregables del proyecto. Estas herramientas permitirán priorizar actividades como levantamiento de requisitos, diseño de wireframes, elaboración del prototipo, implementación del dashboard, integración de datos y evaluación con usuarios. Asimismo, facilitarán el seguimiento del avance del proyecto y la distribución de responsabilidades entre los integrantes.

De manera complementaria, se podrá utilizar un tablero Kanban en herramientas digitales como Trello, Notion o Jira para visualizar el estado de las actividades pendientes, en proceso y finalizadas. Esto permitirá mantener un control más claro del desarrollo durante los meses de ejecución y apoyar la gestión de tiempos, revisiones y entregables parciales.

### 9.3. Prácticas aplicadas

Durante el desarrollo del proyecto se aplicarán iteraciones cortas orientadas a la mejora progresiva del dashboard. Cada iteración incluirá actividades de planificación, diseño, desarrollo, revisión y ajuste. Esta dinámica permitirá validar de manera temprana las decisiones que se adopten y corregir aspectos relacionados con la navegación, visualización, claridad de la información y desempeño del sistema antes de alcanzar la versión final.

En la fase de diseño se aplicará el enfoque User-Centred Design (UCD), con el propósito de considerar las necesidades, características y tareas de los usuarios técnicos y operativos durante la construcción del prototipo. Asimismo, se utilizarán las heurísticas de Nielsen para revisar aspectos de usabilidad como la visibilidad del estado del sistema, consistencia, prevención de errores, correspondencia entre el sistema y el contexto real, control del usuario y diseño visual minimalista. Esta revisión permitirá identificar posibles problemas de interacción antes de efectuar las pruebas con usuarios.

También se aplicarán prácticas de revisión continua y retroalimentación con usuarios, especialmente durante las fases de prototipado y evaluación. Se realizarán revisiones internas entre los integrantes del proyecto para verificar el cumplimiento de requisitos, la coherencia entre diseño e implementación y la correcta integración de los datos. Además, las pruebas de usabilidad permitirán obtener información sobre posibles errores, dificultades de interacción y percepciones relacionadas con la utilidad del dashboard.

Finalmente, se emplearán prácticas de control de versiones, documentación de avances y pruebas funcionales. El control de versiones permitirá registrar los cambios que se realicen en la interfaz y en la implementación del dashboard, mientras que la documentación de avances permitirá mantener evidencia de las decisiones de diseño, ajustes efectuados y resultados que se obtengan. Las pruebas funcionales se utilizarán para verificar que las visualizaciones, indicadores y componentes interactivos operen correctamente antes de la evaluación con usuarios.

### 9.4. Historias de usuario / requisitos

| ID | Historia de Usuario | Prioridad | Iteración |
|---|---|---|:-:|
| HU-01 | Como usuario técnico, quiero visualizar las zonas críticas dentro del entorno industrial para identificar rápidamente los sectores con mayor nivel de riesgo. | Alta | 1 |
| HU-02 | Como usuario operativo, quiero observar la frecuencia y severidad de los eventos para reconocer cuáles situaciones requieren atención prioritaria. | Alta | 1 |
| HU-03 | Como usuario técnico, quiero consultar indicadores de exposición para interpretar mejor las condiciones de riesgo presentes en cada zona. | Alta | 2 |
| HU-04 | Como usuario operativo, quiero disponer de una interfaz clara y fácil de usar para comprender la información sin invertir demasiado tiempo en su interpretación. | Alta | 2 |
| HU-05 | Como usuario técnico, quiero recibir recomendaciones preventivas asociadas a los riesgos identificados para apoyar la toma de decisiones. | Media | 3 |
| HU-06 | Como usuario evaluador, quiero interactuar con el dashboard mediante tareas definidas para valorar su usabilidad, utilidad y claridad de priorización. | Alta | 3 |
| HU-07 | Como equipo de investigación, se requiere medir el tiempo de tarea, la tasa de éxito, los errores y la satisfacción para evaluar el desempeño del dashboard. | Alta | 4 |
| HU-08 | Como equipo de investigación, se requiere generar recomendaciones de rediseño basadas en los resultados de la evaluación para mejorar la solución propuesta. | Media | 4 |

## 10. CRONOGRAMA DE ACTIVIDADES

| Actividad | Agosto | Septiembre | Octubre | Noviembre |
|---|:-:|:-:|:-:|:-:|
| Revisión bibliográfica y definición de requisitos | X | | | |
| Análisis de fuentes de datos e identificación de indicadores | X | X | | |
| Elaboración de wireframes y mapa de navegación | X | X | | |
| Diseño del prototipo interactivo | | X | | |
| Implementación del dashboard funcional | | X | X | |
| Integración de datos y pruebas funcionales | | | X | |
| Diseño de instrumentos de evaluación (SUS/UEQ y guion de tareas) | | | X | |
| Evaluación con usuarios técnicos y operativos | | | X | X |
| Análisis de resultados y recomendaciones de rediseño | | | | X |
| Redacción del informe final del proyecto | | | | X |

## 11. PRESUPUESTO Y FINANCIAMIENTO

| Rubro | Descripción | Costo (USD) |
|---|---|--:|
| Software y herramientas de desarrollo | Licencias o servicios requeridos para diseño, prototipado y desarrollo del dashboard | $250 |
| Infraestructura tecnológica | Servicios de alojamiento, almacenamiento y recursos necesarios para pruebas del sistema | $200 |
| Equipos y recursos informáticos | Uso, mantenimiento y accesorios necesarios para el desarrollo y evaluación | $200 |
| Pruebas de usabilidad | Materiales, instrumentos y recursos requeridos para las evaluaciones con usuarios | $180 |
| Movilización y logística | Traslados y gastos relacionados con reuniones y pruebas con usuarios técnicos y operativos | $150 |
| Conectividad | Servicio de internet y recursos de comunicación utilizados durante el proyecto | $100 |
| Documentación y presentación | Impresión, elaboración de documentos y materiales para presentación de resultados | $120 |
| **TOTAL** | | **$1.200** |

## 12. BENEFICIOS ESPERADOS DEL PROYECTO

- Facilitar la identificación y priorización de riesgos industriales mediante visualizaciones claras de zonas críticas, frecuencia, severidad e indicadores de exposición.
- Reducir el tiempo requerido por los usuarios técnicos y operativos para localizar e interpretar información relevante sobre riesgos.
- Mejorar la usabilidad y claridad de la información mediante un dashboard diseñado de acuerdo con criterios de experiencia de usuario.
- Proporcionar información organizada y recomendaciones preventivas que sirvan como apoyo para la toma de decisiones preventivas.
- Generar evidencia sobre la utilidad de diferentes visualizaciones para el diseño futuro de sistemas de apoyo a la gestión de riesgos industriales.

## 13. DERECHOS DE PROPIEDAD INTELECTUAL

El desarrollo de este trabajo de tesis contempla la generación de resultados susceptibles de protección por Propiedad Intelectual (derechos de autor, patentes, programa de computador).

¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [ ] Software *(casilla resaltada en amarillo)*
- [ ] Modelo/algoritmo
- [ ] Manual/documentación técnica *(casilla resaltada en amarillo)*
- [ ] No aplica

## 14. REFERENCIAS BIBLIOGRÁFICAS

Almasi, S., Bahaadinbeigy, K., Ahmadi, H., Sohrabei, S., y Rabiei, R. (2023). Usability evaluation of dashboards: A systematic literature review of tools. *BioMed Research International, 2023*, Article 9990933. https://doi.org/10.1155/2023/9990933

Asad, U., Khan, M., Khalid, A., y Lughmani, W. A. (2023). Human-centric digital twins in industry: A comprehensive review of enabling technologies and implementation strategies. *Sensors, 23*(8), 3938. https://doi.org/10.3390/s23083938

Chen, C., Han, Y., Galinski, A., Calle, C., Carney, J., Ye, X., y van Westen, C. (2024). *Integrating urban digital twins with cloud-based geospatial dashboards for coastal resilience planning: A case study in Florida* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2403.18188

Dougherty, K., Tesfaye, Y., Biza, H., Belew, M., Benda, N., Gobezayehu, A. G., Cranmer, J., y Bakken, S. (2025). User-centered design of an electronic dashboard for monitoring facility-level basic emergency obstetric care readiness in Amhara, Ethiopia: Mixed methods study. *JMIR Human Factors, 12*, e64131. https://doi.org/10.2196/64131

Elhabashy, A., Elsayed, S., Abdelwahed, A. A., y Fors, H. (2026). An Industry 4.0-based data visualization framework for improved manufacturing data analysis—A case study. *Intelligent and Sustainable Manufacturing, 3*(1), 10001. https://doi.org/10.70322/ism.2026.10001

Gonzalez Capdevila, M., Pistili Rodrigues, K. A., Sartório Furlan, T. A., y Granollers, T. (2025). Quantifying heuristic evaluation. *Computer Standards y Interfaces, 92*, 103891. https://doi.org/10.1016/j.csi.2024.103891

Hamdani, R., y Chihi, I. (2025). Adaptive human-computer interaction for Industry 5.0: A novel concept, with comprehensive review and empirical validation. *Computers in Industry, 168*, 104268. https://doi.org/10.1016/j.compind.2025.104268

Hjelle, S., Mikalef, P., Altwaijry, N., y Parida, V. (2024). Organizational decision making and analytics: An experimental study on dashboard visualizations. *Information y Management, 61*(6), 104011. https://doi.org/10.1016/j.im.2024.104011

Kant, V., Nejeeb, I., Alya, S., Jain, P., y Singh, R. (2025). Supporting cognitive intelligence for smart manufacturing systems using HMI design: Challenges and fundamental issues. *Journal of Engineering Design, 36*(11), 1961–1981. https://doi.org/10.1080/09544828.2024.2343746

Krupas, M., Kajati, E., Liu, C., y Zolotova, I. (2024). Towards a human-centric digital twin for human–machine collaboration: A review on enabling technologies and methods. *Sensors, 24*(7), 2232. https://doi.org/10.3390/s24072232

Kucher, K., Zohrevandi, E., y Westin, C. A. L. (2025). Towards visual analytics for explainable AI in industrial applications. *Analytics, 4*(1), 7. https://doi.org/10.3390/analytics4010007

Lin, Z., Shen, S., Liu, W., Xin, C., Dai, W., Chen, S., Wen, X., y Lan, X. (2025). *DashChat: Interactive authoring of performance dashboard design prototypes through conversation with LLM-powered agent* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2504.12865

Liu, Z. (2025). Evaluating digitalized visualization interfaces: Integrating visual design elements and analytic hierarchy process. *International Journal of Human–Computer Interaction, 41*(9), 5731–5760. https://doi.org/10.1080/10447318.2024.2365454

Liu, Z., y Yang, Y. (2025). Fundamental usability evaluation in visualization: Integrating Nielsen's principles and the analytic hierarchy process. *International Journal of Human–Computer Interaction, 41*(20), 13012–13040. https://doi.org/10.1080/10447318.2025.2467455

Nunes, M., Kayan, H., Burnap, P., Perera, C., y Dykes, J. (2024). Exploiting user-centred design to secure industrial control systems. *Frontiers in the Internet of Things, 3*, 1436023. https://doi.org/10.3389/friot.2024.1436023

Wang, K.-J., y Lee, T.-L. (2024). Designing a digital-twin based dashboard system for a flexible assembly line. Computers y Industrial Engineering, 196, 110491. https://doi.org/10.1016/j.cie.2024.110491

---

## Anexos (páginas escaneadas con anotaciones manuscritas)

> La transcripción de estas páginas es aproximada.

### Anexo I. Formato de evaluación de la propuesta de trabajo de integración curricular

- **Nombre de la propuesta:** Dashboard UX para priorización de riesgos industriales y toma de decisiones preventivas
- **Estudiantes:** Suanny García Anzules; Alberto Reyes Salinas
- **Facultad:** Ingeniería Industrial
- **Carrera:** Sistemas de Información
- **Línea de investigación:** Ciencias básicas, bioconocimiento
- **Sub-línea de investigación:** Inteligencia artificial y ciencia de datos
- **Fecha de presentación / evaluación:** 26/8/2026
- **Cumplimiento (SÍ) en todos los aspectos:** título, línea/sublínea, planteamiento del problema, justificación e importancia, objetivos, metodología, cronograma y presupuesto
- **Resultado:** ☒ Aprobado (sin observaciones)
- **Firma:** Ing. Manuel Samaniego Zamora, MBA, Decano de la Facultad

### Rúbrica de evaluación

| Criterio | Nota evaluador | Nota máxima |
|---|:-:|:-:|
| Planteamiento y formulación del problema; Innovación | 1 | 1 |
| Alcance; Justificación | 1 | 1 |
| Objetivos (General y Específicos) coherentes | 1 | 1 |
| Marco Teórico; Marco Metodológico; Referencias Bibliográficas | 1 | 1 |
| Metodología de Desarrollo | 1 | 1 |
| Cronograma; Presupuesto | 1 | 1 |
| Manejo claro de las ideas; Beneficios esperados del proyecto | 1 | 1 |
| Claridad y coherencia en la redacción | 1 | 1 |
| Referentes teóricos sustentados | 1 | 1 |
| Argumentos para una propuesta | 1 | 1 |
| **NOTA SOBRE 10** | **10** | **10** |

### Anexo C. Rúbrica de evaluación para proyectos grupales de integración curricular

| # | Aspecto evaluado | Resultado |
|---|---|---|
| 1 | Tema del proyecto: describe un tema con problemática de estudio, ajustado a la línea de investigación de la Carrera y a la pirámide de investigación de la Facultad | Cumple |
| 2 | Definición del problema: problema complejo o con múltiples abordajes | Cumple |
| 3 | División de tareas: plan de trabajo detallado con hitos y plazos | Cumple |
| 4 | Desarrollo de objetivos: objetivos con enfoques específicos | Cumple |
| 5 | Descripción de propiedad intelectual | Cumple |
