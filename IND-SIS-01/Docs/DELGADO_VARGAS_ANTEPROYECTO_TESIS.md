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
| **ESTUDIANTE 1** | Delgado Quiñonez | Elian Adonis |
| **ESTUDIANTE 2** | Vargas Ordoñez | Stalyn Gabriel |

**Correo electrónico institucional y personal:**

- elian.delgadoq@ug.edu.ec
- adonisquinonez11@gmail.com
- stalyn.vargaso@ug.edu.ec
- Stalyngabo138@gmail.com

**Teléfono:** 0979440818 / 0991512304

## Tema

**TEMA:** Arquitectura de software para la integración de datos fragmentados de riesgo industrial en un gemelo digital multimodal

**LÍNEA DE INVESTIGACIÓN:**

- [ ] Sostenibilidad, derechos y tecnologías en el ordenamiento territorial, ambiente de la construcción y arquitectura.
- [ ] Desarrollo local y emprendimiento socio económico sostenible.
- [x] Ciencias básicas, bioconocimiento y desarrollo industrial.
- [ ] Salud humana, animal y del ambiente.
- [ ] Tecnologías agrícolas y de la agricultura.
- [ ] Entornos virtuales de aprendizaje y tecnologías educativas.

**COBERTURA:**

- [ ] Nacional
- [ ] Provincial
- [x] Local
- [ ] Otros

---

# DESARROLLO ANTEPROYECTO

## Planteamiento y formulación del problema

La seguridad industrial sigue siendo un problema grande en Ecuador. Según el IESS, entre enero y septiembre de 2023 se registraron 9.887 accidentes laborales, el 19% en el sector industrial y el 15% en comercio (Primicias, 2023). Para 2024 la cifra ya pasaba de los 22.000 casos a nivel nacional, con Guayas entre las provincias más afectadas (Tagline Soluciones Empresariales, 2026).

Parte del problema es que la información sobre estos riesgos casi nunca está en un solo lugar: unos datos están en Excel, otros en papel, otros en sistemas que ni siquiera se conectan entre sí. Eso hace que cuando una empresa detecta algo riesgoso, ya sea tarde para actuar. Y no es solo un problema ecuatoriano: (Tan, y otros, 2025) señalan que muchos procesos de gemelos digitales todavía dependen de integrar la información a mano, lo que genera errores y hace que el gemelo digital no refleje bien lo que está pasando en la realidad. (Picone, Turazza, Martinelli, & Mamei, 2026) agregan que en entornos industriales esto se complica más porque los dispositivos IoT e IIoT usan protocolos y formatos distintos entre sí, lo que hace complicado juntar toda esa información en un solo sistema.

Este trabajo se hace dentro del proyecto RISKTWIN. Otros grupos ya avanzaron con los indicadores de riesgo (SI-01) y con la recolección de datos de incidentes (SI-02), pero falta la parte que conecta todo eso: una arquitectura que tome esos datos y los dejes disponibles para el módulo de visualización (IND-SIS-02) y para la API que se conecta con el gemelo digital multimodal (SIS-API-01).

Actualmente, las organizaciones que gestionan riesgos industriales suelen utilizar herramientas distintas para registrar y controlar la información: hojas de cálculo para incidentes, documentos para inspecciones, otros sistemas para condiciones inseguras. Cada herramienta maneja la información de forma diferente y no existe comunicación directa entre ellas, lo que dificulta obtener una visión general del nivel de riesgo de una planta en un momento determinado. Dentro de RISKTWIN pasa algo parecido, aunque a menor escala: ya se avanzó en definir los indicadores (SI-01) y en organizar el dataset de incidentes (SI-02), pero esa información todavía no tiene una arquitectura que la centralice, organice y ponga a disposición de los demás componentes del proyecto.

Esta falta de arquitectura tiene motivos concretos:

- SI-01 y SI-02 se desarrollan de forma independiente y todavía no comparten un modelo de datos común.
- No existe una API que le permita al dashboard ni al gemelo digital multimodal acceder directamente a los datos que producen estos componentes.
- Los equipos de RISKTWIN no han acordado un formato estandarizado para intercambiar información entre los distintos módulos del sistema.

Como consecuencia, la información de riesgo permanece distribuida entre los distintos componentes del proyecto, sin una visión completa y actualizada del estado del sistema. Esto afecta directamente al dashboard (IND-SIS-02), que no dispone de una fuente centralizada de donde obtener información actualizada, y a la API de integración (SIS-API-01), que no puede interactuar con el gemelo digital multimodal por la ausencia de un servicio que organice y suministre los datos requeridos. Además, los resultados de SI-01 y SI-02 no pueden aprovecharse plenamente dentro del ecosistema RISKTWIN, ya que la falta de mecanismos de integración dificulta el intercambio de información con los demás módulos del proyecto.

