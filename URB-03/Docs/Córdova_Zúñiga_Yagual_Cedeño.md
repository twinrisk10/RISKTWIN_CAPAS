# UNIVERSIDAD DE GUAYAQUIL
## FACULTAD DE INGENIERÍA INDUSTRIAL

### ANTEPROYECTO DE TRABAJO DE TITULACIÓN

## Datos Generales

| | |
|---|---|
| **CARRERA:** | Sistemas de la Información |
| **FECHA:** | 26/08/2026 |

| | APELLIDOS | NOMBRES |
|---|---|---|
| **ESTUDIANTE 1:** | Córdova Zúñiga | Christopher Moisés |
| **ESTUDIANTE 2:** | Yagual Cedeño | Byron Andrés |

**Correo electrónico institucional y personal:**

- christopher.cordovaz@ug.edu.ec
- byron.yagualce@ug.edu.ec
- hope_1005@outlook.com
- byronyagualce@gmail.com

**Teléfono:** 0994085062 / 0939028207

## Tema

**TEMA:** Índice geoespacial de criticidad urbana basado en peligrosidad, exposición y vulnerabilidad

**LÍNEA DE INVESTIGACIÓN**

- [ ] SOSTENIBILIDAD, DERECHOS Y TECNOLOGÍAS EN EL ORDENAMIENTO TERRITORIAL, AMBIENTE DE LA CONSTRUCCIÓN Y ARQUITECTURA.
- [ ] DESARROLLO LOCAL Y EMPRENDIMIENTO SOCIO ECONÓMICO SOSTENIBLE.
- [x] CIENCIAS BÁSICAS, BIOCONOCIMIENTO Y DESARROLLO INDUSTRIAL.
- [ ] SALUD HUMANA, ANIMAL Y DEL AMBIENTE
- [ ] TECNOLOGÍAS AGRÍCOLAS Y DE LA AGRICULTURA.
- [ ] ENTORNOS VIRTUALES DE APRENDIZAJE Y TECNOLOGÍAS EDUCATIVAS

**COBERTURA**

- [ ] Nacional
- [ ] Provincial
- [ ] Local
- [ ] Otros

*(En el original no se distingue ninguna casilla marcada en Cobertura.)*

---

## 1. PLANTEAMIENTO Y FORMULACIÓN DEL PROBLEMA

### 1.1 Antecedentes

Guayaquil, uno de los principales polos económicos del Ecuador, enfrenta una crisis dual de riesgos urbanos que combina una preocupante siniestralidad vial y un incremento de la violencia criminal. Ambas dimensiones son gestionadas por instituciones diferentes, como la Agencia de Tránsito y Movilidad (ATM) en materia de seguridad vial y la Policía Nacional en materia de seguridad ciudadana. Sin embargo, comparten un factor común, ya que su distribución espacial no es aleatoria, sino que se concentra en zonas específicas de la ciudad donde convergen factores de exposición y vulnerabilidad.

#### Siniestralidad vial en Guayaquil

El Observatorio de Movilidad de la ATM ha documentado que, en el primer trimestre de 2026, Guayaquil registró 1.272 víctimas por siniestros viales, con 93 fallecidos y 1.179 lesionados, concentrando junto con Quito el 42.44% de las víctimas a nivel nacional (Diario Expreso, 2026). Esta cifra adquiere relevancia al considerar que evidencia un problema de salud pública que afecta desproporcionadamente a la población guayaquileña, y que su magnitud justifica la necesidad de herramientas que permitan identificar las zonas donde estos incidentes se concentran para focalizar intervenciones.

El análisis de la distribución espacial revela patrones de concentración preocupantes. La autopista Narcisa de Jesús registró 190 siniestros en 2025, con 179 heridos y 17 fallecidos, superando en 10 casos la cifra del año anterior; en enero de 2026 ya se habían reportado 15 siniestros adicionales (El Universo, 2026). Este incremento sostenido sugiere que los factores que generan peligrosidad en esta vía no han sido adecuadamente abordados, y que la intervención debe considerar no solo la infraestructura vial sino también los factores de exposición y vulnerabilidad de la población que transita por ella. De manera similar, la avenida 25 de Julio registró 42 siniestros entre enero y mayo de 2026, con 52 lesionados y dos fallecidos (Ecuavisa, 2026), consolidando un patrón de concentración en vías específicas que será fundamental incorporar en el índice propuesto.

Un caso particularmente revelador es el de la vía a la Costa, donde hasta abril de 2026 se registraron 39 siniestros que dejaron 59 víctimas, de las cuales siete fueron peatones mayores de 70 años (Primicias, 2026). Este dato resulta especialmente significativo porque evidencia cómo la vulnerabilidad asociada a la edad se combina con la exposición en vías de alto flujo para generar criticidad. La ATM ya había identificado este tramo como de "riesgo grave" para peatones desde 2025 y solicitó la implementación de un semáforo, lo que demuestra que existe conciencia institucional sobre el problema, pero persisten brechas en la priorización de intervenciones (Primicias, 2026). La existencia de informes técnicos que identifican el riesgo sin que se materialicen intervenciones efectivas constituye precisamente el tipo de brecha que un índice objetivo de criticidad puede ayudar a cerrar.

#### Violencia criminal en Guayaquil

Paralelamente, la crisis de seguridad ha alcanzado niveles preocupantes. Según datos de la Policía Nacional reportados por medios de comunicación, entre enero y abril de 2026 la ciudad registró 763 homicidios intencionales, consolidándose como el tercer inicio de año más violento de su historia (Radio Pichincha, 2026). La evolución temporal de esta cifra permite identificar un incremento sostenido de la violencia. Entre 2014 y 2020, los homicidios se mantuvieron por debajo de los 100 casos anuales; sin embargo, en 2021 la cifra se duplicó y alcanzó los 202 casos, mientras que en 2025 se registró un máximo de 989 asesinatos. Este comportamiento evidencia que la violencia no constituye únicamente un fenómeno coyuntural, sino un problema de carácter estructural que requiere enfoques territoriales de intervención. En este contexto, la identificación de las zonas críticas constituye un primer paso para orientar de manera eficiente la asignación de recursos y fortalecer las estrategias de seguridad.

Al contextualizar estas cifras a nivel nacional, se observa que Guayaquil concentra una proporción desproporcionada de la violencia del país. Datos oficiales indican que la ciudad acumuló 944 homicidios entre enero y mayo de 2026, equivalentes al 27.1% de todos los asesinatos registrados en el Ecuador, que totalizaron 3,485 en 138 cantones (Radio Pichincha, 2026). La Zona 8, que comprende Guayaquil, Durán y Samborondón, superó los 1,500 homicidios en el primer semestre de 2026. Esta concentración geográfica de la violencia en el área metropolitana de Guayaquil refuerza la necesidad de un índice que permita identificar espacialmente las zonas críticas, ya que la distribución no es uniforme y las intervenciones deben ser territorializadas para ser efectivas.

