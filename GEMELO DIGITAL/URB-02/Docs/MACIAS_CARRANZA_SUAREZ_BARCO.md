# UNIVERSIDAD DE GUAYAQUIL
## FACULTAD DE INGENIERÍA INDUSTRIAL
### ANTEPROYECTO DE TESIS

## DATOS GENERALES

| | APELLIDOS | NOMBRES |
|---|---|---|
| **ESTUDIANTE 1:** | Macias Carranza | Krystel Shanely |
| **ESTUDIANTE 2:** | Suarez Barco | Jose Enrique |

**Correo electrónico institucional y personal:**

- krystel.maciasc@ug.edu.ec / kmaciascarranza@gmail.com
- jose.suarezb@ug.edu.ec / jesb9049@gmail.com

**Teléfono:** 0990873587 / 0939098647

## TEMA

**TEMA:** Construcción de grafos urbanos para exposición, conectividad y criticidad en zonas de riesgo.

**LÍNEA DE INVESTIGACIÓN**

- [x] SOSTENIBILIDAD, DERECHOS Y TECNOLOGÍAS EN EL ORDENAMIENTO TERRITORIAL, AMBIENTE DE LA CONSTRUCCIÓN Y ARQUITECTURA.
- [ ] DESARROLLO LOCAL Y EMPRENDIMIENTO SOCIO ECONÓMICO SOSTENIBLE.
- [ ] CIENCIAS BÁSICAS, BIOCONOCIMIENTO Y DESARROLLO INDUSTRIAL.
- [ ] SALUD HUMANA, ANIMAL Y DEL AMBIENTE
- [ ] TECNOLOGÍAS AGRÍCOLAS Y DE LA AGRICULTURA.
- [ ] ENTORNOS VIRTUALES DE APRENDIZAJE Y TECNOLOGÍAS EDUCATIVAS

**COBERTURA**

- [ ] Nacional
- [ ] Provincial
- [x] Local
- [ ] Otros

---

## Tabla de contenido

- DATOS GENERALES
- TEMA
- 1. PLANTEAMIENTO Y FORMULACIÓN DEL PROBLEMA
  - 1.1 Antecedentes
  - 1.2 Planteamiento del problema
  - 1.3 Causas
  - 1.4 Consecuencias
  - 1.5 Formulación del problema
- 2. ALCANCE
- 3. JUSTIFICACIÓN DE LA INVESTIGACIÓN
  - 3.1 Justificación teórica
  - 3.2 Justificación práctica
  - 3.3 Justificación metodológica
- 4. OBJETIVO GENERAL
- 5. OBJETIVOS ESPECÍFICOS
- 6. HIPÓTESIS DE INVESTIGACIÓN
- 7. MARCO TEÓRICO Y REFERENCIAL
  - 7.1 Redes urbanas y teoría de grafos
  - 7.2 Exposición en el contexto de riesgo urbano
  - 7.3 Conectividad y criticidad
  - 7.4 Datos abiertos y OpenStreetMap
  - 7.5 Aplicación de grafos en gestión de riesgos urbanos
  - 7.6 Trabajos similares
- 8. MARCO METODOLÓGICO
  - 8.1 Tipo de investigación
  - 8.2 Enfoque y modalidad de investigación
  - 8.3 Fuentes, técnicas e instrumentos para la recolección de datos
  - 8.4 Población y muestra
  - 8.5 Análisis y tratamiento de la información
  - 8.6 Matriz de operacionalización de variables
- 9. METODOLOGÍA DE DESARROLLO A EMPLEAR
  - 9.1 Justificación de la metodología
  - 9.2 Fases del desarrollo
  - 9.3 Prácticas aplicadas
  - 9.4 Responsabilidades por estudiante
- 10. CRONOGRAMA DE ACTIVIDADES
- 11. PRESUPUESTO Y FINANCIAMIENTO
- 12. BENEFICIOS ESPERADOS DEL PROYECTO
- 13. DERECHOS DE PROPIEDAD INTELECTUAL
- 14. REFERENCIAS BIBLIOGRÁFICAS

---

## 1. PLANTEAMIENTO Y FORMULACIÓN DEL PROBLEMA

### 1.1 Antecedentes

Guayaquil es una de las ciudades con mayor concentración de riesgos urbanos en el país. La combinación de crecimiento desordenado, redes viales irregulares y alta densidad poblacional genera zonas donde la movilidad se vuelve crítica ante cualquier evento de emergencia. Según reportes de seguridad vial y datos de emergencias, gran parte de los problemas se concentra en sectores con conectividad limitada y alta exposición de la población.

En los últimos años, el uso de grafos para analizar redes urbanas ha ganado relevancia. Representar las calles como nodos y aristas permite calcular métricas de centralidad y conectividad que ayudan a identificar qué partes de la red son más importantes o vulnerables (Porta et al., 2006; Boeing, 2017). Este enfoque ya se aplica en estudios de riesgo vial y resiliencia urbana. Trabajos como los de Gao et al. (2024) y Hu et al. (2024) demuestran que las métricas de grafos permiten capturar relaciones espaciales que no son evidentes con métodos tradicionales. Sin embargo, todavía se utiliza poco de forma sistemática en el contexto local de Guayaquil.

Este trabajo se enmarca en el bloque URB-02 del sistema RISKTWIN, cuya función es construir el grafo de la red vial y generar las métricas de exposición, conectividad y criticidad que luego serán utilizadas por otros módulos (índice de criticidad, análisis de IA y simulación).

