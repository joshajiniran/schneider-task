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
my_map = gpd.read_file(kml_file, driver="KML")
my_map.to_crs(epsg=32663, inplace=True)

lats = []
lons = []

for feature in my_map.geometry:
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

geos = [Point(xy) for xy in zip(lons, lats)]