El análisis de casos específicos permite identificar patrones de violencia territorializada. En agosto de 2026, un ataque armado ocurrido durante un velorio en la cooperativa Vencer o Morir, ubicada en el sur de Guayaquil, dejó dos personas fallecidas y dos heridas (El Diario Ecuador, 2026). De manera similar, en el sector Flor de Bastión, perteneciente al distrito Nueva Prosperina, un ataque contra una vivienda ocasionó la muerte de tres menores de edad y dejó herido a su padre (Infobae, 2026). Estos incidentes evidencian una concentración de hechos violentos en determinadas zonas de la ciudad, entre ellas Nueva Prosperina, Isla Trinitaria, Flor de Bastión y sectores del sur de Guayaquil, las cuales pueden ser consideradas áreas de mayor criticidad. La identificación de estos patrones de concentración puede estar relacionada con diversos factores estructurales, entre ellos la presencia de grupos criminales, la debilidad institucional y la concentración de población en condiciones de vulnerabilidad. Estos elementos deberán ser considerados por el índice propuesto mediante las dimensiones de peligrosidad y vulnerabilidad.

Lo que resulta particularmente relevante para esta investigación es la superposición espacial entre las zonas que presentan una alta siniestralidad vial y aquellas que registran una elevada incidencia criminal. Si bien la literatura ha abordado estos fenómenos de manera independiente, la evidencia disponible sugiere que ambos pueden estar relacionados con factores subyacentes comunes. Esta convergencia plantea la necesidad de adoptar un enfoque integrado para la identificación y priorización de zonas críticas, lo cual constituye el propósito central del índice propuesto.

### 1.2 Planteamiento del Problema

A pesar de los esfuerzos institucionales orientados a fortalecer el uso de datos en la planificación urbana, persiste una importante fragmentación en la gestión de los riesgos asociados a la siniestralidad vial y la criminalidad. Los datos relacionados con incidentes viales y hechos delictivos son recopilados y analizados por diferentes entidades, principalmente la Agencia de Tránsito y Movilidad (ATM) y la Policía Nacional, respectivamente. Sin embargo, actualmente no se dispone de un mecanismo integrado que permita combinar ambas dimensiones para generar un índice de criticidad urbana orientado a la identificación y priorización objetiva de zonas que requieren intervención.

La literatura académica respalda la necesidad de enfoques sistémicos. Barroca (2024) sostiene que las infraestructuras críticas urbanas requieren metodologías que integren análisis de riesgo y métodos de análisis espacial desde una perspectiva sistémica. De manera similar, los estudios sobre gemelos digitales urbanos destacan que la integración de datos heterogéneos y la interoperabilidad entre sistemas constituyen barreras significativas para la implementación de herramientas de gestión urbana (Wang et al., 2024; Mazzetto, 2024).

Además, existe evidencia de una superposición espacial entre zonas que presentan una alta siniestralidad vial y aquellas que registran una elevada incidencia criminal. Ambos fenómenos pueden estar relacionados con factores subyacentes comunes, entre los que se encuentran la degradación del espacio público, la insuficiente iluminación, la baja presencia institucional y la concentración de población en condiciones de vulnerabilidad socioeconómica. Esta convergencia plantea la necesidad de adoptar un enfoque integrado que permita identificar y priorizar aquellas zonas que presentan mayores niveles de criticidad urbana.

### 1.3 Causas

- La fragmentación institucional en la gestión de los datos de siniestralidad vial y criminalidad, debido a que son administrados por entidades diferentes sin mecanismos adecuados de integración, dificulta la obtención de una visión integral del riesgo urbano.
- La ausencia de herramientas objetivas de priorización impide clasificar las zonas de la ciudad de acuerdo con su nivel de criticidad, considerando de manera conjunta las dimensiones de peligrosidad, exposición y vulnerabilidad.
- Las limitaciones metodológicas de los enfoques existentes dificultan la evaluación de la estabilidad de los resultados, debido a la falta de análisis de sensibilidad que permitan determinar cómo las variaciones en la ponderación de las variables afectan la clasificación de las zonas.
- La subjetividad en la asignación de recursos públicos puede generar una priorización poco sistemática de las intervenciones, lo que aumenta el riesgo de que los recursos sean destinados a zonas que no necesariamente presentan los mayores niveles de criticidad.

### 1.4 Consecuencias

- La asignación ineficiente de recursos públicos ocasiona que las intervenciones en materia de seguridad vial y criminalidad no se concentren necesariamente en las zonas con mayores niveles de criticidad, lo que puede reducir su efectividad.
- La persistencia de puntos críticos mantiene condiciones de riesgo en vías con altos niveles de siniestralidad y en zonas con elevada incidencia criminal que no reciben una atención prioritaria acorde con sus niveles de criticidad.
- La duplicación de esfuerzos institucionales entre la Agencia de Tránsito y Movilidad (ATM) y la Policía Nacional genera análisis independientes de fenómenos relacionados, lo que limita el aprovechamiento de posibles sinergias e incrementa los recursos destinados a su gestión.
- La limitada capacidad de monitoreo dificulta la evaluación continua de los resultados de las intervenciones, debido a la ausencia de un índice que pueda actualizarse periódicamente y permita analizar los cambios en los niveles de criticidad urbana.

### 1.5 Formulación del Problema

**Pregunta Principal:**

¿Cómo combinar variables espaciales de siniestralidad vial y criminalidad para construir un índice geoespacial de criticidad urbana, interpretable y replicable, para la ciudad de Guayaquil?

**Preguntas Específicas:**

- ¿Cuáles son las variables de peligrosidad vial y criminal más relevantes para caracterizar la criticidad urbana en el contexto de Guayaquil?
- ¿Qué metodología de normalización y ponderación permite generar un índice estable, interpretable y sensible a las condiciones locales?
- ¿Cómo se comporta el índice propuesto ante variaciones en los pesos asignados a las variables componentes?
- ¿Qué relación existe entre el ranking de zonas críticas generado por el índice y los puntos críticos conocidos reportados por la ATM y la Policía Nacional?

## 2. ALCANCE

El proyecto se circunscribe al área urbana del cantón Guayaquil, abarcando sus 16 parroquias urbanas y utilizando como unidad de análisis los circuitos de planificación policial o, alternativamente, celdas de cuadrícula de 500x500 metros para mayor resolución espacial.

El estudio considera datos correspondientes al período 2023-2026, con énfasis en la información disponible hasta el primer semestre de 2026 para incidentes de tránsito (ATM, 2026) y delitos (Policía Nacional). Las dimensiones de análisis son:

- **Peligrosidad Vial:** Siniestros con lesionados y fallecidos en vías críticas.
- **Peligrosidad Criminal:** Homicidios intencionales y robos en distritos críticos.
- **Exposición:** Densidad poblacional, concentración de POIs, y flujo vehicular estimado.
- **Vulnerabilidad:** Índice de pobreza, calidad de la vivienda, y presencia de grupos poblacionales vulnerables (adultos mayores, menores de edad).

El proyecto incluye el desarrollo de un módulo en Python (`risk_index.py`) que implemente el índice de criticidad, normalización de variables, ponderación mediante análisis multicriterio, generación de rankings y mapas de criticidad, y análisis de sensibilidad.

Sin embargo, el desarrollo de este trabajo académico no incluye ciertos tópicos como los siguientes:

- Desarrollo de una plataforma web o dashboard completo (solo se genera el módulo y mapas estáticos/interactivos).
- Integración en tiempo real con sistemas de monitoreo del ECU911.
- Recolección primaria de datos en campo (se utilizan fuentes secundarias oficiales).
- Implementación operativa en instituciones (solo se entrega propuesta de integración).

## 3. JUSTIFICACIÓN DE LA INVESTIGACIÓN

### 3.1 Justificación Teórica

