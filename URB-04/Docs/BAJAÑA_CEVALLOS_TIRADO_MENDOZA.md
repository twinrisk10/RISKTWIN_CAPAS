# UNIVERSIDAD DE GUAYAQUIL
## FACULTAD DE INGENIERÍA INDUSTRIAL

### ANTEPROYECTO DE TRABAJO DE TITULACIÓN

## Datos Generales

| | |
|---|---|
| **CARRERA:** | Sistemas de la Información |
| **FECHA:** | 27 de agosto de 2026 |

| | APELLIDOS | NOMBRES |
|---|---|---|
| **ESTUDIANTE 1:** | Bajaña Cevallos | Rosa Haydee |
| **ESTUDIANTE 2:** | Tirado Mendoza | Kelvin Aarón |

**Correo electrónico institucional y personal:**

- Rosa.bajanace@ug.edu.ec
- Kelvin.tiradom@ug.edu.ec

**Teléfono:** 0994771204 / 0963955292

## Tema

**TEMA:** Aplicación de inteligencia artificial para detección de patrones de riesgo urbano en datos multimodales.

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
- [x] Local
- [ ] Otros

---

## 0. Ficha técnica del proyecto

| Campo | Descripción |
|---|---|
| **Código** | URB-04 |
| **Bloque / caso** | Sistema / Urbano |
| **Capa principal** | Capa de IA / Big Data |
| **Capas relacionadas / insumos** | Consume datos, grafos e indicadores producidos por otros bloques del proyecto FCI 2026-046 (RISKTWIN); produce un motor analítico integrable a una futura API o dashboard. |
| **Tema de tesis** | Aplicación de IA para detección de patrones de riesgo urbano en datos multimodales. |
| **Tutor líder** | Ing. Juan Carlos García |
| **Pregunta de investigación** | ¿Qué modelos de aprendizaje automático permiten identificar patrones o clasificar zonas de riesgo urbano a partir de datos multimodales? |
| **Objetivo general** | Implementar y evaluar modelos de IA para identificar patrones o niveles de riesgo urbano a partir de variables multimodales. |
| **Producto detallado** | Implementar modelos de IA para detectar patrones, agrupar zonas o clasificar niveles de riesgo, usando variables geoespaciales, de grafos, contextuales y de eventos, incluyendo una comparación con enfoques basados en grafos (GCN/GraphSAGE) que aprovechen explícitamente el insumo de red urbana. |
| **Subproductos verificables** | Dataset de entrenamiento; pipeline ML; modelos baseline (RF/XGBoost); modelo basado en grafos; modelo de clustering; métricas; protocolo de validación de datos sintéticos; explicación de variables (SHAP); notebook reproducible; comparación de modelos; especificación de salida para API. |
| **Responsabilidad Estudiante A** | Datos y features: construir el dataset analítico, seleccionar variables, preparar el baseline, documentar la operacionalización de variables y ejecutar la validación estadística de los datos sintéticos (prueba Kolmogorov-Smirnov). |
| **Responsabilidad Estudiante B** | Modelado y evaluación: entrenar modelos (incluido el enfoque de grafos), comparar resultados, interpretar variables y exportar el componente integrable con su especificación de salida para la API. |
| **Diseño experimental / alcance** | Comparación de modelos supervisados (baseline) y un modelo basado en grafos cuando existan etiquetas; alternativa no supervisada mediante clustering/scoring, incluyendo variantes que incorporan la estructura del grafo (Spectral Clustering o Node2Vec + K-Means), cuando no las haya. |
| **Métodos y tecnologías** | Clustering (k-means, Spectral Clustering, Node2Vec + K-Means); Random Forest / XGBoost; Graph Convolutional Network o GraphSAGE como enfoque avanzado; validación cruzada; SHAP; reducción de dimensionalidad; prueba de Kolmogorov-Smirnov para validación de datos sintéticos. |
| **Métricas clave** | Accuracy, F1-Score macro y PR-AUC si hay etiquetas (con atención al desbalanceo de clases); silhouette, índice de Calinski-Harabasz y de Davies-Bouldin si es clustering; estabilidad; interpretabilidad; coherencia espacial (índice de Moran). |
| **Dataset / fuentes** | Datos de incidentes si están disponibles (ECU-911, portales de datos abiertos de tránsito); variables sintéticas o simuladas, validadas estadísticamente, si no existe un histórico suficiente. |
| **Criterios de aceptación** | Modelo con resultados reproducibles, métrica reportada, datos sintéticos validados frente a un protocolo estadístico y experto, e integración posible con una API mediante una estructura de salida definida. |
| **Entregable verificable** | Modelo ML (baseline + grafo) + notebook + reporte de resultados + especificación de salida (JSON) + exportación para API. |
| **Recomendación metodológica** | CRISP-ML(Q) + Design Science Research + evaluación comparativa de modelos, con un mapa de correspondencia explícito entre ambas metodologías (ver sección 9.3). |
| **Dependencias / integración horizontal** | Consume indicadores y grafo; aporta el motor analítico para un futuro dashboard y simulación. |
| **Riesgo principal y mitigación** | Falta de etiquetas reales y dependencia excesiva de datos sintéticos. Se mitiga con clustering, scoring semi-supervisado, validación experta (urbanistas o Policía de Tránsito) y prueba de Kolmogorov-Smirnov entre datos reales y simulados. |
| **Publicación / artículo potencial** | A4 / J1 |

**Keywords (EN, últimos 3 años):** "machine learning crash prediction"; "spatiotemporal risk prediction"; "graph neural networks"; "urban traffic safety"; "accident severity classification"; clustering; "zero-inflated"; "risk ranking".

Esta ficha resume el encargo puntual de este bloque dentro del proyecto FCI 2026-059 (RISKTWIN) Gemelo Digital Multimodal para la Gestión Inteligente del Riesgo: otros bloques se encargan de captar y estructurar los datos crudos, los grafos y los indicadores; a este bloque (URB-04) le corresponde exclusivamente la capa analítica, es decir, construir, entrenar, comparar e interpretar los modelos de IA que convierten esos insumos en una clasificación de riesgo por zona, lista para ser consumida por una API o un dashboard.

## 1. Planteamiento y formulación del problema

### 1.1 Antecedentes

Guayaquil concentra una carga considerable de eventos de riesgo urbano, tanto delictivos como viales. Según cifras del Ministerio del Interior citadas por Primicias (2026), la ciudad registró 2.545 homicidios intencionales en 2025, el peor año de la historia reciente del país, y el Observatorio Ecuatoriano de Crimen Organizado (OECO, 2025) señala que la zona de planificación 8, que agrupa Guayaquil, Durán y Samborondón, concentra el 39,5 % de los homicidios del país. A esta problemática se suma la siniestralidad vial, un fenómeno igualmente disperso en el espacio urbano y con patrones temporales propios, que en la literatura internacional ha sido abordado con más profundidad metodológica que el riesgo delictivo (Behboudi et al., 2024; Chai et al., 2024).

En ambos dominios, delito y accidentalidad, el reto de fondo es el mismo: los eventos de riesgo no se distribuyen de forma aleatoria en la ciudad, sino que se concentran en ciertas zonas y momentos, en función de variables geoespaciales (ubicación, distancia a puntos de interés), variables de grafo (conectividad de la red vial, cercanía entre sectores), variables contextuales (uso de suelo, densidad, iluminación) y el historial de eventos previos. Estas relaciones no son evidentes a simple vista ni se explotan sistemáticamente en la gestión urbana local, porque no existe un modelo analítico que las combine para producir una clasificación de riesgo por zona.

La literatura reciente sobre predicción de riesgo vial y urbano mediante aprendizaje automático ofrece evidencia consistente de que estos patrones sí son aprendibles. Estudios como el de Gao et al. (2024) y Hu et al. (2024) muestran que las redes neuronales de grafos capturan la dependencia espacial entre zonas contiguas mejor que los modelos que tratan cada sector como independiente, mientras que revisiones sistemáticas como la de Chai et al. (2024) y Behboudi et al. (2024) documentan qué variables y qué algoritmos, desde árboles de decisión hasta arquitecturas profundas, rinden mejor según la disponibilidad de datos. En el contexto ecuatoriano, el trabajo de Arciniegas-Ayala et al. (2024), desarrollado en la Escuela Politécnica Nacional, confirma que arquitecturas relativamente simples pueden clasificar niveles de riesgo de forma competitiva cuando los datos etiquetados son limitados, una condición muy probable en el contexto de este proyecto.

