#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:13:28 2021

@author: stephaniepotts
"""

# Import relevant modules
import pandas as pd

# Reading the arrests .csv file
arrest = pd.read_csv("PublicReleaseArrestDataUPDATE.csv", dtype={'ARR_BEAT':str})

# Making the values in the 'ARR_BEAT' column four digits long (adding in a 
# leading zero here)to match the formatting in the beat boundary shapefile.
arrest['ARR_BEAT'] = arrest['ARR_BEAT'].str.zfill(4)

# Dropping unnecessary columns from file so only arrest beat and year are left
arrest = arrest.drop(columns=["ARR_DISTRICT", "ARR_MONTH", "RACE_CODE_CD",
                              "FBI_CODE", "STATUTE", "STAT_DESCR", "CHARGE_CLASS_CD",
                              "CHARGE_TYPE_CD"])

# Renaming columns to more convenient names
arrest = arrest.rename(columns={"ARR_BEAT":"beat",
                              "ARR_YEAR":"year"})

# Lines 29 and 30 drop all arrests from the dataset that did not occur in 2017.
indexNames = arrest[~(arrest['year'] == 2017)].index
arrest.drop(indexNames, inplace=True)

# Grouping the number of arrests by the beat they occured in
num_bat = arrest.groupby('beat').size()

# Naming the column containing the number of arrests per beat 'arrest_count'
num_bat.name = "arrest_count"

# Saving the number of arrests made by beat they occured in to the .csv file
# 'beat_arrest.csv'
num_bat.to_csv("beat_arrest.csv")