Frente a esto, cabe preguntarse: ¿es posible diseñar una arquitectura de software que integre los datos fragmentados de riesgo industrial generados por los componentes SI-01 y SI-02 del proyecto RISKTWIN, de manera que puedan ser consumidos por el dashboard y la API de integración del gemelo digital multimodal?

## Alcance

Este proyecto se desarrollará a lo largo de cuatro meses. Considerando el tiempo y los recursos asignados, el alcance del proyecto se definió para lograr de manera realista los objetivos establecidos dentro del plazo estipulado.

Las actividades del proyecto incluyen:

- Desarrollo de un modelo de datos que integre los indicadores de riesgo generados por el componente SI-01 con el conjunto de datos de incidentes generado por SI-02.
- Implementación de una base de datos para el almacenamiento y la gestión centralizados de datos.
- Documentación de la arquitectura propuesta mediante diagramas de componentes, modelos objeto-relación y especificaciones de servicio utilizando OpenAPI/Swagger.
- Realización de pruebas de integración con los datos proporcionados por SI-02 para garantizar el correcto funcionamiento de la solución desarrollada.

Además, las siguientes actividades no están incluidas en el alcance de este estudio:

- El análisis o cálculo de los indicadores de riesgo, ya que corresponde a SI-01.
- La construcción del dataset de incidentes, que es responsabilidad de SI-02.
- El diseño de la interfaz gráfica del dashboard, que pertenece a IND-SIS-02.
- La implementación completa del gemelo digital multimodal; este proyecto se limita a la capa de integración de datos que permite conectar los componentes del ecosistema RISKTWIN.

Por lo tanto, este proyecto se centra en el diseño e implementación de una capa de integración de datos que permite la comunicación entre los diferentes componentes para construir el ecosistema RISKTWIN.

## Justificación de la Investigación (teórica, práctica y metodológica)

### Justificación teórica

La integración de datos de diversas fuentes es uno de los mayores desafíos en el desarrollo de empresas digitales. (Tan, y otros, 2025) señalaron que muchos de estos modelos aún dependen de la intervención humana, lo que afecta la precisión de la empresa virtual y limita su capacidad para reflejar el entorno real. (Picone, Turazza, Martinelli, & Mamei, 2026) añadieron otro problema: la presencia de diferentes componentes y formatos de datos en los dispositivos IoT e IIoT limita la comunicación entre sistemas industriales.

Este estudio aborda este problema y lo aplica a un escenario específico: la recopilación de datos de accidentes industriales en el proyecto RISKTWIN. Proporciona un ejemplo práctico de cómo gestionar el proceso de integración de datos en modelos de gemelos digitales a diferentes escalas en un contexto industrial y universitario en Ecuador.

### Justificación práctica

En la práctica, esta arquitectura permitirá integrar la información generada por los sistemas SI-01 y SI-02 en el panel de instrumentos (IND-SIS-02) y en la interfaz API de integración (SIS-API-01). Esto permitirá a los módulos del proyecto RISKTWIN intercambiar información de forma coordinada y, en caso necesario, acceder a los datos actuales.

Este problema no es exclusivo de RISKTWIN: en muchas organizaciones industriales, la información de riesgo está dispersa entre diferentes sistemas, lo que dificulta su integración. Sin embargo, esta solución puede servir de referencia para otros proyectos que se enfrenten a este tipo de problema. La documentación elaborada durante el desarrollo también puede ser útil para otros que deseen reproducir o adaptar el sistema.

### Justificación metodológica

Este proyecto se apoya en TOGAF (The Open Group Architecture Framework) de forma adaptada, ya que su Método de Desarrollo de Arquitectura (ADM) permite estructurar de manera ordenada el diseño de una arquitectura de integración, incluso para un equipo reducido de dos personas y un alcance acotado como el que requiere el trabajo con los sistemas SI-01 y SI-02.

Al trabajar de forma iterativa sobre las fases del ADM, es posible revisar y ajustar las decisiones de arquitectura conforme avanza el análisis de los componentes SI-01 y SI-02, en lugar de definir todo el diseño de una sola vez antes de iniciar la implementación.

## Objetivo general

Diseñar una arquitectura de software que integre el panel de control del proyecto RISKTWIN y una API de integración de gemelos digitales multimodal, que permita el almacenamiento, la gestión y el uso de datos sobre riesgos industriales generados por los componentes SI-01 y SI-02.

## Objetivos específicos

- Diseñar un modelo de datos que integre los indicadores de riesgo generados por el componente SI-01 y el conjunto de datos de incidentes desarrollado por el componente SI-02.
- Implementar una base de datos para el almacenamiento centralizado y la gestión de la información integrada.
- Documentar la arquitectura propuesta mediante diagramas de componentes, modelo entidad-relación y especificación de servicios utilizando OpenAPI/Swagger.
- Validar el funcionamiento de la arquitectura mediante pruebas de integración utilizando datos reales proporcionados por el componente SI-02.