El estudio se fundamenta en el marco de la Evaluación Multicriterio (MCDA) para análisis de riesgo territorial, integrando el concepto de criticidad como función compuesta por peligrosidad, exposición y vulnerabilidad. Este modelo se alinea con la literatura sobre gestión de riesgos urbanos, que enfatiza la necesidad de comprender las interdependencias entre diferentes dimensiones del riesgo para mejorar la resiliencia urbana. En este sentido, Barroca (2024) argumenta que las infraestructuras críticas urbanas requieren metodologías que integren análisis de riesgo y métodos de análisis espacial desde una perspectiva sistémica, considerando las interdependencias entre sistemas que pueden propagar fallas en cascada. Esta perspectiva es particularmente relevante para Guayaquil, donde los riesgos viales y criminales comparten factores estructurales que los hacen converger espacialmente, y donde una visión fragmentada del riesgo puede llevar a intervenciones ineficaces.

La investigación se inscribe en la creciente tendencia de aplicación de gemelos digitales a la gestión urbana, donde el desarrollo de índices geoespaciales constituye un componente fundamental para la toma de decisiones basada en evidencia. Wang et al. (2024) demuestran cómo los gemelos digitales pueden potenciar la resiliencia urbana al crear un ciclo entre el espacio virtual y el mundo real, permitiendo la simulación de escenarios y la evaluación de intervenciones antes de su implementación. De manera similar, Mazzetto (2024) destaca que la interoperabilidad entre sistemas y la integración de datos heterogéneos constituyen barreras significativas para la implementación de herramientas de gestión urbana, barreras que el índice de criticidad propuesto busca contribuir a superar mediante un enfoque metodológico replicable.

La novedad del presente estudio radica en la integración de dos dimensiones de peligrosidad, correspondientes a la siniestralidad vial y la criminalidad, que tradicionalmente han sido analizadas de manera independiente tanto en la literatura como en la práctica institucional. Esta integración permite desarrollar una visión más amplia de la criticidad urbana, considerando que los riesgos pueden coexistir y presentar patrones de concentración espacial en determinadas zonas del territorio. El estudio también toma como referencia investigaciones previas relacionadas con la identificación de puntos críticos en Guayaquil, como la desarrollada por Luzuriaga y Scott (2025), quienes emplearon técnicas de análisis multivariante y geoespacial para identificar puntos calientes asociados con casos de extorsión. Sus resultados evidencian la utilidad de los métodos geoespaciales para la identificación y focalización de zonas de interés, lo que constituye un antecedente metodológico relevante para el desarrollo del presente estudio.

### 3.2 Justificación Práctica

La implementación del índice proporcionará a las autoridades locales una herramienta concreta para la planificación territorial basada en evidencia. En el ámbito de la seguridad, permitirá focalizar operativos policiales en los distritos que el índice identifique como críticos, complementando la estrategia de georeferenciación del delito que la Policía Nacional ya ha implementado (Ecuavisa, 2025). La evidencia de concentración de homicidios en distritos como Nueva Prosperina y el sur de Guayaquil refuerza la necesidad de una herramienta que permita priorizar recursos en estas zonas.

En el ámbito de la movilidad, el índice permitirá intervenir de manera prioritaria las vías con alta siniestralidad identificadas por el Observatorio de Movilidad (Ecuavisa, 2026; El Universo, 2026; Primicias, 2026). La existencia de informes técnicos de la ATM que ya han identificado puntos de "riesgo grave" (Primicias, 2026) sin que se materialicen intervenciones efectivas demuestra que la identificación del riesgo es solo el primer paso; se requiere un mecanismo de priorización que asigne recursos a las zonas donde el riesgo es más crítico. El índice propuesto proporciona precisamente ese mecanismo de priorización objetiva.

Adicionalmente, el índice permitirá establecer un sistema de monitoreo continuo que complemente el Observatorio de Movilidad (ATM, 2026) y los visualizadores de datos abiertos impulsados por el Municipio (Alcaldía de Guayaquil, 2026). Esta capacidad de monitoreo es fundamental para evaluar el impacto de las intervenciones en la reducción de la criticidad y para ajustar las políticas públicas en función de los resultados obtenidos.

### 3.3 Justificación Metodológica

El estudio propone una metodología replicable que combina análisis multicriterio, normalización de variables y análisis de sensibilidad, proporcionando un marco robusto para la gestión de la incertidumbre en contextos urbanos complejos. Gao et al. (2024) demuestran en su investigación sobre predicción de accidentes de tránsito que la incorporación de análisis de incertidumbre mejora significativamente la confiabilidad de los modelos predictivos, un principio que se aplica directamente al análisis de sensibilidad propuesto en este estudio. De manera similar, Chen et al. (2024) destacan la importancia de integrar gemelos digitales con dashboards geoespaciales para la planificación de resiliencia costera, mostrando cómo la combinación de métodos de análisis espacial con herramientas de visualización puede potenciar la toma de decisiones.

El uso de CRISP-DM como metodología de desarrollo garantiza un enfoque estructurado y flexible para proyectos de ciencia de datos, permitiendo iteraciones y la incorporación de aprendizajes a lo largo del proyecto. Esta metodología ha sido ampliamente validada en proyectos de minería de datos y se adapta al tamaño del equipo y al plazo de ejecución. Además, la combinación de CRISP-DM con Design Science Research (DSR) proporciona un marco completo que no solo guía la ejecución técnica, sino que también asegura la relevancia y utilidad del artefacto desarrollado para los usuarios finales.

## 4. OBJETIVO GENERAL

Diseñar un índice geoespacial de criticidad urbana basado en la integración de variables de peligrosidad vial y criminal para la ciudad de Guayaquil, que permita priorizar zonas críticas de manera interpretable y replicable.

## 5. OBJETIVOS ESPECÍFICOS

- Identificar y georreferenciar las variables relacionadas con la peligrosidad vial, la peligrosidad criminal, la exposición y la vulnerabilidad.
- Definir y justificar la fórmula del índice de criticidad mediante el establecimiento del esquema de normalización, la asignación de pesos a las variables y el método de agregación, con base en un análisis multicriterio debidamente documentado.
- Desarrollar e implementar un componente de gemelo digital urbano para Guayaquil, mediante un módulo computacional en Python que permita integrar y actualizar datos relacionados con la siniestralidad vial y la criminalidad, calcular el índice de criticidad urbana, generar rankings y mapas de calor de las zonas críticas.
- Evaluar la estabilidad e interpretabilidad del índice mediante un análisis de sensibilidad y la comparación de sus resultados con puntos críticos identificados previamente, incluyendo vías con altos niveles de siniestralidad.

## 6. HIPÓTESIS DE INVESTIGACIÓN

**Hipótesis Principal:**

El índice geoespacial de criticidad urbana construido a partir de variables de peligrosidad vial y criminal identifica zonas con mayor concentración de riesgos urbanos en Guayaquil, y su ranking de criticidad es estable ante variaciones razonables en los pesos de las variables componentes.

**Hipótesis Específicas:**

- **H1:** Las zonas con altos niveles de criticidad según el índice propuesto presentan una coincidencia espacial significativa con los distritos que registran una alta concentración de delitos, así como con las vías que presentan mayores niveles de siniestralidad vial.
- **H2:** Existe una superposición espacial significativa entre las zonas que presentan altos niveles de siniestralidad vial y aquellas que registran una elevada incidencia criminal en Guayaquil.
- **H3:** El ranking de criticidad generado por el índice propuesto mantiene una alta estabilidad ante variaciones de ±20 % en los pesos asignados a las variables, evidenciada mediante el coeficiente de correlación de Spearman.

