**BORRADOR: DATOS NECESARIOS PARA REALIZAR UN MODELO LLM PARA LA PREDICCIÓN DE INDICADORES DE RIESGO URBANO**



Un modelo basado en LLM aplicado a la predicción de indicadores de riesgo urbano debe recopilar, integrar y procesar información territorial, demográfica, ambiental y climáticas, movilidad y transporte, socioeconómica y seguridad ciudadana. De esta manera, podemos construir un sistema que analice los datos históricos y actuales con el fin de identificar los patrones, estimar los niveles de riesgo, anticipar posibles eventos y generar alertar para la toma de decisiones de autoridades municipales.



Para una predicción de las siguientes variables: accidentes, delitos e inundaciones, el componente principal no debe basarse solamente en LLM, sino en una **arquitectura híbrida** donde los modelos predictivos -*Random Forest, XGBoost, GCN y GraphSAGE*- realizan las predicciones y la integración con LLM actúa como la interfaz explicativa para interpretar resultados, análisis contextual y generación de alertas. 



La **recolección de datos** tenemos con fuente de información: INAMHI, Segura EP, Municipio de Guayaquil, INEC, ATM, Google Traffic, Policía Nacional, ECU911 y GIS. Con esta información, el modelo se construirá inicialmente con accidentes ATM georreferenciados, delitos ECU911 o policía nacional, densidad poblacional del INEC, análisis y representación territorial con GIS  y precipitación INAMHI.



**TIPOS DE DATOS NECESARIOS**

|**Tipo o Dimensión**|**Descripción**|**Información requerida**|
|-|-|-|
|Territoriales|Identificar dónde se producen los riesgos y cómo se distribuyen en el territorio|- Coordenadas geográficas (latitud y longitud)<br />- Parroquias y sectores<br />- Uso del suelo<br />- Densidad urbana<br />- Pendientes y elevación del terreno<br />- Zonas vulnerables<br />- Cartografía y mapas catastrales|
|Demográficos|Determinar la población expuesta a diferentes amenazas|- Población total por sector<br />- Densidad poblacional<br />- Distribución por edad<br />- Población (infantil y adulta)<br />- Personas con discapacidad|
|Ambientales y climáticas|Anticipar las amenazas naturales y ambientales|- Precipitaciones y acumulación de lluvia<br />- Inundaciones registradas<br />- Deslizamientos de tierra<br />- Sequías<br />- Riesgo sísmico<br />- Cobertura vegetal|
|Movilidad y transporte|Reconocer los riesgos que se relacionan con la circulación y la conectividad urbana|- Accidentes de tránsito<br />- Ubicación de puntos críticos<br />- Flujo vehicular y peatonal<br />- Señalización vial<br />- Transporte público|
|Socioeconómicos|Identificar las condiciones sociales que incrementan las vulnerabilidad urbana|- Desempleo<br />- Nivel educativo<br />- Condiciones de vivienda<br />- Desigualdad territorial<br />- Asentamientos informales|
|Seguridad ciudadana|Identificar los patrones territoriales y temporales de seguridad|- Robos y hurtos<br />- Asaltos<br />- Homicidios<br />- Vandalismo<br />- Incidentes reportados<br />- Ubicación de zonas de mayor incidencia|



Estos datos deben relacionarse con **variables objetivo** que representen los riesgos que deseamos anticipar. Como recomendación se deben seleccionar **entre 2 y 3 indicadores prioritarios**, desarrollar los modelos específicos y finalmente integrarlos en una plataforma. Los datos multimodales que se recomiendan se agrupan en **4 dimensiones**:

1. Datos geoespaciales: latitud, longitud, segmento vial, parroquia, uso de suelo, distancia (a intersecciones, escuela y/o hospitales).
2. Datos contextuales: densidad poblacional, estado de vías, índices socioeconómicos, actividad comercial, iluminación pública.
3. Datos de grafos: conectividad vial, centralidad de nodos, grado de intersección, centralidad de intermediación
4. Datos de eventos: accidentes, robos, sicariatos, inundaciones.



