"""
simulation_v02.py - Motor de simulación de escenarios preventivos urbanos (URB-05 / RISKTWIN)

v0.2.0 (auditoría nov-2026): copia de simulation.py v0.1.0 + intervenciones "reduccion_velocidad" y
"separacion_flujos" + estado de severidad (sev) y de conflicto (conf). Con sev = conf = 1 el resultado
es idéntico a v0.1.0 (compatibilidad verificada en la Parte C del notebook complementario).

Metodología: Simulación de Eventos Discretos (DES) con cola de eventos, más Monte Carlo
para incertidumbre y análisis de sensibilidad. No simula agentes individuales (ABM): el
estado del sistema son variables por tramo vial que cambian en instantes discretos.

Contenido
  1. Constantes y configuración
  2. Modelo de criticidad
  3. Red urbana (insumos de FCI-01/02/03)
  4. Intervenciones y escenarios
  5. Motor DES
  6. Monte Carlo y comparación
  7. Análisis de sensibilidad
  8. Contrato de intercambio (JSON) para el dashboard / API
"""
from __future__ import annotations

import copy
import heapq
import itertools
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

VERSION = "0.2.0"
ESQUEMA_RESULTADOS = "risktwin.urb05.resultados/1.0"

# ----------------------------------------------------------------------------
# 1. Constantes y configuración
# ----------------------------------------------------------------------------
# Capacidad nominal por jerarquía vial (veh/h). SUPUESTO documentado: calibrar con ATM.
CAPACIDAD_VEH_H = {"motorway": 3600, "trunk": 2400, "primary": 1800,
                   "secondary": 1200, "tertiary": 800, "residential": 400}
CAPACIDAD_DEFECTO = 600

# Perfiles horarios (multiplicadores con media 1). SUPUESTO: día laborable típico.
_PV = np.array([.25, .18, .15, .15, .25, .60, 1.2, 1.8, 1.7, 1.2, 1.0, 1.0,
                1.1, 1.1, 1.0, 1.1, 1.4, 1.8, 1.7, 1.2, .8, .6, .45, .3])
_PP = np.array([.10, .05, .05, .05, .10, .30, .8, 1.2, 1.1, 1.0, 1.0, 1.3,
                1.5, 1.2, 1.0, 1.1, 1.3, 1.5, 1.2, .9, .6, .4, .25, .15])
PERFIL_VEH = _PV / _PV.mean()
PERFIL_PEAT = _PP / _PP.mean()

PESOS_DEFECTO = {"flujo": 0.30, "peatonal": 0.25, "infra": 0.20, "conflicto": 0.25}

# Parámetros por defecto de cada tipo de intervención (todos son fracciones 0-1)
PARAMS_DEFECTO = {
    "desvio_ruta":        {"fraccion_desvio": 0.50},
    "restriccion_carril": {"reduccion_capacidad": 0.30, "elasticidad_demanda": 1.20,
                           "beneficio_peatonal": 0.15},
    "zona_peatonal":      {"restriccion_vehicular": 0.80, "reduccion_exposicion": 0.60},
    "senalizacion":       {"mejora_infra": 0.35, "beneficio_peatonal": 0.05},
    # --- v0.2.0 ---
    # Modelo de potencia (Nilsson 2004; Elvik 2009): riesgo de siniestro con víctimas ∝ (v1/v0)^exponente.
    "reduccion_velocidad": {"vel_objetivo_kmh": 60.0, "exponente_potencia": 2.0, "efecto_capacidad": 0.0},
    # Separación física de flujos (carril exclusivo moto/bus, barrera, cruce peatonal segregado).
    "separacion_flujos":   {"reduccion_conflicto": 0.60, "reduccion_exposicion": 0.30,
                            "reduccion_capacidad": 0.10, "elasticidad_demanda": 1.00},
}
# Velocidad por defecto si el insumo no trae vel_kmh (km/h). SUPUESTO.
VEL_DEFECTO_KMH = {"motorway": 100, "trunk": 90, "primary": 60, "secondary": 50, "tertiary": 40, "residential": 30}
# Cotas superiores al perturbar parámetros que no son fracciones.
LIMITE_SUP_PARAM = {"elasticidad_demanda": 1.5, "vel_objetivo_kmh": 130.0, "exponente_potencia": 4.5}


