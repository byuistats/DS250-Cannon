# %%
import pandas as pd
import numpy as np 
import altair as alt 


# %%
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])

# %%
df.sort_values("a").head(2).b.mean()
# %%
(df.rename(columns = {'a':'duck'})
    .filter(['duck', 'b'])
    .query('b < 9')
    .duck.min()
    )
# %%
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"

mpg = pd.read_csv(url)

chart_loess = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy")
  .transform_loess("displ", "hwy")
  .mark_line()
)

chart_loess
# %%