## Hipótesis de Investigación

El diseño e implementación de una arquitectura de software basada en un modelo de datos centralizado y una API REST permitirá integrar la información de riesgo industrial generada por los componentes SI-01 y SI-02 del proyecto RISKTWIN, logrando un tiempo de respuesta inferior a 500 milisegundos por consulta y una tasa de éxito superior al 90% en las pruebas de integración, facilitando el acceso y consumo de la información por parte del dashboard (IND-SIS-02) y la API integradora del gemelo digital multimodal (SIS-API-01).

## Marco teórico y referencial reducido

### Marco teórico

El presente trabajo se desarrolla dentro del proyecto RISKTWIN, orientado a la gestión de riesgos industriales mediante un gemelo digital multimodal. En este contexto, los componentes SI-01 (indicadores de riesgo) y SI-02 (recopilación de incidentes) se concibieron de forma independiente. La presente propuesta busca desarrollar la capa de integración que conecte estos componentes con el dashboard (IND-SIS-02) y la API de integración del gemelo digital multimodal (SIS-API-01).

La integración de información heterogénea constituye un aspecto fundamental en arquitecturas cibernéticas e industriales (Leng et al., 2021; Lu et al., 2021). Diversas investigaciones abordan la gestión de datos en gemelos digitales mediante plataformas como un servicio (Aheleroff et al., 2021) y arquitecturas de seis capas integradas por APIs REST (Redelinghuys et al., 2021). Asimismo, se han propuesto enfoques para la captura de datos en edificios inteligentes (Eneyew et al., 2022), estandarizaciones de visualización web (Gattullo et al., 2022) y el uso de estándares de comunicación como el IEEE 1451 (Sepúlveda et al., 2022).

A nivel de interoperabilidad, la literatura actual señala que la dependencia de procesos manuales y la falta de canalizaciones de datos (data pipelines) automatizadas limitan la capacidad del gemelo digital para reflejar el entorno real en tiempo real (Barni et al., 2024; Broo & Schooling, 2023; Haag & Anderl, 2021; Vachálek et al., 2021). A esto se suma la complejidad de conectar subsistemas con patrones de interoperabilidad System-of-Systems (Nativi et al., 2021) y fusionar datos en arquitecturas multimodales (Bortolini et al., 2021; Liu et al., 2022).

En el ámbito de la seguridad industrial, estudios recientes destacan el potencial del gemelo digital para la evaluación dinámica de riesgos (Kousi et al., 2021), la predicción de peligros mediante entornos IoT (Bhatia & Sood, 2021; Jiang et al., 2024) y la evaluación continua de la seguridad del personal (Zhang et al., 2023). Frente a la fragmentación de datos en RISKTWIN, se plantea diseñar una arquitectura de software basada en microservicios y APIs REST escalables (Peruzzi et al., 2023; Serrano & Torres, 2024) que centralice y exponga los datos de SI-01 y SI-02.

### Marco referencial

El proyecto RISKTWIN responde a la problemática de la dispersión de datos de riesgo industrial, donde la información suele registrarse en documentos aislados. Los avances de los componentes SI-01 y SI-02 constituyen el punto de partida técnico para esta investigación.

Esta problemática no es exclusiva del contexto local. A nivel global, la falta de interoperabilidad entre subsistemas constituye la principal traba técnica para consolidar plataformas de gemelos digitales operativas en entornos industriales (Barni et al., 2024; Broo & Schooling, 2023). La ausencia de canalizaciones de datos automatizadas causa pérdida de sincronización entre el estado real de la planta y el modelo digital (Haag & Anderl, 2021; Vachálek et al., 2021).

Para solucionar esta barrera, la literatura en gestión de riesgos en seguridad (Jiang et al., 2024; Zhang et al., 2023) recomienda la implementación de modelos de integración sustentados en arquitecturas de microservicios RESTful (Peruzzi et al., 2023; Serrano & Torres, 2024). Estos antecedentes respaldan la necesidad de diseñar e implementar una arquitectura de software que centralice y exponga los datos de SI-01 y SI-02 para el consumo de IND-SIS-02 y SIS-API-01.

## Marco metodológico

La presente investigación tendrá un enfoque mixto, ya que combinará el análisis cualitativo de la información con la medición de resultados cuantitativos. En la primera parte se analizará la estructura, los formatos, los campos y las relaciones de los datos generados por los componentes SI-01 y SI-02, con el propósito de identificar los elementos necesarios para definir un modelo de integración adecuado. Posteriormente, se utilizarán medidas cuantitativas para evaluar el funcionamiento de la arquitectura desarrollada, principalmente mediante el tiempo de respuesta de las consultas y la tasa de éxito obtenida en las pruebas de integración.

