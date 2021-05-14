#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:05:32 2021

@author: stephaniepotts
"""

# Importing necessary modules
import pandas as pd

# Reading the CPD Crime .csv file into a dataset
crime = pd.read_csv("Crimes_-_Map.csv", dtype={'BEAT':str})

# Making the values in the 'BEAT' column four digits long (adding in a leading 
# zero here)to match the formatting in the beat boundary shapefile.
crime['BEAT'] = crime['BEAT'].str.zfill(4)

# Dropping unnecessary columns so there is only the description of the crime and
# the police beat it occurred in.
crime = crime.drop(columns=["CASE#", "DATE  OF OCCURRENCE", "BLOCK", " IUCR",
                            " SECONDARY DESCRIPTION", " LOCATION DESCRIPTION",
                            "ARREST", "DOMESTIC", "WARD", "FBI CD", "X COORDINATE",
                            "Y COORDINATE", "LATITUDE", "LONGITUDE", "LOCATION"])

# Renaming columns to more convenient names
crime = crime.rename(columns={" PRIMARY DESCRIPTION":"crime_desc",
                              "BEAT":"beat"})

# Printing a list of all the number of each type of crime recorded by the CPD 
# in the last year
print( crime['crime_desc'].value_counts() )

# Below, where 'BATTERY' is listed in line 41, any crime in the printed list produced by
# line 28 can be entered here so it may be joined to the police beat boundary
# map in QGIS. This will then produce a map of the dispersion of this crime
# in the city by police beat.

# Lines 41 and 42 work to drop any undesired crimes from the dataframe. Any crime
# plugged into line 37 where 'BATTERY' is will be kept in the resulting file.
indexNames = crime[~(crime['crime_desc'] == 'BATTERY')].index
crime.drop(indexNames, inplace=True)

# Grouping the number of crimes by the beat they occured in
num_bat = crime.groupby('beat').size()

# Naming the column containing the number of crimes per beat 'crime_count'
num_bat.name = "crime_count"

# Saving the number of crimes committed by beat they occured in to the .csv file
# 'beat_crime.csv'
num_bat.to_csv("beat_crime.csv")
