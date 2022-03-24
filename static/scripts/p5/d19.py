# %%
import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat = pd.read_csv(url)

# %%
# https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python

dat_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 1).melt()
dat = pd.read_csv(url, skiprows =2, header = None )