Este bloque (URB-04) se inserta precisamente en ese punto: no le corresponde construir la infraestructura de captación de datos ni el grafo urbano esos insumos los produce otro bloque del sistema, sino tomar esos datos, grafos e indicadores y convertirlos, mediante modelos de IA comparados de forma rigurosa, en un motor analítico capaz de identificar patrones o clasificar el nivel de riesgo por zona. Dado que el insumo de grafo forma parte central de ese encargo, el diseño experimental de este anteproyecto incorpora ahora, de manera formal, una arquitectura basada en grafos como parte del comparativo de modelos

### 1.2 Planteamiento del problema

Aun cuando un sistema urbano disponga de datos geoespaciales, de grafo, contextuales y de eventos, esos datos por sí solos no constituyen conocimiento accionable. Sin una capa de modelado que los procese, cada variable permanece aislada: la ubicación de un sector no se relaciona con su conectividad vial, y el historial de eventos no se traduce en una probabilidad o un nivel de riesgo comparable entre zonas. La ausencia de esta capa analítica impide que el resto del sistema una eventual API o un dashboard de monitoreo tenga algo que mostrar más allá de datos crudos.

El problema se agrava por una limitación práctica común en proyectos de este tipo, en los que no siempre existe un historial de incidentes suficientemente completo y etiquetado para entrenar un modelo supervisado clásico. Cuando las etiquetas de riesgo no están disponibles o son escasas, la mayoría de los enfoques convencionales de clasificación simplemente no son aplicables, y el proyecto necesita una alternativa metodológica como el agrupamiento no supervisado o el scoring semi-supervisado que aun así permita producir una clasificación de riesgo defendible. Recurrir a variables sintéticas mitiga esta carencia solo de forma parcial: si su representatividad no se valida frente a algún referente real o experto, el artefacto resultante corre el riesgo de perder validez externa, por lo que este anteproyecto incorpora un protocolo específico de validación de los datos simulados.

### 1.3 Causas

- No existe, dentro del sistema urbano, una capa de modelado que combine variables geoespaciales, de grafo, contextuales y de eventos en una clasificación de riesgo por zona.
- El historial de incidentes disponible puede ser parcial, disperso entre fuentes o carecer de etiquetas confiables de nivel de riesgo.
- Los datos de origen (grafo urbano, indicadores) los produce otro bloque del sistema, por lo que este bloque depende de la calidad y el formato en que esos insumos lleguen.
- No existe, hasta el momento, un componente exportable (modelo entrenado, notebook reproducible) que otro bloque dashboard o API pueda consumir directamente, ni una especificación clara de la estructura de esa salida.

### 1.4 Consecuencias

- Los datos urbanos disponibles no se traducen en un indicador de riesgo utilizable por otras capas del sistema.
- La falta de etiquetas confiables deja sin resolver la pregunta de qué zonas requieren atención prioritaria, más allá de la percepción o el criterio operativo.
- Sin un componente analítico reproducible, cualquier futuro dashboard o simulación carecería del insumo que le da sentido.
- La ausencia de una comparación metodológica entre enfoques (supervisado, no supervisado y basado en grafos) deja sin resolver cuál es la estrategia más adecuada según la disponibilidad real de datos.
- Sin validación estadística ni experta de los datos sintéticos, los resultados del modelo podrían presentarse, por error, como válidos para uso operativo directo.

### 1.5 Formulación del problema

¿Qué modelos de aprendizaje automático permiten identificar patrones o clasificar zonas de riesgo urbano a partir de datos multimodales?

## 2. Alcance

Este proyecto de tesis se refiere al bloque URB-04 del sistema urbano: la capa de IA/Big Data que tiene como función convertir datos previamente existentes en términos geoespaciales, de grafo, contextuales y de eventos en un motor analítico para detectar patrones y clasificar riesgos.

Su objetivo específico abarca la creación de un conjunto de datos analítico a partir de variables geoespaciales, contextuales, gráficas y relacionadas con eventos. Esto puede hacerse utilizando datos reales sobre incidentes (si los hay disponibles, como los del ECU-911 o portales abiertos sobre tránsito) o mediante el uso de variables sintéticas/simuladas cuando el registro histórico no sea suficiente; la definición operacional para cada tipo de variable (geográfica, contextual, gráfica y relacionada con eventos) según la matriz de operacionalización del apartado 8.6, el indicador, tipo de dato y ejemplo específico; la elección de variables y elaboración de un modelo baseline documentado de manera reproducible (notebook); el diseño experimental comparativo que consta de tres frentes:

- Modelos supervisados tradicionales (XGBoost, Random Forest) en caso de que haya etiquetas de riesgo disponibles,
- Enfoque basado en grafos (Graph Convolutional Network o GraphSAGE), que utiliza explícitamente la topología del grafo urbano proporcionado como insumo,
- Opción no supervisada (k-means, Node2Vec + K-Means o Spectral Clustering) si no hay etiquetas presentes; el análisis cruzado de los modelos entrenados y su evaluación usando métricas como PR-AUC, F1-Score macro y Accuracy o silhouette, índice de Calinski-Harabasz y Davies-Bouldin (en el caso no supervisado), así como la estabilidad y la interpretabilidad.

La interpretación de las variables a través de SHAP y, si el número de estas lo requiere, reducción previa de dimensionalidad; la validación de que los datos sintéticos son representativos mediante la prueba estadística Kolmogorov-Smirnov y, en la medida de lo posible, revisión por un experto del área (urbanista o personal policial); determinar cómo debe ser estructurada la salida del componente exportable mediante un esquema JSON con los campos `risk_score`, `cluster_id`, `top_shap_features` y `confidence_interval` para que una futura API o tablero pueda utilizarla sin ambigüedades y el envío de un elemento integrable (modelo serializado + cuaderno + informe de resultados) capaz de enlazarse con una API o tablero en el futuro.

La validación experta se realizará a través entrevistas semiestructuradas y talleres de revisión con urbanistas y Policía de Tránsito. Estos actores evaluarán la coherencia de los patrones detectados por el modelo frente a su experiencia operativa, de esta manera se verifica si las variables más influyentes, por ejemplo, iluminación, conectividad vial, densidad de incidentes corresponden con situaciones reales en la ciudad. Los comentarios de los expertos se documentarán e integrarán como parte del protocolo de validación, complementando las métricas estadísticas (Kolmogorov-Smirnov, índice de Moran) para facilitar que los resultados sean interpretables y aplicables en la gestión urbana local.

**El proyecto NO incluye:**

- La construcción de la capa de datos, del grafo urbano o de los indicadores de origen, ya que estos se asumen como insumos entregados por otro bloque del sistema.
- Aunque el proyecto no desarrolla el dashboard ni la API o el módulo de simulación que consumirían el motor analítico producido en el presente trabajo; se limita a definir y documentar la estructura de salida que dichos consumidores requerirían.
- La recolección de video, sensores IoT en tiempo real o infraestructura de videovigilancia; el proyecto trabaja sobre datos ya estructurados o simulados.
- El despliegue en producción del modelo; el entregable llega hasta el componente exportado, documentado y validado.

## 3. Justificación de la investigación

### 3.1 Justificación teórica

El uso del aprendizaje automático para predecir el riesgo urbano y vial es un campo vivo, con estudios recientes que registran de manera sistemática qué algoritmos, variables y tácticas de validación son más eficaces en función de la clase de datos disponible (Chai et al., 2024; Behboudi et al., 2024). Las arquitecturas fundamentadas en grafos han evidenciado que logran capturar con mayor precisión la dependencia espacial entre áreas vecinas que los modelos que no consideran la topología urbana (Feng et al., 2024; Gao et al., 2024; Hu et al., 2024), lo cual es de relevancia directa para un proyecto que recibe datos de grafo como insumo; por este motivo, el presente anteproyecto ya no restringe el comparativo a modelos arbóreos, sino que establece oficialmente la incorporación de una arquitectura de grafos en el diseño experimental.

