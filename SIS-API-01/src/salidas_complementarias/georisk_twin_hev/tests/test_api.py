"""Prueba funcional del flujo validar -> calcular -> priorizar (sin servidor, con TestClient)."""
import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from georisk_twin_hev.api import app

AQUI = Path(__file__).parent
EVID = AQUI.parent / "evidencia"
EVID.mkdir(exist_ok=True)
cliente = TestClient(app)
OBS = json.loads((AQUI / "observaciones_ejemplo.json").read_text(encoding="utf-8"))


def guardar(nombre, solicitud, respuesta):
    (EVID / f"{nombre}.json").write_text(json.dumps({"solicitud": solicitud, "status": respuesta.status_code,
                                                     "respuesta": respuesta.json()}, ensure_ascii=False, indent=1), encoding="utf-8")


def test_1_validar_acepta_observaciones_correctas():
    r = cliente.post("/datos/validar", json=OBS)
    guardar("1_validar_ok", OBS[:3], r)
    assert r.status_code == 200
    assert r.json()["invalidos"] == 0 and r.json()["validos"] == len(OBS)


def test_1b_validar_rechaza_y_explica_errores():
    malos = [dict(OBS[0], id_zona="Z01"),                                    # identificador antiguo
             dict(OBS[0], componente="E"),                                   # componente incoherente con id_variable
             dict(OBS[0], tipo_dato="inventado"),                            # vocabulario
             dict(OBS[0], valor=None, tipo_dato="real")]                     # vacío sin 'pendiente'
    r = cliente.post("/datos/validar", json=malos)
    guardar("1b_validar_errores", malos, r)
    assert r.status_code == 200 and r.json()["invalidos"] == 4


@pytest.mark.parametrize("agregacion", ["aditiva", "multiplicativa"])
def test_2_calcular_indicadores(agregacion):
    sol = {"observaciones": OBS, "agregacion": agregacion}
    r = cliente.post("/indicadores/calcular", json=sol)
    guardar(f"2_calcular_{agregacion}", {"agregacion": agregacion, "n_observaciones": len(OBS)}, r)
    assert r.status_code == 200
    ind = r.json()
    zonas = {o["id_zona"] for o in OBS}
    assert {i["id_zona"] for i in ind if i["riesgo"] == "global"} == zonas
    assert all(0 <= i["indice_criticidad"] <= 1 for i in ind)


def test_3_priorizar_flujo_completo():
    ind = cliente.post("/indicadores/calcular", json={"observaciones": OBS}).json()
    sol = {"indicadores": ind, "top_k": 5}
    r = cliente.post("/analitico/priorizar", json=sol)
    guardar("3_priorizar", {"n_indicadores": len(ind), "top_k": 5}, r)
    assert r.status_code == 200
    rk = r.json()["ranking"]
    assert len(rk) == 5 and [z["posicion"] for z in rk] == [1, 2, 3, 4, 5]
    assert all(rk[i]["indice_criticidad"] >= rk[i + 1]["indice_criticidad"] for i in range(4))


def test_3b_priorizar_sin_global_devuelve_422():
    r = cliente.post("/analitico/priorizar", json={"indicadores": [{"id_zona": "PER-Z01", "periodo": "p", "riesgo": "inundaciones",
                                                                   "indice_criticidad": 0.5, "metodo_agregacion": "aditiva",
                                                                   "nivel": "alto", "tipo_dato": "sintetico"}]})
    assert r.status_code == 422


def test_openapi_documenta_los_tres_endpoints():
    rutas = set(cliente.get("/openapi.json").json()["paths"])
    assert {"/datos/validar", "/indicadores/calcular", "/analitico/priorizar"} <= rutas