### 1.2 Planteamiento del problema

Aunque existen datos abiertos de la red vial y conocimiento empírico sobre las zonas más conflictivas de Guayaquil, no se cuenta con una representación estructurada que permita medir de forma objetiva la exposición, la conectividad y la criticidad de la red. La falta de este análisis dificulta la priorización de intervenciones y limita la capacidad de otros componentes del sistema urbano para trabajar con información clara y cuantificable.

Este vacío metodológico no es menor. Cuando no se dispone de métricas objetivas, la identificación de puntos críticos queda sujeta a la percepción subjetiva o a criterios no sistematizados. Esto puede llevar a que recursos limitados se destinen a zonas que, aunque visibles o políticamente sensibles, no son necesariamente las que presentan mayor riesgo real. Por el contrario, áreas con problemas estructurales menos evidentes, pero igualmente graves pueden permanecer desatendidas, incrementando su vulnerabilidad con el tiempo.

El problema se agrava cuando se considera la naturaleza dinámica de la ciudad. La red vial no es estática; nuevos desarrollos urbanos, cambios en la densidad poblacional y modificaciones en la infraestructura alteran continuamente las condiciones de movilidad y exposición. Sin un sistema de monitoreo basado en indicadores cuantitativos, resulta difícil detectar estos cambios a tiempo o evaluar su impacto en la criticidad general de la red.

Además, la ausencia de un grafo estructurado limita las posibilidades de integración con otras herramientas analíticas. Los modelos de inteligencia artificial, los sistemas de simulación y los índices de criticidad requieren insumos de entrada que sean coherentes, completos y comparables. Un grafo de la red vial que no incorpore adecuadamente las variables de exposición o que no esté correctamente construido desde el punto de vista topológico compromete la calidad de todos los análisis que dependen de él.

### 1.3 Causas

- La red vial de varios sectores de Guayaquil es irregular y poco planificada.
- No se aplica de manera formal el análisis de grafos para estudiar la criticidad urbana.
- Existe poca integración entre los datos de la red vial y variables de exposición.
- Las decisiones sobre zonas de riesgo se toman principalmente con base en percepción o experiencia, sin métricas objetivas.

### 1.4 Consecuencias

- Se mantiene una identificación subjetiva de los puntos críticos de la red.
- Se dificulta la priorización de acciones de mejora o de respuesta ante emergencias.
- Otros módulos del sistema urbano (índice de criticidad, IA y simulación) no cuentan con un insumo de grafo bien estructurado.
- Se pierde la oportunidad de generar información reproducible y comparable entre diferentes zonas de la ciudad.

### 1.5 Formulación del problema

¿Cómo la construcción de un grafo de la red vial urbana permite cuantificar la exposición, la conectividad y la criticidad en zonas de riesgo de Guayaquil?

## 2. ALCANCE

El proyecto se centra en la construcción y análisis de un grafo de la red vial de una zona urbana de Guayaquil. Incluye la obtención de la red a partir de datos abiertos, la generación del grafo, el cálculo de métricas de conectividad y centralidad, la incorporación de variables de exposición y la identificación de los elementos más críticos.

**El proyecto NO incluye:**

- El desarrollo de una aplicación web o sistema completo.
- La recolección de datos primarios mediante levantamientos de campo.
- El modelamiento de amenazas naturales (inundaciones, deslizamientos, etc.).
- La implementación de soluciones físicas de infraestructura vial.

## 3. JUSTIFICACIÓN DE LA INVESTIGACIÓN

### 3.1 Justificación teórica

El análisis de redes urbanas a través de grafos se ha consolidado como una forma efectiva de estudiar la estructura y el comportamiento de los sistemas viales. Al representar las calles como nodos y aristas, es posible aplicar métricas matemáticas que permiten identificar qué elementos de la red tienen mayor influencia en la conectividad general. Autores como Porta et al. (2006) y Latora y Marchiori (2001) sentaron las bases de este enfoque al demostrar que indicadores como el grado, la centralidad de intermediación y la centralidad de cercanía ofrecen una visión más precisa de cómo funciona una red urbana.

En el contexto del riesgo, esta perspectiva adquiere aún más valor. Gao et al. (2024) y Hu et al. (2024) han mostrado que las métricas de grafos permiten detectar puntos vulnerables dentro de la red vial, especialmente aquellos cuya interrupción afectaría de manera significativa la movilidad. Boeing (2017, 2020) ha complementado esta línea al desarrollar herramientas que facilitan la construcción sistemática de grafos a partir de datos abiertos, lo que ha hecho más accesible este tipo de análisis. Como el propio Boeing señala, su herramienta fue diseñada para *"Hacer que la recopilación de datos y la creación y el análisis de redes viarias sean procesos sencillos, coherentes, automatizables y sólidos desde las perspectivas de la teoría de grafos, el transporte y el diseño urbano."* (Boeing, 2017, p. 126), un principio que se alinea directamente con la necesidad de este proyecto de contar con un proceso reproducible y fundamentado.

Aplicar estos conceptos en una ciudad como Guayaquil resulta pertinente porque permite pasar de una comprensión empírica o intuitiva de la criticidad urbana a una evaluación más objetiva y cuantificable. De esta manera, el presente trabajo aporta a la discusión teórica sobre el uso de grafos en la gestión de riesgos urbanos, al mismo tiempo que adapta estos enfoques a un contexto local donde todavía se utilizan de forma limitada.

