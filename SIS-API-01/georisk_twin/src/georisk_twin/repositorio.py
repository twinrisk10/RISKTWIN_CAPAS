"""Almacenamiento. En v0 es en memoria; después se reemplaza por PostGIS sin tocar los servicios."""

from typing import Optional, Protocol

from .contratos import Dominio, Evento, Observacion, VariableDefinicion, Zona
from .errores import IdDuplicado, VariableDesconocida, ZonaNoEncontrada


class Repositorio(Protocol):
    """Puerto que debe cumplir cualquier almacenamiento (memoria, PostGIS, GeoPackage...)."""

    def agregar_variable(self, variable: VariableDefinicion) -> None: ...
    def obtener_variable(self, codigo: str) -> VariableDefinicion: ...
    def agregar_zona(self, zona: Zona) -> None: ...
    def obtener_zona(self, zona_id: str) -> Zona: ...
    def listar_zonas(self, dominio: Optional[Dominio] = None) -> list[Zona]: ...
    def agregar_evento(self, evento: Evento) -> None: ...
    def agregar_observacion(self, observacion: Observacion) -> None: ...
    def existe_observacion(self, observacion_id: str) -> bool: ...
    def observaciones_de_zona(self, zona_id: str) -> list[Observacion]: ...


class RepositorioMemoria:
    def __init__(self) -> None:
        self._variables: dict[str, VariableDefinicion] = {}
        self._zonas: dict[str, Zona] = {}
        self._eventos: dict[str, Evento] = {}
        self._observaciones: dict[str, Observacion] = {}

    # variables
    def agregar_variable(self, variable: VariableDefinicion) -> None:
        if variable.codigo in self._variables:
            raise IdDuplicado(f"la variable '{variable.codigo}' ya existe")
        self._variables[variable.codigo] = variable

    def obtener_variable(self, codigo: str) -> VariableDefinicion:
        try:
            return self._variables[codigo]
        except KeyError:
            raise VariableDesconocida(f"la variable '{codigo}' no está en el catálogo") from None

    # zonas
    def agregar_zona(self, zona: Zona) -> None:
        if zona.zona_id in self._zonas:
            raise IdDuplicado(f"la zona '{zona.zona_id}' ya existe")
        self._zonas[zona.zona_id] = zona

    def obtener_zona(self, zona_id: str) -> Zona:
        try:
            return self._zonas[zona_id]
        except KeyError:
            raise ZonaNoEncontrada(f"la zona '{zona_id}' no existe") from None

    def listar_zonas(self, dominio: Optional[Dominio] = None) -> list[Zona]:
        zonas = sorted(self._zonas.values(), key=lambda z: z.zona_id)
        if dominio is not None:
            zonas = [z for z in zonas if z.dominio == dominio]
        return zonas

    # eventos
    def agregar_evento(self, evento: Evento) -> None:
        if evento.evento_id in self._eventos:
            raise IdDuplicado(f"el evento '{evento.evento_id}' ya existe")
        self.obtener_zona(evento.zona_id)
        self._eventos[evento.evento_id] = evento

    # observaciones
    def agregar_observacion(self, observacion: Observacion) -> None:
        if observacion.observacion_id in self._observaciones:
            raise IdDuplicado(f"la observación '{observacion.observacion_id}' ya existe")
        self._observaciones[observacion.observacion_id] = observacion

    def existe_observacion(self, observacion_id: str) -> bool:
        return observacion_id in self._observaciones

    def observaciones_de_zona(self, zona_id: str) -> list[Observacion]:
        return [o for o in self._observaciones.values() if o.zona_id == zona_id]