Por su finalidad, la investigación será de tipo aplicada y tecnológica, debido a que busca resolver un problema específico del proyecto RISKTWIN mediante el diseño e implementación de una solución de software. En lugar de generar una teoría nueva, el trabajo se enfocará en desarrollar una arquitectura que permita integrar, almacenar y exponer los datos de riesgo generados por SI-01 y SI-02 para que puedan ser utilizados por los demás componentes del proyecto. Para esto se trabajará directamente con los datos y requerimientos reales disponibles dentro de RISKTWIN.

El desarrollo de la investigación se apoyará en los principios de Design Science Research (DSR), metodología orientada a la creación y evaluación de artefactos tecnológicos para resolver problemas concretos (Hevner, A., March, S., Park, J., & Ram, S., 2004). En este caso, el artefacto corresponde a la arquitectura de integración, que estará conformada por el modelo de datos, la base de datos centralizada y la API REST. El proceso comprenderá el análisis del problema, el diseño de la solución, su implementación y finalmente su evaluación mediante pruebas de integración y rendimiento. Esto permitirá determinar si la solución desarrollada cumple con los requerimientos definidos para el proyecto y con los criterios establecidos en la hipótesis.

Para obtener la información necesaria se utilizarán como fuentes principales los conjuntos de datos generados por SI-01 y SI-02, la documentación técnica disponible del proyecto RISKTWIN y los requerimientos relacionados con IND-SIS-02 y SIS-API-01. También se considerará la información obtenida mediante reuniones de coordinación con los equipos responsables de estos componentes, principalmente para conocer las necesidades de intercambio y consumo de información. Como técnicas de recolección se emplearán la revisión documental, el análisis técnico de los conjuntos de datos, el levantamiento de requerimientos y las pruebas de integración. Para este proceso se utilizarán instrumentos como matrices de análisis de datos y requerimientos, documentación técnica y herramientas de prueba como Postman y JMeter.

En cuanto a la población y muestra, la población estará conformada por los registros de información generados por SI-01 y SI-02 dentro del proyecto RISKTWIN, además de los endpoints que formarán parte de la API REST. Debido a que se trata de una investigación de carácter tecnológico, no será necesario aplicar un muestreo probabilístico. Para las pruebas se utilizará la totalidad de los datos disponibles de SI-02 que sean proporcionados para la integración y se evaluará el conjunto de endpoints definidos para la API. El objetivo no será realizar una generalización estadística hacia una población externa, sino comprobar que la arquitectura funciona correctamente utilizando los datos e interfaces reales del proyecto.

Finalmente, los datos de SI-01 y SI-02 serán analizados y organizados antes de ser incorporados al modelo de datos común y almacenados en la base de datos centralizada. Una vez implementada la arquitectura, se realizarán pruebas de integración para verificar la comunicación entre la base de datos, la API REST y los componentes que consumirán la información. Durante estas pruebas se registrará el tiempo de respuesta de las consultas y se calculará la tasa de éxito como el porcentaje de solicitudes procesadas correctamente con respecto al total de solicitudes realizadas. Los resultados obtenidos serán comparados con los valores establecidos en la hipótesis, que plantea un tiempo de respuesta inferior a 500 milisegundos por consulta y una tasa de éxito superior al 90%. Finalmente, los resultados serán organizados mediante tablas y gráficos para determinar si la arquitectura desarrollada cumple con los criterios establecidos y permite integrar de manera adecuada la información generada por los componentes SI-01 y SI-02.

## Metodología de Desarrollo a Emplear

El desarrollo de la solución se realizará utilizando TOGAF (The Open Group Architecture Framework) de forma adaptada, metodología que fue seleccionada y justificada previamente en la sección 3.3 debido a que su Método de Desarrollo de Arquitectura (ADM) se adapta a las características del proyecto y al tamaño reducido del equipo de trabajo. Los dos autores de la investigación participarán en todas las fases del proceso y también estarán involucrados en las actividades de planificación y seguimiento del proyecto. Por su parte, los equipos responsables de SI-01, SI-02, IND-SIS-02 y SIS-API-01, participarán como referentes para la validación de los requerimientos y necesidades de integración de cada componente.

El proceso de desarrollo se organizará en cuatro fases principales, adaptadas del ADM de TOGAF. En la fase de Arquitectura de Negocio se analizarán los objetivos del proyecto RISKTWIN y los requerimientos de integración de SI-01, SI-02, IND-SIS-02 y SIS-API-01, con el propósito de determinar las necesidades y limitaciones técnicas del proyecto. Posteriormente, en la fase de Arquitectura de Datos se diseñará el modelo de datos integrado y se definirán las actividades de desarrollo y el trabajo que podrá realizarse durante cada iteración. Durante las iteraciones correspondientes a la fase de Arquitectura de Aplicaciones se llevará a cabo de manera progresiva el diseño, desarrollo, prueba y documentación de los diferentes elementos de la arquitectura. Finalmente, en la fase de Arquitectura Tecnológica se consolidarán los resultados obtenidos, se realizarán las pruebas de integración finales y se completará la documentación de la solución.

