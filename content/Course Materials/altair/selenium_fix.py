# %%
#import the usual libraries
import pandas as pd
import altair as alt 
from altair_saver import save
from selenium import webdriver


#%%
#Use pandas to read the csv file
names = pd.read_csv("names_year.csv")

#%%
# Filter the names file to see uses of the name Stephen
stephen = names.query('name == "Stephen"')


#%%
# Create a line chart of the queried data to show the trend of my
#name through time.
chart = (alt.Chart(stephen,
        title = "Uses of the name Stephen peaked in the 1950s")
    .encode(
        alt.X ("year:O"),
        alt.Y ("Total"))
    .mark_line()
)
chart

#Use webdriver to save chart as png
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
filename = "chart.png"
save(chart, filename, method="selenium", webdriver=driver)