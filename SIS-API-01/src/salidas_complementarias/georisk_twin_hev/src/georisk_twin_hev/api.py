"""API mínima del gemelo digital: validar -> calcular -> priorizar (contrato común H–E–V)."""
from collections import Counter

from fastapi import Body, FastAPI, HTTPException
from pydantic import ValidationError

from . import __version__
from .contratos import (VERSION_CONTRATO, ErrorFila, IndicadorZona, Observacion, RespuestaPriorizar,
                        ResultadoValidacion, SolicitudIndicadores, SolicitudPriorizar, ZonaPriorizada)
from .indicadores import calcular

app = FastAPI(title="georisk_twin_hev", version=__version__,
              description=f"Contrato común H–E–V v{VERSION_CONTRATO} · RISKTWIN SIS-API-01 (complemento de auditoría)")


@app.post("/datos/validar", response_model=ResultadoValidacion, tags=["1 · Datos"],
          summary="Valida observaciones contra el contrato común")
def datos_validar(registros: list[dict] = Body(..., description="Observaciones crudas (formato del contrato)")):
    errores, validos = [], []
    for i, r in enumerate(registros):
        try:
            validos.append(Observacion.model_validate(r))
        except ValidationError as e:
            for err in e.errors():
                errores.append(ErrorFila(indice=i, campo=".".join(map(str, err["loc"])) or "registro", detalle=err["msg"]))
    return ResultadoValidacion(total=len(registros), validos=len(validos), invalidos=len({e.indice for e in errores}),
                               errores=errores, tipos_dato=dict(Counter(o.tipo_dato for o in validos)))


@app.post("/indicadores/calcular", response_model=list[IndicadorZona], tags=["2 · Indicadores"],
          summary="Calcula H, E, V e índice de criticidad por zona y riesgo (fórmula URB-03)")
def indicadores_calcular(sol: SolicitudIndicadores):
    try:
        return calcular(sol)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/analitico/priorizar", response_model=RespuestaPriorizar, tags=["3 · Analítico"],
          summary="Ordena las zonas por índice global y devuelve el top-k")
def analitico_priorizar(sol: SolicitudPriorizar):
    glob = [i for i in sol.indicadores if i.riesgo == "global"]
    if not glob:
        raise HTTPException(status_code=422, detail="Se requieren indicadores con riesgo = 'global'")
    por_riesgo = {}
    for i in sol.indicadores:
        if i.riesgo != "global":
            por_riesgo.setdefault(i.id_zona, []).append((i.indice_criticidad, i.riesgo))
    orden = sorted(glob, key=lambda i: -i.indice_criticidad)[: sol.top_k]
    tipos = {i.tipo_dato for i in glob}
    tipo = tipos.pop() if len(tipos) == 1 else "mixto"
    return RespuestaPriorizar(
        metodo_agregacion=glob[0].metodo_agregacion, tipo_dato=tipo,
        ranking=[ZonaPriorizada(posicion=k + 1, id_zona=i.id_zona, indice_criticidad=i.indice_criticidad, nivel=i.nivel,
                                riesgo_dominante=max(por_riesgo.get(i.id_zona, [(0, "n/d")]))[1]) for k, i in enumerate(orden)],
        advertencia=None if tipo in ("real", "derivado_real") else
        "Ranking calculado con datos sintéticos o mixtos: sirve para probar el flujo, no para decidir intervenciones.")
