import sys
import xml.etree.ElementTree as ET

import pandas as pd
from fastkml import kml
from pykml import parser
from pykml.factory import nsmap

try:
    kml_file = sys.argv[1]
except IndexError:
    print("""No KML file supplied, please supply using this format below:
          python app.py <kml_file_name.kml>
          Ensure the kml_file_name.kml is in the same folder as python script!""")
    exit()

with open(kml_file, 'r', encoding="utf-8") as kml_file:
    root = parser.parse(kml_file).getroot()
    

places = set()

for place in root.Document.Folder.Placemark.LineString.coordinates[0].text.split():
    # coords = place.LineString.coordinates.text.strip(" ")
    places.add(place)
    

print([coord for coord in places])