@dataclass
class ConfigSim:
    horizonte_h: int = 24                 # un día típico
    sigma_demanda: float = 0.25           # variabilidad lognormal de la demanda por tramo y hora
    tasa_incidentes_dia: float = 6.0      # incidentes viales aleatorios en toda la zona por día
    duracion_incidente_h: float = 0.75    # duración media (exponencial)
    factor_cap_incidente: float = 0.50    # capacidad residual del tramo con incidente
    derrame_incidente: float = 0.15       # fracción del flujo que se desvía a los vecinos
    umbral_critico: float = 60.0          # criticidad a partir de la cual un tramo-hora es "crítico"
    incertidumbre_parametros: float = 0.0 # +/- fracción relativa sobre los parámetros de intervención
    pesos: Dict[str, float] = field(default_factory=lambda: dict(PESOS_DEFECTO))

    def __post_init__(self):
        if abs(sum(self.pesos.values()) - 1.0) > 1e-9:
            raise ValueError("Los pesos de criticidad deben sumar 1.")


# ----------------------------------------------------------------------------
# 2. Modelo de criticidad
# ----------------------------------------------------------------------------
def criticidad(flujo, cap, peat, infra, pesos, sev=1.0, conf=1.0):
    # Índice 0-100: saturación vehicular, exposición peatonal, deterioro y su conflicto.
    # v0.2.0: sev = factor de severidad por velocidad; conf = factor del término de conflicto.
    sat = np.minimum(flujo / np.maximum(cap, 1.0), 1.5) / 1.5
    p = np.clip(peat, 0.0, 1.0)
    i = np.clip(infra, 0.0, 1.0)
    return np.minimum(100.0, 100.0 * sev * (pesos["flujo"] * sat + pesos["peatonal"] * p
                    + pesos["infra"] * i + pesos["conflicto"] * sat * p * conf))


# ----------------------------------------------------------------------------
# 3. Red urbana (insumos)
# ----------------------------------------------------------------------------
COLUMNAS_INSUMO = ["id_segmento", "id_zona", "tipo_via", "longitud_m", "flujo_veh_h",
                   "exposicion_peatonal", "deterioro_infra", "nodo_origen", "nodo_destino",
                   "lat", "lon"]


def validar_insumo(df: pd.DataFrame) -> List[str]:
    # Devuelve la lista de problemas del insumo (vacía = válido). Contrato de HU-01.
    faltan = [c for c in COLUMNAS_INSUMO if c not in df.columns]
    if faltan:
        return [f"Faltan columnas obligatorias: {faltan}"]
    p = []
    if df["id_segmento"].duplicated().any():
        p.append("id_segmento duplicado")
    nulos = df[COLUMNAS_INSUMO].isna().sum()
    p += [f"Nulos en '{c}': {int(n)}" for c, n in nulos.items() if n > 0]
    for c in ("exposicion_peatonal", "deterioro_infra"):
        if ((df[c] < 0) | (df[c] > 1)).any():
            p.append(f"'{c}' fuera de [0, 1]")
    if (df["flujo_veh_h"] < 0).any():
        p.append("flujo_veh_h negativo")
    if (df["longitud_m"] <= 0).any():
        p.append("longitud_m no positiva")
    return p


