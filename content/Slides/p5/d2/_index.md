---
title: "Day 2: Star Wars and strings"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!
#### Announcements
#### What's something you're grateful for today?

<br>

## The `.str` functions in pandas

> - `.str.strip`: [Strip white space](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html)
> - `.str.replace`: [replace one string of characters with another.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
> - `.str.split`: [Separate a character string into two values.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html)
> - `.str.join`: [Join two lists together](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.join.html#pandas.Series.str.join)
> - [Python for Data Science: Strings](https://byuidatascience.github.io/python4ds/strings.html)
> - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#method-summary)

<br>

#### `.str.strip()`

```python
s = pd.Series(['1. Ant.  ', '2. Bee!\n', '3. Cat?\t', '4. Beat?\t', np.nan])

s.str.strip()

s.str.strip('123.!? \n\t')

s.str.strip('1234.!? \n\t')

```

<br>

#### `.str.replace()`

```python
s.str.replace('Ant.', 'Man')
s.str.replace('a', 8)
s.str.replace('a', '8')
s.str.replace('a', '8', case = False)
s.str.replace('a|e', '8', case = False)

s.str.replace('\d', '', case = False)

```

<br>

#### `.str.split()`

```python
s2 = pd.Series(['1-20', '21-50', '51-80', '81-100', np.nan])
s3 = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)

s2.str.split()
s3.str.split()
s2.str.split(pat="-")
```

<br>

#### `.str.join()` or `.str.cat()`

```python
two_columns = s2.str.split("-", expand = True).rename(
   columns = {0: 'minimum', 1: 'maximum'})

two_columns.fillna("").agg("__".join, axis = 1)

two_columns.minimum.str.cat(two_columns.maximum, sep = "__")

```

<br>

## Fixing the column names

Here is some code to get you started:

```{python}
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

starwars_data = pd.read_csv(url, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 2, header = None)

starwars_cols.iloc[0,:].str.upper().str.replace(" ", "!")
```

<br>

## Validating statistical summaries

`len()`, `.query()`, and `.value_counts()` will be your friends.


<!-----------------------------------------------------
### Cleaning our data

#### What do we want our column names to look like?

_Run the two cells below and tell me what we have._

```python
# %%
import pandas as pd
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'
starwars = pd.read_csv(url, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 2, header = None)

starwars_cols

# %%
# This is not complete.
# And maybe not even a good idea....
column_names_1 = starwars_cols.iloc[0,:]
column_names_1 = (column_names_1
                  .replace("Have you seen any of the 6 films in the Star Wars franchise?", "have_seen_any")
                     .replace("Which of the following Star Wars films have you seen? Please select all that apply.", "seen_")
                     .replace("Which character shot first?", "shot_first")
                     .str.replace(" ", "_")
                     .str.replace("Œæ", "")
                     .str.upper()
                     .fillna(method = "ffill"))
print(column_names_1)

column_names_2 = starwars_cols.iloc[1,:]
column_names_2 = (column_names_2
                   .replace("Response", "")
                   .str.replace("Star Wars: Episode ", "")
                   .str.replace(" ", "_")
                   .fillna("")
                   .str.upper())
print(column_names_2)

full_column_names = column_names_1 + column_names_2
print(full_column_names)
```
----------------------------------------->
<br>

## Validating visuals

You're going to make a lot of bar charts!

- [Simple bar chart](https://plotly.com/python/bar-charts/) tutorial.

