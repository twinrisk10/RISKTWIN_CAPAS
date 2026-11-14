"""
Genera la delimitación territorial COMÚN de la zona piloto "Vía Perimetral" (Guayaquil).

Todos los notebooks complementarios (URB-01 a URB-05 y SIS-API-01) usan estas zonas y
el mismo identificador espacial: PER-Z01 ... PER-Z12.

Regla de delimitación (reproducible y fácil de explicar):
  1. Eje vial: las 156 vías de OpenStreetMap con name = "Vía Perimetral"
     (archivo SIS-API-01/test_Data/geoJsonPerimetral.geojson, extraído el 2026-11-09).
  2. Corredor: franja de 200 m a cada lado del eje. Es el mismo umbral con el que se
     filtraron los CSV de siniestros (ATM) y homicidios de URB-04/test_Data
     (columna distancia_via_m <= 200 m).
  3. Zonas: el corredor se corta en 12 franjas de igual amplitud en latitud, de norte a sur.
     La Perimetral corre principalmente en sentido norte-sur, por lo que cada franja
     contiene un tramo continuo de vía de ~1,5 km de largo en sentido N-S.

Uso:  python generar_zonas_perimetral.py
Salidas (en esta misma carpeta): zonas_perimetral.geojson y zonas_perimetral.csv
Dependencias: shapely >= 2, pyproj
"""
from collections import Counter
from pathlib import Path
import csv
import json

from pyproj import Transformer
from shapely import transform as shp_transform
from shapely.geometry import box, mapping, shape
from shapely.ops import unary_union

AQUI = Path(__file__).resolve().parent
RUTA_EJE = AQUI.parent / "SIS-API-01" / "test_Data" / "geoJsonPerimetral.geojson"
BUFFER_M = 200
N_ZONAS = 12
LAT_NORTE, LAT_SUR = -2.0730, -2.2425   # cubre el eje y los eventos de los CSV (lat -2.0736 a -2.2418)

a_utm = Transformer.from_crs(4326, 32717, always_xy=True)
a_geo = Transformer.from_crs(32717, 4326, always_xy=True)


def proyectar(geom, tr):
    return shp_transform(geom, lambda c: __import__("numpy").column_stack(tr.transform(c[:, 0], c[:, 1])))


def predominante(valores):
    v = [x for x in valores if x]
    return Counter(v).most_common(1)[0][0] if v else None


def main():
    eje = json.loads(RUTA_EJE.read_text(encoding="utf-8"))
    vias = [(shape(f["geometry"]), f["properties"]) for f in eje["features"]]
    vias_m = [(proyectar(g, a_utm), p) for g, p in vias]
    corredor_m = unary_union([g for g, _ in vias_m]).buffer(BUFFER_M)

    paso = (LAT_NORTE - LAT_SUR) / N_ZONAS
    filas, features = [], []
    for k in range(N_ZONAS):
        lat_max = LAT_NORTE - k * paso
        lat_min = lat_max - paso
        franja_m = proyectar(box(-80.10, lat_min, -79.80, lat_max), a_utm)
        zona_m = corredor_m.intersection(franja_m)
        if zona_m.is_empty:
            continue
        tramos = [(g.intersection(franja_m), p) for g, p in vias_m if g.intersects(franja_m)]
        long_km = sum(t.length for t, _ in tramos) / 1000 / 2    # calzada doble -> eje aproximado
        vel = predominante([p.get("maxspeed") for _, p in tramos])
        carr = predominante([p.get("lanes") for _, p in tramos])
        zona = proyectar(zona_m, a_geo)
        c = zona.centroid
        idz = f"PER-Z{k + 1:02d}"
        prop = {
            "id_zona": idz,
            "nombre": f"Perimetral tramo {k + 1:02d}" + (" (extremo norte)" if k == 0 else " (extremo sur)" if k == N_ZONAS - 1 else ""),
            "orden_norte_sur": k + 1,
            "lat_max": round(lat_max, 6), "lat_min": round(lat_min, 6),
            "centroide_lat": round(c.y, 6), "centroide_lon": round(c.x, 6),
            "area_km2": round(zona_m.area / 1e6, 3),
            "longitud_eje_km": round(long_km, 2),
            "vel_max_osm_kmh": int(vel) if vel else None,
            "carriles_osm": int(carr) if carr else None,
            "buffer_m": BUFFER_M,
            "fuente": "OSM 2026-11-09 (geoJsonPerimetral.geojson) + regla COMUN v1",
            "tipo_dato": "real",
        }
        filas.append(prop)
        features.append({"type": "Feature", "properties": prop, "geometry": mapping(zona)})

    gj = {"type": "FeatureCollection", "name": "zonas_perimetral_v1",
          "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
          "features": features}
    (AQUI / "zonas_perimetral.geojson").write_text(json.dumps(gj, ensure_ascii=False), encoding="utf-8")
    with open(AQUI / "zonas_perimetral.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    for p in filas:
        print(p["id_zona"], p["centroide_lat"], p["centroide_lon"], p["area_km2"], "km2",
              p["longitud_eje_km"], "km", p["vel_max_osm_kmh"], "km/h", p["carriles_osm"], "carriles")


if __name__ == "__main__":
    main()
