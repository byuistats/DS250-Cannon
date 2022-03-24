# %%
import pandas as pd
import numpy as np
import altair as alt 
import urllib3
import requests
import json

# %%
url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)

# %%
# the long way to help us understand json files and 
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)

# %%
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman', np.nan],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip',np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT, pd.NaT],
                    "power": [np.nan, np.nan, np.nan, np.nan]})
# %%
# When would we ever use `df.dropna()`?
# almost never
df.dropna()
# %%
df.dropna(how = 'all')
# %%
df.dropna(how = 'all', axis = 1).dropna(how='all', axis=0)
# %%
df.dropna(thresh = 2)
# %%
# thresh applies to the subset
df.dropna(subset = ['name', 'toy'], thresh = 2)
# %%
# What if we want to replace all the `NA` values with 
# the mean weight in the `wt` column of the cars data?
cars.wt.fillna(cars.wt.mean())

fill_values = {'wt':cars.wt.mean(), 'hp':cars.hp.mean()}

cars.fillna(value = fill_values)

# %%
# What if we want to replace all the `999` values 
# with `4` in the cars data?
cars.replace(999, 4)

# %%
# fancy
by_c_values = {'car': {'':'missing', 'Merc 230': 'Mercedes 230'}, 'gear': {999:4}}
cars.replace(by_c_values)

# %%
# What if we want to replace all 
# the `NAs` with a linear interpolation?

s = pd.Series([0, 1, np.nan, 3])
s2 = pd.Series([0, 1, np.nan, 3, np.nan, 8, np.nan, 6])
# %%
s.interpolate()
s2.interpolate()
# %%
# Suppose that the missing car names should be the value preceding it in the table (which is not correct).

cars.car.fillna(method='ffill') # doesn't work
cars.car.replace('',np.nan).fillna(method='ffill') # works

# %%
# How many rows have missing months?

flights.month.value_counts()

# %%
#Can we figure out any patterns in the missingness?
pd.crosstab(
    flights.month, 
    flights.airport_code)

pd.crosstab(
    flights.month,
    flights.year)

fslc = flights.query('airport_code == "SLC"')
pd.crosstab(
    fslc.month,
    fslc.year)