Este estudio proporciona pruebas empíricas acerca de qué método supervisado, basado en grafos o no supervisado, es más adecuado cuando la disponibilidad de etiquetas de riesgo es escasa; una circunstancia común en proyectos urbanos locales y que ha sido confirmada como factible por recientes investigaciones ecuatorianas (Arciniegas-Ayala et al., 2024).

### 3.2 Justificación práctica

Para que la información del proyecto FCI 2026-046 RISKTWIN gemelo digital multimodal para la Gestión Inteligente del Riesgo, que ya cuenta con datos, grafos e indicadores, sea provechosa, se requiere una capa que la transforme en una categorización de riesgo comprensible. Este proyecto ofrece precisamente eso: un componente exportable, el cual incluye un modelo, una libreta y un informe que otro bloque del sistema (una API o un panel de control) puede utilizar sin tener que resolver por su cuenta la cuestión del modelado. Además, cuenta con una estructura de salida previamente establecida que disminuye la ambigüedad en la integración.

El proyecto, al contrastar de manera explícita enfoques supervisados, no supervisados y basados en grafos, también proporciona una guía práctica sobre qué hacer cuando los datos etiquetados son escasos; una decisión que de otra manera tendría que tomarse ad hoc en cada nuevo entorno urbano.

### 3.3 Justificación metodológica

El proyecto utiliza CRISP-ML(Q) (Studer et al., 2021) como marco de ciclo de vida debido a que, a diferencia de los métodos genéricos para desarrollar software, proporciona etapas concretas para las dificultades propias del aprendizaje automático: entendimiento de datos, ingeniería de datos, ingeniería de modelo, evaluación y puesta en marcha; cada una cuenta con controles de calidad. Esto es importante en este contexto porque el principal riesgo del proyecto no es la administración de los tiempos, sino la calidad de los datos y la validez del modelo que se genera.

Se complementa con la investigación en ciencia del diseño (Hevner et al., 2004), que considera el motor analítico como un artefacto diseñado y evaluado de manera sistemática para abordar un problema concreto: la ausencia de una capa de IA que clasifique el riesgo urbano, en vez de considerarlo como una práctica exploratoria sin criterios de aceptación. El ciclo que consiste en problema → diseño del artefacto → demostración → evaluación → comunicación de resultados se ajusta naturalmente con los subproductos verificables establecidos para esta sección: conjunto de datos, canalizaciones, modelos, métricas y cuaderno reproducible. En la sección 9.3 se explica detalladamente la relación directa entre las etapas de ambas metodologías, y en la Figura 1 se sintetiza de forma gráfica.

La comparación directa entre modelos (XGBoost/Random Forest, una estrategia de agrupamiento y una de grafos) se hace en respuesta al principal riesgo detectado para el proyecto: la posible ausencia de etiquetas reales. De este modo, no nos comprometemos con un solo enfoque desde el principio que podría no ser factible según los datos que realmente estén disponibles.

La etapa de evaluación no está limitado a las métricas cuantitativas (Accuracy, F1, silhoutte e índice de Moran), sino que incorpora validación cualitativa mediante sesiones de retroalimentación con expertos urbanos. Urbanistas y personal de tránsito revisarán los resultados del motor analítico y confirmarán si los patrones identificados reflejan las condiciones reales de riesgo. Una doble validación por estadística y experta que asegura que el modelo diseñado cumpla con los criterios de calidad técnica y relevancia práctica, consolidando su aplicabilidad en la gestión de riesgos urbanos.

## 4. Objetivo general

Desarrollar una aplicación de Inteligencia artificial para identificar patrones o niveles de riesgo urbano a partir de variables multimodales.

## 5. Objetivos específicos

1. Seleccionar y combinar variables geoespaciales, de grafo, contextuales y de eventos, verificando la representatividad de los datos sintéticos mediante juicio de expertos y la prueba de Kolmogorov-Smirnov.
2. Diseñar un modelo base inicial que esté completamente documentado en un cuaderno para garantizar que el proceso de preparación y modelado sea reproducible.
3. Evaluar experimentos de comparación utilizando métodos supervisados (XGBoost, Random Forest), no supervisados (K-Means, Spectral Clustering, Node2Vec) o basados en grafos (GraphSAGE, GCN), dependiendo de la existencia de etiquetas de riesgo.

## 6. Hipótesis de investigación

Considerando la dificultad de validar una única hipótesis que combina dos situaciones metodológicas debido a la mezcla de métricas de naturaleza diferente (Accuracy/F1 en comparación con silhouette), se proponen a continuación dos hipótesis independientes y cuantificables, cada una vinculada a su propio grupo de métricas.

**Hipótesis 1 (enfoque supervisado)**

**H1:** Cuando haya etiquetas disponibles, los modelos de aprendizaje automático supervisados (Random Forest y XGBoost) y el método basado en grafos (GCN/GraphSAGE) lograrán categorizar niveles de riesgo urbano usando variables geoespaciales, de grafo, contextuales y de eventos. Su rendimiento será mejor que el de un modelo base ingenuo, con valores de Accuracy y F1-Score macro superiores a 0.65 en el conjunto de prueba.

**Hipótesis 2 (enfoque no supervisado)**

**H2:** Un método de agrupamiento (Node2Vec + K-Means, k-means o Spectral Clustering) permitirá identificar grupos de riesgo con un puntaje de silhouette mayor a 0.5 y una coherencia espacial validada por el índice de Moran en la ausencia de etiquetas confiables.

Ambas hipótesis comparten el criterio de reproducibilidad e interpretabilidad como condición de aceptación de los resultados, independientemente del escenario de datos que finalmente se presente.

## 7. Marco teórico y referencial

### 7.1 Riesgo urbano y prevención situacional

La prevención del delito mediante diseño ambiental (CPTED) sostiene que el diseño físico de un espacio iluminación, visibilidad, control de accesos influye directamente en la probabilidad de que ocurra un delito (Newman, 1972; Jacobs, 1961). La teoría de las actividades rutinarias (Cohen & Felson, 1979) complementa esta idea al proponer que un evento de riesgo requiere la convergencia en tiempo y espacio de ciertas condiciones favorables y la ausencia de un factor de control. Estos marcos, originalmente formulados para el delito, son igualmente aplicables al riesgo vial: en ambos casos, el riesgo no es uniforme en el espacio urbano, sino que depende de características del entorno que pueden capturarse como variables contextuales dentro de un modelo.

### 7.2 Datos multimodales urbanos

Un sistema urbano genera datos de naturalezas distintas que, combinados, describen mejor el riesgo de una zona que cualquiera de ellos por separado: variables geoespaciales (coordenadas, distancia a puntos de interés), variables de grafo (conectividad y centralidad de un sector dentro de la red urbana), variables contextuales (uso de suelo, densidad, iluminación) y variables de eventos (historial de incidentes). Sohail et al. (2024), en su gemelo digital urbano de Sídney, mostraron que integrar fuentes heterogéneas de este tipo revela correlaciones espaciales que no son visibles al analizar cada fuente de forma aislada. Este proyecto no construye esas fuentes las recibe como insumo de otro bloque del sistema, pero sí depende de que su combinación sea correcta para que el modelado tenga sentido. La definición operacional de cada tipo de variable, con su indicador y ejemplo concreto, se detalla en la matriz de la sección 8.6.

### 7.3 Predicción de riesgo urbano y vial mediante aprendizaje automático

La revisión de Chai et al. (2024) sobre predicción de accidentalidad vial mediante enfoques no visuales documenta que la fuente de datos más común son los portales de datos abiertos gubernamentales, y que el desempeño de los modelos varía según se busque predecir ocurrencia, frecuencia, severidad o nivel de riesgo. En la misma línea, la revisión de Behboudi et al. (2024), que examina 191 estudios de los últimos cinco años, concluye que la integración de fuentes diversas de datos mejora consistentemente la precisión frente a modelos de fuente única. En el contexto ecuatoriano, Arciniegas-Ayala et al. (2024) entrenaron redes neuronales de función de base radial (RBFNN) sobre un dataset con información de eventos de conducción, y encontraron que arquitecturas relativamente simples pueden igualar a modelos de aprendizaje profundo más costosos cuando los datos disponibles son limitados, una condición realista para este proyecto.

### 7.4 Redes neuronales de grafos para riesgo espacio-temporal