@dataclass
class Red:
    ids: np.ndarray
    zona: np.ndarray
    tipo_via: np.ndarray
    longitud: np.ndarray
    flujo: np.ndarray
    cap: np.ndarray
    peat: np.ndarray
    infra: np.ndarray
    lat: np.ndarray
    lon: np.ndarray
    vecinos: List[np.ndarray]
    indice_fci: Optional[np.ndarray] = None
    vel: Optional[np.ndarray] = None          # v0.2.0: velocidad de operación (km/h)

    @property
    def n(self) -> int:
        return len(self.ids)

    def indices(self, ids) -> np.ndarray:
        pos = {k: i for i, k in enumerate(self.ids)}
        return np.array([pos[i] for i in ids], dtype=int)


def construir_red(df: pd.DataFrame) -> Red:
    problemas = validar_insumo(df)
    if problemas:
        raise ValueError("Insumo inválido: " + "; ".join(problemas))
    df = df.reset_index(drop=True)
    por_nodo: Dict = {}
    for i, (a, b) in enumerate(zip(df["nodo_origen"], df["nodo_destino"])):
        por_nodo.setdefault(a, []).append(i)
        por_nodo.setdefault(b, []).append(i)
    vecinos = []
    for i, (a, b) in enumerate(zip(df["nodo_origen"], df["nodo_destino"])):
        v = set(por_nodo[a]) | set(por_nodo[b])
        v.discard(i)
        vecinos.append(np.array(sorted(v), dtype=int))
    cap = df["tipo_via"].map(lambda t: CAPACIDAD_VEH_H.get(t, CAPACIDAD_DEFECTO)).to_numpy(float)
    return Red(ids=df["id_segmento"].to_numpy(), zona=df["id_zona"].to_numpy(),
               tipo_via=df["tipo_via"].to_numpy(), longitud=df["longitud_m"].to_numpy(float),
               flujo=df["flujo_veh_h"].to_numpy(float), cap=cap,
               peat=df["exposicion_peatonal"].to_numpy(float),
               infra=df["deterioro_infra"].to_numpy(float),
               lat=df["lat"].to_numpy(float), lon=df["lon"].to_numpy(float), vecinos=vecinos,
               indice_fci=(df["indice_criticidad_fci03"].to_numpy(float)
                           if "indice_criticidad_fci03" in df.columns else None),
               vel=(df["vel_kmh"].to_numpy(float) if "vel_kmh" in df.columns else
                    df["tipo_via"].map(lambda t: VEL_DEFECTO_KMH.get(t, 50)).to_numpy(float)))


def indice_estatico(red: Red, pesos=None) -> np.ndarray:
    # Criticidad del estado promedio (sin perfil horario ni ruido). Equivale al índice "base" de FCI-03.
    return criticidad(red.flujo, red.cap, red.peat, red.infra, pesos or PESOS_DEFECTO)


# ----------------------------------------------------------------------------
# 4. Intervenciones y escenarios
# ----------------------------------------------------------------------------
@dataclass
class Intervencion:
    tipo: str                      # desvio_ruta | restriccion_carril | zona_peatonal | senalizacion
                                   # | reduccion_velocidad | separacion_flujos (v0.2.0)
    objetivo: List[str]            # ids de tramos intervenidos
    params: Dict[str, float] = field(default_factory=dict)
    inicio_h: float = 0.0
    fin_h: float = 24.0

    def __post_init__(self):
        if self.tipo not in PARAMS_DEFECTO:
            raise ValueError(f"Tipo de intervención desconocido: {self.tipo}")
        self.params = {**PARAMS_DEFECTO[self.tipo], **self.params}


@dataclass
class Escenario:
    nombre: str
    intervenciones: List[Intervencion] = field(default_factory=list)
    descripcion: str = ""


def seleccionar_objetivo(red: Red, k: int = 10, zona: Optional[str] = None, ids=None) -> List[str]:
    # Regla de selección: los k tramos más críticos (opcionalmente de una zona) o una lista explícita.
    if ids is not None:
        return list(ids)
    c = indice_estatico(red)
    idx = np.arange(red.n) if zona is None else np.where(red.zona == zona)[0]
    idx = idx[np.argsort(-c[idx])][:k]
    return list(red.ids[idx])


