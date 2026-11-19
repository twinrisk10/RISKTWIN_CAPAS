"""Modelos de respuesta de la API (GeoJSON y detalle H-E-V)."""

from typing import Literal, Optional

from pydantic import Field

from .entidades import ContratoBase, Geometria, IdStr, Normalizado, Observacion, Zona
from .enums import Dominio, TipoZona
from .hev import IndicadorHEV


class PropiedadesZona(ContratoBase):
    zona_id: IdStr
    nombre: Optional[str] = None
    tipo: TipoZona
    dominio: Dominio
    peligrosidad: Optional[Normalizado] = None
    exposicion: Optional[Normalizado] = None
    vulnerabilidad: Optional[Normalizado] = None
    criticidad: Optional[Normalizado] = None
    sintetico: bool = False


class FeatureZona(ContratoBase):
    type: Literal["Feature"] = "Feature"
    id: IdStr
    geometry: Geometria
    properties: PropiedadesZona


class ColeccionZonas(ContratoBase):
    """FeatureCollection GeoJSON: insumo del mapa de zonas críticas (IND-SIS-02)."""

    type: Literal["FeatureCollection"] = "FeatureCollection"
    total: int
    features: list[FeatureZona]


class DetalleHEV(ContratoBase):
    """Detalle H-E-V de una zona: insumo del wireframe de detalle (IND-SIS-02)."""

    zona: Zona
    indicador: IndicadorHEV
    observaciones: list[Observacion]


class LoteObservaciones(ContratoBase):
    observaciones: list[Observacion] = Field(min_length=1, max_length=1000)


class ResultadoCarga(ContratoBase):
    aceptadas: int
    zonas_afectadas: list[str]
