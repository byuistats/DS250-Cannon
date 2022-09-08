---
title: "Introduction"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---

A competent student should be able to finish the exercises within 60 minutes. You should work through it on your own. This serves as an assessment of your understanding of the assigned readings.
## Before you start

Make sure you have installed VS-code, pandas, and altair on your computer. You can install these package by typing this line in the terminal. 

_```pip install pandas altair```_

OR if you have more than one version of python

_```pip3.9 install pandas altair```_

`pip3.9` indicates the version of python you are installing the packages to.

# **Part 1** 
## *Get familiar with your tools*

Programming involves a lot of **research**. Unlike subjects like Mathematics or History, we are not required to remember every single function and its usage. It is natural for experienced programmers to look for answers on the internet, books, even from other people's code. Programming will be extremely frustrating if we are not allowed to do web searches, so please get familiar with the tools you have and use them often.
### Offical Documentation

This should be your first resort for understanding any code/function. Scanning the documentation of a function will allow you to get an overview of its usage.  
Here is a link to the documentation of the `assign()` function:  

(https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)  

__Example of assign() (as shown in the documentation)__

```python
    import pandas as pd

    df1 = pd.DataFrame({'temp_c': [17.0, 25.0]},
                  index=['Portland', 'Berkeley'])
    
    df2 = df1.assign(temp_f=df1.temp_c * 9 / 5 + 32)
```
  
__Exercise 1:__ After reading the documentation for `assign()`, write a short paragraph to explain `assign()` as if you were talking to someone with zero programming experience (use the example above to help you explain `assign()`). 

- What is the difference between df1 and df2? 
- How was df2 derived from df1?)

### Online textbook
It pains us to see students would rather be stuck at problems for hours yet they refuse to use the textbook. This is another very useful resource since this is designed for this class.
link to the textbook:
(https://byuidatascience.github.io/python4ds/)

__Exercise 2:__ Locate the section where the textbook talks about `query()` and answer these questions.

- What function in R's dplyr is equivalent or comparable to `query()` in pandas (You should include the section number in your answer)?
- What is the easiest mistake for python beginner to make that was shown in the text about `query()` (You should include the section number in your answer)?

### The internet

Google is a programmer's friend. Get used to googling thing, in fact, you want to be an expert in googling 

- _Question that cannot be answered by the textbook and documentation?_ __Google it.__   
- _A function you have never seen before?_ __Google it.__
- _An error in your code?_ __Google it.__

__Exercise 3:__ Provide at least 2 extra resources you could find about the pandas function `drop()` on the internet.

### Tutor, TA (Through slack, zoom, or in-person)

We want to help you with your work; we want to answer your questions; but most importantly, we want to help you succeed in this class. That will require you to put in the necessary time in understanding the readings, coding and debugging. When you ask us a question, we expect that you have read the documentation, searched the textbook, and done your own research. Then we can be most helpful and can provide insights on top of your understanding. 

#### Examples of bad questions

- __How does `drop()` work?__ _We will ask you to read the documentation for `drop()`._
- __How do you make a table in a markdown file?__ _We will refer you to the textbook._
- __I don't want these columns in my data, how can I drop them?__ _We will ask you if you have found any things on the internet._
#### Examples of good questions

- __I am still confused about the syntax of `drop()`. After reading the documentation, this is my understanding of the function... . What am I missing?__
- __I tried making a table in markdown (show code), it is still not giving me what I want, how can I fix this?__
- __I am trying to drop these columns in my dataframe, I think `drop()` is what I am looking for. Am I in the right direction? If not, what keywords should I be googling?__

__Exercise 4:__ 

_Using the code and tools mentioned above, finish question 4 and 5 under 3.2.4 in the textbook.(use the data in mpg for your plot):_


```{python}
# library import
import pandas as pd 
import altair as alt

# data import
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"

mpg = pd.read_csv(url)
```

- Question 4: Make a scatterplot of `hwy` vs `cyl`.

- Question 5: What happens if you make a scatterplot of `class` vs `drv`? Why is the plot not useful?

{{< faq "After you have completed this skill builder with your team (or on your own) then compare your work to our script" >}}

__See the [script](introduction.py).__

{{</ faq >}}
