"""Convenciones comunes v0.

Son una PROPUESTA de SIS-API-01 y deben validarse con los demás equipos
(ver docs/decisiones_pendientes.md).
"""

VERSION_CONTRATO = "0.1.0"

# GeoJSON que entra y sale de la API (WGS 84, longitud/latitud).
CRS_INTERCAMBIO = "EPSG:4326"

# Cálculos de distancia (UTM zona 17 sur). Es el mismo CRS que declaran URB-01 y URB-02.
CRS_CALCULO = "EPSG:32717"

# Identificadores: letras, números, guion y guion bajo; sin espacios ni tildes.
PATRON_ID = r"^[A-Za-z0-9_-]{1,64}$"
