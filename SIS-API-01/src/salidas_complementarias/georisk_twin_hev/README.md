# georisk_twin_hev 0.1.0

Contrato común H–E–V (v1.0.0) y API mínima del gemelo digital RISKTWIN. Generado por la Parte C del notebook complementario de SIS-API-01.

## Instalación
```bash
pip install -e ".[test]"
```

## Ejecutar la API
```bash
uvicorn georisk_twin_hev.api:app --reload
# documentación interactiva: http://127.0.0.1:8000/docs
```

## Endpoints (flujo de la presentación)
| Método | Ruta | Entrada | Salida |
|---|---|---|---|
| POST | /datos/validar | lista de `Observacion` (JSON) | `ResultadoValidacion` (errores por fila y campo) |
| POST | /indicadores/calcular | `SolicitudIndicadores` (observaciones, agregación, pesos) | lista de `IndicadorZona` (H, E, V, índice y nivel por zona y riesgo, más el global) |
| POST | /analitico/priorizar | `SolicitudPriorizar` (indicadores, top_k) | `RespuestaPriorizar` (ranking, con advertencia si los datos no son reales) |

## Contrato
`contrato/contrato_hev_v1.schema.json`, generado desde `src/georisk_twin_hev/contratos.py`. Corresponde a `COMUN/contrato_hev_v1.json` del repositorio.

## Pruebas
```bash
pytest -v tests
```
La evidencia (pares solicitud/respuesta y reporte) se guarda en `evidencia/`.
