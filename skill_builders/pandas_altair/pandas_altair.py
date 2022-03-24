
#%%
import numpy as np
import pandas as pd
import altair as al 
# data import
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

#%%
# 1.1 Using a line of code, select all the columns in this dataset, assign it to a list called col_list

col_list = dat.columns

# 1.2 `Using one line of code, show the number of columns and rows in dat.`

dat.shape

# `Just from looking at the output, what column(s) seems to be redundant with the row number?`

## unnamed:0 is redundant

# %%
# 2. Using a line of code, drop the column "Unnamed: 0" using the variable col_list
dat = dat.drop([col_list[0]], axis = 1)


#%%

# `what is the difference between exp1 and exp2?`
## exp1 is a bool value, while exp2 is a list of bool values

# `By putting dat.violent < 300, and the violent column from dat into a dataframe, what is the relationship between the two columns?`
## dat.violent<300 is the list evaulations of the expression according to dat.violent. 

# Filter down the data set show that it only shows the data for idaho
dat = dat.query("state == 'Idaho'")

#%%
# Create a new column that show the ratio between murder rate and violent rate.
dat.assign(ratio = dat.murder/dat.violent)

#%%
# Create a scatter plot that shows the relationship between murder rate and violent rate for the state of Idaho.
#     Your chart should show murder rate as the x-axis, violent as the y-axis.
mdat = dat.query("state == 'Idaho'")

(al.Chart(mdat)
.encode(x = al.X("murder", scale=al.Scale(zero = False)),
        y = al.Y("violent", scale=al.Scale(zero = False)))
.mark_circle())
# %%
# Filter down the data set show that it only shows the data between 1993 and 1997
dat.query("year >= 1993 and year <= 1997")

# Create a line chart that show prisoners numbers for the state of Idaho, Utah, and Oregon
# Your chart should show year as the x-axis, prisoner as the y-axis, along with a title
states = ["Idaho", "Utah", "Oregon"]

cdat = dat.query("state in @states")

(al.Chart(cdat)
.encode(x = al.X("year", axis = al.Axis(format = "d")),
        y = "prisoners",
        color = "state")
.mark_line()
.properties(title = "Prisoner number in the three states"))

# Without using query(), finshed exercise 2,5 and 7(jsut the wrangling). 
# 2
dat[dat.state == "Idaho"]
# 5
dat[(dat.year >= 1993) & (dat.year<= 1997)]
# 6
dat[dat["state"].isin(["Idaho", "Utah", "Oregon"])]
