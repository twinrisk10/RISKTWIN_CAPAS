"""Pruebas de los contratos de datos H-E-V, zona, evento y observación."""

from datetime import date, datetime, timezone

import pytest
from pydantic import ValidationError

from georisk_twin.contratos import (
    Dimension,
    Dominio,
    Evento,
    Geometria,
    Observacion,
    ResultadoEscenario,
    TipoEvento,
    TipoZona,
    VariableDefinicion,
    Zona,
)

GEOM = {"type": "LineString", "coordinates": [[-79.94, -2.25], [-79.93, -2.24]]}
UTC = timezone.utc


def _zona(**cambios):
    datos = dict(
        zona_id="T-001", tipo=TipoZona.TRAMO, dominio=Dominio.URBANO, geometria=GEOM,
        fecha_captura=date(2026, 11, 1), fuente="prueba", version="v0.1",
    )
    datos.update(cambios)
    return Zona(**datos)


def test_zona_valida_y_alias_tramo_id():
    assert _zona().zona_id == "T-001"
    datos = _zona().model_dump(by_alias=False)
    datos.pop("zona_id")
    assert Zona(tramo_id="T-777", **datos).zona_id == "T-777"


def test_zona_rechaza_coordenadas_utm():
    utm = {"type": "Point", "coordinates": [622000.0, 9757000.0]}
    with pytest.raises(ValidationError):
        Geometria(**utm)


def test_zona_rechaza_tipo_y_dominio_incoherentes():
    with pytest.raises(ValidationError):
        _zona(tipo=TipoZona.ZONA_INDUSTRIAL, dominio=Dominio.URBANO)


def test_id_con_espacios_se_rechaza():
    with pytest.raises(ValidationError):
        _zona(zona_id="T 001")


def test_zona_rechaza_campos_desconocidos():
    with pytest.raises(ValidationError):
        _zona(campo_inventado=1)


def _obs(**cambios):
    datos = dict(
        observacion_id="O-1", zona_id="T-001", variable="H_vel_prom", dimension=Dimension.H,
        valor=50.0, unidad="km/h", valor_normalizado=0.5,
        fecha_captura=datetime(2026, 11, 1, tzinfo=UTC), fuente="prueba", version="v0.1",
    )
    datos.update(cambios)
    return Observacion(**datos)


def test_observacion_valida():
    assert _obs().valor_normalizado == 0.5


def test_observacion_normalizado_fuera_de_rango():
    with pytest.raises(ValidationError):
        _obs(valor_normalizado=1.2)


def test_observacion_exige_zona_horaria():
    with pytest.raises(ValidationError):
        _obs(fecha_captura=datetime(2026, 11, 1))


def test_evento_severidad_y_zona_horaria():
    base = dict(
        evento_id="E-1", zona_id="T-001", tipo=TipoEvento.CASI_ACCIDENTE,
        fecha_hora=datetime(2026, 10, 1, tzinfo=UTC), severidad=3, fuente="prueba", version="v0.1",
    )
    assert Evento(**base).severidad == 3
    with pytest.raises(ValidationError):
        Evento(**{**base, "severidad": 9})
    with pytest.raises(ValidationError):
        Evento(**{**base, "fecha_hora": datetime(2026, 10, 1)})


def test_variable_rango_invalido():
    with pytest.raises(ValidationError):
        VariableDefinicion(
            codigo="X", nombre="x", dimension=Dimension.H, dominio=Dominio.URBANO,
            unidad="u", fuente="f", rango_min=10, rango_max=5,
        )


def test_resultado_urb05_acepta_nombres_de_la_matriz():
    r = ResultadoEscenario(**{
        "tramo_id": "T-001", "escenario:id": "ESC-BASE", "volumen_simulado": 900,
        "tiempo_espera_promedio": 35.5, "nuevo_nivel_criticidad": 0.4,
    })
    assert r.zona_id == "T-001" and r.escenario_id == "ESC-BASE"
