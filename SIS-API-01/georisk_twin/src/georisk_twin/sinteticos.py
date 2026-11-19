"""Datos SINTÉTICOS para pruebas. No representan tramos, sensores ni eventos reales.

Las coordenadas son ilustrativas (cerca de Guayaquil) y todo lleva `sintetico=True`.
El catálogo de variables es una propuesta mínima: el real lo definen SI-01 y URB-01.
"""

import random
from datetime import date, datetime, timedelta, timezone

from .contratos import (
    Dimension,
    Dominio,
    Evento,
    Geometria,
    Observacion,
    TipoEvento,
    TipoZona,
    VariableDefinicion,
    Zona,
)
from .repositorio import Repositorio

FUENTE = "sintetico_sis_api_01"
VERSION = "v0.1"
BASE = datetime(2026, 11, 1, tzinfo=timezone.utc)

U, I = Dominio.URBANO, Dominio.INDUSTRIAL
H, E, V = Dimension.H, Dimension.E, Dimension.V

# (codigo, nombre, dimension, dominio, unidad, rango_min, rango_max)
_VARIABLES = [
    ("H_vel_prom", "Velocidad promedio vehicular", H, U, "km/h", 20.0, 80.0),
    ("H_conflictos_ped_veh", "Conflictos peatón-vehículo", H, U, "eventos/mes", 0.0, 30.0),
    ("E_flujo_peatonal", "Flujo peatonal", E, U, "peatones/h", 0.0, 2000.0),
    ("E_aforo_vehicular", "Aforo vehicular", E, U, "veh/h", 0.0, 4000.0),
    ("V_deficit_acera", "Déficit de infraestructura peatonal", V, U, "%", 0.0, 100.0),
    ("V_cruces_sin_semaforo", "Cruces peatonales sin semáforo", V, U, "unidades", 0.0, 5.0),
    ("H_vel_vehiculo_planta", "Velocidad de vehículos en planta", H, I, "km/h", 5.0, 40.0),
    ("E_trabajadores_en_ruta", "Trabajadores en la ruta", E, I, "personas/turno", 0.0, 50.0),
    ("V_senalizacion_deficiente", "Señalización deficiente", V, I, "indice", 0.0, 1.0),
]


def _linea(i: int) -> Geometria:
    x0, y0 = -79.940 + i * 0.004, -2.250 + i * 0.003
    return Geometria(type="LineString", coordinates=[[x0, y0], [x0 + 0.004, y0 + 0.003]])


def _poligono(x0: float, y0: float, d: float = 0.002) -> Geometria:
    return Geometria(
        type="Polygon",
        coordinates=[[[x0, y0], [x0 + d, y0], [x0 + d, y0 + d], [x0, y0 + d], [x0, y0]]],
    )


def cargar_sinteticos(repo: Repositorio, semilla: int = 42) -> dict[str, int]:
    """Carga catálogo, 5 tramos urbanos, 2 zonas industriales, observaciones y eventos."""
    rng = random.Random(semilla)

    catalogo = []
    for codigo, nombre, dim, dom, unidad, rmin, rmax in _VARIABLES:
        var = VariableDefinicion(
            codigo=codigo, nombre=nombre, dimension=dim, dominio=dom, unidad=unidad,
            fuente=FUENTE, rango_min=rmin, rango_max=rmax,
        )
        repo.agregar_variable(var)
        catalogo.append(var)

    zonas: list[Zona] = []
    for i in range(5):
        zonas.append(Zona(
            zona_id=f"T-{i + 1:03d}", nombre=f"Tramo sintético {i + 1}", tipo=TipoZona.TRAMO,
            dominio=U, geometria=_linea(i), fecha_captura=date(2026, 11, 1),
            fuente=FUENTE, version=VERSION, sintetico=True,
        ))
    for j in range(2):
        zonas.append(Zona(
            zona_id=f"PI-{j + 1:03d}", nombre=f"Zona industrial sintética {j + 1}",
            tipo=TipoZona.ZONA_INDUSTRIAL, dominio=I,
            geometria=_poligono(-79.920 + j * 0.005, -2.260),
            fecha_captura=date(2026, 11, 1), fuente=FUENTE, version=VERSION, sintetico=True,
        ))

    n_obs = n_eventos = 0
    for zona in zonas:
        repo.agregar_zona(zona)
        for var in catalogo:
            if var.dominio != zona.dominio:
                continue
            normalizado = round(rng.random(), 3)
            valor = round(var.rango_min + normalizado * (var.rango_max - var.rango_min), 2)
            repo.agregar_observacion(Observacion(
                observacion_id=f"OBS-{zona.zona_id}-{var.codigo}",
                zona_id=zona.zona_id, variable=var.codigo, dimension=var.dimension,
                valor=valor, unidad=var.unidad, valor_normalizado=normalizado,
                fecha_captura=BASE, fuente=FUENTE, version=VERSION, sintetico=True,
            ))
            n_obs += 1
        for k in range(rng.randint(1, 3)):
            repo.agregar_evento(Evento(
                evento_id=f"EV-{zona.zona_id}-{k + 1}", zona_id=zona.zona_id,
                tipo=rng.choice(list(TipoEvento)), severidad=rng.randint(1, 5),
                fecha_hora=BASE - timedelta(days=rng.randint(1, 60)),
                descripcion="Evento sintético de prueba", fuente=FUENTE, version=VERSION,
                sintetico=True,
            ))
            n_eventos += 1

    return {
        "variables": len(catalogo), "zonas": len(zonas),
        "observaciones": n_obs, "eventos": n_eventos,
    }
