"""Cálculo H–E–V (fórmula de URB-03): normalización min-max, promedio por componente y agregación."""
import numpy as np
import pandas as pd

from .contratos import IndicadorZona, SolicitudIndicadores

CORTES = [0.25, 0.50, 0.75]
EPS = 0.01


def nivel(x: float) -> str:
    return ["bajo", "medio", "alto", "critico"][int(np.searchsorted(CORTES, x, side="right"))]


def calcular(sol: SolicitudIndicadores) -> list[IndicadorZona]:
    df = pd.DataFrame([o.model_dump() for o in sol.observaciones]).dropna(subset=["valor"])
    if df.empty:
        raise ValueError("No hay observaciones con valor")
    periodo = df.periodo.iloc[0] if df.periodo.nunique() == 1 else "mixto"
    tipos = set(df.tipo_dato)
    tipo = "sintetico" if tipos <= {"sintetico"} else "real" if tipos <= {"real"} else "derivado_real" if tipos <= {"real", "derivado_real"} else "mixto"
    X = df.pivot_table(index="id_zona", columns="id_variable", values="valor", aggfunc="mean")
    rango = (X.max() - X.min()).replace(0, np.nan)
    N = ((X - X.min()) / rango).fillna(0.5)
    neg = [c for c in sol.sentido_negativo if c in N.columns]
    N[neg] = 1 - N[neg]
    meta = df.drop_duplicates("id_variable").set_index("id_variable")[["riesgo", "componente"]]
    p = sol.pesos
    w = {"H": p.w_H, "E": p.w_E, "V": p.w_V}
    sw = sum(w.values()); w = {k: v / sw for k, v in w.items()}
    out, glob = [], {z: [] for z in N.index}
    for riesgo, m in meta.groupby("riesgo"):
        comps = {c: N[m.index[m.componente == c]].mean(axis=1) for c in "HEV" if (m.componente == c).any()}
        if set(comps) != {"H", "E", "V"}:
            continue                                  # un riesgo sin H, E y V completos no se agrega
        for z in N.index:
            h, e, v = (float(comps[c][z]) for c in "HEV")
            if sol.agregacion == "aditiva":
                r = w["H"] * h + w["E"] * e + w["V"] * v
            else:
                r = max(h, EPS) ** w["H"] * max(e, EPS) ** w["E"] * max(v, EPS) ** w["V"]
            out.append(IndicadorZona(id_zona=z, periodo=periodo, riesgo=riesgo, H=round(h, 4), E=round(e, 4), V=round(v, 4),
                                     indice_criticidad=round(r, 4), metodo_agregacion=sol.agregacion, nivel=nivel(r), tipo_dato=tipo))
            glob[z].append((riesgo, r))
    for z, lst in glob.items():
        if not lst:
            continue
        a = {rg: sol.pesos.alpha.get(rg, 0) for rg, _ in lst}
        sa = sum(a.values()) or 1
        g = sum(a[rg] / sa * r for rg, r in lst)
        out.append(IndicadorZona(id_zona=z, periodo=periodo, riesgo="global", indice_criticidad=round(g, 4),
                                 metodo_agregacion=sol.agregacion, nivel=nivel(g), tipo_dato=tipo))
    return out