def _redistribuir(flujo, obj_idx, quitado, red):
    # El flujo retirado de los tramos objetivo NO desaparece: pasa a los vecinos no intervenidos,
    # proporcional a su capacidad. Así se mide si el conflicto solo se traslada a otra zona.
    es_obj = np.zeros(red.n, bool)
    es_obj[obj_idx] = True
    for k, q in zip(obj_idx, quitado):
        vec = red.vecinos[k]
        vec = vec[~es_obj[vec]]
        if len(vec) == 0:
            flujo[k] += q            # sin salida posible: el flujo permanece
        else:
            w = red.cap[vec]
            flujo[vec] += q * w / w.sum()


def _aplicar(estado: dict, iv: Intervencion, red: Red):
    idx = red.indices(iv.objetivo)
    p = iv.params
    f = estado["flujo"]
    if iv.tipo == "desvio_ruta":
        quitado = f[idx] * p["fraccion_desvio"]
        f[idx] -= quitado
        _redistribuir(f, idx, quitado, red)
    elif iv.tipo == "restriccion_carril":
        r = p["reduccion_capacidad"]
        estado["cap"][idx] *= (1 - r)
        quitado = f[idx] * min(0.95, p["elasticidad_demanda"] * r)
        f[idx] -= quitado
        _redistribuir(f, idx, quitado, red)
        estado["peat"][idx] *= (1 - p["beneficio_peatonal"])
    elif iv.tipo == "zona_peatonal":
        quitado = f[idx] * p["restriccion_vehicular"]
        f[idx] -= quitado
        _redistribuir(f, idx, quitado, red)
        estado["peat"][idx] *= (1 - p["reduccion_exposicion"])
    elif iv.tipo == "senalizacion":
        estado["infra"][idx] *= (1 - p["mejora_infra"])
        estado["peat"][idx] *= (1 - p["beneficio_peatonal"])
    elif iv.tipo == "reduccion_velocidad":
        v0 = red.vel[idx] if red.vel is not None else np.full(len(idx), 50.0)
        razon = np.minimum(1.0, p["vel_objetivo_kmh"] / np.maximum(v0, 1.0))    # solo reduce, nunca sube
        estado["sev"][idx] *= razon ** p["exponente_potencia"]
        estado["cap"][idx] *= (1 - p["efecto_capacidad"] * (1 - razon))
    elif iv.tipo == "separacion_flujos":
        r = p["reduccion_capacidad"]
        estado["cap"][idx] *= (1 - r)
        quitado = estado["flujo"][idx] * min(0.95, p["elasticidad_demanda"] * r)
        estado["flujo"][idx] -= quitado
        _redistribuir(estado["flujo"], idx, quitado, red)
        estado["conf"][idx] *= (1 - p["reduccion_conflicto"])
        estado["peat"][idx] *= (1 - p["reduccion_exposicion"])


def _perturbar(ivs, incert, rng_p):
    # Incertidumbre paramétrica (Monte Carlo). El uniforme se consume siempre, para que el flujo de
    # números aleatorios no dependa de 'incert' y los escenarios queden sincronizados.
    out = []
    for iv in ivs:
        iv2 = copy.deepcopy(iv)
        for k in sorted(iv2.params):
            u = rng_p.uniform(-1, 1)
            if incert > 0:
                iv2.params[k] = float(np.clip(iv2.params[k] * (1 + incert * u), 0.0, LIMITE_SUP_PARAM.get(k, 0.95)))
        out.append(iv2)
    return out