### 3.2 Justificación práctica

Este trabajo desarrolla el bloque URB-02 del proyecto FCI 2026-059 "Gemelo Digital Multimodal para la Gestión Inteligente del Riesgo". Como bloque URB-02, nuestra función específica es construir la capa geoespacial de grafos que sirve como columna vertebral del sistema. Para ello, recibimos el modelo de datos urbano estructurado que genera el bloque URB-01 y, a partir de él, construimos el grafo de la red vial con sus métricas de exposición, conectividad y criticidad. Los resultados que generamos son el grafo, las métricas y el índice de criticidad, son entregados a los bloques URB-03 (índice de criticidad), URB-04 (análisis con inteligencia artificial), URB-05 (simulación de escenarios) y SIS-API-01 (servicios de datos para aplicaciones externas). Esta integración vertical asegura que nuestro trabajo no sea un ejercicio aislado, sino una pieza fundamental del ecosistema RISKTWIN que permite que los análisis posteriores cuenten con una base estructural sólida y reproducible.

Desde el punto de vista práctico, el proyecto responde a una necesidad concreta: contar con información clara y estructurada sobre la exposición, la conectividad y la criticidad de la red vial en zonas de riesgo. En muchos sectores de Guayaquil, las decisiones relacionadas con la movilidad y la respuesta ante emergencias se toman todavía con base en la experiencia o en observaciones generales, sin un respaldo cuantitativo sólido.

Al construir un grafo de la red vial e incorporar métricas de centralidad junto con variables de exposición, se genera un insumo técnico que puede ayudar a identificar de forma más precisa los tramos y nodos más críticos. Esta información resulta útil no solo para el análisis del caso de estudio, sino también como base para otros componentes del sistema RISKTWIN, especialmente el índice de criticidad, los modelos de inteligencia artificial y la simulación de escenarios.

Además, al trabajar con datos abiertos y herramientas de código abierto, el proceso se vuelve reproducible y de bajo costo, lo que facilita su eventual aplicación en otras zonas de la ciudad o incluso en contextos similares.

### 3.3 Justificación metodológica

Metodológicamente, el trabajo se sustenta en el uso de datos abiertos y en un proceso de construcción y análisis de grafos que puede ser documentado de manera clara y reproducible. La literatura especializada coincide en que el uso de fuentes como OpenStreetMap, combinado con herramientas computacionales, abre nuevas posibilidades para el análisis urbano desde perspectivas tanto cuantitativas como cualitativas (Boeing, 2020).

En este sentido, el enfoque adoptado combina la construcción del grafo con el cálculo de métricas de centralidad y la incorporación de variables de exposición. Esta secuencia permite validar cada etapa del proceso y deja un producto final (grafo, métricas y mapas) que puede ser utilizado por otros módulos del sistema. Al documentar todo el procedimiento en un notebook reproducible, se garantiza transparencia y se facilita la replicación del trabajo en futuras investigaciones o en otras áreas urbanas.

## 4. OBJETIVO GENERAL

Construir un grafo de la red vial urbana de una zona de Guayaquil para cuantificar la exposición, la conectividad y la criticidad como apoyo al análisis de zonas de riesgo.

## 5. OBJETIVOS ESPECÍFICOS

- Delimitar el área de estudio y construir el grafo de la red vial a partir de datos abiertos.
- Analizar las métricas de conectividad y centralidad de la red vial seleccionada.
- Desarrollar variables de exposición en el grafo para identificar los tramos y nodos de mayor criticidad.
- Evaluar mapas temáticos y un informe de criticidad que identifique los nodos y tramos con mayor exposición y conectividad crítica.

## 6. HIPÓTESIS DE INVESTIGACIÓN

No aplica. El trabajo es de carácter aplicado y descriptivo. No se plantea una hipótesis de contrastación estadística, sino la construcción de un artefacto (grafo + métricas) que permita cuantificar las variables de estudio.

## 7. MARCO TEÓRICO Y REFERENCIAL

### 7.1 Redes urbanas y teoría de grafos

Una red urbana puede representarse como un grafo, donde los nodos corresponden a intersecciones o puntos relevantes y las aristas a los tramos de calles que los conectan. Esta forma de modelar el espacio permite aplicar herramientas matemáticas para analizar la estructura de la red y evaluar su comportamiento frente a diferentes escenarios.

Porta et al. (2006) fueron de los primeros en sistematizar el análisis de calles urbanas mediante grafos. En su trabajo, introducen el concepto de *multiple centrality assessment* (MCA), una metodología que, a diferencia de otros enfoques, *"se basa en grafos de calles primales, en lugar de duales"* y *"opera dentro de un marco métrico, más que topológico"* (Porta et al., 2006, p. 706), lo que permite un análisis más rico y cercano a la experiencia espacial real. Latora y Marchiori (2001) aportaron métricas fundamentales, como la eficiencia de la red, que han sido ampliamente utilizadas en estudios posteriores. Por su parte, Boeing (2017, 2020) ha impulsado el uso de datos abiertos y herramientas computacionales para construir y analizar estos grafos de manera más accesible y reproducible.

Entre las métricas más relevantes se encuentran el grado de los nodos, que indica cuántas conexiones tiene una intersección; la centralidad de intermediación que identifica los nodos por los que pasan la mayor cantidad de caminos más cortos; y la centralidad de, que mide qué tan accesible es un nodo respecto al resto de la red. Estas medidas permiten identificar elementos clave de la estructura vial y constituyen la base del análisis de criticidad.

