"""Contrato del indicador H-E-V por zona."""

from typing import Annotated, Optional

from pydantic import AliasChoices, AwareDatetime, Field

from ..convenciones import VERSION_CONTRATO
from .entidades import ContratoBase, IdStr, Normalizado


class IndicadorHEV(ContratoBase):
    """Resumen H-E-V de una zona.

    Los nombres de campo (`peligrosidad`, `exposicion`, `vulnerabilidad`, `criticidad`) siguen
    el vocabulario de URB-03. El valor de `criticidad` definitivo lo calcula URB-03; aquí puede
    venir de un método de referencia (ver `metodo`).
    """

    zona_id: IdStr = Field(validation_alias=AliasChoices("zona_id", "tramo_id"))
    peligrosidad: Optional[Normalizado] = None
    exposicion: Optional[Normalizado] = None
    vulnerabilidad: Optional[Normalizado] = None
    criticidad: Optional[Normalizado] = None
    metodo: str = Field(min_length=1, max_length=120)
    n_variables: Annotated[int, Field(ge=0)] = 0
    version_contrato: str = VERSION_CONTRATO
    calculado_en: AwareDatetime
    sintetico: bool = False
