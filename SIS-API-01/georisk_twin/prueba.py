from georisk_twin.repositorio import RepositorioMemoria
from georisk_twin.sinteticos import cargar_sinteticos
from georisk_twin.servicios import resumen_hev

repo = RepositorioMemoria()
cargar_sinteticos(repo)

ind = resumen_hev(repo, "T-001")
print(ind.peligrosidad, ind.exposicion, ind.vulnerabilidad, ind.criticidad, ind.zona_id, ind.metodo, ind.n_variables, ind.sintetico)