### 7.2 Exposición en el contexto de riesgo urbano

La exposición se entiende como la presencia de personas, viviendas o infraestructura en zonas susceptibles de verse afectadas por un evento de riesgo. En el análisis de redes viales, esta dimensión puede incorporarse asignando pesos a los nodos o a las aristas según variables como la densidad poblacional, la presencia de puntos de interés o el nivel de actividad que concentra cada tramo.

Como han señalado Wang et al. (2024), combinar la estructura de la red con variables de exposición permite pasar de un análisis puramente topológico a uno orientado a la gestión de riesgos. Estos autores proponen que el uso de gemelos digitales en el análisis de resiliencia urbana permite *"deducción y control dinámicos del proceso del desastre"* (Wang et al., 2024, p. 35), una capacidad que resulta fundamental para entender la criticidad de la red en escenarios de emergencia. Zhang et al. (2023) refuerzan esta idea al mostrar que la incorporación de información contextual mejora la capacidad de identificar zonas críticas.

En este trabajo se retoma esa lógica: no se busca solo medir la conectividad de la red, sino entender qué tan relevante resulta cada tramo o nodo cuando se considera la exposición real de la población e infraestructura.

### 7.3 Conectividad y criticidad

La conectividad describe el grado en que los elementos de la red están interrelacionados. Una red con baja conectividad presenta tramos o nodos cuya interrupción puede afectar significativamente la movilidad. La criticidad, por su parte, combina la importancia estructural de un elemento (medida a través de las métricas de centralidad) con su nivel de exposición. Identificar los elementos críticos permite priorizar acciones de mejora o de respuesta ante emergencias.

### 7.4 Datos abiertos y OpenStreetMap

OpenStreetMap se ha convertido en una fuente fundamental para estudios urbanos porque ofrece información detallada de la red vial de forma libre y actualizada. A partir de estos datos es posible construir grafos de calles con atributos como longitud, tipo de vía y dirección, lo que facilita el análisis de conectividad y criticidad sin necesidad de levantamientos de campo costosos.

### 7.5 Aplicación de grafos en gestión de riesgos urbanos

Diversos estudios han demostrado que el análisis de grafos resulta útil para evaluar la resiliencia de las redes viales y para identificar puntos vulnerables ante eventos de riesgo. Este enfoque permite pasar de una visión cualitativa o empírica a una evaluación más objetiva y reproducible, lo que resulta especialmente valioso en ciudades con crecimiento irregular como Guayaquil.

### 7.6 Trabajos similares

El análisis de redes viales mediante grafos ha sido aplicado en diversos contextos urbanos, y resulta útil revisar algunos de estos trabajos para situar el presente proyecto en el panorama actual de la investigación.

Gao et al. (2024) desarrollaron un enfoque basado en redes neuronales de grafos probabilísticos para predecir accidentes de tráfico a nivel de calles. Su trabajo demuestra que las métricas de centralidad y la estructura de la red son predictores significativos del riesgo vial. Sin embargo, su enfoque está orientado principalmente a la predicción de accidentes a partir de datos históricos, y no incorpora variables de exposición como densidad poblacional o proximidad a puntos de interés críticos. Además, su aplicación se centra en contextos urbanos de ciudades con redes viales bien consolidadas y sistemas de recolección de datos robustos, lo que difiere significativamente del contexto latinoamericano donde la disponibilidad y calidad de los datos pueden ser más limitadas.

Hu et al. (2024), por su parte, propusieron un modelo que combina inferencia causal de Granger con redes convolucionales de grafos para la predicción de riesgos de colisión. Su trabajo destaca la importancia de capturar dependencias espaciales y temporales en la red vial, y utiliza datos de siniestros para validar sus modelos. Al igual que Gao et al. (2024), su enfoque es altamente predictivo y requiere de volúmenes significativos de datos históricos de accidentes, una condición que no siempre se cumple en contextos como el de Guayaquil, donde el registro sistemático de incidentes viales puede ser incompleto o estar fragmentado entre diferentes entidades.

En contraste con estos trabajos, el presente proyecto se diferencia en varios aspectos fundamentales. En primer lugar, su objetivo no es la predicción de accidentes a partir de datos históricos, sino la caracterización estructural de la red para identificar elementos críticos con base en la combinación de métricas de centralidad y variables de exposición. En segundo lugar, el proyecto se inscribe en un contexto de disponibilidad de datos más limitada, lo que exige un enfoque que priorice el uso de fuentes abiertas y accesibles como OpenStreetMap, en lugar de depender de bases de datos de siniestros que pueden no estar disponibles o ser incompletas. En tercer lugar, el trabajo forma parte de un sistema mayor (RISKTWIN), lo que implica que sus resultados deben ser entregados en un formato que pueda ser integrado con otros módulos del sistema, una exigencia que no está presente en los trabajos mencionados.

Zhang et al. (2023) aportan una perspectiva complementaria al incorporar información semántica visual y espacial en la predicción de riesgos de accidentes. Su trabajo muestra cómo la integración de múltiples fuentes de información contextual puede mejorar la capacidad de identificar zonas de riesgo. Este enfoque es coherente con la línea que adoptamos en nuestro proyecto, donde la incorporación de variables de exposición (densidad poblacional, proximidad a puntos de interés) enriquece el análisis puramente topológico de la red.

