"""Prueba funcional de extremo a extremo con datos SINTÉTICOS (entregable del 18/11).

Flujo: cargar sintéticos -> API -> zonas con H-E-V -> detalle -> carga de observaciones.
"""

import pytest
from fastapi.testclient import TestClient

from georisk_twin.api.app import crear_app
from georisk_twin.repositorio import RepositorioMemoria
from georisk_twin.servicios import resumen_hev
from georisk_twin.sinteticos import cargar_sinteticos

CAMPOS_HEV = ("peligrosidad", "exposicion", "vulnerabilidad", "criticidad")


@pytest.fixture()
def repo():
    r = RepositorioMemoria()
    cargar_sinteticos(r)
    return r


@pytest.fixture()
def cliente(repo):
    return TestClient(crear_app(repo))


def _obs_json(obs_id, variable, dimension, valor, normalizado, fecha="2026-12-01T00:00:00Z"):
    return {
        "observacion_id": obs_id, "zona_id": "T-001", "variable": variable,
        "dimension": dimension, "valor": valor, "unidad": "u",
        "valor_normalizado": normalizado, "fecha_captura": fecha,
        "fuente": "prueba", "version": "v0.1", "sintetico": True,
    }


def test_health(cliente):
    r = cliente.get("/health")
    assert r.status_code == 200 and r.json()["estado"] == "ok"


def test_listar_zonas_devuelve_geojson_con_hev(cliente):
    r = cliente.get("/v1/zonas")
    assert r.status_code == 200
    cuerpo = r.json()
    assert cuerpo["type"] == "FeatureCollection"
    assert cuerpo["total"] == 7  # 5 tramos urbanos + 2 zonas industriales
    for f in cuerpo["features"]:
        assert f["type"] == "Feature"
        assert f["properties"]["sintetico"] is True
        for campo in CAMPOS_HEV:
            assert 0.0 <= f["properties"][campo] <= 1.0


def test_filtro_por_dominio(cliente):
    r = cliente.get("/v1/zonas", params={"dominio": "industrial"})
    assert r.json()["total"] == 2
    assert all(f["properties"]["dominio"] == "industrial" for f in r.json()["features"])


def test_detalle_hev_de_una_zona(cliente):
    r = cliente.get("/v1/zonas/T-001/hev")
    assert r.status_code == 200
    d = r.json()
    ind = d["indicador"]
    esperado = (ind["peligrosidad"] + ind["exposicion"] + ind["vulnerabilidad"]) / 3
    assert ind["criticidad"] == pytest.approx(esperado, abs=1e-5)
    assert {o["dimension"] for o in d["observaciones"]} == {"H", "E", "V"}
    assert d["zona"]["zona_id"] == "T-001"


def test_zona_inexistente_devuelve_404(cliente):
    r = cliente.get("/v1/zonas/NO-EXISTE/hev")
    assert r.status_code == 404
    assert r.json()["tipo_error"] == "ZonaNoEncontrada"


def test_carga_de_observaciones_actualiza_el_hev(cliente):
    lote = {"observaciones": [
        _obs_json("OBS-NUEVA-1", "H_vel_prom", "H", 80.0, 1.0),
        _obs_json("OBS-NUEVA-2", "H_conflictos_ped_veh", "H", 30.0, 1.0),
    ]}
    r = cliente.post("/v1/observaciones", json=lote)
    assert r.status_code == 201
    assert r.json() == {"aceptadas": 2, "zonas_afectadas": ["T-001"]}

    ind = cliente.get("/v1/zonas/T-001/hev").json()["indicador"]
    assert ind["peligrosidad"] == pytest.approx(1.0)


def test_carga_rechaza_dimension_incorrecta_y_no_guarda_nada(cliente, repo):
    lote = {"observaciones": [
        _obs_json("OBS-OK", "H_vel_prom", "H", 80.0, 1.0),
        _obs_json("OBS-MAL", "H_vel_prom", "E", 80.0, 1.0),  # H_vel_prom es de la dimensión H
    ]}
    r = cliente.post("/v1/observaciones", json=lote)
    assert r.status_code == 422
    assert not repo.existe_observacion("OBS-OK")  # el lote es atómico


def test_carga_rechaza_variable_de_otro_dominio(cliente):
    lote = {"observaciones": [_obs_json("OBS-X", "H_vel_vehiculo_planta", "H", 20.0, 0.5)]}
    assert cliente.post("/v1/observaciones", json=lote).status_code == 422


def test_carga_rechaza_variable_desconocida_y_duplicados(cliente):
    desconocida = {"observaciones": [_obs_json("OBS-Y", "NO_EXISTE", "H", 1.0, 0.1)]}
    assert cliente.post("/v1/observaciones", json=desconocida).status_code == 422

    ok = {"observaciones": [_obs_json("OBS-DUP", "H_vel_prom", "H", 40.0, 0.4)]}
    assert cliente.post("/v1/observaciones", json=ok).status_code == 201
    assert cliente.post("/v1/observaciones", json=ok).status_code == 409


def test_reproducibilidad_libreria_vs_api(repo, cliente):
    """Mismo resultado usando la librería directamente y a través de la API."""
    via_api = cliente.get("/v1/zonas/T-002/hev").json()["indicador"]
    via_lib = resumen_hev(repo, "T-002").model_dump()
    for campo in CAMPOS_HEV:
        assert via_lib[campo] == pytest.approx(via_api[campo])


def test_datos_sinteticos_son_reproducibles():
    a, b = RepositorioMemoria(), RepositorioMemoria()
    cargar_sinteticos(a, semilla=7)
    cargar_sinteticos(b, semilla=7)
    assert resumen_hev(a, "T-003").criticidad == resumen_hev(b, "T-003").criticidad