Cuando el riesgo urbano se distribuye sobre una red de sectores conectados entre sí, tratar cada zona como independiente ignora información valiosa. Gao et al. (2024) proponen una red neuronal de grafos probabilística que modela explícitamente la incertidumbre y la naturaleza dispersa ("zero-inflated") de los eventos de riesgo a nivel de tramo vial, mientras que Hu et al. (2024) combinan inferencia causal de Granger con redes convolucionales de grafos para identificar relaciones causales entre zonas a partir de datos de colisión escasos. Feng et al. (2024) extienden esta línea con un enfoque de aprendizaje espaciotemporal multivista que además modela el "precursor" del evento de riesgo, no solo su ocurrencia. Estos tres trabajos son directamente relevantes porque este proyecto recibe un grafo urbano como insumo; por ello, y a diferencia de la versión previa de este anteproyecto que citaba estos antecedentes en el marco teórico sin incorporarlos formalmente al diseño experimental, la sección 2 y la sección 8.5 ya incluyen una arquitectura de tipo Graph Convolutional Network o GraphSAGE como parte explícita del comparativo de modelos, así como variantes de clustering que aprovechan la estructura del grafo (Spectral Clustering, Node2Vec + K-Means).

### 7.5 Modelos de árboles interpretables: Random Forest y XGBoost

Random Forest y XGBoost combinan múltiples árboles de decisión para mejorar la capacidad predictiva sin sacrificar por completo la interpretabilidad, una ventaja frente a los modelos de caja negra cuando el objetivo incluye explicar qué variables determina el riesgo de una zona. Zhang et al. (2020) compararon distintos algoritmos de clasificación para la predicción de concentraciones delictivas y encontraron que los modelos de árboles superaban de forma consistente a los modelos lineales, mientras que la revisión de Butt et al. (2020) confirma este patrón en un espectro más amplio de estudios de predicción espaciotemporal de riesgo. Dado que el criterio de aceptación de este proyecto exige resultados reproducibles y una métrica reportada, estos modelos se mantienen como punto de partida (baseline) frente al cual se compara el enfoque basado en grafos.

### 7.6 Clustering y detección de patrones no supervisada

Cuando no existen etiquetas confiables de riesgo, los algoritmos de agrupamiento (k-means, DBSCAN, clustering jerárquico, Spectral Clustering) permiten identificar zonas con perfiles similares de variables geoespaciales, de grafo y contextuales sin necesidad de una variable objetivo-previa. El resultado no es una predicción de riesgo en sentido estricto, sino una segmentación de sectores que puede interpretarse como niveles relativos de riesgo si se combina con el conocimiento de un experto del dominio (validación experta), que es precisamente la estrategia de mitigación prevista para el riesgo de falta de etiquetas identificado en este proyecto. Cuando el clustering incorpora la estructura del grafo urbano mediante Spectral Clustering o embeddings de Node2Vec seguidos de K-Means, la segmentación resultante refleja además la conectividad entre sectores, no solo su similitud en variables tabulares.

### 7.7 Interpretabilidad de modelos: SHAP

SHAP (SHapley Additive exPlanations) asigna a cada variable una contribución cuantificada a la predicción de un modelo, basada en la teoría de juegos cooperativos (Lundberg & Lee, 2017). Aplicado a un modelo de clasificación de riesgo urbano, SHAP permite responder no solo qué zona tiene mayor riesgo, sino qué factores, por ejemplo, baja iluminación, alta conectividad vial o proximidad a puntos de interés, centralidad en el grafo, densidad de eventos históricos influyen más en esa clasificación. Esta información es directamente útil para cualquier bloque posterior del sistema (dashboard o API) que necesite justificar sus recomendaciones frente a usuarios técnicos o autoridades locales. Además, los valores SHAP pueden ser revisados por expertos urbanos para validar la coherencia práctica de las variables influyentes. Por esta razón, los valores SHAP de las variables más relevantes forman parte de la estructura de salida definida en la sección 8.7 (campo `top_shap_features`), garantizando que el motor analítico no solo produzca predicciones, también explicaciones interpretables y defendibles.

### 7.8 Autocorrelación espacial

El índice de Moran y los estadísticos de autocorrelación espacial (Getis, 2009) permiten determinar si los valores de una variable. Por ejemplo, el nivel de riesgo estimado por el modelo está distribuidos de forma aleatoria en el espacio o si forman clústeres de sectores con valores similares. Esta técnica se usará como validación adicional de que los patrones detectados por los modelos de esta tesis tienen coherencia espacial y no son ruido estadístico disperso entre sectores no contiguos.

### 7.9 Validación estadística de datos Sintéticos en prueba de Kolmogorov-Smirnov como plan B en caso de que no haya suficientes datos

Cuando el proyecto recurre a variables sintéticas o simuladas por insuficiencia de historial real, es necesario verificar que su distribución sea plausible. La prueba de Kolmogorov-Smirnov (K-S) es una prueba de bondad de ajuste no paramétrica que compara la función de distribución acumulativa empírica de una muestra con una distribución teórica de referencia, o compara dos muestras entre sí para determinar si provienen de la misma distribución.

En este proyecto, la prueba K-S se aplicará para comparar la distribución de las variables sintéticas frente a la de los datos reales disponibles (aunque sean parciales), como criterio objetivo que complementa la validación experta y reduce el riesgo de que el artefacto pierda validez externa por depender únicamente de datos simulados.

### 7.10 Métricas de evaluación bajo desbalanceo de clases y calidad de Clustering

La métrica de precisión puede ser engañosa si las clases de riesgo están desbalanceadas, lo cual suele suceder porque las áreas de alto riesgo tienden a ser minoritarias en comparación con las zonas de bajo riesgo. Por lo tanto, este proyecto también reporta el F1-Score macro, que promedia el rendimiento por clase sin ponderar por su frecuencia, y el área bajo la curva de precisión-recall (PR-AUC), que ofrece más información en situaciones desequilibradas que la curva ROC. Para los modelos de agrupamiento, además del coeficiente de silhouette, se reportan también el índice de Calinski-Harabasz (que mide la razón entre la dispersión intra-clúster e interclúster) y el índice de Davies-Bouldin (que penaliza clústeres que no son compactos o están poco separados) para que la calidad del agrupamiento no se base en una única métrica.

### 7.11 CRISP-ML(Q)

CRISP-ML(Q) (Studer et al., 2021) ajusta el proceso CRISP-DM, ya familiarizado, a las especificidades del aprendizaje automático. Seis etapas se definen: entendimiento del negocio y de los datos, ingeniería de datos, ingeniería de modelo, evaluación, implementación y seguimiento. En cada una de ellas se llevan a cabo actividades para asegurar la calidad. CRISP-ML(Q), a diferencia de los métodos genéricos de desarrollo de software, admite explícitamente que la calidad de un proyecto de inteligencia artificial depende tanto del modelo como del dato, lo que se ajusta a la naturaleza de este bloque. Su insumo principal (datos, grafos, indicadores) no está bajo su control directo.

Esta metodología sigue un paso a paso el cual ayuda a mejorar la calidad de los datos. A continuación, se mostrará en una matriz el resumen de lo que compone esta metodología:

