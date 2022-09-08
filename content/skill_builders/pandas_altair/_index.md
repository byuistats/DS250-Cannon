---
title: "pandas and Altair"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

For this skill builder, we are exploring some important functions in the package of pandas and Altair. DS programming requires a lot of data wrangling. Using the proper functions, we can create concise and comprehensive codes. You should be exposed to a few functions through the readings this week. 

You may want to at least scan the readings before beginning this task since this serves as an assessment of your understanding of the assigned readings. A prepared student should be able to finish the exercises within 60 minutes. You should work through it on your own.

## Before you start

Make sure you have installed VS-code, pandas, and Altair on your computer. You can install these packages by typing this line in the terminal:

_```pip install pandas altair```_

OR if you have more than one version of python:

_```pip3.9 install pandas altair```_

pip3.9 indicates the version of python you are installing the packages to.

# Data import

__Run the following code to import the data we need for this skill builder:__

```python

# package import
import numpy as np
import pandas as pd
import altair as al 
# data import
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

```

Make sure the variable `dat` is correctly assigned in your environment and finish the following exercises. You can read the documentation of the data on this page - 
https://vincentarelbundock.github.io/Rdatasets/doc/AER/Guns.html

### Exercise 1

One of the first things we can do to a freshly imported data is to check its columns. This will help us understand the basic structure of the dataframe(table). 

> __Using one line of code, select all the columns in dat, assign it to a variable called col_list.__ 

<details>
  <summary>Hint</summary>
  Every dataframe has an attribute "columns".  
  Accessing this attribute will give you a list of all column names 
</details>

We often want to know the dimension of a dataframe. How many columns are in the dataset? How many rows are in the dataset?

> __Using one line of code, show the number of columns and rows in `dat`.__

<details>
  <summary>Hint</summary>
  Every dataframe has an attribute "shape".  
  Accessing this attribute will give you the dimension of a datafarme
</details>


Now run `dat.head()`. It will print out the first 5 rows of data in `dat`.

> __Just from looking at the output, what column(s) seems to be redundant with the row number?__

<details>
  <summary>Hint</summary>
  There is one column that serves as nothing but a row counter, that columns is redundant.
</details>

### Exercise 2

After a  brief investigation of the data, we will clean up the data. By **cleaning up**, we are trying to filter down `dat` so this only holds data we need. We will first get rid of the extra column we found in the previous excercise.

> __Using one line of code, drop the redundant column using the variable col_list (created in excercise 1)__

<details>
  <summary>Hint</summary>
  Use `drop()`.  

  Understand what "axis" is as a parameter of `drop()`.  

  Your function should looks like this:  

  `dat.drop([col_list[_]], axis = _)`  

  fill the "_"'s with the correct values and assign the output to `dat`.
</details>

Don't forget to save the changes in `dat`. Run `dat.head()` to make sure the column is dropped in `dat`.

### Exercise 3

We have filtered `dat` vertically by dropping a column. Now we will try to filter `dat` horizontally, meaning we will get rid of some the rows. 

We can do that by applying a condition to `dat`. A condition is an expression that can be evaluated as `True`/`False`. For example, `8 > 5` is an expression that evaluates to be True. This is trivial because 8 will always be greater than 5. 

Run the code below:

> __what is the difference between exp1 and exp2?__

```{python} 
exp1 = 8 > 5
exp2 = dat.violent < 300
```

<details>
  <summary>Hint</summary>
  Try type() on else variable OR calling else variable.
</details>

Run ths code below:

> __By putting `dat.violent < 300`, and the violent column from `dat` into a dataframe, what is the relationship between the two columns?__


```{python}
exp = pd.DataFrame({"dat.violent < 300" : exp2,
                    "violent value from dat" : dat.violent})

exp
```

<details>
  <summary>Hint</summary>
  Try computing `dat.violent[n] < 300` and `(dat.violent < 300)[n]` where n is less than the number of row. The two expressions will always be the same as long as n is less than the number of rows.
</details>

> __Using `query()`, filter down the `dat` so that it only contains the data for idaho__

<details>
  <summary>Hint</summary>
  query() takes in expressions and filters down data.
</details>

Don't forget to save the changes in `dat`. Run `dat.shape()` to make sure the there are 23 rows and 13 columns.

### Exercise 4

Besides filtering, we can manipulate the data by adding new data to it. By adding a new column to the data, we assign a new value to each row.

> __Using `assign()`, create a new column that show the ratio between murder rate and violent rate.__

<details>
  <summary>Hint</summary>
  Use assign()  

  You see get the ratio by computing this code:  

  `dat.murder/dat.violent`
</details>

## Exercise 5

> __Create a scatter plot that shows the relationship between murder rate and violent rate for the state of Idaho. Your chart should show murder rate as the x-axis, violent as the y-axis.__

<details>
  <summary>Hint</summary>
  Can you mimic this plot?  

  (https://altair-viz.github.io/gallery/scatter_tooltips.html)
</details>

<div style="page-break-after: always;"></div>

## For an extra push
### Exercise 6

> __Using a line of code, filter down the data set so that it only shows the data in years between 1993 and 1997.__
### Exercise 7

> __Create a line chart that show prisoners numbers for the state of Idaho, Utah, and Oregon.__

Your chart should show year as the x-axis, prisoner as the y-axis, states as different colours, along with an appropriate title.

## Exercise 8

> __Without using `query()`, finshed the data wrangling in question 2,5 and 6.__

{{< faq "After you have completed this skill builder with your team (or on your own) then compare your work to our script" >}}

__See the [script](pandas_altair.py).__

{{</ faq >}}