En resumen, mientras que la literatura existente se ha centrado principalmente en la predicción de accidentes utilizando datos históricos y modelos avanzados de aprendizaje automático, el presente proyecto se orienta a la caracterización estructural de la red vial y su criticidad, utilizando exclusivamente fuentes de datos abiertos y generando un artefacto que puede ser integrado en un sistema de gemelo digital. El valor distintivo de este trabajo radica en su aplicación al contexto específico de Guayaquil, una ciudad con patrones de crecimiento irregular y desafíos particulares en la gestión de riesgos y en su integración con el ecosistema RISKTWIN, lo que lo convierte en un insumo fundamental para análisis posteriores de simulación, inteligencia artificial y planificación urbana.

## 8. MARCO METODOLÓGICO

### 8.1 Tipo de investigación

La investigación es de tipo aplicada, porque busca generar una solución concreta para un problema real de análisis de riesgo urbano. No se trata de un trabajo puramente teórico o especulativo, sino de la construcción de un artefacto que pueda ser utilizado directamente por otros componentes del sistema RISKTWIN y que, en última instancia, sirva como herramienta de apoyo para la toma de decisiones en la gestión de riesgos. En este sentido, el proyecto se inscribe en la tradición de la investigación orientada a la resolución de problemas prácticos mediante el uso de métodos y herramientas de la ciencia de datos y el análisis geoespacial.

El trabajo también tiene un carácter descriptivo, ya que se propone caracterizar la red vial de la zona de estudio a través de indicadores de exposición, conectividad y criticidad. Esta caracterización no se limita a una mera enumeración de elementos, sino que busca establecer relaciones significativas entre la estructura de la red y las variables de contexto que determinan su vulnerabilidad. Se trata, en definitiva, de construir una imagen detallada y cuantificable del comportamiento de la red vial frente a posibles escenarios de riesgo.

Adicionalmente, puede considerarse que el proyecto posee un componente exploratorio, en la medida en que aborda una temática el análisis sistemático de redes viales mediante grafos en el contexto local de Guayaquil que cuenta con escasos antecedentes directos en la literatura regional. Esta condición implica que el trabajo no parte de hipótesis preconcebidas, sino que se orienta a la generación de conocimiento nuevo a partir del procesamiento y análisis de los datos disponibles.

### 8.2 Enfoque y modalidad de investigación

El enfoque es cuantitativo, puesto que se trabaja con datos numéricos obtenidos del grafo (métricas de centralidad, valores de exposición y niveles de criticidad). Este enfoque permite operacionalizar las variables de estudio de manera precisa y aplicar procedimientos estadísticos y computacionales para su análisis. La cuantificación de la conectividad, la exposición y la criticidad no es un fin en sí mismo, sino un medio para lograr una comprensión más objetiva y reproducible de las dinámicas de la red vial.

La modalidad es no experimental, ya que no se manipulan variables ni se controlan condiciones experimentales. El estudio se basa en el análisis de información existente sobre la red vial y su contexto, sin intervención directa sobre el objeto de estudio. Esta característica es propia de los estudios observacionales y se ajusta perfectamente a los objetivos del proyecto, que busca describir y analizar una realidad tal como se presenta, sin alterarla.

El carácter geoespacial de la investigación es otro rasgo distintivo. El trabajo se desarrolla en un entorno geográfico definido una zona urbana de Guayaquil y todas las variables analizadas tienen una componente espacial que es fundamental para su interpretación. El uso de sistemas de información geográfica (SIG) y herramientas de análisis espacial no es un añadido accesorio, sino un elemento central de la metodología. Como señala Boeing (2017, p. 127), *"La combinación de la ciencia de redes y los SIG proporciona un marco poderoso para comprender los sistemas urbanos."*, y es precisamente esta sinergia la que se busca aprovechar en el presente trabajo.

### 8.3 Fuentes, técnicas e instrumentos para la recolección de datos

| Tipo de Fuente | Fuente | Técnica | Instrumento |
|---|---|---|---|
| Secundaria | OpenStreetMap | Extracción de red vial | OSMnx |
| Secundaria | Datos geoespaciales abiertos | Análisis espacial | GeoPandas |
| Secundaria | Información de exposición (densidad, puntos de interés) | Asignación de pesos | NetworkX + datos abiertos |

### 8.4 Población y muestra

La población objeto de estudio corresponde a la red vial de zonas urbanas de Guayaquil que presentan características de riesgo. Esta población no se define en términos de individuos o unidades muestrales tradicionales, sino como un conjunto de elementos de infraestructura vial (tramos de calles e intersecciones) que conforman un sistema interconectado. La complejidad y extensión de la red vial de la ciudad hacen inviable un análisis exhaustivo de toda su extensión en el marco de este proyecto, por lo que se ha optado por un enfoque de muestreo no probabilístico, de tipo intencional o deliberado.

La muestra está constituida por el grafo generado a partir de la red vial de un sector representativo de la ciudad, delimitado para el estudio. Este grafo incluye los nodos (intersecciones) y las aristas (tramos de calles) contenidos dentro del área seleccionada. La selección de la zona de estudio se realizará con base en criterios de relevancia en términos de exposición poblacional, complejidad de la red y disponibilidad de datos. Se privilegiarán áreas que presenten una combinación de alta densidad de edificación, patrones de conectividad irregulares y antecedentes de eventos de riesgo, de manera que los resultados del análisis tengan la mayor aplicabilidad posible.