| Etapa | Significado | Forma de trabajo | Control de calidad |
|---|---|---|---|
| **1. Entendimiento del negocio y de los datos** | Traduce el problema de negocio a un problema de ML y valida si los datos lo sostienen. | Definición de KPIs, restricciones legales/éticas, EDA inicial y baseline. | Verificación de objetivos medibles; revisión de riesgos legales/éticos; documentación de supuestos. |
| **2. Ingeniería de datos** | Convierte datos crudos en un dataset limpio y consistente para modelar. | Limpieza, integración de fuentes, feature engineering, split train/val/test, balanceo de clases, normalización. | Validación estadística de distribuciones; chequeo de data leakage; trazabilidad del linaje de datos; pruebas de esquema/rango con herramientas tipo Great Expectations o TFDV. |
| **3. Ingeniería de modelo** | Selección, entrenamiento y ajuste de algoritmos. | Elección de algoritmos candidatos, entrenamiento de baseline y modelos complejos. | Control de overfitting vía validación cruzada; comparación contra baseline; reproducibilidad (semillas fijas, entorno versionado); experiment tracking (MLflow o similar). |
| **4. Evaluación** | Confirma que el modelo cumple los requisitos técnicos y de negocio antes de producción. | Cálculo de métricas técnicas (F1, AUC, RMSE, etc.), pruebas de robustez, análisis de sesgo/equidad. | Cumplimiento de umbrales mínimos definidos en fase 1; auditoría de sesgos y edge cases; revisión conjunta técnico-negocio. |
| **5. Implementación** | Despliegue del modelo en producción, integrado a los sistemas del negocio. | Selección de estrategia (batch, tiempo real, edge), empaquetado, integración con sistemas existentes. | Pruebas de integración end-to-end en staging; pruebas de carga/latencia; detección de training-serving skew; plan de rollback; aprobación formal de despliegue. |
| **6. Monitoreo y mantenimiento** | Vigilancia continua del modelo en producción, dado que los datos cambian con el tiempo. | Monitoreo de métricas en vivo, detección de data drift y concept drift, recolección de feedback, reentrenamiento periódico. | Umbrales de alerta automática; auditorías periódicas de sesgo en producción; versionado de cada nueva versión desplegada; retroalimentación formal hacia fases anteriores (ciclo, no proceso lineal). |

### 7.12 Design Science Research (DSR)

El paradigma de investigación en sistemas de información conocido como Design Science Research (Hevner et al., 2004) tiene como objetivo la creación y evaluación rigurosa de artefactos que solucionen problemas auténticos dentro de las organizaciones. En este proyecto, el "artefacto" es un motor analítico para detectar patrones de riesgo. El ciclo DSR (identificación del problema, diseño de la solución, demostración, evaluación y comunicación) organiza el trabajo de tal forma que cada entregable (dataset, pipeline, modelos, métricas y notebook) se relacione con una fase comprobable del ciclo en lugar de estar vinculado a una lista de tareas desconectadas. La figura 1 (sección 9.3) muestra la relación entre las fases de CRISP-ML(Q) y las etapas de DSR.

A continuación, se mostrará una matriz especificando cada paso de esta metodología:

| Etapa | Significado | Forma de trabajo | Control de calidad |
|---|---|---|---|
| **1. Identificación del problema** | Define y justifica el problema real a resolver con el artefacto. | Revisión del estado del arte, levantamiento con stakeholders, formulación de la pregunta de diseño, criterios de éxito. | Contraste con literatura previa; validación con negocio; trazabilidad de la motivación; criterios medibles antes de avanzar. |
| **2. Diseño de la solución** | Traduce el problema en arquitectura y objetivos concretos del artefacto. | Requisitos funcionales/no funcionales, arquitectura del motor analítico, selección de técnicas, diseño preliminar del pipeline. | Trazabilidad problema-diseño; validación técnica de factibilidad; revisión por pares; documentación versionada. |
| **3. Demostración** | Construye y ejecuta una versión funcional del artefacto. | Implementación del pipeline, entrenamiento de modelos, ejecución sobre caso real, generación de entregables tangibles. | Verificación de ejecución completa; prueba de reproducibilidad; checklist contra requisitos de diseño; registro de limitaciones. |
| **4. Evaluación** | Determina con evidencia si el artefacto resuelve el problema. | Métricas técnicas del modelo, evaluación funcional con usuarios, comparación contra el estado previo, análisis de limitaciones. | Métricas predefinidas sin ajuste posterior; validación técnica + funcional; documentación de fallos; quality gate de avance o iteración. |
| **5. Comunicación** | Difunde el artefacto y el conocimiento generado. | Documentación técnica, informes para negocio, registro de lecciones aprendidas, entrega de artefactos reproducibles. | Revisión de reproducibilidad por terceros; consistencia entre lo comunicado y lo real; control de versiones final; retroalimentación al ciclo. |

## 8. Marco metodológico

### 8.1 Tipo de investigación

La investigación es de carácter aplicado, con una configuración experimental comparativa. Esto es, se entrenan y analizan varios modelos de aprendizaje automático (supervisados, no supervisados y basados en grafos) utilizando el mismo grupo de datos, y se evalúa su rendimiento bajo condiciones controladas a través de medidas cuantitativas.

### 8.2 Enfoque y modalidad

El enfoque es cuantitativo, ya que la ejecución de cada modelo se mide utilizando métricas numéricas (Davies-Bouldin, silhouette, Calinski-Harabasz, PR-AUC, F1-Score macro y precisión) y la interpretabilidad se determina a través de los valores SHAP de las variables. La modalidad es experimental, dado que el proyecto contrasta, de manera controlada, un mínimo de tres estrategias de modelado (supervisada, basada en grafos y no supervisada) con el fin de establecer cuál es la más adecuada en función de la disponibilidad efectiva de etiquetas.

### 8.3 Fuentes, técnicas e instrumentos para la recolección de datos

| Tipo de fuente | Fuente | Técnica | Instrumento |
|---|---|---|---|
| Secundaria | Datos de incidentes urbanos/viales, si están disponibles (portales de datos abiertos, ECU-911, estadísticas oficiales) | Recolección y limpieza de series históricas | Repositorios de datos abiertos |
| Primaria | Variables sintéticas o simuladas, en caso de no existir histórico suficiente | Generación de datos sintéticos con distribución realista | Scripts Python / NumPy / SciPy |
| Primaria | Validación de la representatividad de los datos sintéticos | Prueba de bondad de ajuste Kolmogorov-Smirnov; revisión por experto del dominio (urbanista o Policía de Tránsito) | SciPy (kstest) / protocolo de entrevista |
| Primaria | Grafo urbano e indicadores producidos por otros bloques del sistema | Consumo de insumos estructurados (nodos, aristas, indicadores) | Archivos estructurados (CSV/JSON/GraphML) |
| Primaria | Construcción del dataset analítico y selección de variables | Feature engineering y análisis exploratorio | Pandas / GeoPandas / scikit-learn |
| Primaria | Entrenamiento y comparación de modelos (baseline, grafo y clustering) | Validación cruzada, ajuste de hiperparámetros | scikit-learn / XGBoost / PyTorch Geometric o DGL |
| Primaria | Interpretación de variables | Cálculo de valores SHAP | SHAP (Python) |
| Secundaria | Artículos científicos (IEEE, ACM, arXiv, ScienceDirect, MDPI) | Revisión bibliográfica | Matrices de análisis documental |

### 8.4 Población y muestra

La población está constituida por las zonas o sectores urbanos que forman parte del grafo entregado como insumo al proyecto. La muestra corresponde al subconjunto de zonas con datos suficientes en las cuatro categorías de variables (geoespaciales, de grafo, contextuales y de eventos) para un periodo determinado. Si los datos reales de incidentes resultan insuficientes para entrenar un modelo supervisado robusto, se generará un conjunto de variables sintéticas con una distribución de riesgo controlada, cuya representatividad se validará mediante la prueba de Kolmogorov-Smirnov frente a los datos reales disponibles y, cuando sea posible, mediante revisión de un experto del dominio. El carácter simulado de estas variables se documentará explícitamente en el reporte final, de modo que los resultados no se presenten como válidos para uso operativo directo sin una validación posterior con datos reales.

### 8.5 Análisis y tratamiento de la información

- Limpieza y normalización de las variables geoespaciales, de grafo, contextuales y de eventos recibidas como insumo.
- Selección de variables mediante análisis de correlación e importancia, descartando las redundantes o de baja varianza.
- División del dataset en entrenamiento, validación y prueba, con validación cruzada para reducir la varianza de la estimación de desempeño.
- Entrenamiento y comparación de modelos supervisados (Random Forest, XGBoost) y de un modelo basado en grafos (GCN o GraphSAGE) frente a un modelo base ingenuo, cuando existan etiquetas, con el fin de establecer si la ganancia de desempeño justifica la mayor complejidad del enfoque de grafos.
- Entrenamiento y evaluación de clustering (k-means, Spectral Clustering o Node2Vec + K-Means) mediante silhouette, Calinski-Harabasz y Davies-Bouldin, cuando no existan etiquetas.
- Validación estadística de las variables sintéticas mediante la prueba de Kolmogorov-Smirnov y, cuando sea posible, validación experta con urbanistas o personal de la Policía de Tránsito.
- Interpretación de los modelos finales mediante SHAP y, de ser necesario, reducción de dimensionalidad (PCA u otra técnica) para facilitar la visualización de los resultados.
- Validación de la coherencia espacial de los patrones detectados mediante autocorrelación espacial (índice de Moran).
- Especificación y documentación de la estructura de salida del modelo (esquema JSON) para su consumo por una futura API o dashboard.