# ----------------------------------------------------------------------------
# 5. Motor DES
# ----------------------------------------------------------------------------
@dataclass
class Resultado:
    escenario: str
    semilla: int
    crit_t: np.ndarray      # (horas, tramos) criticidad en cada muestreo horario
    flujo_t: np.ndarray     # (horas, tramos) flujo efectivo en veh/h
    n_incidentes: int
    log: list

    def metricas(self, cfg: ConfigSim) -> dict:
        c = self.crit_t
        return {"crit_media": float(c.mean()),
                "crit_p95": float(np.percentile(c, 95)),
                "frac_critica": float((c > cfg.umbral_critico).mean()),
                "crit_max": float(c.max()),
                "n_incidentes": self.n_incidentes}


def simular(red: Red, escenario: Escenario, semilla: int = 0, cfg: Optional[ConfigSim] = None,
            registrar: bool = False) -> Resultado:
    # Tres flujos de números aleatorios independientes -> misma semilla = mismas condiciones
    # externas (demanda, incidentes) en todos los escenarios (números aleatorios comunes).
    cfg = cfg or ConfigSim()
    H, n = cfg.horizonte_h, red.n
    rng_d = np.random.default_rng([semilla, 1])
    rng_i = np.random.default_rng([semilla, 2])
    rng_p = np.random.default_rng([semilla, 3])
    s = cfg.sigma_demanda
    ruido = rng_d.lognormal(-0.5 * s * s, s, size=(H, n))          # media 1
    ivs = _perturbar(escenario.intervenciones, cfg.incertidumbre_parametros, rng_p)

    # --- estado del sistema ---
    base = {"flujo": red.flujo.copy(), "cap": red.cap.copy(),
            "peat": red.peat.copy(), "infra": red.infra.copy(),
            "sev": np.ones(n), "conf": np.ones(n)}             # v0.2.0
    est = {k: v.copy() for k, v in base.items()}
    activas: List[Intervencion] = []
    cap_factor = np.ones(n)
    extra = np.zeros(n)
    hora = [0]
    crit_t = np.zeros((H, n))
    flujo_t = np.zeros((H, n))
    log: list = []

    def recalcular():
        nonlocal est
        est = {k: v.copy() for k, v in base.items()}
        for iv in activas:
            _aplicar(est, iv, red)

    def calcular():
        h = hora[0]
        flujo = est["flujo"] * PERFIL_VEH[h % 24] * ruido[h] + extra
        cap = est["cap"] * cap_factor
        peat = est["peat"] * PERFIL_PEAT[h % 24]
        return flujo, criticidad(flujo, cap, peat, est["infra"], cfg.pesos, est["sev"], est["conf"])

    # --- cola de eventos: (tiempo, prioridad, secuencia, tipo, dato) ---
    cola: list = []
    seq = itertools.count()

    def programar(t, prio, tipo, dato=None):
        heapq.heappush(cola, (t, prio, next(seq), tipo, dato))

    for h in range(H):
        programar(h, 0, "CAMBIO_FRANJA", h)
        programar(h + 0.5, 9, "MUESTREO", h)
    for iv in ivs:
        programar(iv.inicio_h, 1, "INTERV_ON", iv)
        if iv.fin_h < H:
            programar(iv.fin_h, 1, "INTERV_OFF", iv)
    t, n_inc = 0.0, 0
    lam = cfg.tasa_incidentes_dia / 24.0
    while lam > 0:
        t += rng_i.exponential(1 / lam)
        if t >= H:
            break
        programar(t, 5, "INCIDENTE", (rng_i.random(), rng_i.exponential(cfg.duracion_incidente_h)))

    # --- bucle principal: se procesa el evento más próximo hasta vaciar la cola ---
    while cola:
        t, _, _, tipo, dato = heapq.heappop(cola)
        if tipo == "CAMBIO_FRANJA":
            hora[0] = dato
        elif tipo == "INTERV_ON":
            activas.append(dato)
            recalcular()
        elif tipo == "INTERV_OFF":
            activas.remove(dato)
            recalcular()
        elif tipo == "INCIDENTE" and t < H:
            u, dur = dato
            flujo, c = calcular()
            cum = np.cumsum(c + 1e-9)
            k = int(min(np.searchsorted(cum, u * cum[-1]), n - 1))
            vec = red.vecinos[k]
            aporte = cfg.derrame_incidente * flujo[k] / max(1, len(vec))
            cap_factor[k] *= cfg.factor_cap_incidente
            extra[vec] += aporte
            n_inc += 1
            programar(t + dur, 4, "FIN_INCIDENTE", (k, vec, aporte))
            dato = {"tramo": str(red.ids[k]), "dur_h": round(dur, 2)}
        elif tipo == "FIN_INCIDENTE":
            k, vec, aporte = dato
            cap_factor[k] /= cfg.factor_cap_incidente
            extra[vec] = np.maximum(extra[vec] - aporte, 0.0)
            dato = {"tramo": str(red.ids[k])}
        elif tipo == "MUESTREO":
            flujo, c = calcular()
            flujo_t[dato], crit_t[dato] = flujo, c
        if registrar and tipo not in ("MUESTREO", "CAMBIO_FRANJA"):
            log.append({"t_h": round(t, 2), "evento": tipo,
                        "detalle": (dato if isinstance(dato, dict) else
                                    getattr(dato, "tipo", None))})
    return Resultado(escenario.nombre, semilla, crit_t, flujo_t, n_inc, log)