Para el desarrollo se aplicarán prácticas ágiles complementarias dentro de las fases del ADM de TOGAF adaptado. Las historias de usuario permitirán representar las necesidades de los diferentes componentes de RISKTWIN y establecer los requerimientos que debe cumplir la arquitectura. También se utilizará el principio de diseño simple, buscando implementar únicamente las soluciones necesarias para cumplir con los objetivos definidos, evitando agregar funcionalidades que no formen parte del alcance del proyecto. La integración continua permitirá mantener el código en un repositorio compartido y facilitar la incorporación frecuente de los cambios realizados por los integrantes del equipo. Asimismo, se aplicará la refactorización durante el desarrollo para mejorar progresivamente la estructura del código, del modelo de datos y de los servicios de la API sin modificar su funcionamiento. Finalmente, se aplicará la propiedad colectiva del código, de manera que ambos integrantes puedan trabajar sobre cualquiera de los componentes de la solución y no existan módulos asignados exclusivamente a un solo desarrollador.

El proyecto se organizará en iteraciones de aproximadamente dos semanas, y cada iteración tendrá como resultado un avance funcional que pueda ser revisado y probado. Este esquema permitirá desarrollar progresivamente el modelo de datos, la base de datos y la API REST, incorporando también su documentación mediante OpenAPI/Swagger desde las primeras etapas. De esta manera, los posibles problemas de integración podrán identificarse y corregirse durante el desarrollo, en lugar de esperar hasta las pruebas finales para detectar errores que puedan afectar el cumplimiento de los objetivos del proyecto.

## Cronograma de actividades

El proyecto se ejecutará en un periodo de cuatro meses (dieciséis semanas), organizados en iteraciones de dos semanas conforme a las fases del ADM de TOGAF adaptado. El siguiente cronograma se resume las distribuciones de las actividades definidas en el alcance de este proyecto.

| Actividad | S1-2 | S3-4 | S5-6 | S7-8 | S9-10 | S11-12 | S13-14 | S15-16 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Análisis de las fuentes de datos (SI-01, SI-02) y definición de requisitos de integración | X | X | | | | | | |
| Diseño del modelo de datos integrado | | X | X | | | | | |
| Implementación de la base de datos centralizada | | | X | X | | | | |
| Diseño y documentación de la API REST con OpenAPI/Swagger | | | | X | X | | | |
| Pruebas de integración con datos de SI-02 | | | | | | X | X | X |
| Documentación final y elaboración del informe de tesis | | | | | | | X | X |

## Presupuesto y financiamiento

El desarrollo del proyecto será financiado en su totalidad con recursos propios de los dos autores de la investigación. No se contará con financiamiento externo ni con recursos económicos proporcionados por la Universidad de Guayaquil. Debido a que la mayor parte de las herramientas utilizadas para el desarrollo de la solución son gratuitas o de código abierto, los costos principales estarán relacionados con los recursos tecnológicos, el despliegue de pruebas, el material bibliográfico, la impresión y los traslados necesarios durante el desarrollo del proyecto.

| Rubro | Descripción | Costo estimado |
|---|---|--:|
| Recursos tecnológicos | Uso de laptops propias y costos asociados al acceso a internet durante el desarrollo y las pruebas de la API. | $10.00 |
| Software y herramientas | Motor de base de datos, entorno de desarrollo, herramientas para OpenAPI/Swagger y sistema de control de versiones, utilizando alternativas gratuitas o de código abierto. | $0.00 |
| Hosting y despliegue de pruebas | Uso de servicios de alojamiento en la nube para realizar el despliegue y las pruebas de la API REST. | $10.00 |
| Material bibliográfico | Consulta de artículos científicos y fuentes académicas mediante recursos institucionales y de acceso abierto. | $10.00 |
| Impresión y trámites administrativos | Impresión, copias y anillado de documentos relacionados con el anteproyecto y el desarrollo del trabajo. | $40.00 |
| Movilización | Traslados necesarios para reuniones presenciales y actividades relacionadas con el proyecto. | $20.00 |
| Imprevistos | Corresponde al 10% del subtotal de los rubros anteriores. | $9.00 |
| **TOTAL** | | **$99.00** |

## Beneficios esperados del proyecto

El desarrollo de la arquitectura de integración generará beneficios para los diferentes actores relacionados con el proyecto. En primer lugar, para RISKTWIN, permitirá mejorar el intercambio de información entre SI-01, SI-02 y los demás componentes del sistema, facilitando que el dashboard (IND-SIS-02) y la API integradora del gemelo digital multimodal (SIS-API-01) puedan acceder a información centralizada y actualizada.

