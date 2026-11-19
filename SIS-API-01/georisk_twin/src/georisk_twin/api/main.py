"""Punto de entrada para uvicorn: `uvicorn georisk_twin.api.main:app --reload`.

Con GEORISK_CARGAR_SINTETICOS=0 arranca vacío.
"""

import os

from ..repositorio import RepositorioMemoria
from ..sinteticos import cargar_sinteticos
from .app import crear_app

_repo = RepositorioMemoria()
if os.getenv("GEORISK_CARGAR_SINTETICOS", "1") == "1":
    cargar_sinteticos(_repo)

app = crear_app(_repo)