## 7. MARCO TEÓRICO Y REFERENCIAL

### 7.1 Gestión del Riesgo Urbano y Criticidad

El concepto de riesgo urbano integra tres dimensiones fundamentales: peligrosidad, entendida como la probabilidad de ocurrencia de eventos adversos; exposición, relacionada con la presencia de personas e infraestructura en zonas de riesgo; y vulnerabilidad, asociada con la susceptibilidad al daño. Este modelo ha sido ampliamente abordado en la literatura sobre gestión de riesgos y constituye el marco conceptual para el índice propuesto. La literatura especializada señala la importancia de considerar las interdependencias entre los diferentes componentes urbanos, debido a que los efectos de un riesgo pueden propagarse y generar impactos adicionales. Barroca (2024) sostiene que esta perspectiva sistémica permite comprender cómo los riesgos presentes en un componente del sistema urbano pueden afectar a otros, generando efectos que no serían identificados mediante análisis sectoriales.

El concepto de resiliencia, entendido como la capacidad de un sistema para absorber perturbaciones y recuperar sus niveles de funcionamiento, también ha adquirido relevancia en la planificación urbana. En este contexto, los gemelos digitales urbanos, como representaciones virtuales que integran información de diferentes fuentes, constituyen una herramienta para el análisis y la gestión de riesgos urbanos. Wang et al. (2024) señalan que estos pueden contribuir a fortalecer la resiliencia urbana mediante la integración de información, la simulación de escenarios y la evaluación de posibles intervenciones. Por su parte, Mazzetto (2024) destaca que la interoperabilidad entre sistemas y la integración de datos heterogéneos representan desafíos para la gestión urbana basada en datos. Estos antecedentes respaldan la necesidad de integrar diferentes fuentes de información en el desarrollo de herramientas orientadas a la identificación y priorización de zonas de criticidad urbana.

### 7.2 Geografía del Crimen y Análisis de Siniestralidad Vial

La geografía del crimen ha evidenciado que la violencia no se distribuye de manera aleatoria en el territorio, sino que presenta patrones espaciales que pueden ser identificados mediante técnicas de análisis geoespacial. Este campo de estudio ha desarrollado herramientas metodológicas orientadas a la identificación de puntos calientes y al análisis de los factores asociados con la concentración espacial del delito. En Guayaquil, investigaciones previas han aplicado técnicas de análisis multivariante y geoespacial para identificar zonas de concentración delictiva. Luzuriaga y Scott (2025), en su investigación sobre extorsiones en Guayaquil, emplearon la Razón Estandarizada de Mortalidad, el Riesgo Relativo, el análisis de componentes principales (PCA) y estadísticos espaciales como Getis-Ord Gi\* e Índice Local de Moran. Sus resultados permitieron identificar agrupaciones significativas de circuitos considerados puntos calientes, principalmente entre la zona noroeste y el sur de la ciudad. Este estudio constituye un antecedente relevante para la presente investigación, al evidenciar la aplicabilidad de las técnicas de análisis espacial en el contexto de Guayaquil.

De manera similar, el análisis de la siniestralidad vial permite identificar patrones de concentración de accidentes asociados con factores como las características de la infraestructura vial, el flujo vehicular y la presencia de población vulnerable. El Observatorio de Movilidad de la ATM (2026) constituye una fuente relevante para este análisis, al proporcionar información que permite identificar patrones de siniestralidad en diferentes vías de la ciudad. La integración de los enfoques de geografía del crimen y análisis de siniestralidad vial constituye un elemento central del presente estudio, debido a que permite analizar de manera conjunta dos dimensiones de peligrosidad que tradicionalmente han sido estudiadas por separado y que pueden presentar patrones de concentración espacial en el territorio.

### 7.3 Análisis Multicriterio y Normalización

El análisis multicriterio (MCDA) proporciona el marco metodológico para integrar dimensiones heterogéneas en un índice compuesto. Técnicas como el Proceso de Análisis Jerárquico (AHP) y la normalización min-max permiten la agregación de variables en escalas comparables. La investigación sobre índices compuestos ha demostrado que la selección del método de normalización y ponderación afecta significativamente los resultados, lo que justifica la inclusión de análisis de sensibilidad como componente metodológico esencial. Gao et al. (2024) demuestran en su investigación sobre predicción de accidentes de tránsito que la incorporación de análisis de incertidumbre mejora significativamente la confiabilidad de los modelos predictivos, un principio que se aplica directamente al análisis de sensibilidad propuesto en este estudio.

Chen et al. (2024), por su parte, destacan la importancia de integrar gemelos digitales con dashboards geoespaciales para la planificación de resiliencia costera, mostrando cómo la combinación de métodos de análisis espacial con herramientas de visualización puede potenciar la toma de decisiones. La experiencia de estos autores en la integración de datos heterogéneos y la visualización de resultados es directamente relevante para el presente estudio, que busca no solo calcular un índice sino también comunicar sus resultados de manera efectiva a los tomadores de decisiones.

### 7.4 CRISP-DM como Metodología de Desarrollo

CRISP-DM (Cross-Industry Standard Process for Data Mining) constituye un marco metodológico estructurado y flexible para proyectos de minería de datos y ciencia de datos. Sus seis fases, correspondientes a la comprensión del negocio, comprensión de los datos, preparación de los datos, modelado, evaluación y despliegue, permiten desarrollar el proyecto de manera iterativa y organizada (Wirth & Hipp, 2000). Esta metodología resulta adecuada para el presente estudio, debido a que permite estructurar las diferentes etapas relacionadas con la recopilación, preparación y análisis de los datos, así como con el desarrollo y evaluación del índice de criticidad urbana.

La combinación de CRISP-DM con Design Science Research (DSR) permite complementar el proceso técnico con un enfoque orientado al desarrollo y evaluación de un artefacto. Mientras CRISP-DM proporciona una estructura para la gestión y análisis de los datos, DSR orienta el diseño, desarrollo y evaluación del índice de criticidad propuesto, procurando que este responda al problema de investigación y pueda ser utilizado como una herramienta para la identificación y priorización de zonas críticas en Guayaquil.

## 8. MARCO METODOLÓGICO

### 8.1 Tipo de Investigación

La presente investigación es de tipo aplicada, debido a que busca desarrollar un artefacto metodológico, representado por un índice de criticidad urbana, que permita identificar y priorizar zonas críticas de Guayaquil a partir de la integración de variables de peligrosidad, exposición y vulnerabilidad. Asimismo, presenta un alcance descriptivo y exploratorio, ya que busca caracterizar la distribución espacial de las variables consideradas y explorar los patrones de concentración y relación entre las diferentes dimensiones del riesgo urbano. Finalmente, corresponde a un enfoque cuantitativo, debido a que emplea técnicas estadísticas, espaciales y computacionales para el procesamiento de los datos, la construcción del índice y la evaluación de sus resultados.

### 8.2 Enfoque y Modalidad de Investigación

La investigación adopta un enfoque cuantitativo, debido a que se fundamenta en la recopilación, procesamiento y análisis de datos espaciales y estadísticos para la construcción del índice de criticidad urbana. El análisis contempla el cálculo del índice, la generación de rankings de criticidad, el análisis espacial y la evaluación de su estabilidad ante variaciones en los pesos asignados a las variables.

