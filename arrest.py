#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:13:28 2021

@author: stephaniepotts
"""

# Import relevant modules
import pandas as pd

# Reading the arrests .csv file
arrest = pd.read_csv("PublicReleaseArrestDataUPDATE.csv")

# Dropping unnecessary columns from file so only arrest beat and year are left
arrest = arrest.drop(columns=["ARR_DISTRICT", "ARR_MONTH", "RACE_CODE_CD",
                              "FBI_CODE", "STATUTE", "STAT_DESCR", "CHARGE_CLASS_CD",
                              "CHARGE_TYPE_CD"])

count = arrest['ARR_BEAT'].value_counts()
print(count)

indexNames = arrest[~(arrest['ARR_YEAR'] == 2017)].index
arrest.drop(indexNames, inplace=True)

arrest.to_csv("arrest.csv")

