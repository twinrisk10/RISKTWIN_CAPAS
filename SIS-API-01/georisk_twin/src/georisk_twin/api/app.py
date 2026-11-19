"""API v0 (FastAPI). Solo transporte y traducción de errores: la lógica vive en la librería."""

from typing import Optional

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .. import __version__
from ..contratos import (
    ColeccionZonas,
    DetalleHEV,
    Dominio,
    FeatureZona,
    LoteObservaciones,
    PropiedadesZona,
    ResultadoCarga,
)
from ..errores import ErrorDominio
from ..repositorio import RepositorioMemoria
from ..servicios import registrar_observaciones, resumen_hev, ultimas_por_variable

DESCRIPCION = (
    "API del núcleo compartido georisk_twin (SIS-API-01). v0 con datos sintéticos: "
    "expone zonas con su resumen H-E-V, el detalle por zona y la carga validada de observaciones."
)


def crear_app(repositorio: Optional[RepositorioMemoria] = None) -> FastAPI:
    repo = repositorio if repositorio is not None else RepositorioMemoria()
    app = FastAPI(title="georisk_twin API", version=__version__, description=DESCRIPCION)
    app.state.repo = repo

    @app.exception_handler(ErrorDominio)
    async def _error_dominio(request: Request, exc: ErrorDominio) -> JSONResponse:
        return JSONResponse(
            status_code=exc.codigo_http,
            content={"tipo_error": type(exc).__name__, "detalle": str(exc)},
        )

    @app.get("/health", tags=["sistema"])
    def health() -> dict:
        return {"estado": "ok", "version": __version__}

    # Endpoint 1: mapa de zonas críticas (GeoJSON con H-E-V por zona)
    @app.get("/v1/zonas", response_model=ColeccionZonas, tags=["zonas"])
    def listar_zonas(dominio: Optional[Dominio] = None) -> ColeccionZonas:
        features = []
        for zona in repo.listar_zonas(dominio):
            ind = resumen_hev(repo, zona.zona_id)
            features.append(FeatureZona(
                id=zona.zona_id,
                geometry=zona.geometria,
                properties=PropiedadesZona(
                    zona_id=zona.zona_id, nombre=zona.nombre, tipo=zona.tipo,
                    dominio=zona.dominio, peligrosidad=ind.peligrosidad,
                    exposicion=ind.exposicion, vulnerabilidad=ind.vulnerabilidad,
                    criticidad=ind.criticidad, sintetico=zona.sintetico,
                ),
            ))
        return ColeccionZonas(total=len(features), features=features)

    # Endpoint 2: detalle H-E-V de una zona
    @app.get("/v1/zonas/{zona_id}/hev", response_model=DetalleHEV, tags=["zonas"])
    def detalle_hev(zona_id: str) -> DetalleHEV:
        zona = repo.obtener_zona(zona_id)
        return DetalleHEV(
            zona=zona,
            indicador=resumen_hev(repo, zona_id),
            observaciones=ultimas_por_variable(repo.observaciones_de_zona(zona_id)),
        )

    # Endpoint 3: carga validada de observaciones (plantillas de carga de URB-01 / SI-02)
    @app.post(
        "/v1/observaciones",
        response_model=ResultadoCarga,
        status_code=status.HTTP_201_CREATED,
        tags=["observaciones"],
    )
    def cargar_observaciones(lote: LoteObservaciones) -> ResultadoCarga:
        n = registrar_observaciones(repo, lote.observaciones)
        zonas = sorted({o.zona_id for o in lote.observaciones})
        return ResultadoCarga(aceptadas=n, zonas_afectadas=zonas)

    return app