En cuanto a su modalidad, la investigación corresponde al desarrollo tecnológico, debido a que se orienta al diseño y evaluación de un artefacto metodológico destinado a la identificación y priorización de zonas críticas. Para su desarrollo se empleará Design Science Research (DSR) como enfoque para el diseño y evaluación del índice, mientras que CRISP-DM será utilizada como metodología para organizar las etapas relacionadas con la recopilación, preparación, procesamiento y análisis de los datos.

### 8.3 Fuentes, Técnicas e Instrumentos para la Recolección de Datos

| Tipo de Fuente | Fuente | Técnica | Instrumento |
|---|---|---|---|
| Secundaria | Observatorio de Movilidad de Guayaquil (ATM) | Minería de Datos | Visualizador web, bases de datos descargables |
| Secundaria | Policía Nacional / ECU911 | Análisis de Datos | Reportes oficiales, bases de datos de emergencias |
| Secundaria | Instituto Nacional de Estadística y Censos (INEC) | Extracción de Datos | Plataforma de Datos Abiertos, Censos poblacionales |
| Secundaria | GAD Municipal de Guayaquil | Geoprocesamiento | Geoportal Municipal, archivos SIG |
| Secundaria | OpenStreetMap | Geoprocesamiento | API OSM, archivos de datos geográficos |
| Secundaria | Artículos científicos | Revisión Bibliográfica | Matrices de análisis documental, gestores bibliográficos |
| Secundaria | Informes institucionales y medios de comunicación | Análisis Documental | Reportes técnicos, notas periodísticas, documentos oficiales |

*Tabla 1. Fuentes, técnicas e instrumentos para la recolección de datos.*

### 8.4 Población y Muestra

La población de estudio comprende el área urbana del cantón Guayaquil, conformada por sus 16 parroquias urbanas. Esta delimitación territorial permite integrar información relacionada con la siniestralidad vial, la criminalidad, la exposición y la vulnerabilidad dentro de un mismo espacio geográfico, con el propósito de identificar y analizar patrones de concentración de criticidad urbana.

Para el análisis espacial se considerarán como unidades de análisis los circuitos de planificación policial definidos por la Policía Nacional, correspondientes a 67 circuitos según información reportada por Ecuavisa (2025). De manera complementaria, se contempla la posibilidad de utilizar una cuadrícula espacial de 500 × 500 metros, en caso de que la disponibilidad y resolución de los datos permitan un nivel de desagregación mayor. Esta alternativa facilitaría la identificación de áreas específicas con mayores niveles de criticidad dentro de los circuitos establecidos.

En cuanto a la cobertura temporal, se utilizarán datos correspondientes al período comprendido entre 2023 y 2026, priorizando el primer semestre de 2026 cuando exista información disponible. Esta delimitación permitirá considerar tanto información histórica para identificar patrones espaciales como datos recientes que contribuyan a representar las condiciones actuales de criticidad urbana en Guayaquil.

### 8.5 Análisis y Tratamiento de la Información

El tratamiento de la información comenzará con la integración de las diferentes fuentes de datos relacionadas con la siniestralidad vial, criminalidad, exposición y vulnerabilidad. Estas fuentes serán consolidadas en un conjunto de datos geográfico utilizando herramientas como GeoPandas, procurando estandarizar los sistemas de coordenadas y resolver posibles inconsistencias que puedan afectar la integración y el análisis posterior.

Una vez integrada la información, las variables serán sometidas a un proceso de normalización que permita hacer comparables sus diferentes escalas y unidades de medida. Como método principal se contempla la normalización min-max, mientras que el uso de z-score podrá ser considerado como una alternativa para evaluar el efecto que el método de normalización tiene sobre los resultados del índice.

Posteriormente, se realizará la agregación de las variables correspondientes a las dimensiones de peligrosidad vial, peligrosidad criminal, exposición y vulnerabilidad. El índice de criticidad se construirá mediante una combinación ponderada de estas dimensiones, de acuerdo con los pesos definidos en el diseño metodológico. Esta etapa permitirá obtener un valor de criticidad para cada unidad espacial de análisis y establecer un ranking de las zonas con mayores niveles de criticidad.

El análisis espacial permitirá identificar patrones de concentración y posibles agrupaciones de zonas con niveles elevados de criticidad. Para ello, se emplearán estadísticos espaciales que permitan cuantificar y visualizar la autocorrelación espacial de los valores del índice. Se aplicará el estadístico Getis-Ord Gi\*, una herramienta que permite identificar puntos calientes (hotspots) o puntos fríos (coldspots) de criticidad, es decir, áreas donde los valores altos o bajos se agrupan de manera estadísticamente significativa en el espacio. Paralelamente, se calculará el Índice de Moran Global, una medida que resume el grado de dependencia espacial en el conjunto de datos, indicando si la distribución de la criticidad tiende a ser agrupada, dispersa o aleatoria a lo largo del área de estudio. Para un análisis más detallado, se podrá utilizar el Índice de Moran Local (LISA), el cual permite identificar la contribución de cada unidad espacial a la autocorrelación global y detectar agrupaciones locales de valores similares que pueden no ser evidentes a nivel global. La combinación de estas técnicas permitirá no solo identificar zonas con altos niveles de criticidad, sino también caracterizar su relación con el entorno inmediato, proporcionando una base sólida para la planificación de intervenciones territoriales. En este sentido, investigaciones previas han demostrado que la incorporación de análisis de incertidumbre y sensibilidad en modelos de riesgo urbano mejora significativamente la confiabilidad de los resultados, lo que resulta particularmente relevante para la toma de decisiones en contextos de alta complejidad como el de Guayaquil (Gao et al., 2024).

La estabilidad del índice será evaluada mediante un análisis de sensibilidad que considere variaciones en los pesos asignados a las variables. El presente estudio se enfocará en un rango de variación de ±10 %, ±20 % y ±30 % en los pesos de las dimensiones que componen el índice. Para cuantificar la estabilidad del ranking, se empleará el coeficiente de correlación de Spearman, una medida no paramétrica que evalúa la fuerza y dirección de la asociación monótona entre dos rankings, lo que es particularmente adecuado para datos ordinales o cuando no se asume una distribución normal. Un coeficiente de Spearman cercano a 1 indicaría que el orden de las zonas se mantiene prácticamente inalterado a pesar de los cambios en la ponderación, lo que confirmaría la robustez del índice propuesto. Esta metodología se alinea con buenas prácticas en la construcción de índices compuestos para la evaluación de riesgos, donde el análisis de sensibilidad es un paso crítico para dotar de credibilidad y solidez a los resultados (Chen et al., 2024). Así lo demuestran también estudios sobre predicción de accidentes de tránsito, los cuales han evidenciado que la inclusión de análisis de incertidumbre permite una mejor comprensión de los factores que influyen en la ocurrencia de eventos adversos y fortalece la confianza en los modelos predictivos (Gao et al., 2024).

Finalmente, los resultados obtenidos serán contrastados con información disponible sobre zonas que presentan altos niveles de siniestralidad vial y criminalidad, tomando como referencia registros institucionales y fuentes secundarias verificables. De acuerdo con la disponibilidad y factibilidad del proceso de investigación, también podrá incorporarse la valoración de expertos como elemento complementario para analizar la interpretabilidad y utilidad del índice propuesto.

### 8.6 Matriz de Operacionalización de Variables