# ----------------------------------------------------------------------------
# 6. Monte Carlo y comparación
# ----------------------------------------------------------------------------
def zonas_escenario(red: Red, esc: Escenario):
    # (tramos intervenidos, zona de influencia = intervenidos + vecinos directos)
    ids = sorted({i for iv in esc.intervenciones for i in iv.objetivo})
    if not ids:
        v = np.array([], dtype=int)
        return v, v
    obj = red.indices(ids)
    infl = np.unique(np.concatenate([obj] + [red.vecinos[k] for k in obj]))
    return obj, infl


def _red_pct(b, e):
    return 100.0 * (b - e) / b if b > 0 else 0.0


@dataclass
class ResultadosMC:
    resumen: pd.DataFrame            # una fila por (escenario, réplica)
    crit_seg: Dict[str, np.ndarray]  # criticidad media por tramo (promedio de réplicas)
    crit_hora: Dict[str, np.ndarray] # criticidad media por hora (promedio de tramos y réplicas)
    objetivos: Dict[str, List[str]]

    def tabla(self) -> pd.DataFrame:
        g = self.resumen.groupby("escenario", sort=False)
        n = g.size()
        t = pd.DataFrame({
            "n_rep": n,
            "crit_media": g["crit_media"].mean(),
            "reduccion_obj_pct": g["reduccion_obj_pct"].mean(),
            "reduccion_infl_pct": g["reduccion_infl_pct"].mean(),
            "ic95_inf": g["reduccion_infl_pct"].mean() - 1.96 * g["reduccion_infl_pct"].std(ddof=1) / np.sqrt(n),
            "ic95_sup": g["reduccion_infl_pct"].mean() + 1.96 * g["reduccion_infl_pct"].std(ddof=1) / np.sqrt(n),
            "reduccion_ciudad_pct": g["reduccion_pct"].mean(),
            "prob_mejora": g["reduccion_infl_pct"].apply(lambda s: float((s > 0).mean())),
            "desplazamiento_max": g["desplazamiento_max"].mean(),
            "segmentos_empeorados": g["segmentos_empeorados"].mean(),
        })
        return t.sort_values("reduccion_infl_pct", ascending=False)