### 8.6 Matriz de operacionalización de variables

| Variable | Dimensión | Indicador | Tipo de dato | Ejemplo | Técnica / Instrumento |
|---|---|---|---|---|---|
| **V. independiente:** Estrategia de modelado | Enfoque (supervisado / basado en grafo / no supervisado) | Disponibilidad de etiquetas de riesgo | Categórica (nominal) | "supervisado", "grafo", "no_supervisado" | Experimento controlado; scripts de entrenamiento (Python) |
| **V. independiente:** Arquitectura del modelo | Tipo de algoritmo (RF / XGBoost / GCN-GraphSAGE / clustering) | Configuración de hiperparámetros | Categórica / numérica (hiperparámetros) | n_estimators=200; learning_rate=0.05; num_layers=2 (GCN) | Experimento controlado; scikit-learn / XGBoost / PyTorch Geometric |
| **V. independiente:** Variable geoespacial | Ubicación y proximidad | Coordenadas y distancia a puntos de interés | Numérica continua | Distancia a la vía principal = 350 m | GeoPandas / shapely |
| **V. independiente:** Variable de grafo | Conectividad y centralidad | Grado del nodo, centralidad de intermediación | Numérica continua | Centralidad de intermediación del sector = 0,42 | networkx / archivo GraphML |
| **V. independiente:** Variable contextual | Uso de suelo y entorno construido | Densidad poblacional, tipo de uso de suelo, iluminación | Numérica / categórica | Densidad = 120 hab/ha; uso de suelo = "comercial" | Indicadores recibidos de otro bloque del sistema |
| **V. independiente:** Variable de evento | Historial de incidentes | Frecuencia y severidad de eventos previos por zona | Numérica (conteo) / categórica (severidad) | 3 incidentes en los últimos 6 meses; severidad = "media" | ECU-911 / datos abiertos de tránsito |
| **V. dependiente:** Desempeño de clasificación | Precisión del modelo supervisado y del modelo de grafo | Accuracy, F1-Score macro y PR-AUC en conjunto de prueba | Numérica continua (0–1) | F1-Score macro = 0,71 | Evaluación cuantitativa; protocolo de pruebas |
| **V. dependiente:** Calidad del agrupamiento | Cohesión y separación de clústeres | Silhouette, Calinski-Harabasz, Davies-Bouldin | Numérica continua | Silhouette = 0,56 | Evaluación cuantitativa; scikit-learn |
| **V. dependiente:** Interpretabilidad | Contribución de cada variable a la predicción | Valores SHAP por variable | Numérica continua | SHAP de "centralidad de grafo" = 0,18 | Análisis post-hoc SHAP (Python) |
| **V. dependiente:** Representatividad de datos sintéticos | Ajuste frente a datos reales | Estadístico y p-valor de la prueba K-S | Numérica continua | D = 0,08; p = 0,32 (no se rechaza H0 de igual distribución) | SciPy (kstest) |
| **V. moderadora:** Calidad y disponibilidad de datos | Cobertura y completitud de los insumos recibidos | Porcentaje de datos faltantes por zona | Numérica continua (%) | 12 % de datos faltantes en variables de grafo | Análisis descriptivo — Pandas / NumPy |

### 8.7 Especificación de la estructura de salida para la integración con la API

Se define el esquema JSON que el componente exportado deberá producir por cada zona evaluada, de modo que un futuro bloque de dashboard o API pueda consumirlo sin ambigüedad:

| Campo | Tipo | Descripción |
|---|---|---|
| `risk_score` | float (0–1) | Puntuación de riesgo estimada para la zona, proveniente del modelo supervisado o de grafo. |
| `cluster_id` | integer \| null | Identificador del clúster asignado por el modelo no supervisado, cuando no existan etiquetas; null si se usó el enfoque supervisado. |
| `top_shap_features` | array de objetos {feature, value} | Lista de las variables con mayor contribución SHAP a la predicción de esa zona, en orden descendente. |
| `confidence_interval` | objeto {lower, upper} | Intervalo de confianza asociado a risk_score, calculado a partir de la validación cruzada o de la incertidumbre del modelo. |

## 9. Metodología de desarrollo

### 9.1 Justificación de la metodología

Se opta por utilizar CRISP-ML(Q) junto con Design Science Research, ya que el proyecto no es un desarrollo de software tradicional en sí mismo, sino un ciclo de vida modelado. La calidad de este depende de decisiones relacionadas con datos, variables, arquitecturas y validación, las cuales una metodología genérica de desarrollo de software no abarca con el nivel de detalle necesario. CRISP-ML(Q) proporciona la estructura de fases y el control de calidad; por su parte, DSR ofrece el marco para evaluar el motor analítico como un artefacto que debe demostrar que resuelve el problema propuesto, no únicamente que fue creado.

### 9.2 Fases CRISP-ML(Q) aplicadas al proyecto

| Fase CRISP-ML(Q) | Actividad en el proyecto | Responsable principal |
|---|---|---|
| Comprensión del negocio y los datos | Definir el problema de clasificación/detección de riesgo y explorar los insumos (grafo, indicadores) recibidos | Estudiante A |
| Ingeniería de datos | Construir el dataset analítico, seleccionar variables, operacionalizarlas y preparar el baseline reproducible | Estudiante A |
| Ingeniería de modelo | Entrenar y comparar modelos supervisados, el modelo basado en grafos y los modelos no supervisados | Estudiante B |
| Evaluación | Medir Accuracy/F1-Score macro/PR-AUC o silhouette/Calinski-Harabasz/Davies-Bouldin; validar estabilidad; interpretar con SHAP; validar datos sintéticos con K-S | Estudiante B |
| Despliegue | Exportar el modelo, el notebook y la especificación JSON como componente integrable | Estudiante B |

### 9.3 Ciclo Design Science Research aplicado

| Etapa DSR | Correspondencia en el proyecto |
|---|---|
| Identificación del problema | Ausencia de una capa de IA que clasifique riesgo urbano a partir de datos multimodales (Sección 1) |
| Diseño del artefacto | Pipeline de datos + modelos comparados (supervisado, basado en grafo y no supervisado) + módulo de interpretación |
| Demostración | Ejecución del pipeline sobre el dataset piloto (real o sintético, validado con K-S) en un notebook reproducible |
| Evaluación | Métricas de desempeño (Accuracy/F1-Score macro/PR-AUC/silhouette/Calinski-Harabasz/Davies-Bouldin), estabilidad, coherencia espacial (Moran) e interpretabilidad (SHAP) |
| Comunicación | Reporte de resultados, comparación de modelos y especificación JSON del componente exportado para integración |

*Figura 1. Mapa metodológico de integración CRISP-ML(Q) + DSR.* (La figura es una imagen en el PDF original y no se reproduce aquí; su contenido equivale a la tabla de correspondencia siguiente.)

La siguiente tabla formaliza, la relación entre ambas metodologías como necesaria en la revisión del anteproyecto: cada fase técnica de CRISP-ML(Q) se enlaza con su etapa equivalente en el ciclo de DSR, mostrando que el proyecto no solo sigue un ciclo técnico, sino que también valida el motor analítico como un artefacto evaluable.

| CRISP-ML(Q) | Integración | DSR (Design Science Research) |
|---|:-:|---|
| Comprensión de los datos | → | Identificación del problema |
| Ingeniería de datos / Ingeniería de modelo | → | Diseño del artefacto |
| Ingeniería de modelo (entrenamiento) | → | Demostración del artefacto |
| Evaluación del modelo | → | Evaluación de la solución |
| Despliegue y mejora | → | Comunicación de resultados |

En el ciclo completo, la evaluación y retroalimentación de DSR alimentan nuevamente la etapa de comprensión de datos de CRISP-ML(Q), concluyendo así el proceso iterativo entre las dos metodologías. Esta integración garantiza un artefacto validado, un enfoque técnico (CRISP-ML(Q)) y un problema que puede ser evaluado de manera sistemática (DSR).