| Variable | Dimensión | Indicador | Técnica | Instrumento |
|---|---|---|---|---|
| **Siniestros con lesionados** | Peligrosidad Vial | N° / unidad espacial | Densidad | Observatorio ATM (2026) |
| **Siniestros con fallecidos** | Peligrosidad Vial | N° / unidad espacial | Densidad | Observatorio ATM (2026) |
| **Homicidios intencionales** | Peligrosidad Criminal | N° / unidad espacial | Densidad | Policía Nacional |
| **Robos (personas y domicilios)** | Peligrosidad Criminal | N° / unidad espacial | Densidad | Policía Nacional |
| **Densidad poblacional** | Exposición | Hab/km² | Conteo | INEC |
| **POIs** | Exposición | N° / unidad espacial | Conteo | GAD/OSM |
| **Flujo vehicular** | Exposición | Veh/día | Estimación | ATM/modelo propio |
| **Índice de pobreza** | Vulnerabilidad | % población | Porcentaje | INEC |
| **Vivienda precaria** | Vulnerabilidad | % viviendas | Porcentaje | INEC |
| **Servicios básicos** | Vulnerabilidad | % población | Porcentaje | INEC |

*Tabla 2. Matriz de operación de variables.*

## 9. METODOLOGÍA DE DESARROLLO A EMPLEAR

### 9.1 Justificación de la Metodología

El proyecto se desarrollará mediante la metodología CRISP-DM (Cross-Industry Standard Process for Data Mining), la cual proporciona un marco estructurado y flexible para la ejecución de proyectos de minería de datos y ciencia de datos (Wirth & Hipp, 2000). Su aplicación permitirá organizar de manera sistemática las diferentes etapas del proyecto, desde la comprensión y preparación de los datos hasta el desarrollo y evaluación del índice de criticidad urbana.

La selección de esta metodología responde a su carácter iterativo, que permite incorporar los resultados obtenidos durante el desarrollo y realizar ajustes cuando se identifiquen nuevos hallazgos o requerimientos. Asimismo, sus fases claramente definidas facilitan la organización de las actividades, la distribución de responsabilidades entre los investigadores y el seguimiento de los avances durante el período establecido para el proyecto. De esta manera, CRISP-DM proporciona una estructura metodológica que permite orientar el desarrollo del índice y mantener un proceso ordenado para el cumplimiento de los objetivos planteados.

### 9.2 Prácticas Aplicadas

El desarrollo del proyecto se realizará de manera iterativa, contemplando tres etapas principales. En una primera etapa se trabajará con un conjunto reducido de datos correspondientes a 2025, con el propósito de comprobar el funcionamiento inicial del modelo conceptual e identificar posibles ajustes. Posteriormente, se realizará la implementación con el conjunto completo de datos correspondientes al período 2023-2026, a partir de la cual se obtendrán los resultados del índice de criticidad. Finalmente, se efectuará una etapa de refinamiento y documentación de los resultados, incorporando los hallazgos obtenidos durante el desarrollo y las observaciones derivadas del proceso de revisión.

Para garantizar la trazabilidad y facilitar el trabajo colaborativo, se utilizarán Git y GitHub como herramientas de control de versiones del código fuente. Esto permitirá registrar los cambios realizados durante el desarrollo y mantener un historial organizado de las diferentes versiones del proyecto.

El seguimiento del proyecto se realizará mediante revisiones periódicas con el docente tutor, previstas inicialmente con una frecuencia quincenal. Estas revisiones permitirán verificar el avance de las actividades, identificar posibles ajustes y mantener la correspondencia entre el desarrollo del proyecto y los objetivos establecidos. Finalmente, se realizarán pruebas de validación utilizando información de contraste disponible sobre zonas identificadas previamente como puntos críticos, con el propósito de evaluar la coherencia y utilidad de los resultados obtenidos mediante el índice propuesto.

### 9.3 Historias de Usuario / Requisitos

| ID | Tipo | Requisito | Descripción | Prioridad | Iteración |
|---|---|---|---|---|---|
| RF-01 | Funcional | Carga de datos viales | Cargar datos de siniestros viales (ATM) en formato CSV. | Alta | 1 |
| RF-02 | Funcional | Carga de datos criminales | Cargar datos de homicidios y robos (Policía Nacional) en formato CSV. | Alta | 1 |
| RF-03 | Funcional | Carga de datos contextuales | Cargar datos socioeconómicos (INEC) y geoespaciales. | Alta | 1 |
| RF-04 | Funcional | Georreferenciación | Unir incidentes a unidades de análisis (circuitos/celdas) mediante join espacial. | Alta | 1 |
| RF-05 | Funcional | Normalización | Implementar normalización min-max y z-score para todas las variables. | Alta | 2 |
| RF-06 | Funcional | Cálculo del índice | Calcular índice como media ponderada de dimensiones (vial, criminal, exposición, vulnerabilidad). | Alta | 2 |
| RF-07 | Funcional | Ranking de zonas | Generar ranking de zonas críticas con percentiles (crítico, alto, medio, bajo). | Alta | 2 |
| RF-08 | Funcional | Análisis de sensibilidad | Variar pesos (±10%, ±20%, ±30%) y calcular correlación de Spearman entre rankings. | Media | 2 |
| RF-09 | Funcional | Mapas de criticidad | Generar mapas interactivos (Folium) y mapas de calor de criticidad. | Media | 2 |
| RF-10 | Funcional | Exportación de resultados | Exportar ranking, índices y mapas en formatos CSV, GeoJSON y HTML. | Baja | 3 |
| RF-11 | Funcional | Registro de ejecución | Generar log con parámetros, fechas y advertencias del procesamiento. | Baja | 3 |
| RNF-01 | No Funcional | Rendimiento | Procesar datos completos en menos de 10 minutos en hardware estándar. | Alta | |
| RNF-02 | No Funcional | Portabilidad | Ejecutable en Windows, macOS y Linux con dependencias open source. | Alta | |
| RNF-04 | No Funcional | Reproducibilidad | Resultados reproducibles con parámetros documentados y semillas fijas. | Alta | |
| RNF-05 | No Funcional | Mantenibilidad | Código modular con separación clara de responsabilidades. | Media | |
| CA-01 | Criterio | Estabilidad del ranking | Correlación de Spearman > 0.85 ante variaciones de ±20% en pesos. | Alta | 3 |
| CA-02 | Criterio | Coincidencia espacial | Tasa de coincidencia > 70% con puntos críticos reportados por ATM y Policía. | Alta | 3 |

*Tabla 3. Historia de usuarios / requisitos. (El original no incluye RNF-03.)*

## 10. CRONOGRAMA DE ACTIVIDADES

| Actividad | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|:-:|:-:|:-:|:-:|
| **Fase 1: Comprensión del Negocio** | | | | |
| Análisis institucional y definición de objetivos | X | | | |
| **Fase 2: Comprensión de Datos** | | | | |
| Recolección de datos (ATM, Policía, INEC, GAD) | X | X | | |
| Análisis exploratorio y calidad de datos | | X | | |
| **Fase 3: Preparación de Datos** | | | | |
| Limpieza, geocodificación y normalización | | X | X | |
| **Fase 4: Modelado** | | | | |
| Desarrollo del módulo risk_index.py | | | X | |
| Generación de rankings y mapas | | | X | |
| Módulo de análisis de sensibilidad | | | X | |
| **Fase 5: Evaluación** | | | | |
| Análisis de sensibilidad | | | | X |
| Validación con criterio experto y puntos críticos | | | | X |
| **Fase 6: Despliegue** | | | | |
| Documentación técnica e informe final | | | | X |
| Preparación de sustentación | | | | X |

*Tabla 4. Cronograma de actividades.*