def monte_carlo(red: Red, escenarios: List[Escenario], n_rep: int = 100,
                cfg: Optional[ConfigSim] = None, semilla0: int = 1000) -> ResultadosMC:
    cfg = cfg or ConfigSim()
    base_sc = Escenario("Base", descripcion="Sin intervención")
    escs = [base_sc] + [e for e in escenarios if e.nombre != "Base"]
    objetivos = {e.nombre: sorted({i for iv in e.intervenciones for i in iv.objetivo}) for e in escs}
    es_obj = {e.nombre: np.isin(red.ids, objetivos[e.nombre]) for e in escs}
    zonas = {e.nombre: zonas_escenario(red, e) for e in escs}
    acum_seg = {e.nombre: np.zeros(red.n) for e in escs}
    acum_hora = {e.nombre: np.zeros(cfg.horizonte_h) for e in escs}
    filas = []
    for r in range(n_rep):
        s = semilla0 + r
        rb = simular(red, base_sc, s, cfg)
        mb, seg_b = rb.metricas(cfg), rb.crit_t.mean(0)
        for e in escs:
            res = rb if e.nombre == "Base" else simular(red, e, s, cfg)
            m = res.metricas(cfg)
            seg = res.crit_t.mean(0)
            d = seg - seg_b
            fuera = ~es_obj[e.nombre]
            obj, infl = zonas[e.nombre]
            r_obj = _red_pct(seg_b[obj].mean(), seg[obj].mean()) if len(obj) else 0.0
            r_inf = _red_pct(seg_b[infl].mean(), seg[infl].mean()) if len(infl) else 0.0
            filas.append({"escenario": e.nombre, "rep": r, "semilla": s, **m,
                          "reduccion_obj_pct": r_obj, "reduccion_infl_pct": r_inf,
                          "reduccion_abs": mb["crit_media"] - m["crit_media"],
                          "reduccion_pct": 100 * (mb["crit_media"] - m["crit_media"]) / mb["crit_media"],
                          "desplazamiento_max": float(d[fuera].max()) if fuera.any() else 0.0,
                          "segmentos_empeorados": int((d > 1.0).sum())})
            acum_seg[e.nombre] += seg
            acum_hora[e.nombre] += res.crit_t.mean(1)
    return ResultadosMC(pd.DataFrame(filas),
                        {k: v / n_rep for k, v in acum_seg.items()},
                        {k: v / n_rep for k, v in acum_hora.items()}, objetivos)


# ----------------------------------------------------------------------------
# 7. Análisis de sensibilidad
# ----------------------------------------------------------------------------
def _con_parametro(esc: Escenario, cfg: ConfigSim, clave: str, valor: float):
    # Claves: "cfg.sigma_demanda"  |  "iv0.fraccion_desvio" (intervención 0, parámetro ...)
    esc, cfg = copy.deepcopy(esc), copy.deepcopy(cfg)
    if clave.startswith("cfg."):
        setattr(cfg, clave[4:], valor)
    else:
        i, p = clave[2:].split(".", 1)
        esc.intervenciones[int(i)].params[p] = valor
    return esc, cfg


def _valor_central(esc: Escenario, cfg: ConfigSim, clave: str) -> float:
    if clave.startswith("cfg."):
        return float(getattr(cfg, clave[4:]))
    i, p = clave[2:].split(".", 1)
    return float(esc.intervenciones[int(i)].params[p])


def reduccion_media_pct(red, esc, cfg, n_rep=30, semilla0=5000) -> float:
    # Métrica de sensibilidad: reducción media de criticidad en la zona de influencia (%).
    base = Escenario("Base")
    _, infl = zonas_escenario(red, esc)
    v = []
    for r in range(n_rep):
        s = semilla0 + r
        cb = simular(red, base, s, cfg).crit_t.mean(0)[infl].mean()
        ce = simular(red, esc, s, cfg).crit_t.mean(0)[infl].mean()
        v.append(_red_pct(cb, ce))
    return float(np.mean(v))


