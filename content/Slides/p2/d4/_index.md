---
title: "Day 4: Exporting JSON"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

## Spiritual Thought
  - Silver Rule
  - Matthew 19:16-22
  - Camel through the eye of the needle =>  
    - "with men this is impossible..."

#### Announcements

<br>

## Question 5

Let's do an example of question 5 using the `mtcars` data.

### Load packages and data

```python
#%%
import pandas as pd
import numpy as np
import json

url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)
```

<br>

### Find all the missing values

```python
#%%
# method 1: find "official" null values
# hp, wt, and vs
cars.isnull().sum()

#%%
# method 2: just look at the data
# car, hp, wt, vs, gear
cars.head(10)

#%%
# method 3: look at summaries
# the values in 'gear' look funny
cars.describe()

#%%
# method 4: count up categories
# looks like 4 rows are blank
cars.car.value_counts()
```

<br>

### Reformat the missing values

Remember, you need to reformat your missing values to make them consistent!

**Reading the examples in the [`replace` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html) might give you some ideas.**

```python
#%% 
# There are a lot of functions
# we could use to give the missing values
# a consistent format.

# `replace()` is one of the easiest
# let's change everything to np.nan
cars_new = cars.replace(999, np.nan).replace("", np.nan)

# or equivalently:
cars_new = cars.replace([999, ""], np.nan)


# did we get them all?
cars_new.isnull().sum()
```
<br>

### Saving JSON files from a pandas dataframe

You can save a DataFrame as a JSON file like this:

```python
#%%
# save the new data as a json
cars_new.to_json("my_cars_data.json")
```

The [df.to_json() documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) shows us how to change the way the JSON file is organized. (By row? By column? etc.) 

This is the format we would like to see in the report:

```JS
[
  {
    "car": "Mazda RX4",
    "mpg": 21,
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.62,
    "qsec": 16.46,
    "vs": 0,
    "am": 1,
    "gear": 4,
    "carb": 4
  }
]
```

And here are the various options:

```python
# %%
# Question 5 wants us to "include one record example"
# in our md report that "has a missing value"

# you can print out a json file like this:
json_data = cars_new.to_json()
print(json_data)

# but that won't look good in our report.
# instead....

#%%
# you can do this.
# in this format, the json file is
# organized/printed by column
json_data = cars_new.to_json()
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)

# %%
# we can change the format of the
# json file using 'orient'
json_data = cars.to_json(orient="split")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)

# %%
# by table
json_data = cars.to_json(orient="table")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)

# %%
# by "record" or "row"
json_data = cars.to_json(orient="records")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)
```
