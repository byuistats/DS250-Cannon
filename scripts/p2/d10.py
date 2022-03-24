# %%
import pandas as pd 
import numpy as np 
import json
import urllib3

# %%
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
http = urllib3.PoolManager()
response = http.request('GET', url)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)

# %%
flights.head(10).to_json("test_pandas.json", orient = 'records')

# %%
# https://stackoverflow.com/questions/30912746/pandas-remove-null-values-when-to-json
json_text = json.dumps([row.dropna().to_dict() for index,row in flights.head(10).iterrows()])


# %%
# https://pythonexamples.org/python-write-string-to-text-file/
text_file = open("test_dump.json", "w")
n = text_file.write(json_text)
text_file.close()

# %%
