from enum import Enum


class Dimension(str, Enum):
    """Dimensiones del modelo de riesgo H-E-V."""

    H = "H"  # Peligrosidad (hazard)
    E = "E"  # Exposición
    V = "V"  # Vulnerabilidad


class Dominio(str, Enum):
    URBANO = "urbano"
    INDUSTRIAL = "industrial"


class TipoZona(str, Enum):
    TRAMO = "tramo"
    INTERSECCION = "interseccion"
    ZONA_INDUSTRIAL = "zona_industrial"


class TipoEvento(str, Enum):
    """Taxonomía PROVISIONAL: la definitiva la entrega SI-02."""

    INCIDENTE = "incidente"
    CASI_ACCIDENTE = "casi_accidente"
    CONDICION_INSEGURA = "condicion_insegura"
