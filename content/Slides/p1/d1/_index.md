---
title: "Day 1: Exploring names with pandas"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-22T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

## Welcome to Class!

#### Announcements

* Data Science Society Kickoff!  Wednesday at 6 in the STC 394
* The [data science lab](https://byuidatascience.github.io/lab/)

<br>

## Completing Last Week

1. Quarto - "out of the frying pan and into the fire"
2. __Finishing the Introduction Project__    
    - Use the QMD Template [project template](https://byuistats.github.io/DS250-Cannon/template/ds250_project_template_clean.qmd)
    - Render as HTML and upload in Canvas

{{< faq "What was that data science community portion of our grade?" >}}

__The [Syllabus](https://byuistats.github.io/DS250-Cannon/course-materials/syllabus/) has this section which says:__

> Data science community

To earn credit for the DS Community element you must complete two different tasks from the list below. At the end of the semester, you will be asked to report on which tasks you completed and what you learned from them.

Attend Data Science Society at least once.
* Sign up for an email newsletter that will teach you more about data science. [Data Science Weekly](https://www.datascienceweekly.org/) or [Data Elixir](https://dataelixir.com/) are good options.
* Listen to a podcast episode about data science. [Build a Career in Data Science](https://www.datascienceweekly.org/) has some excellent episodes.
* Watch a professional presentation on YouTube about data science. Be prepared to share the link and a summary of the video.
* Reach out to someone who works in a data-related field and ask them for 15 minutes of their time. Use this time to conduct an “[informational interview](https://brightspotcdn.byu.edu/54/b6/2554ebb842fab54640a15ff0afb3/informational-interview.pdf)” and learn more about their responsibilities and career path.
* Research and apply to at least 5 data-related jobs or internships.


__Interview Question:__  How do you keep up with the current methods in data science?

__Don't Say:__ _Nothing_

{{</ faq >}}


#### Let's Code!

{{< faq "DS 250 workflow" >}}

- You are going to hit `SHIFT + ENTER` thousands of times.
- We don't usually source our scripts.
- Think of Python Interactive like a graphing calculator or Excel on steroids.
- You code in pieces.
- Rewrite for clarity!

{{</ faq >}}


{{< faq "Can you figure out the functions of pandas?" >}}

{{% notice tip %}}
[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) and [Basics Blog Post](https://towardsdatascience.com/pandas-basics-cheat-sheet-2021-python-for-data-science-8beb76afa85f)
{{% /notice %}}

```python
# Pause: can you explain what this code is doing?
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})
```

**Use the cheat sheet to find the functions you would need to implement the following steps.**

__Group 1__

1. sort my table by column `a` then
1. only use the first 2 rows then
1. calculate the mean of column `b`.

__Group 2__

1. rename column `a` to `duck` then
1. subset to only have `duck` and `b` columns then
1. keep all rows where `b` is less than 9 then
1. find the min of `duck`

{{</ faq >}}


{{< faq "What is method chaining?" >}}

Pandas is built to allow for method chaining. Here is a great resource on how to use method chaining: [How to write neat pandas code](https://pandasninja.com/2019/04/how-to-write-neat-pandas-code/). 


- plotly.express creates a chart object
- pandas creates a DataFrame object
- We usually include `()` around our entire method so we can show it in steps.

{{</ faq >}}

# Project 1 - Intro

#### Understanding your data

You should be able to introduce your data sets to people, the same way you introduce a friend!

- What does each row represent? If you don't know, then you don't understand what groups you can analyze.
- What does each column represent? If you don't know, then you don't understand what information you can evaluate for each group.

Being able to explain your data out loud to someone else follows the same principles as [rubber duck debugging](https://rubberduckdebugging.com/).

<br>

#### Introduction to pandas "DataFrame"

What is a pandas DataFrame? We can read the [official documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe). I also like the video in [this tutorial](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python).

DataFrames come with attributes and built-in functions that can help us get a feel for our data.

Run the code below one line at a time (or use other functions of your choice) to explore the `names` data. What do you learn?

```{python}
my_data.columns
my_data.shape
my_data.size
my_data.head()
my_data.describe()
```
<!---- https://towardsdatascience.com/wrangling-data-with-pandas-27ef828aff01 ----->

<br>

# Setup for Project 1

#### Create the folder and files to get prepared.

- `DS250 > project_1 >`    
    - `names.py`   
    - `names.qmd`
    - `data.csv` _(just in case the internet is down)_

#### "How should we start each file?"

__I would do this process for every project.__

- **names.py:** Every file starts with the same cells 1) import packages, 2) load data.
- **names.md:** Let's start with the [course template](https://byuistats.github.io/DS250-Course/template/ds250_project_template_clean.qmd)
- **notes.md:** Keep project noteson the readings and things you learn.
- **my_cheat_sheet.md:** Update your own cheat sheet


Read in the data.

```python
#%%
# load packages
import pandas as pd
import plotly.express as px

#%%
# load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)
```


**1. How many unique names does the `names` dataframe contain?** Work with a partner to find the answer. You might want to look at this [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

{{< faq "Hint" >}}

1. Pull the name column out as a series
1. Use the pandas unique function `pd.unique()`
1. Find the size of the series

{{</ faq >}}

**2. What is the range of years in the `names` dataframe?** Again, work with a partner and use the pandas cheat sheet.

{{< faq "Hint2" >}}

1. Pull the year column out as a series
1. Find the max
1. Find the min

{{</ faq >}}

