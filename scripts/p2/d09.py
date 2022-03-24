# %%
# import libraries
import pandas as pd 
import numpy as np 
import altair as alt
import urllib3
import json

# %%
# load data
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)
# %%
pd.crosstab(
    flights.month, 
    flights.airport_code)

# %%

def missing_checks(df, column ):
    out1 = df[column].isnull().sum(axis = 0)
    out2 = df[column].describe()
    out3 = df[column].describe(exclude=np.number)
    print('\n\n\n')
    print('Checking column' + column)
    print('\n')
    print('Missing summary')
    print(out1)
    print('\n')
    print("Numeric summaries")
    print(out2)
    print('\n')
    print('Non Numeric summaries')
    print(out3)

missing_checks(flights, 'num_of_delays_nas')
missing_checks(flights, 'num_of_delays_late_aircraft')
missing_checks(flights, 'num_of_delays_weather')    

# %%
flights.num_of_delays_weather.describe()

weather = (flights.assign(
    severe = flights.num_of_delays_weather, # no missing
    nodla_nona = lambda x: (x.num_of_delays_late_aircraft
        .replace(-999, np.nan)), #missing is -999
    mild_late = lambda x: x.nodla_nona.fillna(x.nodla_nona.mean())*0.3,
    mild = np.where(
        flights.month.isin(['April', 'May', 'June', 'July', 'August']), 
            flights.num_of_delays_nas*0.4,
            flights.num_of_delays_nas*0.65),
    weather = lambda x: x.severe + x.mild_late + x.mild,
    proportion_weather_delay = lambda x: x.weather / x.num_of_delays_total,
    proportion_weather_total = lambda x:  x.weather / x.num_of_flights_total)
    .filter(['airport_code','month','year', 'severe','mild', 'mild_late',
    'weather', 'proportion_weather_total', 
    'proportion_weather_delay', 'num_of_flights_total', 'num_of_delays_total']))
