# %%
import pandas as pd 
import altair as alt
import numpy as np
# %%
url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'
dat = pd.read_csv(url)

dat_john = dat.query('name == "John"')

my_data = pd.DataFrame({'year':[1976], 'Total': [20000], 'label':['October, 1976']})
# %%
# How does your name at your birth year compare to its use historically?

# %%
# Histogram

day_1976 = (dat_john
    .query('year == "1976"')
    .filter(['name', 'year', 'OR', 'Total'])
    )

# https://datavizpyr.com/histogram-with-median-line-using-altair-in-python/
mark = (alt.Chart(day_1976)
    .encode(
        alt.X('Total', title = ""),
        size=alt.value(5))
    .mark_rule())


hist = (alt.Chart(dat_john)
    .encode(
        alt.X('Total', bin = alt.Bin(step=3000)),
        alt.Y('count()'))
    .mark_bar()
    .properties(
        title = {
            "text": "Distribution of John birth names by year.",
            "subtitle": "My 1976 birth year marked."
        })
    )

chart = alt.layer(hist, mark).configure_title(anchor = 'start')

chart.save('hist.png')

# %%
# not good
(alt.Chart(dat_john)
    .encode(
        alt.X('Total', bin = alt.Bin(step=3000)),
        alt.Y('count()'),
        alt.Color('year:O', scale=alt.Scale(scheme='dark2')))
    .mark_bar()
    .properties(
        title = {
            "text": "Distribution of John birth names by year.",
            "subtitle": "My 1976 birth year marked."
        })
    )
# %%