def sensibilidad_oat(red, esc, cfg, rangos: Dict[str, tuple], n_rep=30, semilla0=5000) -> pd.DataFrame:
    # Un parámetro a la vez (tornado): se mueve cada parámetro a su mínimo y máximo.
    central = reduccion_media_pct(red, esc, cfg, n_rep, semilla0)
    filas = []
    for clave, (lo, hi) in rangos.items():
        r = []
        for v in (lo, hi):
            e2, c2 = _con_parametro(esc, cfg, clave, v)
            r.append(reduccion_media_pct(red, e2, c2, n_rep, semilla0))
        filas.append({"parametro": clave, "valor_central": _valor_central(esc, cfg, clave),
                      "min": lo, "max": hi, "reduccion_en_min": r[0], "reduccion_en_max": r[1],
                      "reduccion_central": central, "rango_abs": abs(r[1] - r[0])})
    return pd.DataFrame(filas).sort_values("rango_abs", ascending=False).reset_index(drop=True)


def sensibilidad_global(red, esc, cfg, rangos: Dict[str, tuple], n_muestras=64, n_rep=8,
                        semilla=7) -> pd.DataFrame:
    # Todos los parámetros varían a la vez (hipercubo latino); se mide la correlación de rangos (Spearman).
    from scipy.stats import qmc, spearmanr
    claves = list(rangos)
    lo = np.array([rangos[k][0] for k in claves])
    hi = np.array([rangos[k][1] for k in claves])
    X = qmc.scale(qmc.LatinHypercube(d=len(claves), seed=semilla).random(n_muestras), lo, hi)
    y = []
    for fila in X:
        e2, c2 = esc, cfg
        for k, v in zip(claves, fila):
            e2, c2 = _con_parametro(e2, c2, k, float(v))
        y.append(reduccion_media_pct(red, e2, c2, n_rep, 9000))
    y = np.array(y)
    rho = [spearmanr(X[:, j], y)[0] for j in range(len(claves))]
    out = pd.DataFrame({"parametro": claves, "spearman": rho})
    out["abs"] = out["spearman"].abs()
    return out.sort_values("abs", ascending=False).reset_index(drop=True)


# ----------------------------------------------------------------------------
# 8. Contrato de intercambio (JSON) para el dashboard / API
# ----------------------------------------------------------------------------
def _resolver_objetivo(red: Red, obj) -> List[str]:
    return seleccionar_objetivo(red, **obj) if isinstance(obj, dict) else list(obj)


def escenario_desde_dict(red: Red, d: dict) -> Escenario:
    ivs = [Intervencion(tipo=i["tipo"], objetivo=_resolver_objetivo(red, i["objetivo"]),
                        params=i.get("params", {}), inicio_h=i.get("inicio_h", 0.0),
                        fin_h=i.get("fin_h", 24.0)) for i in d.get("intervenciones", [])]
    return Escenario(d["nombre"], ivs, d.get("descripcion", ""))


def resultados_a_dict(red: Red, mc: ResultadosMC, cfg: ConfigSim) -> dict:
    tabla = mc.tabla().reset_index()
    seg = []
    base = mc.crit_seg["Base"]
    for nombre, arr in mc.crit_seg.items():
        for i in range(red.n):
            seg.append({"id_segmento": str(red.ids[i]), "id_zona": str(red.zona[i]),
                        "escenario": nombre, "criticidad_media": round(float(arr[i]), 3),
                        "delta_vs_base": round(float(arr[i] - base[i]), 3)})
    return {"esquema": ESQUEMA_RESULTADOS, "version_modulo": VERSION,
            "generado": datetime.now().isoformat(timespec="seconds"),
            "configuracion": asdict(cfg),
            "escenarios": json.loads(tabla.round(4).to_json(orient="records")),
            "resultados_segmento": seg}


def ejecutar_desde_dict(red: Red, payload: dict) -> dict:
    # Punto de entrada para una API: recibe JSON de configuración y devuelve JSON de resultados.
    cfg = ConfigSim(**payload.get("cfg", {}))
    escs = [escenario_desde_dict(red, e) for e in payload["escenarios"]]
    mc = monte_carlo(red, escs, n_rep=payload.get("n_rep", 50), cfg=cfg,
                     semilla0=payload.get("semilla", 1000))
    return resultados_a_dict(red, mc, cfg)
