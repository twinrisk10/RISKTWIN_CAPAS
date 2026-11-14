"""Contratos de datos del gemelo digital RISKTWIN (versión ejecutable de COMUN/contrato_hev_v1.json)."""
from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

VERSION_CONTRATO = "1.0.0"
PATRON_ZONA = r"^(PER|IND)-Z\d{2}$"

Riesgo = Literal["accidentes_viales", "seguridad_urbana", "inundaciones"]
RiesgoEvento = Literal["accidentes_viales", "seguridad_urbana", "inundaciones", "industrial"]
Componente = Literal["H", "E", "V"]
TipoDato = Literal["real", "derivado_real", "proxy", "sintetico", "pendiente"]
Nivel = Literal["bajo", "medio", "alto", "critico"]
Agregacion = Literal["aditiva", "multiplicativa"]


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Zona(_Base):
    """Unidad espacial común (corredor Perimetral PER-Z## o planta industrial IND-Z##)."""
    id_zona: str = Field(pattern=PATRON_ZONA, examples=["PER-Z04"])
    nombre: str = Field(min_length=1)
    area_km2: float = Field(ge=0)
    longitud_eje_km: Optional[float] = Field(default=None, ge=0)
    centroide_lat: float = Field(ge=-90, le=90)
    centroide_lon: float = Field(ge=-180, le=180)


class Evento(_Base):
    """Evento georreferenciado (siniestro, homicidio, anegamiento, incidente industrial)."""
    id_evento: str = Field(min_length=1, examples=["ATM00001012024"])
    riesgo: RiesgoEvento
    id_zona: str = Field(pattern=PATRON_ZONA)
    fecha_hora: datetime
    lat: Optional[float] = Field(default=None, ge=-90, le=90)
    lon: Optional[float] = Field(default=None, ge=-180, le=180)
    subtipo: Optional[str] = None
    severidad: int = Field(ge=1, le=4, description="1 sin víctimas/leve · 2 lesionados/moderada · 3 grave · 4 fallecidos/crítica")
    lesionados: int = Field(default=0, ge=0)
    fallecidos: int = Field(default=0, ge=0)
    fuente: str = Field(min_length=1)
    tipo_dato: Literal["real", "sintetico"]


class Observacion(_Base):
    """Valor de una variable H–E–V para una zona y un periodo (URB-01 produce, URB-03 agrega, la API expone)."""
    id_zona: str = Field(pattern=PATRON_ZONA)
    periodo: str = Field(min_length=1, examples=["2024-01/2026-05", "piloto"])
    id_variable: str = Field(pattern=r"^(ACC|SEG|INU)_[HEV]_[A-Za-z0-9_]+$", examples=["ACC_H_tasa_siniestros_km"])
    riesgo: Riesgo
    componente: Componente
    valor: Optional[float] = None
    unidad: str
    tipo_dato: TipoDato
    fuente: str

    @model_validator(mode="after")
    def _coherencia(self):
        pref = {"ACC": "accidentes_viales", "SEG": "seguridad_urbana", "INU": "inundaciones"}[self.id_variable[:3]]
        if pref != self.riesgo:
            raise ValueError(f"id_variable {self.id_variable} no corresponde al riesgo {self.riesgo}")
        if self.id_variable[4] != self.componente:
            raise ValueError(f"id_variable {self.id_variable} no corresponde al componente {self.componente}")
        if self.valor is None and self.tipo_dato != "pendiente":
            raise ValueError("valor vacío solo se admite con tipo_dato = 'pendiente'")
        return self


class IndicadorZona(_Base):
    id_zona: str = Field(pattern=PATRON_ZONA)
    periodo: str
    riesgo: Literal["accidentes_viales", "seguridad_urbana", "inundaciones", "global"]
    H: Optional[float] = Field(default=None, ge=0, le=1)
    E: Optional[float] = Field(default=None, ge=0, le=1)
    V: Optional[float] = Field(default=None, ge=0, le=1)
    indice_criticidad: float = Field(ge=0, le=1)
    metodo_agregacion: Agregacion
    nivel: Nivel
    tipo_dato: Literal["real", "derivado_real", "sintetico", "mixto"]


# --------- Solicitudes y respuestas de la API ---------
class Pesos(_Base):
    w_H: float = Field(default=1 / 3, gt=0)
    w_E: float = Field(default=1 / 3, gt=0)
    w_V: float = Field(default=1 / 3, gt=0)
    alpha: dict[Riesgo, float] = Field(default_factory=lambda: {"accidentes_viales": 1 / 3, "seguridad_urbana": 1 / 3, "inundaciones": 1 / 3})


class SolicitudIndicadores(_Base):
    observaciones: list[Observacion] = Field(min_length=1)
    sentido_negativo: list[str] = Field(default_factory=lambda: ["INU_H_elevacion_media_m"],
                                        description="Variables donde un valor mayor reduce el riesgo")
    agregacion: Agregacion = "aditiva"
    pesos: Pesos = Field(default_factory=Pesos)


class SolicitudPriorizar(_Base):
    indicadores: list[IndicadorZona] = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=100)


class ErrorFila(_Base):
    indice: int
    campo: str
    detalle: str


class ResultadoValidacion(_Base):
    version_contrato: str = VERSION_CONTRATO
    total: int
    validos: int
    invalidos: int
    errores: list[ErrorFila]
    tipos_dato: dict[str, int]


class ZonaPriorizada(_Base):
    posicion: int
    id_zona: str
    indice_criticidad: float
    nivel: Nivel
    riesgo_dominante: str


class RespuestaPriorizar(_Base):
    version_contrato: str = VERSION_CONTRATO
    metodo_agregacion: str
    tipo_dato: str
    ranking: list[ZonaPriorizada]
    advertencia: Optional[str] = None
