# %%
# Loading modules
"""
Contains code that completes the Clean Movies skill builder. Note there are
many ways to accomplish the exercises! Spend time running each piece of code individually
and really understanding what's going on.
"""
import pandas as pd
import numpy as np
import altair as alt

# %%
# Loading in data
url = ""
data = pd.read_csv(url)

print(data.head(5).to_markdown(index=False))

# %%
#### Exercise 1 ####
# Splitting the column into two where the second column only contains the high range number.
# Print range_columns to see what this code did
range_columns = data.box_office_rev.str.split("- €", expand=True)

# Grabbing the second column and saving into our original dataframe with correct column name
# Changing data type to numeric! It was previously a string
data["high_range_rev"] = range_columns[1].astype(int)

# Dropping the old revenu column
data.drop("box_office_rev", axis=1, inplace=True)

print(data.head(5).to_markdown(index=False))

# %%
#### Exercise 2 ####
data['major_hit'] = np.where(data.major_hit == "yes", 1, 0)

print(data.head(5).to_markdown(index=False))

# %%
#### Exercise 3 ####

# Creating dictionary that maps rating to a number
ratings_dict = {
    "G": 0,
    "PG": 1,
    "PG-13": 2,
    "R": 3
}

# Using map method to convert the strings to their corresponding numbers and saving back into content_rating column
data["content_rating"] = data.content_rating.map(ratings_dict)

print(data.head(5).to_markdown(index=False))

# %%
#### Exercise 4 ####

# One hot encoding the genre column
data2 = pd.get_dummies(data, columns=["genre"])
# print(data2.head(5).to_markdown())

# %%
#### Exercise 5 ####

# Creating a fun graphic
# Using the five thirty eight theme
alt.themes.enable('fivethirtyeight')

# Getting the percentage of movies by rating
chart_data = data.content_rating.value_counts(normalize=True).reset_index()

# Chart specs
title = "Rated R movies are by far the most frequent"
chart = alt.Chart(chart_data, title=title).mark_bar().encode(
    alt.X("content_rating", title="Percentage of Movies", axis=alt.Axis(format=".0%")),
    alt.Y("index", title="Rating", sort='-x')
).properties(height=200)

chart.save("movie_sb.png")
