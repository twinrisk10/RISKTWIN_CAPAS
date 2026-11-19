"""Errores del dominio. La API los traduce a códigos HTTP."""


class ErrorDominio(Exception):
    codigo_http = 400


class ZonaNoEncontrada(ErrorDominio):
    codigo_http = 404


class VariableDesconocida(ErrorDominio):
    codigo_http = 422


class ConflictoContrato(ErrorDominio):
    codigo_http = 422


class IdDuplicado(ErrorDominio):
    codigo_http = 409