Es importante señalar que, aunque la muestra es acotada, los procedimientos metodológicos desarrollados son escalables y replicables. Esto significa que, en futuras fases del proyecto o en trabajos derivados, la misma metodología podría aplicarse a otras zonas de la ciudad o incluso a la totalidad de la red vial, siempre que se disponga de la capacidad computacional necesaria.

### 8.5 Análisis y tratamiento de la información

El procesamiento de la información se realiza en las siguientes etapas, cada una de las cuales está diseñada para garantizar la calidad y consistencia de los resultados:

- **Delimitación del área de estudio:** Se define un polígono que abarca la zona de interés, utilizando como referencia barrios o sectores con características de riesgo. Esta delimitación se realiza mediante herramientas SIG, asegurando que el área sea suficientemente extensa como para capturar la estructura de la red, pero lo bastante acotada como para permitir un análisis detallado.
- **Descarga y limpieza de la red vial:** Se extrae la información de OpenStreetMap utilizando OSMnx. Los datos descargados incluyen atributos como tipo de vía, longitud, nombre y dirección. Posteriormente, se realiza un proceso de limpieza que consiste en eliminar elementos irrelevantes para el análisis (como vías peatonales o ciclovías, a menos que sean relevantes para el caso) y corregir posibles inconsistencias topológicas.
- **Construcción del grafo:** La red vial se convierte en un grafo dirigido o no dirigido, según las características del análisis. Los nodos representan las intersecciones y las aristas representan los tramos de calle. A cada arista se le asigna un peso basado en su longitud, lo que permite calcular distancias reales y caminos más cortos.
- **Cálculo de métricas de conectividad y centralidad:** Se aplican algoritmos de NetworkX para obtener indicadores como el grado de los nodos (número de conexiones), la centralidad de intermediación (*betweenness centrality*), que mide la frecuencia con que un nodo actúa como puente en los caminos más cortos, y la centralidad de cercanía (*closeness centrality*), que indica la distancia promedio de un nodo al resto de la red. Estas métricas permiten identificar los elementos estructuralmente más relevantes.
- **Incorporación de variables de exposición:** Se asignan pesos adicionales a nodos y aristas en función de variables de contexto, como la densidad de población en el área circundante o la proximidad a puntos de interés (hospitales, escuelas, mercados). Esta etapa permite enriquecer el análisis topológico con información del mundo real.
- **Identificación de los elementos más críticos:** Se combinan las métricas de centralidad con las variables de exposición para generar un índice de criticidad. Los nodos y aristas con valores más altos en este índice se consideran críticos, ya que su interrupción afectaría de manera significativa la movilidad y pondría en riesgo a una mayor cantidad de personas.
- **Generación de mapas temáticos y análisis de resultados:** Los resultados se visualizan mediante mapas que representan la distribución espacial de las métricas calculadas. Estos mapas facilitan la interpretación de los hallazgos y permiten comunicar los resultados de manera efectiva.

Todo el proceso se documenta en un notebook reproducible (Jupyter o Google Colab) que incluye el código, los comentarios explicativos y las visualizaciones generadas. Esta práctica garantiza transparencia y posibilidad de verificación, aspectos fundamentales en cualquier investigación científica.

### 8.6 Matriz de operacionalización de variables

| Variable | Dimensión | Indicador | Técnica | Instrumento |
|---|---|---|---|---|
| **Conectividad** | Estructura de la red | Grado de los nodos, componentes conectados, caminos más cortos | Análisis de grafos | NetworkX |
| **Exposición** | Vulnerabilidad | Densidad de nodos, proximidad a puntos de interés, pesos asignados a aristas | Análisis geoespacial | GeoPandas + NetworkX |
| **Criticidad** | Centralidad | Betweenness centrality, closeness centrality, grado ponderado | Cálculo de métricas | NetworkX |
| **Red vial urbana** | Infraestructura | Nodos, aristas, longitud de tramos | Extracción de datos | OSMnx |

## 9. METODOLOGÍA DE DESARROLLO A EMPLEAR

### 9.1 Justificación de la metodología

Para el desarrollo de este trabajo se adopta un enfoque metodológico dual que combina dos marcos complementarios: Design Science Research (DSR) como metodología general de investigación, y KGC Pipeline (Knowledge Graph Construction Pipeline) como flujo de trabajo técnico para la construcción del artefacto.

Esta combinación responde a la naturaleza del proyecto, que no se limita a describir un fenómeno, sino que busca construir un artefacto concreto —el grafo de la red vial con sus métricas de conectividad, centralidad y criticidad— que pueda ser evaluado y utilizado por otros módulos del sistema RISKTWIN.

Design Science Research (DSR) fue formalizado por Hevner et al. (2004) como una metodología para la investigación en sistemas de información que reconoce dos tipos de conocimiento: el descriptivo (lo que existe) y el prescriptivo (cómo construir algo que resuelva un problema). DSR se organiza en un ciclo iterativo que incluye la identificación del problema, el diseño y desarrollo del artefacto, su evaluación y la comunicación de los resultados. La elección de DSR responde a cuatro razones concretas: porque estamos construyendo un artefacto (el grafo con sus métricas), porque el problema es real y está bien definido (la falta de medición objetiva de criticidad en Guayaquil), porque DSR es iterativo y permite ajustar decisiones metodológicas sobre la marcha, y porque exige evaluar la utilidad del artefacto, no solo construirlo (Hevner et al., 2004).