### 9.4 Responsabilidades por estudiante

| Estudiante | Responsabilidad | Entregables asociados |
|---|---|---|
| **Estudiante A — Datos y features** | Construir el dataset analítico, seleccionar y operacionalizar variables, preparar el baseline, ejecutar la validación K-S de los datos sintéticos y la documentación reproducible | Dataset de entrenamiento; pipeline ML; matriz de operacionalización; reporte de validación de datos sintéticos; documentación reproducible |
| **Estudiante B — Modelado y evaluación** | Entrenar modelos (baseline, grafo y clustering), comparar resultados, interpretar variables y exportar el componente integrable con su especificación JSON | Modelos entrenados; métricas; explicación de variables; comparación de modelos; especificación de salida; exportación para API |

### 9.5 Requerimientos del sistema

| ID | Requerimiento | Prioridad | Fase CRISP-ML(Q) |
|---|---|---|---|
| REQ-01 | El sistema debe construir un dataset analítico a partir de variables geoespaciales, de grafo, contextuales y de eventos, con su definición operacional. | Alta | Ingeniería de datos |
| REQ-02 | El sistema debe generar variables sintéticas o simuladas cuando el histórico real de incidentes sea insuficiente, documentando este hecho. | Alta | Ingeniería de datos |
| REQ-03 | El sistema debe validar estadísticamente las variables sintéticas mediante la prueba de Kolmogorov-Smirnov frente a datos reales disponibles. | Alta | Ingeniería de datos |
| REQ-04 | El sistema debe entrenar y comparar al menos dos modelos supervisados (Random Forest, XGBoost) cuando existan etiquetas de riesgo. | Alta | Ingeniería de modelo |
| REQ-05 | El sistema debe entrenar y evaluar un modelo basado en grafos (GCN o GraphSAGE) que aproveche el insumo de grafo urbano. | Media | Ingeniería de modelo |
| REQ-06 | El sistema debe entrenar y evaluar un modelo de clustering (incluyendo variantes basadas en grafo) como alternativa cuando no existan etiquetas confiables. | Alta | Ingeniería de modelo |
| REQ-07 | El sistema debe reportar Accuracy, F1-Score macro y PR-AUC (caso supervisado/grafo) o silhouette, Calinski-Harabasz y Davies-Bouldin (caso no supervisado) sobre un conjunto de prueba. | Alta | Evaluación |
| REQ-08 | El sistema debe interpretar las variables más influyentes en el modelo final mediante SHAP. | Media | Evaluación |
| REQ-09 | El sistema debe validar la coherencia espacial de los patrones detectados mediante el índice de Moran. | Media | Evaluación |
| REQ-10 | El sistema debe exportar el modelo entrenado, el notebook y una especificación JSON (risk_score, cluster_id, top_shap_features, confidence_interval) integrable con una futura API. | Alta | Despliegue |

## 10. Cronograma de actividades

| Actividad | M1 | M2 | M3 | M4 | M5 | M6 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Revisión bibliográfica y marco teórico | ✔ | | | | | |
| Comprensión del negocio y de los datos/grafo/indicadores recibidos | ✔ | | | | | |
| Construcción del dataset analítico, operacionalización y selección de variables (REQ-01) | ✔ | ✔ | | | | |
| Generación y validación K-S de variables sintéticas (REQ-02, REQ-03) | | | ✔ | | | |
| Preparación del baseline y documentación reproducible | | | ✔ | | | |
| Entrenamiento y comparación de modelos supervisados (REQ-04) | | | | ✔ | ✔ | |
| Entrenamiento y evaluación del modelo basado en grafos (REQ-05) | | | | | ✔ | ✔ |
| Entrenamiento y evaluación de clustering (REQ-06) | | | | ✔ | | |
| Evaluación de métricas y validación de estabilidad y coherencia espacial (REQ-07, REQ-09) | | | | | ✔ | ✔ |
| Interpretación de variables con SHAP (REQ-08) | | | | | ✔ | |
| Especificación y exportación del componente integrable (REQ-10) | | | | | ✔ | ✔ |
| Redacción y presentación de la tesis | | | | | | ✔ |

*Nota: las posiciones de algunas marcas se leyeron de un PDF con tabla paginada y pueden variar en una columna respecto al original.*

## 11. Presupuesto y financiamiento

| Rubro | Descripción | Costo (USD) |
|---|---|---:|
| Recurso humano | 2 investigadores × 6 meses (valorado) | Aporte propio |
| Cómputo en la nube | Google Colab Pro (entrenamiento y validación de modelos, incluido el modelo de grafos) | $70.00 |
| Software | Herramientas open source (Python, scikit-learn, XGBoost, SHAP, GeoPandas, PyTorch Geometric) | $0.00 |
| Material bibliográfico | Acceso a artículos científicos | $0.00 (acceso institucional) |
| Impresión y empastado | Documento final de tesis | $90.00 |
| Imprevistos (10 %) | | $16.00 |
| **TOTAL** | | **$176.00** |

## 12. Beneficios esperados del proyecto

- Aportar al sistema urbano una capa de IA que hoy no existe: un motor analítico capaz de clasificar el riesgo por zona a partir de los datos, grafos e indicadores ya disponibles.
- Dejar documentada una comparación metodológica entre enfoques supervisados, basados en grafos y no supervisados, útil para decidir qué estrategia aplicar según la disponibilidad real de etiquetas en futuros bloques o proyectos similares.
- Entregar un componente reproducible y exportable (modelo + notebook + reporte + especificación JSON) listo para integrarse a una futura API o dashboard del sistema urbano.
- Generar evidencia empírica sobre la interpretabilidad de los modelos de riesgo urbano mediante SHAP, facilitando la comunicación de resultados a actores no técnicos.
- Establecer un protocolo de validación de datos sintéticos (estadístico y experto) replicable en proyectos donde el historial de incidentes reales sea insuficiente.
- Contribuir, como antecedente metodológico, a proyectos futuros de la línea de investigación institucional en analítica urbana.

## 13. Derechos de propiedad intelectual

El desarrollo de este trabajo de tesis contempla la generación de resultados susceptibles de protección por Propiedad Intelectual (derechos de autor, patentes, programa de computador).

¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [x] Software (pipeline de datos + modelos de clasificación/clustering/grafos)
- [x] Modelo/algoritmo (pesos del modelo entrenado y lógica de selección de variables)
- [x] Manual/documentación técnica (notebook reproducible y especificación de la API)
- [ ] No aplica

Los derechos patrimoniales de los productos generados en el presente trabajo de tesis corresponderán a la institución, de conformidad con la normativa vigente. Los autores conservarán los derechos morales sobre su obra.

## 14. Referencias bibliográficas

Arciniegas-Ayala, C., Marcillo, P., Valdivieso Caraguay, Á. L., & Hernández-Álvarez, M. (2024). Prediction of accident risk levels in traffic accidents using deep learning and radial basis function neural networks applied to a dataset with information on driving events. *Applied Sciences, 14*(14), 6248. <https://doi.org/10.3390/app14146248>

Behboudi, N., Moosavi, S., & Ramnath, R. (2024). Recent advances in traffic accident analysis and prediction: A comprehensive review of machine learning techniques. *arXiv preprint arXiv:2406.13968.* <https://arxiv.org/abs/2406.13968>

Butt, U. M., Letchmunan, S., Hassan, F. H., Ali, M., Baqir, A., & Sherazi, H. H. R. (2020). Spatio-temporal crime hotspot detection and prediction: A systematic literature review. *IEEE Access, 8*, 166553–166574. <https://doi.org/10.1109/ACCESS.2020.3022808>

Chai, A. B. Z., Lau, B. T., Tee, M. K. T., & McCarthy, C. (2024). Enhancing road safety with machine learning: Current advances and future directions in accident prediction using non-visual data. *Engineering Applications of Artificial Intelligence, 137*(Part A), 109086. <https://doi.org/10.1016/j.engappai.2024.109086>

Cohen, L. E., & Felson, M. (1979). Social change and crime rate trends: A routine activity approach. *American Sociological Review, 44*(4), 588–608. <https://doi.org/10.2307/2094589>

