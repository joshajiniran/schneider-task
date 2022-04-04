import sys
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import LineString, MultiLineString, Point
import numpy as np


try:
    kml_file = sys.argv[1]
except IndexError:
    print("No KML file supplied, kindly supply one")
    exit()

gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
map_data = gpd.read_file(kml_file, driver="KML")

lats = []
lons = []

for feature in map_data.geometry:
    if isinstance(feature, LineString):
        linestrings = [feature]
    elif isinstance(feature, MultiLineString):
        linestrings = feature.geoms
    else:
        continue

    for linestring in linestrings:
        x, y = linestring.xy
        lats = np.append(lats, y)
        lons = np.append(lons, x)

geom = [Point(xy) for xy in zip(lons, lats)]
gdf = gpd.GeoDataFrame(geometry=geom, crs={'init': 'epsg:4326'})

gdf.to_crs(epsg=32663, inplace=True)
total_distance = gdf.distance(gdf.shift())
print(f'{total_distance/1000}km')