Para la Universidad de Guayaquil, el proyecto representa un aporte a la investigación aplicada, ya que permite desarrollar una solución tecnológica sobre un caso real y, al mismo tiempo, facilita la coordinación entre diferentes trabajos de titulación que forman parte de una misma línea de investigación. Además, la arquitectura y la documentación generada podrán servir como referencia para futuros proyectos relacionados con la integración de datos y los gemelos digitales.

En cuanto al sector industrial, la solución propuesta puede servir como referencia para organizaciones que presenten problemas similares relacionados con la dispersión de información sobre riesgos. La arquitectura desarrollada podría ser adaptada a diferentes contextos de acuerdo con las necesidades y características de cada organización.

Finalmente, para los autores, el proyecto permitirá aplicar y fortalecer conocimientos relacionados con arquitectura de software, bases de datos, desarrollo de API REST, integración de sistemas y metodologías ágiles. Además, trabajar con datos y requerimientos de un proyecto real permitirá adquirir experiencia práctica en el desarrollo de soluciones de software orientadas a la gestión de información industrial.

## Derechos de Propiedad Intelectual

¿El proyecto genera productos protegibles por Propiedad Intelectual?

- [x] Software
- [ ] Modelo/algoritmo
- [x] Manual/documentación técnica
- [ ] No aplica

Los aspectos relacionados con la propiedad intelectual del presente trabajo de titulación se regirán por lo establecido en el (Código Orgánico de la Economía Social de los Conocimientos, Creatividad e Innovación [COESC], 2016), así como por la normativa y los reglamentos vigentes de la Universidad de Guayaquil en materia de propiedad intelectual y trabajos de titulación.

Los autores, Delgado Quiñonez Elian Adonis y Vargas Ordoñez Stalyn Gabriel, serán reconocidos como autores del presente trabajo de titulación. Los derechos relacionados con su uso, publicación y explotación se sujetarán a las disposiciones establecidas por la normativa nacional y por la Universidad de Guayaquil, incluyendo los procedimientos correspondientes para la cesión o autorización de derechos que sean requeridos al momento de la presentación de la tesis.

Debido a que esta investigación forma parte del proyecto RISKTWIN y utiliza información generada por los componentes SI-01 y SI-02, desarrollados por otros equipos de titulación, se reconocerá la participación y autoría correspondiente a cada componente. Los productos desarrollados específicamente en esta investigación, como el modelo de datos integrado, la base de datos y la API REST documentada, corresponderán al trabajo realizado por los autores dentro del alcance definido para esta tesis. Su utilización e integración con los demás componentes del proyecto se realizará de acuerdo con los acuerdos de colaboración y las disposiciones institucionales aplicables.

## Referencias Bibliográficas

Aheleroff, E., Xu, X., Zhong, R. Y., & Lu, Y. (2021). Digital Twin as a Service (DTaaS) in Industry 4.0: An architecture reference model. *Advanced Engineering Informatics, 47*, 101225. doi:10.1016/j.aei.2020.101225

Awouda, A., Traini, E., Bruno, G., & Chiabert, P. (2024). IoT-based framework for digital twins in the Industry 5.0 era. *Sensors, 24*(2), 594. doi:10.3390/s24020594

Barni, A., Fontana, A., Menato, S., & Sorlini, M. (2024). Data integration for digital twins in industrial automation: A systematic literature review. IEEE Access, 12, 139129–139153. doi:10.1109/ACCESS.2024.3465632

Bhatia, M., & Sood, S. K. (2021). Quantum-inspired IoT-enabled digital twin framework for risk prediction and management. IEEE Transactions on Industrial Informatics, 17(11), 7723–7731. doi:10.1109/TII.2021.3053303

Bortolini, M., Faccio, M., Gamberi, M., & Pilati, F. (2021). Multi-modal data fusion architecture for real-time digital twins in manufacturing systems. Computers & Industrial Engineering, 156, 107222. doi:10.1016/j.cie.2021.107222

Broo, D. G., & Schooling, J. (2023). Digital twins' maturity: The need for interoperability. IEEE Systems Journal, 18(1), 713–724. doi:10.1109/JSYST.2023.3338521

Eneyew, D. D., Capretz, M. A. M., & Bitsuamlak, G. (2022). Toward smart-building digital twins: BIM and IoT data integration. IEEE Access, 10, 130420–130433. doi:10.1109/ACCESS.2022.3229370

Gattullo, M., Scurati, G. W., Mourtzis, D., & Uva, A. E. (2022). Industrial digital twin visualization architectures: A review of standards and web-based approaches. Journal of Industrial Information Integration, 26, 100318. doi:10.1016/j.jii.2021.100318

Haag, S., & Anderl, R. (2021). Digital Twin – Proof of concept showing connectivity vs. interoperability in Industry 4.0. Manufacturing Letters, 28, 56–59. doi:10.1016/j.mfglet.2021.04.004

