# %%
import pandas as pd 
import altair as alt
import numpy as np

# %%
# handgrenade data https://github.com/byuidatascience/data4soils/blob/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv
url = 'https://github.com/byuidatascience/data4soils/raw/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv'
dat = pd.read_csv(url)
# %%
# plot each samples hmx and rdx value
alt.Chart(dat).encode(x = 'hmx', y = 'rdx').mark_circle()

# %%
# plot the hmx on their grid layout with a better color
chart = (alt.Chart(dat)
    .encode(
        x = 'row', 
        y = 'column', 
        color = alt.Color('hmx', scale = alt.Scale(scheme = 'goldorange')))
    .mark_square(size = 500))

chart
# %%
# Make a histogram of hmx and rdx
(alt.Chart(dat)
    .encode(
        x = alt.X('hmx', bin = alt.Bin(step = 0.05)), 
        y = 'count()')
    .mark_bar(color = 'red')
    .configure_title(fontSize = 20)
    .properties(title = "Distribution of HMX soild samples")

)
# %%
