"""Lógica de la librería (sin dependencia de FastAPI).

IMPORTANTE: `resumen_hev` usa una media simple como método de REFERENCIA para poder probar
el flujo de extremo a extremo. NO reemplaza el índice de URB-03: cuando URB-03 entregue su
cálculo se registra como proceso y esta función deja de ser la fuente de `criticidad`.
"""

from datetime import datetime, timezone

from .contratos import Dimension, IndicadorHEV, Observacion
from .errores import ConflictoContrato, IdDuplicado
from .repositorio import Repositorio

METODO_REFERENCIA = "media_simple_referencia (no reemplaza URB-03)"


def ultimas_por_variable(observaciones: list[Observacion]) -> list[Observacion]:
    """Se queda con la observación más reciente de cada variable."""
    ultimas: dict[str, Observacion] = {}
    for o in observaciones:
        actual = ultimas.get(o.variable)
        if actual is None or o.fecha_captura >= actual.fecha_captura:
            ultimas[o.variable] = o
    return sorted(ultimas.values(), key=lambda o: o.variable)


def _media(valores: list[float]):
    return round(sum(valores) / len(valores), 6) if valores else None


def resumen_hev(repo: Repositorio, zona_id: str) -> IndicadorHEV:
    zona = repo.obtener_zona(zona_id)
    usadas = ultimas_por_variable(repo.observaciones_de_zona(zona_id))

    por_dimension: dict[Dimension, list[float]] = {d: [] for d in Dimension}
    for o in usadas:
        if o.valor_normalizado is not None:
            por_dimension[o.dimension].append(o.valor_normalizado)

    h = _media(por_dimension[Dimension.H])
    e = _media(por_dimension[Dimension.E])
    v = _media(por_dimension[Dimension.V])
    criticidad = _media([h, e, v]) if None not in (h, e, v) else None

    return IndicadorHEV(
        zona_id=zona_id,
        peligrosidad=h,
        exposicion=e,
        vulnerabilidad=v,
        criticidad=criticidad,
        metodo=METODO_REFERENCIA,
        n_variables=len(usadas),
        calculado_en=datetime.now(timezone.utc),
        sintetico=zona.sintetico,
    )


def registrar_observaciones(repo: Repositorio, observaciones: list[Observacion]) -> int:
    """Valida TODO el lote contra el catálogo y las zonas; solo si todo es válido, lo guarda."""
    vistos: set[str] = set()
    for o in observaciones:
        zona = repo.obtener_zona(o.zona_id)
        variable = repo.obtener_variable(o.variable)
        if variable.dimension != o.dimension:
            raise ConflictoContrato(
                f"la variable '{o.variable}' pertenece a la dimensión {variable.dimension.value}, "
                f"no a {o.dimension.value}"
            )
        if variable.dominio != zona.dominio:
            raise ConflictoContrato(
                f"la variable '{o.variable}' es del dominio {variable.dominio.value} "
                f"y la zona '{zona.zona_id}' es {zona.dominio.value}"
            )
        if o.observacion_id in vistos or repo.existe_observacion(o.observacion_id):
            raise IdDuplicado(f"la observación '{o.observacion_id}' ya existe")
        vistos.add(o.observacion_id)

    for o in observaciones:
        repo.agregar_observacion(o)
    return len(observaciones)