## 11. PRESUPUESTO Y FINANCIAMIENTO

### 11.1 Tabla de Presupuestos

| Rubro | Descripción | Costo Total (USD) |
|---|---|---:|
| **Recursos Humanos** | | |
| Investigador 1 | Dedicación al proyecto (4 meses × SBU $470) | $1.880,00 |
| Investigador 2 | Dedicación al proyecto (4 meses × SBU $470) | $1.880,00 |
| **Subtotal Recursos Humanos** | | **$3.760,00** |
| **Recursos Técnicos** | | |
| Software y herramientas | Python, QGIS, librerías open source (licencias gratuitas) | $0,00 |
| Equipo de cómputo | Computador portátil y PC para procesamiento de datos geoespaciales | $2.400,00 |
| **Subtotal Recursos Técnicos** | | **$2.400,00** |
| **Movilización** | | |
| Transporte | Visitas a instituciones para recolección de datos, entrevistas y reuniones | $100,00 |
| **Subtotal Movilización** | | **$100,00** |
| **Materiales** | | |
| Impresión y encuadernación | Informes, manual técnico, presentación de sustentación | $80,00 |
| **Subtotal Materiales** | | **$80,00** |
| **TOTAL PRESUPUESTO** | | **$6.340,00** |

*Tabla 5. Presupuesto establecido.*

### 11.2 Tabla de financiamiento

| Rubro | Costo Total (USD) | Fuente de Financiamiento |
|---|---:|---|
| **Recursos Humanos** | | |
| Investigador 1 | $1.880,00 | Autores del proyecto |
| Investigador 2 | $1.880,00 | Autores del proyecto |
| **Recursos Técnicos** | | |
| Software y herramientas | $0,00 | No aplica |
| Equipo de cómputo | $2.400,00 | Autores del proyecto |
| **Movilización** | | |
| Transporte | $100,00 | Autores del proyecto |
| **Materiales** | | |
| Impresión y encuadernación | $80,00 | Autores del proyecto |
| **TOTAL** | **$6.340,00** | **Autores del proyecto** |

*Tabla 6. Tabla de financiamiento.*

## 12. BENEFICIOS ESPERADOS DEL PROYECTO

El estudio contribuirá a la generación de conocimiento metodológico relacionado con la construcción de índices geoespaciales de criticidad urbana que integren las dimensiones de peligrosidad vial y criminal, aplicados al contexto ecuatoriano. Asimismo, se contempla el desarrollo de un módulo de código abierto en Python que facilite la replicación de la metodología en otras ciudades con características similares. De esta manera, la investigación contribuirá al fortalecimiento de la línea de investigación en Ciencias Básicas de Datos aplicada al análisis y desarrollo urbano.

En el ámbito institucional, el estudio proporcionará una herramienta objetiva para apoyar la priorización de intervenciones relacionadas con la seguridad vial y la seguridad ciudadana en Guayaquil. Esta herramienta podrá complementar iniciativas institucionales existentes, como el Observatorio de Movilidad de la Agencia de Tránsito y Movilidad (ATM, 2026), las estrategias de georreferenciación implementadas por la Policía Nacional (Ecuavisa, 2025) y los visualizadores de datos desarrollados por el Municipio de Guayaquil (Alcaldía de Guayaquil, 2026). La integración de estas dimensiones permitirá disponer de información que facilite la identificación de zonas donde convergen diferentes factores de riesgo y contribuya a una mejor coordinación de las intervenciones institucionales.

Desde una perspectiva social, el estudio contribuirá a mejorar la eficiencia en la asignación de recursos públicos mediante la identificación y priorización de zonas en las que convergen elevados niveles de siniestralidad vial e incidencia criminal. La disponibilidad de esta información permitirá orientar las intervenciones hacia sectores con mayores niveles de criticidad, contribuyendo a reducir la exposición de la población a diferentes riesgos urbanos y favoreciendo el desarrollo de una ciudad más segura y resiliente.

En el ámbito tecnológico, el estudio permitirá desarrollar un módulo reutilizable que pueda integrarse posteriormente con plataformas orientadas a la representación y análisis de entornos urbanos, incluidos los sistemas de gemelos digitales. Asimismo, se contempla la generación de dashboards interactivos que faciliten la visualización y comunicación de los resultados a los responsables de la toma de decisiones. El diseño del módulo considerará la posibilidad de actualizar periódicamente los datos, lo que permitirá realizar un seguimiento de los cambios en los niveles de criticidad urbana.

## 13. DERECHOS DE PROPIEDAD INTELECTUAL

El desarrollo de este trabajo de tesis contempla la generación de resultados susceptibles de protección por Propiedad Intelectual (derechos de autor, patentes, programa de computador).

¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [x] Software
- [x] Modelo/algoritmo
- [x] Manual/documentación técnica
- [ ] No aplica

Los derechos patrimoniales de los productos generados en el presente trabajo de tesis corresponderán a la institución, de conformidad con la normativa vigente. Los autores conservarán los derechos morales sobre su obra.

## 14. REFERENCIAS BIBLIOGRÁFICAS

Alcaldía de Guayaquil. (2026, abril 19). *Alcaldía de Guayaquil fortalece la planificación de la seguridad vial con apoyo técnico internacional.* <https://guayaquil.gob.ec/planificacion-seguridad-vial-guayaquil/>

ATM Agencia de Tránsito y Movilidad. (2026). *Observatorio de Movilidad de Guayaquil.* <https://atm.gob.ec/observatorio/>

Barroca, B. (2024). Urban critical infrastructures vulnerability and resilience: A systemic approach. *HAL Archives Ouvertes.* <https://api.archives-ouvertes.fr/>

Chen, C., Li, X., & Zhang, Y. (2024). Integrating urban digital twins with cloud-based geospatial dashboards for coastal resilience planning: A case study in Florida. *arXiv.* <https://arxiv.org/abs/2403.18188>

Diario Expreso. (2026, junio 15). Guayas se mantiene como la provincia con más fallecidos por siniestros viales en 2026. *Diario Expreso.* <https://www.expreso.ec/guayaquil/guayas-mantiene-provincia-fallecidos-siniestros-viales-2026-285933.html>

Ecuavisa. (2025, diciembre 11). Policía elabora mapeo de delitos en Guayaquil, Durán y Samborondón. *Ecuavisa.* <https://www.ecuavisa.com/ecuador/policia-elabora-mapeo-de-delitos-en-guayaquil-duran-y-samborondon-20140616-0009.html>

Ecuavisa. (2026, junio 20). Choque en el sur de Guayaquil deja tres heridos, entre ellos un menor de edad. *Ecuavisa.* <https://www.ecuavisa.com/guayaquil/choque-25-de-julio-guayaquil-tres-heridos-20260621-0020.html>

El Diario Ecuador. (2026, agosto 18). Tía y sobrino mueren tras ataque armado durante un velorio en Guayaquil. *El Diario Ecuador.* <https://www.eldiario.ec/seguridad/tia-y-sobrino-mueren-tras-ataque-armado-durante-un-velorio-en-guayaquil-18082026/>

El Universo. (2026, marzo 5). 'Siempre hay accidentes', dicen moradores y trabajadores de la autopista Narcisa de Jesús, donde en 2025 se reportaron 190 siniestros. *El Universo.* <https://www.eluniverso.com/guayaquil/comunidad/siempre-hay-accidentes-dicen-moradores-y-trabajadores-de-la-avenida-narcisa-de-jesus-donde-en-2025-se-reportaron-190-siniestros-nota/>

