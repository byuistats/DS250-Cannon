# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:49:27 2019

@author: matthewz
"""

import requests
import pandas as pd
import time
from math import ceil
import json

s= requests.session()
url_base = "http://www.ratemyprofessors.com/paginate/professors/ratings?tid={}&page={}"

raw_data=pd.read_csv('RateMyProfessorCleaned.csv')

raw_data = raw_data.to_dict(orient='record')


for i,prof in enumerate(raw_data):
    N_Pages = ceil(prof['N Ratings']/20)
    
    reviews = []
    
    for page in range(N_Pages):
        time.sleep(.05)
        result = s.get(url_base.format(prof['ID'],page+1))
        reviews+=result.json()['ratings']
    raw_data[i]['Reviews'] = reviews
    print('Finished '+prof['Name'])

with open('all_ratings.json','w') as f:
    json.dump(raw_data,f)