KGC Pipeline (Knowledge Graph Construction Pipeline), por su parte, es un marco metodológico que ha sido ampliamente utilizado en proyectos que involucran la construcción de grafos de conocimiento a partir de datos estructurados y semiestructurados (Cuzzocrea et al., 2024; Ehrlinger & Wöß, 2016). Su aplicación se ha documentado en diversos dominios, incluyendo ciudades inteligentes, manufactura y salud, donde se ha utilizado para guiar la construcción sistemática de grafos que integran datos heterogéneos (UrbanKG, 2023; Ortiz, 2024; Niu et al., 2024). Este enfoque proporciona un flujo de trabajo claro y reproducible que abarca desde la adquisición de datos hasta la generación de conocimiento accionable, lo cual se alinea perfectamente con las necesidades técnicas de nuestro proyecto.

### 9.2 Fases del desarrollo

El desarrollo se estructura en siete fases que integran el flujo de KGC Pipeline dentro del ciclo DSR. Cada fase produce un entregable concreto que sirve como insumo para la siguiente, y se prevén iteraciones y ajustes a medida que se avanza en el trabajo.

| Fase | Actividad principal | Resultado esperado |
|---|---|---|
| **1. Adquisición y extracción de datos** | Delimitar el área de estudio y descargar la red vial desde OpenStreetMap utilizando OSMnx | Red vial limpia y delimitada |
| **2. Preprocesamiento y limpieza** | Eliminar elementos irrelevantes y corregir inconsistencias topológicas mediante simplificación de grafos | Grafo coherente y libre de sesgos |
| **3. Construcción del grafo y cálculo de métricas estructurales** | Convertir la red en un grafo de nodos y aristas; calcular métricas de conectividad y centralidad | Grafo estructurado con métricas calculadas |
| **4. Incorporación de variables de exposición** | Asignar pesos a nodos y aristas según densidad poblacional y proximidad a puntos de interés | Grafo ponderado con variables de contexto |
| **5. Análisis de criticidad y modelado predictivo** | Combinar métricas de centralidad con exposición; aplicar correlación de Spearman y regresión logística | Índice de criticidad, ranking de nodos, modelo predictivo de riesgo (Alto/Medio/Bajo) |
| **6. Visualización y documentación** | Generar mapas temáticos y documentar todo el proceso en un notebook reproducible | Entregables finales |
| **7. Evaluación y validación** | Validar la coherencia del grafo, evaluar el modelo predictivo y verificar la reproducibilidad del proceso | Artefacto evaluado y validado |

### 9.3 Prácticas aplicadas

El desarrollo del proyecto se rige por un conjunto de buenas prácticas que garantizan la calidad, reproducibilidad y utilidad de los resultados:

- **Uso de datos abiertos** (OpenStreetMap) para garantizar reproducibilidad y reducir costos.
- **Documentación completa del proceso** en un notebook de Jupyter que combina código, explicaciones y visualizaciones.
- **Validación de la coherencia del grafo**, verificando la conectividad y ausencia de elementos aislados no justificados.
- **Aplicación de métodos estadísticos** (Spearman y regresión logística) para validar y enriquecer el análisis.
- **Generación de mapas temáticos** para facilitar la interpretación de resultados.
- **Versionado simple** de los archivos de trabajo para mantener trazabilidad.
- **Evaluación del modelo predictivo** mediante métricas de rendimiento y validación cruzada.

### 9.4 Responsabilidades por estudiante

| Estudiante | Responsabilidad principal | Entregables asociados |
|---|---|---|
| **Macias Carranza Krystel Shanely** | Construcción del grafo, limpieza de la red, cálculo de métricas de conectividad y centralidad | Grafo base, métricas estructurales, documentación del proceso de construcción |
| **Suarez Barco José Enrique** | Incorporación de variables de exposición, análisis de criticidad, correlación de Spearman, regresión logística y generación de mapas | Grafo ponderado, índice de criticidad, modelo predictivo (Alto/Medio/Bajo), mapas temáticos y análisis final |

## 10. CRONOGRAMA DE ACTIVIDADES

| Actividad | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Semana 5 | Semana 6 | Semana 7 | Semana 8 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Revisión bibliográfica y marco teórico** | ✔ | ✔ | | | | | | |
| **Delimitación del área y descarga de la red vial** | | ✔ | ✔ | | | | | |
| **Construcción y limpieza del grafo** | | | ✔ | ✔ | | | | |
| **Cálculo de métricas de conectividad y centralidad** | | | | ✔ | ✔ | | | |
| **Incorporación de variables de exposición** | | | | | ✔ | ✔ | | |
| **Análisis de criticidad y generación de mapas** | | | | | | ✔ | ✔ | |
| **Redacción del informe y ajustes finales** | | | | | | | ✔ | ✔ |

## 11. PRESUPUESTO Y FINANCIAMIENTO

| Rubro | Descripción | Costo (USD) |
|---|---|---|
| **Recurso humano** | 2 estudiantes durante el desarrollo del trabajo | Aporte propio |
| **Software** | Herramientas de código abierto (Python, OSMnx, NetworkX, GeoPandas) | $0.00 |
| **Cómputo** | Uso de equipo personal y entornos gratuitos (Google Colab si se requiere) | $0.00 |
| **Material bibliográfico** | Acceso a artículos a través de repositorios abiertos e institucionales | $0.00 |
| **Impresión y empastado** | Documento final del trabajo de titulación | $80.00 |
| **Imprevistos (10 %)** | | $8.00 |
| **TOTAL** | | **$88.00** |

## 12. BENEFICIOS ESPERADOS DEL PROYECTO

