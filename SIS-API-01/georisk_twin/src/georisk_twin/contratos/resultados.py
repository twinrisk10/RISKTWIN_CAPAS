"""BORRADOR de contratos de salida de URB-04 y URB-05.

Se construyen a partir de lo que cada equipo declara en la matriz de interfaces.
Deben ser confirmados por sus responsables antes de usarse.
"""

from typing import Optional

from pydantic import AliasChoices, Field

from .entidades import ContratoBase, IdStr, Normalizado


class ResultadoEscenario(ContratoBase):
    """Salida de URB-05 por tramo y escenario."""

    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id"))
    escenario_id: IdStr = Field(validation_alias=AliasChoices("escenario_id", "escenario:id"))
    volumen_simulado: float = Field(ge=0, description="vehículos/hora")
    tiempo_espera_promedio: float = Field(ge=0, description="segundos")
    nuevo_nivel_criticidad: Normalizado


class ResultadoPrediccion(ContratoBase):
    """Salida de URB-04. Tipos de `nivel_riesgo` y `prediccion` por confirmar."""

    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id", "id"))
    nivel_riesgo: Optional[str] = None
    cluster_features: Optional[dict[str, float]] = None
    prediccion: Optional[float] = None
