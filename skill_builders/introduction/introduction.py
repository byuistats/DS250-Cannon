#%%
## Exercise 1

'''
A good explaination that be able to mention that df2 contains
one extra column nameed "temp_f", and the column "temp_f" is derived
from the formula (temp_c * 9 / 5 + 32)
Using assign(), it creates a new columns from df1 and assign all the columns
to df2 as a dataframe
'''

## Exercise 2
# 1. What function in R dplyr to equivalent or comparable to query() in pandas? 
''' 
5.1.3 in the text. 
filter()
'''
# 2. What is the easiest mistake for python beginner to make that was shown in the text about query()?

'''5.2.1 in the text. 
"When you’re starting out with Python, the easiest mistake to make is to use = instead of == when testing for equality."
'''

## Exercise 3
'''
Any source that provides insights on drop()
'''

## Exercise 4
# %%
import pandas as pd 
import altair as alt
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

#Make a scatterplot of hwy vs cyl.
chart = (alt.Chart(mpg)
  .encode(
    x='cyl', 
    y='hwy')
  .mark_circle()
)
chart
#What happens if you make a scatterplot of class vs drv? Why is the plot not useful?
# %%
chart = (alt.Chart(mpg)
  .encode(
    x='class', 
    y='drv')
  .mark_circle()
)
chart
# The plot is not useful because scatterplot requires two numerical variables while both class and drv are categorical vataibles.

# %%
