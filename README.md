# KML Sensor Distance Calculator

A Python script that calculates total distance in kilometres, from a KML datafile.

## Description

The Script accepts a KML file as a parameter, processes it and filters out ambiguous coordinates, and sums up the total distance in kilometers which is given in the output.

The filtering logic is based on the python's set data structure and transformation of the coordinate reference system (CRS) used in GeoPandas on the data file from EPSG:4326 - WGS 84 (longitude/latitude) to EPSG:32663 - WGS 84 (World Equidistant Cylindrical) to give result in metres/km.

## Getting Started

### Dependencies

* The python script was tested on Linux Ubuntu 20.04 and Python 3.10.1.
* Python 3.8+
* pykml (already in requirements.txt)
* geopandas (already in requirements.txt)

### Installing

* The python script can be downloaded from [Github](https://github.com/joshuajiniran/schneider-task.git)
* Or cloned using
```
git clone https://github.com/joshajiniran/schneider-task.git
```

### Executing the script

* You can create a virtual environment to avoid install requirements in system wide location.
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python script.py <kml_file.kml> or python script.py <kml_file.kmz>
```
* Ensure the KML file is in the same location with the script.py file.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Joshua Ajiniran  

## Version History
* 1.0 (coming)
    * Process other files such as .shp, zip. .csv with KML data
    * Process multiple Folders/Placemarks/coordinates in a KML file.
* 0.1
    * Initial Release