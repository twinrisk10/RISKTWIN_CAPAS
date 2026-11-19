# georisk_twin

Núcleo compartido de software (**librería Python + API**) para integrar los subproductos del gemelo
digital multimodal urbano-industrial del FCI 46. Capa **SIS-API-01**.

> **Estado: v0.1.0, esqueleto inicial.** Trabaja con **datos sintéticos**. Los contratos son una
> **propuesta** que debe validarse con las demás capas (ver `docs/decisiones_pendientes.md`).

## Qué problema resuelve

Cada capa (SI-01, SI-02, IND-SIS-01/02, URB-01 a URB-05) produce su parte, pero no hay una estructura
común que defina cómo se conectan los datos. Este paquete ofrece:

- **Contratos de datos** (esquemas validados) para que todos hablen el mismo formato.
- **Librería** con la lógica de integración, utilizable en notebooks y scripts.
- **API** documentada (OpenAPI) que consume el dashboard.

No reemplaza el trabajo de ninguna tesis: les da un lugar común donde conectarse.

## Estructura

```
georisk_twin/
├── pyproject.toml
├── README.md
├── docs/
│   ├── contratos_hev.md            # campos de cada contrato
│   └── decisiones_pendientes.md    # qué confirmar con cada equipo
├── src/georisk_twin/
│   ├── convenciones.py             # CRS, patrón de identificadores, versión del contrato
│   ├── errores.py                  # errores de dominio -> códigos HTTP
│   ├── contratos/                  # Zona, Evento, Observación, H-E-V, respuestas
│   ├── repositorio.py              # almacenamiento (en memoria; luego PostGIS)
│   ├── servicios.py                # lógica: resumen H-E-V, carga validada
│   ├── sinteticos.py               # datos de prueba reproducibles
│   └── api/
│       ├── app.py                  # FastAPI: 3 endpoints + /health
│       └── main.py                 # entrada para uvicorn
└── tests/
    ├── test_contratos.py
    └── test_funcional_sintetico.py # prueba de extremo a extremo
```

## Instalación

Requiere Python 3.11 o superior.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

pip install -e ".[api,dev]"
```

Solo la librería (sin API): `pip install -e .`

## Ejecutar las pruebas

```bash
pytest -v
```

La prueba funcional (`tests/test_funcional_sintetico.py`) carga datos sintéticos, consulta la API,
carga observaciones nuevas y verifica que el H-E-V cambie, además de comparar el resultado de la
librería con el de la API.

## Ejecutar la API

```bash
uvicorn georisk_twin.api.main:app --reload
```

Abrir http://127.0.0.1:8000/docs para ver y probar los endpoints.

## Endpoints propuestos (v0)

| Método y ruta | Para qué sirve | Quién lo usa |
|---|---|---|
| `GET /v1/zonas?dominio=urbano\|industrial` | GeoJSON con H-E-V y criticidad por zona | Mapa de zonas críticas (IND-SIS-02) |
| `GET /v1/zonas/{zona_id}/hev` | Detalle H-E-V de una zona con sus observaciones | Detalle de zona (IND-SIS-02) |
| `POST /v1/observaciones` | Carga validada de observaciones (lote atómico) | URB-01, SI-02, IND-SIS-01 |
| `GET /health` | Estado del servicio | Operación |

Previstos para la siguiente versión: `POST /v1/zonas`, `POST /v1/eventos`, `GET /v1/variables`,
`POST /v1/procesos/{id}/ejecucion` (índice URB-03, IA URB-04, simulación URB-05).

## Uso como librería

```python
from georisk_twin.repositorio import RepositorioMemoria
from georisk_twin.sinteticos import cargar_sinteticos
from georisk_twin.servicios import resumen_hev

repo = RepositorioMemoria()
cargar_sinteticos(repo)

ind = resumen_hev(repo, "T-001")
print(ind.peligrosidad, ind.exposicion, ind.vulnerabilidad, ind.criticidad)
```

## Convenciones v0 (propuesta)

| Tema | Convención |
|---|---|
| Identificador de unidad espacial | `zona_id` (para tramos coincide con `tramo_id` de URB-01; `tramo_id` se acepta como alias) |
| Geometrías | GeoJSON en WGS 84 (EPSG:4326) en la API |
| Cálculos de distancia | EPSG:32717 (UTM 17S), el mismo de URB-01 y URB-02 |
| Fechas | ISO 8601 con zona horaria (UTC recomendado) |
| Valores normalizados | `valor_normalizado` en [0, 1]; **1 = mayor contribución al riesgo** |
| Identificadores | letras, números, `-` y `_`; sin espacios |
| Campos desconocidos | se rechazan |

## Limitaciones conocidas

- **Datos sintéticos**: coordenadas ilustrativas, catálogo de variables y valores inventados.
- **Criticidad de referencia**: `resumen_hev` usa una media simple solo para probar el flujo. El
  índice real lo calcula URB-03 y se integrará como proceso.
- **Almacenamiento en memoria**: se pierde al reiniciar. Se reemplazará por PostGIS.
- **Sin autenticación** todavía.
- **Adaptadores pendientes**: GraphML (URB-02), CSV/XLSX, GeoPackage/PostGIS (URB-01), JSON (URB-04).

## Próximos pasos

1. Validar contratos y convenciones con cada equipo.
2. Reemplazar el catálogo sintético por las variables de SI-01 y URB-01.
3. Adaptadores de ingesta reales.
4. Registro de procesos para URB-03, URB-04 y URB-05.
5. PostGIS, autenticación y Docker.