Gao, J., Chen, Y., & Wang, H. (2024). Uncertainty-aware probabilistic graph neural networks for road-level traffic crash prediction. *Accident Analysis & Prevention.* <https://doi.org/10.1016/j.aap.2024.107801>

Infobae. (2026, agosto 17). Violencia en Ecuador: tres menores fueron asesinados durante un ataque armado contra una vivienda en Guayaquil. *Infobae.* <https://www.infobae.com/america/america-latina/2026/08/17/violencia-en-ecuador-tres-menores-fueron-asesinados-durante-un-ataque-armado-contra-una-vivienda-en-guayaquil/>

Luzuriaga, P. J., & Scott, O. A. (2025). *Identificación de puntos calientes mediante análisis multivariante y geoespacial de extorsiones en la ciudad Guayaquil empleando aprendizaje automático* [Tesis de pregrado, ESPOL]. <http://www.dspace.espol.edu.ec/handle/123456789/65682>

Mazzetto, F. (2024). A review of urban digital twins integration, challenges, and future directions in smart city development. *Sustainability, 16*(19), 8337. <https://doi.org/10.3390/su16198337>

Primicias. (2026, mayo 13). Tras muerte de Jaime Pacheco en vía a la Costa, resurge informe técnico de ATM que pedía un semáforo por "riesgo grave" para peatones. *Primicias.* <https://www.primicias.ec/guayaquil/muerte-jaime-pacheco-via-costa-informe-tecnico-atm-semaforo-riesgo-peatones-122770/>

Radio Pichincha. (2026, mayo 22). 763 homicidios: Guayaquil vive su tercer inicio de año más violento de toda su historia. *Radio Pichincha.* <https://www.radiopichincha.com/763-homicidios-guayaquil-violento-historia/>

Radio Pichincha. (2026, junio 22). El segundo año más violento de la historia: 3.485 homicidios registrados entre enero y mayo ocurrieron en 138 cantones ecuatorianos. *Radio Pichincha.* <https://www.radiopichincha.com/violento-historia-3485-homicidios-138-cantones-ecuatorianos/>

Wang, Z., Liu, Y., & Zhang, X. (2024). Digital twin approach for enhancing urban resilience: A cycle between virtual space and the real world. *Resilient Cities and Structures, 3*(2), 34–45. <https://doi.org/10.1016/j.rcns.2024.06.002>

Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining*, 29-39.

---

## ANEXOS

### ANEXO I.- Formato de evaluación de la propuesta de trabajo de integración curricular

*(Formulario manuscrito escaneado; contenido transcrito.)*

**Facultad de Ingeniería Industrial — Carrera de Sistemas de Información**

| Campo | Contenido |
|---|---|
| Nombre de la propuesta de trabajo de integración curricular | Índice Geoespacial de criticidad Urbana basado en Peligrosidad, exposición y Vulnerabilidad |
| Nombre del estudiante(s) | Yagual Cedeño Byron Andrés, Christopher Córdova Zúñiga |
| Facultad | Ing. Industrial |
| Carrera | Sist. Información |
| Línea de investigación | Ciencias Básicas |
| Sub-línea de investigación | Inteligencia Artificial y Ciencia de Datos |
| Fecha de presentación de la propuesta de trabajo de integración curricular | 26/8/2026 |
| Fecha de evaluación de la propuesta de trabajo de integración curricular | 26/8/2026 |

| Aspectos para considerar | Cumple (Sí) | Cumple (No) | Observaciones |
|---|:-:|:-:|---|
| Título de la propuesta de trabajo de integración curricular | ✔ | | |
| Línea de investigación / Sublínea de investigación | ✔ | | |
| Planteamiento del problema | ✔ | | |
| Justificación e importancia | ✔ | | |
| Objetivos de la investigación | ✔ | | |
| Metodología a emplearse | ✔ | | |
| Cronograma de actividades | ✔ | | |
| Presupuesto y financiamiento | ✔ | | |

- [x] APROBADO
- [ ] APROBADO CON OBSERVACIONES
- [ ] NO APROBADO

Ing. Manuel Samaniego Zamora, MBA — DECANO DE LA FACULTAD
CC: Director de Carrera, Gestor de Titulación

### Rúbrica de evaluación

*(Anteproyecto de Trabajo de Titulación — Sistemas de la Información, página 29.)*

| Criterios generales de calificación | | Nota evaluador | Nota máxima |
|---|---|:-:|:-:|
| Estructura | Planteamiento y formulación del problema. Innovación (aporte novedoso o mejora significativa) | 1 | 1 |
| | Alcance — Justificación | 1 | 1 |
| | Objetivos (General y Específicos) coherentes | 1 | 1 |
| | Marco Teórico — Marco Metodológico — Referencias Bibliográficas | 1 | 1 |
| | Metodología de Desarrollo | 1 | 1 |
| **(Subtotal Estructura)** | | | **5** |
| Aspectos de Fondo | Cronograma — Presupuesto | 1 | 1 |
| | Manejo claro de las ideas. Beneficios esperados del proyecto | 1 | 1 |
| | Claridad y coherencia en la redacción | 1 | 1 |
| | Referentes teóricos sustentados | 1 | 1 |
| | Argumentos para una propuesta | 1 | 1 |
| **(Subtotal Aspectos de Fondo)** | | | **5** |
| **NOTA SOBRE 10** | | **10** | **10** |

### ANEXO C — Rúbrica de evaluación para proyectos grupales de integración curricular

*(Página 30; marcas manuscritas transcritas.)*

| # | Aspectos evaluados | No cumple | Cumple parcialmente | Cumple |
|:-:|---|:-:|:-:|:-:|
| 1 | **Tema del proyecto:** se describe un tema que contenga la problemática de estudio, y que se ajuste a la línea de investigación de la Carrera y a la pirámide de investigación de la Facultad. | | | ✔ |
| 2 | **Definición del problema:** se identifica un problema complejo o con múltiples abordajes, y se especifican los múltiples enfoques de la investigación planteada. | | | ✔ |
| 3 | **División de tareas:** se indica el plan de trabajo detallado incluyendo hitos y plazos para cada fase del proyecto. | | | ✔ |
| 4 | **Desarrollo de objetivos:** se describen los objetivos con enfoques específicos para abordar los diferentes aspectos del problema planteado; estos se ajustan al tema propuesto. | | | ✔ |
| 5 | **Descripción de propiedad intelectual:** se indica si el proyecto tendrá como resultado un diseño industrial, desarrollo de software, modelos de utilidad, patentes de invención o algún otro producto enmarcado en la normativa ecuatoriana de propiedad intelectual; se deberá especificar y detallar en la propuesta. | | | ✔ |

*Para aprobación del proyecto de tesis, se considerará la siguiente valoración: los proyectos deberán cumplir con todos los puntos de la rúbrica; en caso de cumplimiento parcial o incumplimiento de 1 o más puntos, el estudiante tendrá que realizar las respectivas correcciones para volver a ser evaluado.*

### FIRMAS

*(Página 31; firmas manuscritas.)*

- Christopher Moisés Córdova Zúñiga — C.I.# 0959360744
- Byron Andrés Yagual Cedeño — C.I.# 0956926670
- Docente revisor del anteproyecto: Michelle Vera *(lectura aproximada de la firma)* — C.I.# 0918586298
- Docente revisor del anteproyecto: Juan Carlos García — C.I.# 130857930 *(lectura aproximada)*
