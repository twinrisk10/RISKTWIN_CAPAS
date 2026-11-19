# Contratos de datos v0

Versión del contrato: `0.1.0`. Propuesta pendiente de validación con SI-01, SI-02, URB-01 a URB-05,
IND-SIS-01 e IND-SIS-02.

## Dimensiones H-E-V

| Código | Dimensión      |
| ------ | -------------- |
| `H`    | Peligrosidad   |
| `E`    | Exposición     |
| `V`    | Vulnerabilidad |

Cada **variable** pertenece a una sola dimensión y a un solo dominio (`urbano` o `industrial`).

## VariableDefinicion (catálogo)

| Campo                    | Tipo                    | Obligatorio | Descripción                             |
| ------------------------ | ----------------------- | ----------- | --------------------------------------- |
| `codigo`                 | texto (patrón de ID)    | Sí          | Código único, por ejemplo `H_vel_prom`  |
| `nombre`                 | texto                   | Sí          | Nombre legible                          |
| `dimension`              | `H`, `E` o `V`          | Sí          | Dimensión a la que aporta               |
| `dominio`                | `urbano` o `industrial` | Sí          | A qué tipo de zona aplica               |
| `unidad`                 | texto                   | Sí          | Unidad de medida                        |
| `fuente`                 | texto                   | Sí          | Origen del dato                         |
| `descripcion`            | texto                   | No          | Definición                              |
| `rango_min`, `rango_max` | número                  | No          | Rango de referencia (min menor que max) |

## Zona

| Campo                        | Tipo                                           | Obligatorio | Descripción                   |
| ---------------------------- | ---------------------------------------------- | ----------- | ----------------------------- |
| `zona_id` (alias `tramo_id`) | texto (patrón de ID)                           | Sí          | Identificador persistente     |
| `nombre`                     | texto                                          | No          |                               |
| `tipo`                       | `tramo`, `interseccion`, `zona_industrial`     | Sí          |                               |
| `dominio`                    | `urbano` o `industrial`                        | Sí          | Debe ser coherente con `tipo` |
| `geometria`                  | GeoJSON (Point, LineString, Polygon, Multi...) | Sí          | WGS 84, [longitud, latitud]   |
| `crs`                        | `EPSG:4326`                                    | No          | Fijo en v0                    |
| `fecha_captura`              | fecha                                          | Sí          |                               |
| `fuente`                     | texto                                          | Sí          |                               |
| `version`                    | texto                                          | Sí          |                               |
| `sintetico`                  | booleano                                       | No          | `true` en datos de prueba     |

## Evento

| Campo                            | Tipo                                                | Obligatorio | Descripción                                     |
| -------------------------------- | --------------------------------------------------- | ----------- | ----------------------------------------------- |
| `evento_id`                      | texto (patrón de ID)                                | Sí          |                                                 |
| `zona_id`                        | texto                                               | Sí          | Zona asociada                                   |
| `tipo`                           | `incidente`, `casi_accidente`, `condicion_insegura` | Sí          | **Provisional**: la taxonomía final es de SI-02 |
| `fecha_hora`                     | fecha y hora con zona horaria                       | Sí          |                                                 |
| `severidad`                      | entero de 1 a 5                                     | Sí          | **Provisional**: escala pendiente de SI-02      |
| `descripcion`                    | texto                                               | No          |                                                 |
| `fuente`, `version`, `sintetico` |                                                     |             | Igual que Zona                                  |

## Observacion

| Campo                            | Tipo                          | Obligatorio | Descripción                        |
| -------------------------------- | ----------------------------- | ----------- | ---------------------------------- |
| `observacion_id`                 | texto (patrón de ID)          | Sí          |                                    |
| `zona_id`                        | texto                         | Sí          |                                    |
| `variable`                       | texto                         | Sí          | Debe existir en el catálogo        |
| `dimension`                      | `H`, `E`, `V`                 | Sí          | Debe coincidir con la del catálogo |
| `valor`                          | número                        | Sí          | Valor en su unidad original        |
| `unidad`                         | texto                         | Sí          |                                    |
| `valor_normalizado`              | número entre 0 y 1            | No          | 1 = mayor contribución al riesgo   |
| `fecha_captura`                  | fecha y hora con zona horaria | Sí          |                                    |
| `fuente`, `version`, `sintetico` |                               |             |                                    |

Reglas de validación al cargar: la zona debe existir, la variable debe estar en el catálogo, la
dimensión debe coincidir, el dominio de la variable debe coincidir con el de la zona y el
`observacion_id` no puede repetirse. Si una observación del lote falla, **no se guarda ninguna**.

## IndicadorHEV

| Campo                                          | Tipo                | Descripción                                         |
| ---------------------------------------------- | ------------------- | --------------------------------------------------- |
| `zona_id`                                      | texto               |                                                     |
| `peligrosidad`, `exposicion`, `vulnerabilidad` | número 0 a 1 o nulo | Resumen por dimensión                               |
| `criticidad`                                   | número 0 a 1 o nulo | Nulo si falta alguna dimensión                      |
| `metodo`                                       | texto               | Cómo se calculó (en v0, media simple de referencia) |
| `n_variables`                                  | entero              | Variables usadas                                    |
| `version_contrato`                             | texto               |                                                     |
| `calculado_en`                                 | fecha y hora        |                                                     |

## Borradores de salida de URB-04 y URB-05

Basados en lo declarado en la matriz de interfaces; deben ser confirmados por sus responsables.

- `ResultadoEscenario` (URB-05): `zona_id` (alias `tramo_id`), `escenario_id` (alias `escenario:id`),
  `volumen_simulado` (veh/h), `tiempo_espera_promedio` (s), `nuevo_nivel_criticidad` (0 a 1).
- `ResultadoPrediccion` (URB-04): `zona_id` (alias `tramo_id`, `id`), `nivel_riesgo`,
  `cluster_features`, `prediccion`.
