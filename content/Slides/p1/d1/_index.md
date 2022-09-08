---
title: "Day 1: Exploring names with pandas"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-22T10:42:26+06:00
weight: 4
draft: true
# search related keywords
keywords: [""]
---

## Welcome to Class!

#### Announcements

The [data science lab](https://byuidatascience.github.io/lab/) opens this week!

<br>

## Completing Last Week

1. __Markdown Preview Enhanced__ [Install](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) & [Manual](https://shd101wyy.github.io/markdown-preview-enhanced/#/)
2. __Stop saving files everywhere!__ Structure your folders. [Example 1](https://drivendata.github.io/cookiecutter-data-science/), [Example 2](https://github.com/BYUIDSS/blank_project_repository).
3. __Finishing the Introduction Project__    
    A. `data_science_programming > introduction`   
    B. In  `introduction` I will save my `.py`, `.md`, and any `.png` files that are created with my `.py` file.   
    C. Let's use the [project template](https://byuistats.github.io/DS250-Cannon/template/cse250_project_template_clean.md)     
    D. Now lets use __Markdown Preview Enhanced__ to finish our introduction project.   
    E. Now submit it in Canvas.   

{{< faq "What was that data science community portion of our grade?" >}}

__The [Syllabus](https://byuistats.github.io/DS250-Cannon/course-materials/syllabus/) has this section which says;__

> Data science community
> 1. Attend data science society at least once during the semester.
> 2. Register to get a regular email on topics related to data science.

__Interview Question:__  What do you do to stay up with the current methods in data science?

__Don't Say:__ _Nothing_

{{</ faq >}}


## Project 1

#### Import packages

```
import ??? as ???
```

<br>

#### Load the names data

```
my_data = pd.read_csv()
```

<br>

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

#### Let's practice!

**1. How many unique names does the `names` dataframe contain?** Work with a partner to find the answer. You might want to look at this [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

{{< faq "Hint" >}}

1. Pull the name column out as a series
1. Use the pandas unique function `pd.unique()`
1. Find the size of the series

{{</ faq >}}

**2. What is the range of years in the `names` dataframe?** Again, work with a partner and use the pandas cheat sheet.

{{< faq "Hint" >}}

1. Pull the year column out as a series
1. Find the max
1. Find the min

{{</ faq >}}


<!-------------------------------------
## Working with Pandas

{{< faq "Loading the names data" >}}

#### Visit the [Project 1 Instructions](../../../projects/project-1) to download the data.

```{python}
#%%
# load packages
import pandas as pd
import altair as alt

#%%
# load data from url
url = "this_is_the_url_to_the_csv_file"
names = pd.read_csv(url)

#%%
# or, you can load data from file
names2 = pd.read_csv("names_year.csv")
```
{{</ faq >}}


{{< faq "Pandas and DataFrames" >}}

#### What is a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe)?

DataFrames come with attributes and built-in functions that can help us get a feel for our data.

Run the code below one line at a time (or use other functions of your choice) to explore the `names` data. What do you learn?

```{python}
names.columns
names.shape
names.size
names.head()
names.describe()
```
{{</ faq >}}

## Understanding the power of pandas

{{< faq "What is the data science workflow?" >}}

## The data science workflow

> - __You are going to hit `SHIFT + ENTER` thousands of times.__
> - __We don't usually source our scripts.__
> - __Think of Python Interactive like a [TI-86](https://en.wikipedia.org/wiki/TI-86) or Excel on steroids.__
> - __You code in pieces.__
> - __Rewrite for clarity!__

{{</ faq >}}



{{< faq "Can you figure out the functions of pandas?" >}}

{{% notice tip %}}
[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
{{% /notice %}}

```python
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]})
# Can someone read this code in english?
```


### Use the cheat sheet to find the functions you would need to implement the following steps.

__I want to;__

1. sort my table by column `a` then
1. only use the first 2 rows then
1. calculate the mean of column `b`.

__I want to;__

1. rename column `a` to `duck` then
1. subset to only have `duck` and `b` columns then
1. keep all rows where `b` is less than 9 then
1. find the min of `duck`



----------------------------------------->





<!-----------------------------
{{< faq "How many unique years do we have for our name?" >}}

```
pd.unique(dat.query('name == "John"').year).min()
pd.unique(dat.query('name == "John"').year).max()
pd.unique(dat.query('name == "John"').year).size
```


<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:175px;"></iframe>

{{</ faq >}}

{{< faq "Filtering rows of a DataFrame" >}}

#### Make sure to do the project readings!

- [P4DS: 5.2 Filter rows with .query()](https://byuidatascience.github.io/python4ds/transform.html#filter-rows-with-.query)
- [The query method](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-query-method)

{{</ faq >}}
------------------------------------>

<br>





## Extra Practice

{{< faq "DS 250 workflow" >}}

- You are going to hit `SHIFT + ENTER` thousands of times.
- We don't usually source our scripts.
- Think of Python Interactive like a graphing calculator or Excel on steroids.
- You code in pieces.
- Rewrite for clarity!

{{</ faq >}}


<!----------------------------------
{{< faq "Setup for Project 1" >}}

#### Create the folder and files to get prepared.

- `DS250 > project_1 >`    
    - `names.py`   
    - `names.md`
    - `notes.md`
    - `data.csv` _(just in case the internet is down)_

#### "How should we start each file?"

__I would do this process for every project.__

- **names.py:** Every file starts with the same cells 1) import packages, 2) load data.
- **names.md:** Let's start with the [course template](../../template/cse250_project_template.md)
= **notes.md:** I would copy over the project information and then keep notes on the readings in that section.

{{</ faq >}}



{{< faq "First steps for Project 1" >}}

__Read through the instructions for [Project 1: What's in a name?](../../../projects/introduction/project-1)__

Let's make sure we can read in the data.

```python
#%%
# load packages
import pandas as pd
import altair as alt

#%%
# load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)
```
{{</ faq >}}
------------------------------------>

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

__I want to:__

- sort my table by column `a` (low to high)
- only keep the first two rows
- calculate the mean of column `b`

{{</ faq >}}


{{< faq "What is method chaining?" >}}

Pandas and Altiar are built to allow for method chaining. Here is a great resource on how to use method chaining: [How to write neat pandas code](https://pandasninja.com/2019/04/how-to-write-neat-pandas-code/). 

- Altair creates a chart object
- pandas creates a DataFrame object
- We usually include `()` around our entire method so we can show it in steps.

```python
# read in data
flights_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/flights/flights.csv"
flights = pd.read_csv(flights_url)
flights['time_hour'] = pd.to_datetime(flights.time_hour, format = "%Y-%m-%d %H:%M:%S")

# without method chaining
flights = flights.filter(['dep_time'])
flights = flights.assign(hour = lambda x: x.dep_time // 100)
flights = flights.assign(minute = lambda x: x.dep_time % 100)
flights.head(5)

# with method chaining
(flights
    .filter(['dep_time'])
    .assign(
      hour = lambda x: x.dep_time // 100,
      minute = lambda x: x.dep_time % 100
      )
    .head(5)
)
```
<!----------------
```python
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
```
-------------------->
{{</ faq >}}

{{< faq "Your turn" >}}

```python
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})
```

__Use method chaining to do all of the following steps:__

1. rename column `a` to `duck,` then
1. subset to only have `duck` and `b` columns, then
1. keep all rows where `b` is greater than 9, then
1. find the min of `duck`

<br>

#### Bonus: Can you use `.query()` to find your name in the baby names data?

{{</ faq >}}
















<!----------------------------------------
## Completing Last Week

{{< faq "Trouble with `altair_saver`?" >}}

Let's take 10 minutes and make sure everyone can save an Altair chart. Teach one another!

{{</ faq >}}



{{< faq "Project 0: Final report" >}}

__Stop saving files everywhere!__ Structure your folders the same way for each project.

1. Create a `cse250` folder with another `introduction` folder inside
2. In  `introduction` I will save my `.py`, `.md`, and any `.png` files that are created with my `.py` file  
3. The `.md` can be copy-and-pasted from the [project template](../../../../static/template/cse250_project_template.md)  
4. Now lets use [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) to see the changes to our `.md` report
5. Save the report at a `.pdf` and submit it in Canvas ([Video tutorial](../../../course-materials/markdown) for final reports)

{{</ faq >}}
-------------------------------------------------------------->

<!------------
{{< faq "What was that data science community portion of our grade?" >}}

__The [Syllabus](../../course-materials/syllabus) has this section which says;__

> Data science community
> 1. Attend data science society at least once during the semester.
> 2. Find two data science in Python articles (or blog posts) and lead a discussion in the class.
> 3. Register to get a regular email on topics related to data science.

__Interview Question:__  What do you do to stay up with the current methods in data science?

__Don't Say:__ _Nothing_


### Register for a newsletter

> - https://www.datascienceweekly.org/
> - https://dataelixir.com/ [Archives](https://dataelixir.com/newsletters/)
> - https://tinyletter.com/data-is-plural
> - https://towardsdatascience.com/tagged/tds-letter [sign-up](https://towardsdatascience.com/receive-our-newsletters-681049ffa0cf)

### Find 2 data science in Python articles and lead 2 discussions in class.

> 1. You need at least 3 people in your discussion.
> 2. You should share the discussion article with your group by the second class day of the project. [Google Doc Share](https://docs.google.com/spreadsheets/d/17X_6WNEPOqhJhkEfJFkUF-C3vxbMwrsB865w3mGMxcE/edit?usp=sharing)
> 3. You are expected to __keep the group busy for 10 minutes__ with the article.
>    A. You could find an article that teaches a new Python Pandas or Altair method.     
>    B. You could find a good data ethics or how to find a data science job article and lead a discussion.    
>    C. You could provide questions or activity material before the class.

{{</ faq >}}
------------>

