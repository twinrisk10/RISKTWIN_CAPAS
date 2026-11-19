"""Contratos de datos v0: Zona, Evento, Observación y catálogo de variables.

Convenciones:
- `zona_id` es el identificador canónico. Para tramos urbanos coincide con el `tramo_id` de URB-01
  (se acepta `tramo_id` como alias de entrada).
- Geometrías en GeoJSON, WGS 84 (EPSG:4326).
- Fechas con zona horaria (se recomienda UTC).
- `valor_normalizado` en [0, 1], donde 1 = mayor contribución al riesgo.
"""

from datetime import date
from typing import Annotated, Literal, Optional

from pydantic import (
    AliasChoices,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    model_validator,
)

from ..convenciones import CRS_INTERCAMBIO, PATRON_ID
from .enums import Dimension, Dominio, TipoEvento, TipoZona

IdStr = Annotated[str, StringConstraints(pattern=PATRON_ID)]
Normalizado = Annotated[float, Field(ge=0.0, le=1.0)]


class ContratoBase(BaseModel):
    """Base de todos los contratos: no se aceptan campos desconocidos."""

    model_config = ConfigDict(extra="forbid")


# --------------------------------------------------------------------------- geometría
def _posiciones(coords):
    if isinstance(coords, (list, tuple)) and coords and isinstance(coords[0], (int, float)):
        yield coords
    elif isinstance(coords, (list, tuple)):
        for sub in coords:
            yield from _posiciones(sub)
    else:
        raise ValueError("coordenadas mal formadas")


class Geometria(ContratoBase):
    """Geometría GeoJSON en WGS 84."""

    type: Literal["Point", "LineString", "Polygon", "MultiLineString", "MultiPolygon"]
    coordinates: list

    @model_validator(mode="after")
    def _validar_wgs84(self) -> "Geometria":
        n = 0
        for pos in _posiciones(self.coordinates):
            if len(pos) < 2:
                raise ValueError("cada posición necesita [longitud, latitud]")
            lon, lat = pos[0], pos[1]
            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                raise ValueError(
                    f"posición fuera de rango para {CRS_INTERCAMBIO}: {list(pos[:2])}. "
                    "Si viene en EPSG:32717 (UTM), conviértala a WGS 84 antes de enviarla."
                )
            n += 1
        if n == 0:
            raise ValueError("geometría vacía")
        return self


# --------------------------------------------------------------------------- catálogo H-E-V
class VariableDefinicion(ContratoBase):
    """Definición de una variable del modelo H-E-V (catálogo que entregan SI-01 y URB-01)."""

    codigo: IdStr
    nombre: str = Field(min_length=1, max_length=120)
    dimension: Dimension
    dominio: Dominio
    unidad: str = Field(min_length=1, max_length=32)
    fuente: str = Field(min_length=1, max_length=120)
    descripcion: Optional[str] = None
    rango_min: Optional[float] = None
    rango_max: Optional[float] = None

    @model_validator(mode="after")
    def _rango(self) -> "VariableDefinicion":
        if (
            self.rango_min is not None
            and self.rango_max is not None
            and self.rango_min >= self.rango_max
        ):
            raise ValueError("rango_min debe ser menor que rango_max")
        return self


# --------------------------------------------------------------------------- zona
_DOMINIO_POR_TIPO = {
    TipoZona.TRAMO: Dominio.URBANO,
    TipoZona.INTERSECCION: Dominio.URBANO,
    TipoZona.ZONA_INDUSTRIAL: Dominio.INDUSTRIAL,
}


class Zona(ContratoBase):
    """Unidad espacial de análisis: tramo, intersección o zona industrial."""

    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id"))
    nombre: Optional[str] = Field(default=None, max_length=120)
    tipo: TipoZona
    dominio: Dominio
    geometria: Geometria
    crs: Literal["EPSG:4326"] = CRS_INTERCAMBIO
    fecha_captura: date
    fuente: str = Field(min_length=1, max_length=120)
    version: str = Field(min_length=1, max_length=32)
    sintetico: bool = False

    @model_validator(mode="after")
    def _coherencia_tipo_dominio(self) -> "Zona":
        if _DOMINIO_POR_TIPO[self.tipo] != self.dominio:
            raise ValueError(
                f"el tipo '{self.tipo.value}' es incompatible con el dominio '{self.dominio.value}'"
            )
        return self


# --------------------------------------------------------------------------- evento
class Evento(ContratoBase):
    """Incidente, casi accidente o condición insegura asociado a una zona (taxonomía de SI-02)."""

    evento_id: IdStr
    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id"))
    tipo: TipoEvento
    fecha_hora: AwareDatetime
    # Escala PROVISIONAL 1 (leve) a 5 (crítico). La definitiva depende de SI-02.
    severidad: Annotated[int, Field(ge=1, le=5)]
    descripcion: Optional[str] = Field(default=None, max_length=500)
    fuente: str = Field(min_length=1, max_length=120)
    version: str = Field(min_length=1, max_length=32)
    sintetico: bool = False


# --------------------------------------------------------------------------- observación
class Observacion(ContratoBase):
    """Valor de una variable H-E-V medido o calculado para una zona en un instante."""

    observacion_id: IdStr
    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id"))
    variable: IdStr
    dimension: Dimension
    valor: float
    unidad: str = Field(min_length=1, max_length=32)
    valor_normalizado: Optional[Normalizado] = None
    fecha_captura: AwareDatetime
    fuente: str = Field(min_length=1, max_length=120)
    version: str = Field(min_length=1, max_length=32)
    sintetico: bool = False
