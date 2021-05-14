# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Summary

This analysis aims to join Census data, police beat data, and Chicago Police 
Department (CPD) crime and arrest data to understand more deeply how biased
policing data can influence future data-driven policing strategies. It is 
commonly understood and accepted that if an entity uses biased data to create
an algorithm, the algorithm will perpetuate those same biases. This analysis
demonstrates exactly where and how CPD arrest and crime data has geographical
(and potential racial and class biases) which might negtaively influence
the equity of future data-driven policing efforts in the City of Chicago.

### Input Data

There are four files to be downloaded to conduct this analysis: 2 shapefiles 
and 2 .csv files containing crime and arrest data.

The first data sources needed to be downloaded are shapefiles that map out the 
boundaries of Census tracts and police beats being used in this analysis. The 
first, a Census shapefile that provides the boundaries of the 2010 Census tracts 
in Cook County, IL (the county the city of Chicago is located in). The file can 
be downloaded from the following URL:

https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2010&layergroup=Census+Tracts

To download the shapefile, select Illinois from the drop-down menu under 'Census
Tract (2010)', then select Cook County under the 'Select a County:' drop-down
menu. Then hit the download button to download the shapefile. It will be named
**tl_2010_17031_tract10.zip**.

The second shapefile to be downloaded contains the boundaries of police beats,
which is a specific assigned territory that an officer patrols during their 
shift. This file can be downloaded from the Chicago Office of Public Safety 
Administration's website:

https://gis.chicagopolice.org/datasets/police-beat-boundary-view-1?geometry=-88.732%2C41.651%2C-86.754%2C42.009&selectedAttribute=BEAT_NUMBER

Select the option to download the full dataset from the drop-down menu under
the 'Download' button on the right side of the page to download the shapefile.
When downloaded it will be called **Police_Beat_Boundary_View-shp.zip**.

The next set of files to be downloaded are crime and arrest records kept by the 
Chicago Police Department.

To download data from the Chicago Police Department on crime, go to the 
following URL:

https://data.cityofchicago.org/Public-Safety/Crimes-Map/dfnk-7re6

Click the 'Export' button in the menu at the top left corner of the map, and 
select the 'CSV' option. The file downloaded will be named **Crimes_-_Map.csv**.
This file contains crimes committed in Chicago from one year prior to the 
present day.

The second .csv file to be downloaded for the analysis is a record of all 
arrests recorded in Chicago between 2014 and 2017, which is the most recent data 
on arrests the CPD has released to the public. For the purposes of this 
analysis, we will only be looking at arrests that took place in 2017 to stay
as close as possible to current crime trends. The data can be downloaded from 
the following link:

https://home.chicagopolice.org/statistics-data/public-arrest-data/

Click the 'Click Here To Download Arrest Data' button at the bottom of the page,
and the file will download as **PublicReleaseArrestDataUPDATE.csv**.

### Output Files

**housing.py**

This script produces a .csv file that, when joined to the **tl_2010_17031_tract10.zip**
shapefile in QGIS and mapped using a graduated layer style, shows housing density 
per Census tract in Cook County, IL. See the files **results.md** for analysis 
of this map.

**race.py**

This script produces a .csv file that, when joined to the **tl_2010_17031_tract10.zip**
shapefile in QGIS and mapped using a graduated layer style, shows the number of 
Black and African American householders per Census tract in Cook County, IL. 
See the files **results.md** for analysis of this map.

**crime.py**

This script produces a .csv file that, when joined to the **Police_Beat_Boundary_View-shp.zip**
file in QGIS by beat number and mapped using a graduated layer style by crime_count,
shows the numbers of any given crime (recorded by the CPD in the last calendar 
year) in the police beat it occured in.

This script, when run, also produces a table of every crime recorded by CPD in
the last calendar year and the number of times each crime occured.

**arrest.py**

This script produces a .csv file that, when joined to the **Police_Beat_Boundary_View-shp.zip**
file in QGIS by beat number and mapped using a graduated layer style by arrest_count,
shows the numbers of all arrests in 2017 in the police beat they occured in.

**population.png**

This map was produce by **housing.py** joined on to **tl_2010_17031_tract10.zip**
and details the number of housing units per Census tract in Cook County, IL. This
map can be created after joining the two files in QGIS and constructing the map 
with the graduated layer settings, and saved as **population.png**.

**race_pop.png**

This map was produce by **race.py** joined on to **tl_2010_17031_tract10.zip**
and details the number of Black householders per Census tract in Cook County, IL. 
This map can be created after joining the two files in QGIS and constructing the 
map with the graduated layer settings, and saved as **race_pop.png**.

**battery_map.png**

This map was produce by **crime.py** joined on to **Police_Beat_Boundary_View-shp.zip**
and details the number of batteries by police beat in Chicago, IL. This map can 
be created by changing line 41's field that specifies which crime to track to 
"BATTERY". This map can be created after joining the two files in QGIS and 
constructing the map with the graduated layer settings, and saved as **battery_map.png**.

**narcotics_map.png**

This map was produce by **crime.py** joined on to **Police_Beat_Boundary_View-shp.zip**
and details the number of narcotics-related crimes tracked by police beat in 
Chicago, IL. This map can be created by changing line 41's field that specifies 
which crime to track to "NARCOTICS". This map can be created after joining the 
two files in QGIS and constructing the map with the graduated layer settings, 
and saved as **narcotics_map.png**.

**arrest_map.png**

This map was produce by **arrest.py** joined on to **Police_Beat_Boundary_View-shp.zip**
and details the number of arrests recorded by police beat in Chicago, IL in 2017. 
This map can be created after joining the two files in QGIS and constructing 
the map with the graduated layer settings, and saved as **narcotics_map.png**.











