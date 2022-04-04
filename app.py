import sys
from dataclasses import dataclass
from enum import unique

import geopandas as gpd
import pandas as pd
from fiona.errors import DriverError
from pykml import parser
from pykml.factory import nsmap
from shapely.geometry import Point

namespace = {'ns': nsmap[None]}

@dataclass
class InvalidKMLFileError(Exception):
    file: str

try:
    kml_file = sys.argv[1]
    if not (kml_file.endswith('.kml') or kml_file.endswith('.kmz')):
        raise InvalidKMLFileError(kml_file)

    # open kml file and parse with pykml
    with open(kml_file, 'r', encoding="utf-8") as kml_file:
        root = parser.parse(kml_file).getroot()
        placemarks = root.xpath(".//ns:Placemark[.//ns:LineString]", namespaces=namespace)
except IndexError:
    print("No KML file supplied, kindly supply one")
    exit()
except InvalidKMLFileError as e:
    print(f"File is not a proper KML: {e.file}")
    exit()
except DriverError:
    print(f"File does not exist")
    exit()
    
# filter out duplicate datapoints
unique_points = {place for place in root.Document.Folder.Placemark.LineString.coordinates[0].text.split()}

# create tuple of (lon, lat) from unique_points
df_points = [(float(coord.split(",")[0]), float(coord.split(",")[1])) for coord in unique_points]

geom = [Point(xy) for xy in df_points]
gdf = gpd.GeoDataFrame(geometry=geom, crs="EPSG:4326")
gdf.to_crs(epsg=32663, inplace=True)
dis = gdf.distance(gdf.shift()).sum() / 1000
print("{:.2f}km".format(dis))
