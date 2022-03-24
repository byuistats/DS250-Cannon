# %%
import pandas as pd 
import numpy as np
import altair as alt

# %%
url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'
dat = pd.read_csv(url)

# %%
pd.unique(dat.name).size

# %%
pd.unique(dat.query('name == "John"').year).min()

# %%
pd.unique(dat.query('name == "John"').year).max()

# %%
pd.unique(dat.query('name == "John"').year).size

# %%
dat_total = dat.groupby('name').agg(n = ('Total', 'sum')).reset_index()

print(dat_total
    .query('n in [@dat_total.n.max(), @dat_total.n.min()]')
    .to_markdown(showindex = False, floatfmt=".0f"))
# %%