Por ejemplo, entre los datos fundamentales que debemos aplicar en 3 principales indicadores (accidentes viales, seguridad urbana e inundaciones) son la(s) variable(s) objetivo(s), categorías (variables predictivas), y datos requeridos (atributos):

&#x09;a.  Accidentes viales: 

|**Variable objetivo:**|Cantidad, severidad y tipo de accidente|
|-|-|
|**Categorías**|**Datos Requeridos**|
|Temporal - espacial|Fecha, hora, latitud, longitud, segmento vial|
|Tráfico vehicular|Tipo de vehículo, volumen vehicular y velocidad promedio|
|Infraestructura|Número de carriles, intersecciones y semáforos|
|Climáticas|Lluvia, temperatura, visibilidad|





&#x09;b. Seguridad urbana: robos, sicariatos y delitos 

|**Variable objetivo:**|Cantidad de delitos por zona, tasa de criminalidad y nivel de riesgo de seguridad|
|-|-|
|**Categorías**|**Datos Requeridos**|
|Temporal|Fecha y hora del incidente|
|Geográfico|Coordenadas del evento|
|Infraestructura|Iluminación pública, señalización|
|Social|Densidad poblacional|





&#x09;c. Inundaciones

|**Variable objetivo:**|Probabilidad de inundación y nivel de afectación|
|-|-|
|**Categorías**|**Datos Requeridos**|
|Hidrológica|Intensidad de lluvia|
|Geográfica|Elevación, cobertura del suelo|
|Topografía|Pendiente del terreno|
|Climáticas|Pronóstico meteorológico|





**ESTRUCTURA DE LA BASE DE DATOS**



La construcción de una base de datos integrada con información espacial y temporal: 

a. Campo: id, fecha, hora, parroquia, sector, latitud, longitud, población, precipitación, delitos, accidentes, inundaciones, nivel de riesgo

b. Tipo de dato: fecha, hora, texto, entero, decimal

c. Descripción: identificador único, fecha registrada, hora del evento, parroquia, barrio o sector, coordenada geográfica, lluvia registrada, accidentes registrado, evento de inundación, bajo, medio, etc.



Por ejemplo: Base de datos para el entrenamiento del modelo

|Fecha|Sector|Lluvia (mm)|Población|Inundación|Nivel de Riesgo|
|-|-|-|-|-|-|
|1/01/2025|Las Orquídeas|15|2050|3|Alto|
|5/10/2025|Vía Perimetral|10|1402|5|Alto|

Nota: El uso de tablas independientes deben estar relacionadas por fecha, ubicación e indicador. Es importante resaltar que las variables más importantes a considerar son fecha y hora del evento, ubicación geográfica, tipo de incidente, nivel de riesgo (severidad), registro histórico.



**INTEGRACIÓN CON LLM**

La aplicación de LLM nos permite interpretar los resultados y generar informes, sin embargo, no debe inventar probabilidades ni sustituir al modelo estadístico. Los datos necesarios en el LLM para entrenar y evaluar el modelo que necesitamos:

1. **Variables objetivo.** Son los resultados reales que deseamos predecir.
2. **Variables predictivas.** Condiciones que influyen en la ocurrencia de los eventos.
3. **Etiquetas.** Clasificación de los eventos según el nivel de riesgo
4. **Metadatos.** Procedencia, unidad de medida y calidad de cada variable



**NO OLVIDAR:** evitar los sesgos territoriales y no confundir la ausencia de registros con la ausencia de riesgo.



Ejemplos de variables: segmento vial, puntuación de riesgo (risk score), cluster, accidentes, precipitación, densidad poblacional, robos, inundaciones.



REQUERIMIENTOS EN EL PROYECTO: 

1. Los formatos pueden ser CSV, XLS o JSON.
2. Fuentes confiables con registros históricos: un mínimo de 3 años, con información basada en la cobertura territorial, geográfica y temporal.
3. Variables o indicadores relevantes
4. Almacenamiento en PostgreSQL o un repositorio de datos.
5. Dashboard geográfico

