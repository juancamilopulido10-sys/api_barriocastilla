import geopandas as gpd
from sqlalchemy import create_engine

gdf = gpd.read_file(r"C:\Users\Usuario\Downloads\barriocastilla\castilla.geojson")
print("Elementos leídos:", len(gdf))

engine = create_engine("postgresql://postgres:camilo90@localhost:5432/castilla")
gdf.to_postgis("castilla_osm", engine, if_exists="replace")
print("Datos cargados en PostGIS: tabla castilla_osm")