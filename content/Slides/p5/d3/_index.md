---
title: "Day 3: Validating data, cleaning columns"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Announcements

* Practice Coding Challenge quesitons

#### Spiritual Thought

* Lotus eaters

## Let's validate some data!

Pick something from [the Star Wars article](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/) you want to validate ("double check").


<!--------------------------------------
These videos (about 13 minutes each) should help answer your questions with Grand Question 1.

- Video: [Renaming columns](https://www.loom.com/share/4408110072d040e592891993bc8c9731)
- Video: [Summarizing data for Altair bar charts](https://www.loom.com/share/db922f92304b494aa43330a234ecf8ff)

And this code will help you get the columns renamed:

```python
# %%
# load packages
import pandas as pd
import altair as alt

# data url
starwars_url = "https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv"

# load data and columns
starwars = pd.read_csv(starwars_url, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(starwars_url, encoding = "ISO-8859-1", nrows = 2, header = None)

# clean up the column names
starwars_cols_clean = (starwars_cols
 .transpose()
 .rename(columns = {0:'pre', 1:'post'})
 .assign(pre = (lambda x: x.pre
                     .replace("Have you seen any of the 6 films in the Star Wars franchise?", "have_seen_any")
                     .replace("Do you consider yourself to be a fan of the Star Wars film franchise?", "fan_star_wars")
                     .replace("Which of the following Star Wars films have you seen? Please select all that apply.", "seen_film_")
                     .replace("Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.", "rank_")
                     .replace("Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.","rank_")
                     .replace("Which character shot first?", "shot_first")
                     .replace("Are you familiar with the Expanded Universe?", "expanded_universe")
                     .replace("Do you consider yourself to be a fan of the Star Trek franchise?", "fan_star_trek")
                     .str.replace("Do you consider yourself to be a fan of the Expanded Universe?", "fan_expanded_universe")
                     .str.replace(" ", "_")
                     .str.replace("[(|)\?]", "")
                     .str.lower()
                     .ffill()),
         
         post = (lambda x: x.post
                 .replace("Response", "")
                 .str.replace("Star Wars: Episode ", "")
                 .str.replace(" ", "_")
                 .fillna("")
                 .str.lower()),
         
         col_names = (lambda x: x.pre.str.cat(x.post, sep="")))
 )

starwars.columns = starwars_cols_clean.col_names
starwars.head()
```
-------------------------------------->

<br>


## Moving from categories to values.

> 1. __Create an additional column(s) that converts the income ranges to a number.__
> 1. __Create an additional column(s) that converts the age ranges to a number.__
> 1. __Create an additional column(s) that converts the school groupings to a number.__

- [str.replace('', '9')](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
- [astype('float')](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html)
- [pd.concat(axis=1)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

<br>


## Validating visuals

You're going to make a lot of bar charts!

- [Simple bar chart](https://altair-viz.github.io/gallery/simple_bar_chart.html) tutorial.
- Make Altair do the counting for you! Tutorials [here](https://altair-viz.github.io/user_guide/transform/aggregate.html) and [here](https://stackoverflow.com/questions/62405935/altair-pandas-value-counts-horizontal-bar-chart).

<br>

## Getting started on Question 3

### One-hot encoding

Project 5 asks you to **"one-hot encode all columns that have categories"** and **"convert all yes/no responses to 1/0 numeric"**.

The `get_dummies` method can be used to create one-hot encoded variables. The [pd.get_dummies documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html) is a great place to start.

After reading the documentation, study the code below and get started on Grand Question #3.

```python
#%%
# When we use machine learning to predict salary,
# let's only look at people that have seen at least
# one star wars film
starwars = starwars.query('have_seen_any == "Yes"')

# Discuss - what's a better way to filter out people 
# who haven't seen star wars?

# %%
# Format columns for machine learning

# Let's try this first: convert categories to "one-hot" encodings
shot_first_onehot = pd.get_dummies(starwars.shot_first)
shot_first_onehot

# What the difference between code above,
# and this? Which one is better?
shot_first_onehot = pd.get_dummies(starwars.shot_first, drop_first=True)
shot_first_onehot

# %%
# 'get_dummies()' can also be used to convert yes/no answers to 0/1

episode_i = pd.get_dummies(starwars.seen_film_i__the_phantom_menace)
episode_i

# %%
episode_i.value_counts()
```

<!-------------------
- [pd.factorize(x)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html)
----------------------->
