# %%
# The usuals
import pandas as pd
import numpy as np
import altair as alt 

# %%
# project 2
import urllib3
import requests
import json

url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"

# %%
# urlib3 and json
http = urllib3.PoolManager()
response = http.request('GET', url)
cars_json = json.loads(response.data.decode('utf-8'))
# %%
req_cars_json = requests.get(url).json()

# %%

cars = pd.DataFrame.from_dict(req_cars_json)
cars = pd.DataFrame.from_dict(cars_json)
# %%
cars = pd.json_normalize(cars_json) 
cars = pd.json_normalize(req_cars_json) 


# %%
# missing data
df = (pd.DataFrame(
    np.random.randn(5, 3), 
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three'])
  .assign(
    four = 'bar', 
    five = lambda x: x.one > 0,
    six = [np.nan, np.nan, 2, 2, 1],
    seven = [4, 5, 5, np.nan, np.nan])
  )
# %%
df.seven + df.six
# %%
df.seven.sum()
# %%
df.seven.fillna(0) + df.six.fillna(0)
# %%