Jiang, Y., Liu, X., & Wang, L. (2024). Digital twin simulation and implementation in safety risk management process: A systematic literature review. IEEE Access, 12, 195671–195695. doi:10.1109/ACCESS.2024.3519704

Kousi, N., Gkournelos, C., Aivaliotis, S., Giannoulis, C., Michalos, G., & Makris, S. (2021). Digital twin for dynamic risk evaluation in human-robot collaborative workstations. CIRP Annals - Manufacturing Technology, 70(1), 341–344. doi:10.1016/j.cirp.2021.04.084

Leng, J., Wang, D., Shen, W., Li, X., Liu, Q., & Chen, X. (2021). Digital twin-driven manufacturing cyber-physical system for parallel controlling of smart workshop. Journal of Ambient Intelligence and Humanized Computing, 12(3), 3625–3638. doi:10.1007/s12652-020-02647-8

Liu, Z., Meyendorf, N., & Mrad, N. (2022). The role of data fusion in predictive maintenance and digital twins for structural health monitoring. Sensors, 22(7), 2545. doi:10.3390/s22072545

Lu, Y., Liu, C., Wang, K. I. K., Huang, H., & Xu, X. (2021). Digital Twin-driven smart manufacturing: Connotation, reference model, and research agenda. Robotics and Computer-Integrated Manufacturing, 61, 101837. doi:10.1016/j.rcim.2019.101837

Nativi, S., Mazzetti, P., & Craglia, M. (2021). Digital Ecosystems for Digital Twins: System-of-Systems interoperability patterns. Environmental Modelling & Software, 144, 105172. doi:10.1016/j.envsoft.2021.105172

Peruzzi, L., Stazi, F., & Bonechi, S. (2023). RESTful microservices architecture for real-time heterogeneous data collection in industrial digital twins. ACM Transactions on Internet Technology, 23(4), 1–24. doi:10.1145/3597426

Redelinghuys, A. J. H., Basson, A. H., & Kruger, K. (2021). A six-layer architecture for Digital Twins with RESTful API integration in Industry 4.0. Computers in Industry, 123, 103294. doi:10.1016/j.compind.2020.103294

Sepúlveda, A., Errandonea, I., & Beltrán, S. (2022). An interoperable digital twin with the IEEE 1451 standards for real-time monitoring. Sensors, 22(19), 7558. doi:10.3390/s22197558

Serrano, M., & Torres, J. (2024). Scalable REST API design for multi-source data aggregation in industrial edge-cloud platforms. IEEE Transactions on Services Computing, 17(2), 512–525. doi:10.1109/TSC.2023.3321104

Vachálek, J., Šišmišová, D., & Vaňo, R. (2021). Industrial data pipeline design for cloud-integrated digital twins. IEEE Access, 9, 78210–78222. doi:10.1109/ACCESS.2021.3083415

Zhang, L., Zhou, L., & Ren, L. (2023). Data-driven industrial safety assessment using Digital Twins and machine learning: A review. Computers & Industrial Engineering, 178, 109120. doi:10.1016/j.cie.2023.109120

Código Orgánico de la Economía Social de los Conocimientos, Creatividad e Innovación [COESC]. (2016). Registro Oficial Suplemento No. 899, 9 de diciembre de 2016.

Conde, J., Munoz-Arcentales, A., Alonso, Á., López-Pernas, S., & Salvachúa, J. (2022). Modeling digital twin data and architecture: A building guide with FIWARE as enabling technology. IEEE Internet Computing, 26(3), 7–14. doi:10.1109/MIC.2021.3056923

Document360. (20 de febrero de 2026). ¿Qué es la API abierta? Ventajas, desventajas y ejemplos. Obtenido de https://document360.com/es/blog/api-abiertas/

Hevner, A., March, S., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly.

IBM. (28 de mayo de 2026). ¿Qué es la arquitectura de datos? Obtenido de https://www.ibm.com/es-es/think/topics/data-architecture

Inesdi Digital Business School. (17 de febrero de 2025). Arquitectura de software: definición y tipos principales. Obtenido de https://www.inesdi.com/blog/arquitectura-de-software-5-patrones-

Instituto Tecnológico de Informática [ITI]. (31 de octubre de 2023). Gemelos digitales en la transición a la Industria 4.0. Obtenido de https://www.iti.es/proyectosidi/proyecto-gemelos-digitales-industria-4-0/

OpenAPI Initiative. (2017). OpenAPI Specification (versión 3.0.0). Obtenido de https://www.openapis.org/

Picone, M., Turazza, F., Martinelli, M., & Mamei, M. (2026). Digital twins & ZeroConf AI: Structuring automated intelligent pipelines for industrial applications. Recuperado el 18 de Agosto de 2026, de arXiv: https://arxiv.org/abs/2602.04385

Primicias. (30 de octubre de 2023). Manufactura y comercio, los sectores con más accidentes laborale. Recuperado el 18 de agosto de 2026, de Primicias: https://www.primicias.ec/noticias/economia/accidentes-laborales-manufacturera-comercio-iess/

