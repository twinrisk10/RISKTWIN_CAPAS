CREATE TABLE fuente (
  fuente_id   TEXT PRIMARY KEY,
  nombre      TEXT NOT NULL,
  tesis       TEXT NOT NULL
);
CREATE TABLE zona (
  id_zona     TEXT PRIMARY KEY CHECK (id_zona GLOB 'IND-Z[0-9][0-9]'),
  nombre      TEXT NOT NULL UNIQUE,
  area_m2     REAL CHECK (area_m2 > 0)
);
CREATE TABLE incidente (
  id_evento     TEXT PRIMARY KEY,
  fecha         TEXT NOT NULL,                                   -- ISO 8601
  id_zona       TEXT NOT NULL REFERENCES zona(id_zona),
  tipo_evento   TEXT NOT NULL,
  severidad     INTEGER NOT NULL CHECK (severidad BETWEEN 1 AND 4),
  dias_perdidos INTEGER CHECK (dias_perdidos >= 0),
  fuente_id     TEXT NOT NULL REFERENCES fuente(fuente_id),
  tipo_dato     TEXT NOT NULL CHECK (tipo_dato IN ('real', 'sintetico'))
);
CREATE INDEX ix_incidente_zona_fecha ON incidente(id_zona, fecha);
CREATE TABLE indicador_riesgo (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  id_zona           TEXT NOT NULL REFERENCES zona(id_zona),
  periodo           TEXT NOT NULL,                               -- AAAA-MM
  indice_frecuencia REAL NOT NULL CHECK (indice_frecuencia >= 0),
  indice_gravedad   REAL NOT NULL CHECK (indice_gravedad >= 0),
  exposicion_horas  REAL NOT NULL CHECK (exposicion_horas > 0),
  nivel_riesgo      TEXT NOT NULL CHECK (nivel_riesgo IN ('bajo', 'medio', 'alto', 'critico')),
  fuente_id         TEXT NOT NULL REFERENCES fuente(fuente_id),
  UNIQUE (id_zona, periodo)
);
CREATE TABLE observacion_hev (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  id_zona     TEXT NOT NULL REFERENCES zona(id_zona),
  periodo     TEXT NOT NULL,
  id_variable TEXT NOT NULL,
  componente  TEXT NOT NULL CHECK (componente IN ('H', 'E', 'V')),
  valor       REAL,
  tipo_dato   TEXT NOT NULL,
  UNIQUE (id_zona, periodo, id_variable)
);
