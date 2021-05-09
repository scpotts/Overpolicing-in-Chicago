# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Summary

### Input Data

The first dataset containing arrest records will be obtained from The Chicago 
Police Department's website at the following URL:
https://home.chicagopolice.org/statistics-data/public-arrest-data/
This page contains a .csv file that can be downloaded, which contains arrest
records from 2014-2017 in the City of Chicago. This file is organized by beat, 
which we will use to match this data with the other input files.

The second input file is a shapefile of police beat boundaries, which can be 
downloaded from the Chicago Office of Public Safety Administration's website:
https://gis.chicagopolice.org/datasets/police-beat-boundary-view-1?geometry=-88.732%2C41.651%2C-86.754%2C42.009&selectedAttribute=BEAT_NUMBER
We will download the full dataset and attach the data from the inputted .csv files
to the beat boundaries in GIS when we create our crime and arrest maps.

### Output Files


