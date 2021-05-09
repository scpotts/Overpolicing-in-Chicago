#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:05:32 2021

@author: stephaniepotts
"""

# Importing necessary modules
import pandas as pd
import geopandas

# Reading the Crime.csv file into a dataset
crime = pd.read_csv("Crimes_-_Map.csv")

# Dropping unnecessary columns so there is only the description of the crime and
# the police beat it occurred in
crime = crime.drop(columns=["CASE#", "DATE  OF OCCURRENCE", "BLOCK", " IUCR",
                            " SECONDARY DESCRIPTION", " LOCATION DESCRIPTION",
                            "ARREST", "DOMESTIC", "WARD", "FBI CD", "X COORDINATE",
                            "Y COORDINATE", "LATITUDE", "LONGITUDE", "LOCATION"])

# Renaming columns to more convenient names
crime = crime.rename(columns={" PRIMARY DESCRIPTION":"crime_desc",
                              "BEAT":"beat"})

# Printing a list of all the different types of crimes listed under crime_desc
print( crime['crime_desc'].value_counts() )

indexNames = crime[~(crime['crime_desc'] == 'BATTERY')].index
crime.drop(indexNames, inplace=True)

crime.to_csv("crimestats.csv")

d = {'beat': ,
     'battery_count': }

