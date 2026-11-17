create extension if not exists postgis;

create table if not exists urb01_aforo (
  id_aforo text primary key,
  id_segmento text,
  fecha_hora timestamp,
  vehiculos_hora bigint,
  origen_dato text,
  fuente_id text,
  geom geometry(Point, 4326)
);

create table if not exists urb01_contexto_precipitacion (
  id_registro text primary key,
  fecha date,
  precipitacion_mm double precision,
  id_estacion text,
  origen_dato text,
  fuente_id text,
  geom geometry(Point, 4326)
);

create table if not exists urb01_incidente (
  id_incidente text primary key,
  tipo text,
  subtipo text,
  severidad bigint,
  fecha_hora timestamp,
  origen_dato text,
  fuente_id text,
  geom geometry(Point, 4326)
);

create table if not exists urb01_nodo_vial (
  id_nodo text primary key,
  osmid bigint,
  grado bigint,
  fuente_id text,
  geom geometry(Point, 4326)
);

create table if not exists urb01_poi (
  id_poi text primary key,
  categoria text,
  nombre text,
  fuente_id text,
  geom geometry(Point, 4326)
);

create table if not exists urb01_segmento_vial (
  id_segmento text primary key,
  id_nodo_origen text,
  id_nodo_destino text,
  tipo_via text,
  nombre_via text,
  longitud_m double precision,
  fuente_id text,
  geom geometry(LineString, 4326)
);

create table if not exists urb01_zona_analisis (
  id_zona text primary key,
  nombre text,
  area_km2 double precision,
  fuente_id text,
  geom geometry(Polygon, 4326)
);