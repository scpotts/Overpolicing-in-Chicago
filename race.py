#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:54:41 2021

@author: stephaniepotts
"""

# Importing relevant modules
import pandas as pd
import requests

api = 'http://api.census.gov/data/2010/dec/sf1?'

for_clause = 'county:031'
in_clause = 'state:17'

key_value = '457ffa1fa904b82b0fd1ed4ee8d53c870945d670'

payload = {'get': 'H006003',
           'for': for_clause,
           "in": in_clause,
           'key': key_value}

response = requests.get(api, payload)

if response.status_code == 200:
    print("Request Succeeded")
else:
    print(response.status_code)
    print(response.text)
    assert False
        
row_list = response.json()

colnames = row_list[0]
datarows = row_list[1:]

race_total = pd.DataFrame(columns=colnames, data=datarows)

race_total.to_csv("race_total.csv")