Robles, J., Martín, C., & Díaz, M. (2023). OpenTwins: An open-source framework for the development of next-gen compositional digital twins. Computers in Industry, 152, 104007. doi:10.1016/j.compind.2023.104007

Rodríguez-Alonso, C., Pena-Regueiro, I., & García, Ó. (2024). Digital twin platform for water treatment plants using microservices architecture. Sensors, 24(5), 1568. doi:10.3390/s24051568

SAP. (2026). Integración de datos: qué es, cómo funciona, tipos y tendencias modernas. Obtenido de https://www.sap.com/latinamerica/products/technology-platform/what-is-enterprise-integration/data-integration.html

Tagline Soluciones Empresariales. (21 de enero de 2026). Accidentes laborales en Ecuador 2026: Guía de reporte, IESS y multas. Recuperado el 18 de agosto de 2026, de Tagline Soluciones Empresariales: https://tagline-soluciones.com/accidentes-laborales/

Tan, Y., Hofmeister, M., Phua, S., Brownbridge, G., Rustagi, K., Akroyd, J., . . . Kraft, M. (2025). Beyond connected digital twins – Can digital twins really deliver sustainable cities? Sustainable Cities and Society, 131, 106596. Recuperado el 18 de Agosto de 2026, de https://www.sciencedirect.com/science/article/pii/S2210670725004706

Tao, F., Sun, X., Cheng, J., Zhu, Y., Liu, W., Wang, Y., . . . Jin, X. (2024). makeTwin: A reference architecture for digital twin software platform. Chinese Journal of Aeronautics, 37(1), 1–18. doi:10.1016/j.cja.2023.05.002

---

## Rúbrica de Evaluación

> **Nota:** esta sección corresponde a páginas escaneadas con anotaciones manuscritas; la transcripción es aproximada.

### Anexo I. Formato de evaluación de la propuesta de trabajo de integración curricular

- **Nombre de la propuesta:** Arquitectura de software para la integración de datos fragmentados de riesgo industrial en un gemelo digital multimodal en la Universidad de Guayaquil
- **Estudiantes:** Delgado Quiñonez Elian Adonis; Vargas Ordoñez Stalyn Gabriel
- **Facultad:** Ingeniería Industrial
- **Carrera:** Ingeniería en Sistemas de la Información
- **Línea de investigación:** Ciencias básicas, bioconocimiento y desarrollo industrial
- **Sub-línea de investigación:** Procesos computacionales en sus diferentes aplicaciones, analítica y modelación de datos
- **Fecha de presentación / evaluación:** 26/08/2026
- **Resultado:** ☒ Aprobado con observaciones
- **Firma:** Ing. Manuel Samaniego Zamora, MBA, Decano de la Facultad

**Observaciones manuscritas:**

- Modificar Marco Teórico
- Metodología de Diagnóstico (lectura incierta)
- Incluir DOI en Referencias Bibliográficas
- Corregir Objetivo General y Específicos
- Cronograma

### Rúbrica de evaluación (notas)

| Criterio | Nota evaluador | Nota máxima |
|---|:-:|:-:|
| Planteamiento y formulación del problema; Innovación | 1 | 1 |
| Alcance; Justificación | 0.5 | 1 |
| Objetivos (General y Específicos) coherentes | 0.5 | 1 |
| Marco Teórico; Marco Metodológico; Referencias Bibliográficas | 0.5 | 1 |
| Metodología de Desarrollo | 0.5 | 1 |
| Cronograma; Presupuesto | 1 | 1 |
| Manejo claro de las ideas; Beneficios esperados del proyecto | 1 | 1 |
| Claridad y coherencia en la redacción | 1 | 1 |
| Referentes teóricos sustentados | 1 | 1 |
| Argumentos para una propuesta | 1 | 1 |
| **NOTA SOBRE 10** | **8** | **10** |

### Anexo C. Rúbrica de evaluación para proyectos grupales de integración curricular

| # | Aspecto evaluado | Resultado |
|---|---|---|
| 1 | Tema del proyecto: describe un tema con problemática de estudio, ajustado a la línea de investigación de la Carrera y a la pirámide de investigación de la Facultad | Cumple |
| 2 | Definición del problema: problema complejo o con múltiples abordajes | Cumple |
| 3 | División de tareas: plan de trabajo detallado con hitos y plazos | Cumple |
| 4 | Desarrollo de objetivos: objetivos con enfoques específicos | Cumple |
| 5 | Descripción de propiedad intelectual | Cumple |

Firmantes: Delgado Quiñonez Elian Adonis (C.I. 0850150319); Vargas Ordoñez Stalyn Gabriel (C.I. 0932039878); LSI. García Plúa Juan Carlos, MSIG; LSI. Lino Castillo Katty Nancy, MSIG.
