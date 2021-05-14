#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:11:07 2021

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

# Searching for variable H001001 which detects the total number of housing 
# units in a given area
payload = {'get': 'H001001',
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

# Creating columns of data from response
colnames = row_list[0]
datarows = row_list[1:]

# Creating a dataframe from queried Census data called 'housing_total'
housing_total = pd.DataFrame(columns=colnames, data=datarows)

# Creating a column in the dataframe that displays the geoid of the Census tract
# by concatenating the IL state FIPS code, the Cook county FIPS code, and the 
# Census tract FIPS code into a single value. This will help us to match the IDs
# when the data is joined in QGIS later
housing_total["geoid"] = housing_total["state"]+housing_total["county"]+housing_total["tract"]

# Saving dataframe to a .csv file called 'housing_total.csv'. This will display
# the total number of housing units per Census tract in Cook County
housing_total.to_csv("housing_total.csv")