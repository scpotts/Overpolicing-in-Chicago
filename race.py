#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:54:41 2021

@author: stephaniepotts
"""

# Importing relevant modules
import pandas as pd
import requests

# Querying 2010 Census
api = 'http://api.census.gov/data/2010/dec/sf1?'

# Extracting Census data at the Census tract level in IL (state 17)
for_clause = 'tract:*'
in_clause = 'state:17'

# Insert your Census data API key here:
key_value = '457ffa1fa904b82b0fd1ed4ee8d53c870945d670'

# Searching for variable H006003 which detects the total number of householders 
# who are Black or African American
payload = {'get': 'H006003',
           'for': for_clause,
           "in": in_clause,
           'key': key_value}

response = requests.get(api, payload)

# Checking status of request
if response.status_code == 200:
    print("Request Succeeded")
else:
    print(response.status_code)
    print(response.text)
    assert False
       
row_list = response.json()

# Creating column of data from response
colnames = row_list[0]
datarows = row_list[1:]

# Creating a dataframe from queried Census data called 'race_total'
race_total = pd.DataFrame(columns=colnames, data=datarows)

# Creating a column in the dataframe that displays the geoid of the Census tract
# by concatenating the IL state FIPS code, the Cook county FIPS code, and the 
# Census tract FIPS code into a single value. This will help us to match the IDs
# when the data is joined in QGIS later
race_total["geoid"] = race_total["state"]+race_total["county"]+race_total["tract"]

# Saving dataframe to a .csv file called 'race_total.csv'. This will display
# the total number of Black householders per Census tract in Cook County
race_total.to_csv("race_total.csv")

