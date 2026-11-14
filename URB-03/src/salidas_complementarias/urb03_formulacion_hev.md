# URB-03 · Formulación del índice H–E–V (documento matemático)

Generado por `Indice_criticidad_urbana_Guayaquil_piloto_COMPLEMENTARIO.ipynb`, Parte C. Datos: sintetico, 12 zonas.

## Definiciones
- Zonas: identificador común PER-Z## (COMUN/zonas_perimetral.geojson).
- Riesgos r: accidentes_viales, seguridad_urbana, inundaciones.
- Variables: 19 (COMUN/matriz_variables_hev.csv), cada una asignada a un riesgo y un componente H, E o V, con sentido + o −.

## Normalización
- N1 min-max: x' = (x − min) / (max − min)
- N2 z-score + Φ: x' = Φ((x − media) / desviación)
- Sentido −: x' ← 1 − x'

## Componentes
C(z, r) = promedio de x' de las variables del riesgo r y componente C ∈ {H, E, V}

## Agregación por riesgo (pesos w_H + w_E + w_V = 1)
- A, aditiva ponderada: R_A = w_H·H + w_E·E + w_V·V
- B, multiplicativa geométrica: R_B = max(H, ε)^w_H · max(E, ε)^w_E · max(V, ε)^w_V, con ε = 0.01

## Índice global
IC(z) = Σ_r α_r · R(z, r), con Σ α_r = 1

## Niveles
bajo < 0,25 ≤ medio < 0,50 ≤ alto < 0,75 ≤ crítico

## Pesos base
w_H = w_E = w_V = 1/3; α_r = 1/3 (neutrales y provisionales).

## Resultados de la ejecución
- Spearman mínimo entre las 4 combinaciones de normalización y agregación: 0.965
- Spearman mínimo en la sensibilidad ±30 %: aditiva 0.937, multiplicativa 0.937
- Top-3 (aditiva, min-max): PER-Z10, PER-Z02, PER-Z05