- Generar un grafo de la red vial que permita medir de forma objetiva la exposición, la conectividad y la criticidad en una zona urbana de Guayaquil.
- Entregar un insumo estructurado y reproducible que pueda ser utilizado por otros módulos del sistema urbano (índice de criticidad, análisis de IA y simulación).
- Aportar una metodología clara y de bajo costo para el análisis de redes viales en contextos de riesgo urbano.
- Facilitar la identificación de nodos y tramos críticos, apoyando una mejor priorización de acciones en gestión de riesgos.
- Dejar documentado un proceso replicable que pueda aplicarse en otras zonas de la ciudad.

## 13. DERECHOS DE PROPIEDAD INTELECTUAL

El desarrollo de este trabajo de tesis contempla la generación de resultados susceptibles de protección por Propiedad Intelectual (derechos de autor, patentes, programa de computador). ¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [x] Software (notebook y scripts de construcción y análisis del grafo)
- [x] Modelo/algoritmo (proceso de cálculo de métricas y asignación de criticidad)
- [x] Manual/documentación técnica (notebook reproducible y descripción metodológica)
- [ ] No aplica

Los derechos patrimoniales de los productos generados en el presente trabajo de tesis corresponderán a la institución, de conformidad con la normativa vigente. Los autores conservarán los derechos morales sobre su obra.

## 14. REFERENCIAS BIBLIOGRÁFICAS

Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. *Computers, Environment and Urban Systems, 65*, 126–139. <https://doi.org/10.1016/j.compenvurbsys.2017.05.004>

Boeing, G. (2020). Exploring urban form through OpenStreetMap data and complex network science. *Urban Science, 4*(3), 37. <https://doi.org/10.3390/urbansci4030037>

Gao, X., Jiang, X., Haworth, J., Zhuang, D., Wang, S., Chen, H., & Law, S. (2024). Uncertainty-aware probabilistic graph neural networks for road-level traffic crash prediction. *Accident Analysis & Prevention, 208*, 107801. <https://doi.org/10.1016/j.aap.2024.107801>

Hu, J., Bai, J., Yang, J., & Lee, J. J. (2024). Crash risk prediction using sparse collision data: Granger causal inference and graph convolutional network approaches. *Expert Systems with Applications, 259*, 125315. <https://doi.org/10.1016/j.eswa.2024.125315>

Latora, V., & Marchiori, M. (2001). Efficient behavior of small-world networks. *Physical Review Letters, 87*(19), 198701. <https://doi.org/10.1103/PhysRevLett.87.198701>

Mazzetto, S. (2024). A review of urban digital twins integration, challenges, and future directions in smart city development. *Sustainability, 16*(19), 8337. <https://doi.org/10.3390/su16198337>

Porta, S., Crucitti, P., & Latora, V. (2006). The network analysis of urban streets: A primal approach. *Environment and Planning B: Planning and Design, 33*(5), 705–725. <https://doi.org/10.1068/b32045>

Wang, Y., Zhang, H., & Liu, X. (2024). Digital twin approach for enhancing urban resilience: A cycle between virtual space and the real world. *Resilient Cities and Structures, 3*(2), 34–45. <https://doi.org/10.1016/j.rcns.2024.06.002>

Zhang, Y., Wang, X., & Zeng, Y. (2023). Research on traffic accident risk prediction method based on spatial and visual semantics. *ISPRS International Journal of Geo-Information, 12*(12), 496. <https://doi.org/10.3390/ijgi12120496>

---

## RÚBRICA DE EVALUACIÓN

*(Página manuscrita escaneada; notas transcritas.)*

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

## Anexo C — Rúbrica de evaluación para proyectos grupales de integración curricular

*(Página manuscrita escaneada; marcas transcritas.)*

| # | Aspectos evaluados | No cumple | Cumple parcialmente | Cumple |
|:-:|---|:-:|:-:|:-:|
| 1 | Tema del proyecto: se describe un tema que contenga la problemática de estudio, y que se ajuste a la línea de investigación de la Carrera y a la pirámide de investigación de la Facultad. | | | ✔ |
| 2 | Definición del problema: se identifica un problema complejo o con múltiples abordajes, y se especifican los múltiples enfoques de la investigación planteada. | | ✔ | |
| 3 | División de tareas: se indica el plan de trabajo detallado incluyendo hitos y plazos para cada fase del proyecto. | | | ✔ |
| 4 | Desarrollo de objetivos: se describen los objetivos con enfoques específicos para abordar los diferentes aspectos del problema planteado; estos se ajustan al tema propuesto. | | ✔ | |
| 5 | Descripción de propiedad intelectual: se indica si el proyecto tendrá como resultado un diseño industrial, desarrollo de software, modelos de utilidad, patentes de invención o algún otro producto enmarcado en la normativa ecuatoriana de propiedad intelectual; se deberá especificar y detallar en la propuesta. | | | ✔ |

> Nota: las marcas de la imagen escaneada son manuscritas y la columna exacta de los ítems 2 y 4 no es del todo nítida; verificar contra el original.

**Firmas**

- Macias Carranza Krystel Shanely — C.I.# 0951179662
- Suarez Barco Jose Enrique — C.I.# 0950655100
- LSI. García Plúa Juan Carlos, MSIG. — C.I.# 130857930 *(lectura aproximada de la firma manuscrita)*
- LSI. Lino Castillo Katty Nancy, MSIG. — C.I.# 0719040972 *(lectura aproximada de la firma manuscrita)*