Feng, J., Liu, T., & Qiao, Y. (2024). Traffic accident prediction method based on multi-view spatial-temporal learning. *Bulletin of the Polish Academy of Sciences: Technical Sciences, 72*(6), e151955. <https://doi.org/10.24425/bpasts.2024.151955>

Gao, X., Jiang, X., Haworth, J., Zhuang, D., Wang, S., Chen, H., & Law, S. (2024). Uncertainty-aware probabilistic graph neural networks for road-level traffic crash prediction. *Accident Analysis & Prevention, 208*, 107801. <https://doi.org/10.1016/j.aap.2024.107801>

Getis, A. (2009). Spatial autocorrelation. En M. M. Fischer & A. Getis (Eds.), *Handbook of applied spatial analysis* (pp. 255–278). Springer.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105. <https://doi.org/10.2307/25148625>

Hu, J., Bai, J., Yang, J., & Lee, J. J. (2024). Crash risk prediction using sparse collision data: Granger causal inference and graph convolutional network approaches. *Expert Systems with Applications, 259*, 125315. <https://www.sciencedirect.com/science/article/pii/S0957417424021821>

Jacobs, J. (1961). *The death and life of great American cities.* Random House.

Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems (NeurIPS), 30.*

Newman, O. (1972). *Defensible space: Crime prevention through urban design.* Macmillan. <https://archive.org/details/defensiblespace0000osca/page/n9/mode/2up>

Observatorio Ecuatoriano de Crimen Organizado [OECO]. (2025). *Boletines de homicidios.* <https://oeco.padf.org/category/boletines-de-homicidios/>

Primicias. (2026, 20 de febrero). El crimen muta: Homicidios se reducen 7,9 % en Ecuador en el primer bimestre de 2026 · Quito reporta alza del 33 %. <https://www.primicias.ec/seguridad/muertes-violentas-crimen-ecuador-baja-guayaquil-sube-quito-datos-118619/>

Sohail, A., Shen, B., Cheema, M. A., Ali, M. E., Ulhaq, A., Babar, M. A., & Qureshi, A. (2024). Beyond data, towards sustainability: A Sydney case study on urban digital twins. *arXiv preprint arXiv:2406.04902.* <https://arxiv.org/abs/2406.04902>

Studer, S., Bui, T. B., Drescher, C., Hanuschkin, A., Winkler, L., Peters, S., & Müller, K.-R. (2021). Towards CRISP-ML(Q): A machine learning process model with quality assurance methodology. *Machine Learning and Knowledge Extraction, 3*(2), 392–413. <https://doi.org/10.3390/make3020020>

Zhang, X., Liu, L., Xiao, L., & Ji, J. (2020). Comparison of machine learning algorithms for predicting crime hotspots. *IEEE Access, 8*, 181302–181310.

Tirado Mendoza, K. A., & Bajaña Cevallos, R. H. (2026). *Prototipo de detección de patrones de riesgo urbano (URB-04)* [Notebook de Jupyter]. Google Colaboratory. <https://colab.research.google.com/drive/13LNGR9Bks5T2hTgj_UFW7nx1POsAmked>

*(El enlace termina en "…POsAmked" en el original, partido en dos líneas.)*

---

## ANEXOS

### ANEXO I.- Formato de evaluación de la propuesta de trabajo de integración curricular

*(Página manuscrita escaneada; contenido transcrito.)*

**Facultad de Ingeniería Industrial — Carrera de Sistemas de Información**

| Campo | Contenido |
|---|---|
| Nombre de la propuesta de trabajo de integración curricular | Aplicación de Inteligencia Artificial para detección de patrones de riesgo urbano en datos multimodales. |
| Nombre del estudiante(s) | Tirado Mendoza Kelvin Aarón, Bajaña Cevallos Rosa Haydee |
| Facultad | Ingeniería Industrial |
| Carrera | Sistemas de Información |
| Línea de investigación | Ciencias básicas, bioconocimiento y desarrollo industrial |
| Sub-línea de investigación | Inteligencia artificial y Ciencia de Datos |
| Fecha de presentación | Miércoles, 26 de agosto de 2026 |
| Fecha de evaluación | Miércoles, 26 de agosto de 2026 |

| Aspectos para considerar | Cumple (Sí) | Cumple (No) |
|---|:-:|:-:|
| Título de la propuesta de trabajo de integración curricular | ✔ | |
| Línea de investigación / Sublínea de investigación | ✔ | |
| Planteamiento del Problema | ✔ | |
| Justificación e importancia | ✔ | |
| Objetivos de la investigación | ✔ | |
| Metodología a emplearse | ✔ | |
| Cronograma de actividades | ✔ | |
| Presupuesto y financiamiento | ✔ | |

**Observaciones (manuscritas):**

- Modificar los objetivos.
- Datos sintéticos como plan B (en caso de falta de datos).
- Uso de la metodología (CRISP-MLQ), considerar el paso a paso.

- [x] APROBADO
- [ ] APROBADO CON OBSERVACIONES
- [ ] NO APROBADO

*(En la imagen, la marca está en "APROBADO", aunque existen observaciones manuscritas.)*

Ing. Manuel Samaniego Zamora, MBA — DECANO DE LA FACULTAD
CC: Director de Carrera, Gestor de Titulación

### Rúbrica de evaluación

*(Universidad de Guayaquil — Facultad de Ingeniería Industrial — Sistemas de la Información; notas manuscritas transcritas.)*

| Criterios generales de calificación | Nota evaluador | Nota máxima |
|---|:-:|:-:|
| Estructura — Planteamiento y formulación del problema. Innovación (aporte novedoso o mejora significativa) | 1 | 1 |
| Alcance — Justificación | 1 | 1 |
| Objetivos (general y específicos) coherentes | 1 | 1 |
| Marco teórico — Marco metodológico — Referencias bibliográficas | 1 | 1 |
| Metodología de desarrollo | 1 | 1 |
| **(Subtotal estructura)** | **5** | **5** |
| Aspectos de fondo — Cronograma — Presupuesto | 1 | 1 |
| Manejo claro de las ideas. Beneficios esperados del proyecto | 1 | 1 |
| Claridad y coherencia en la redacción | 1 | 1 |
| Referentes teóricos sustentados | 1 | 1 |
| Argumentos para una propuesta | 1 | 1 |
| **(Subtotal aspectos de fondo)** | **5** | **5** |
| **NOTA SOBRE 10** | **10** | **10** |

### Anexo C — Rúbrica de evaluación para proyectos grupales de integración curricular

| # | Aspectos evaluados | No cumple | Cumple parcialmente | Cumple |
|:-:|---|:-:|:-:|:-:|
| 1 | Tema del proyecto: se describe un tema que contenga la problemática de estudio, y que se ajuste a la línea de investigación de la Carrera y a la pirámide de investigación de la Facultad. | | | ✔ |
| 2 | Definición del problema: se identifica un problema complejo o con múltiples abordajes, y se especifican los múltiples enfoques de la investigación planteada. | | | ✔ |
| 3 | División de tareas: se indica el plan de trabajo detallado incluyendo hitos y plazos para cada fase del proyecto. | | | ✔ |
| 4 | Desarrollo de objetivos: se describen los objetivos con enfoques específicos para abordar los diferentes aspectos del problema planteado; estos se ajustan al tema propuesto. | | | ✔ |
| 5 | Descripción de propiedad intelectual: se indica si el proyecto tendrá como resultado un diseño industrial, desarrollo de software, modelos de utilidad, patentes de invención o algún otro producto enmarcado en la normativa ecuatoriana de propiedad intelectual; se deberá especificar y detallar en la propuesta. | | | ✔ |

*Para aprobación del proyecto de tesis, se considerará la siguiente valoración: Los proyectos deberán cumplir con todos los puntos de la rúbrica; en caso de cumplimiento parcial o incumplimiento de uno o más puntos, el estudiante tendrá que realizar las respectivas correcciones para volver a ser evaluado.*

**Firmas** *(manuscritas)*

- Bajaña Cevallos Rosa Haydee — C.I.# 0954397261 *(lectura aproximada)*
- Tirado Mendoza Kelvin Aarón — C.I.# 0955262323 *(lectura aproximada)*
- Docente revisor del anteproyecto — C.I.# 130853930 *(lectura aproximada)*
- Docente revisor del anteproyecto — C.I.# 0918586298
