---
title: "Day 1: The war with Star Wars"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Spiritual Thought

#### Announcements

Next Thursday, 3/14, at 11:30 in RKS 229, John Stevens, Chair of the Department of Mathematics and Statistics at Utah State University, will speak on “Graduate School: What/Why/How, including at USU”. 

After that (from 12:45 to 1:45), Dr. Stevens is providing a free catered lunch in the Manwaring Center for interested students. There is room for 15 students who are interested in learning more about a graduate degree in mathematics or statistics at USU. If you can come to lunch, please sign up here: [Here](https://www.signupgenius.com/go/10C0D4AA9AF2CA2FCC34-48316304-lunch#/)  (There is no cost for the lunch unless you are unable to attend and don't let us know at least 5 hours in advance, in which case your BYU-I account will be billed for $17.)

Dr. Stevens has reserved some time between 2:00 and 3:00 to meet one-on-one with potential graduate students and talk about mathematics and statistics at USU. It would be a great time to meet with him, talk about the courses you’ve had and plan to take, and get tips on getting into graduate school. If you would like 10 minutes to chat with him, sign up here: [Here](https://www.signupgenius.com/go/10C0D4AA9AF2CA2FCC34-48316568-10minutes#/)


1. Project 4 thoughts
    * Feature Importances - Sorted Bar Graph, not unsorted tables
    * And the winner is...


<br>

## The Star Wars data

## Load the Star Wars data

```python
# %%
import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat = pd.read_csv(url)

```
<br>

#### ???

### What do the data look like?

**Take the time to understand how the current data is organized.**

#### First things first...

Each group should answer these questions:

1. Where are the column names?
1. What does each row represent?
1. What does each column represent?

<br>

### What do we *want* the data to look like?

Each group should answer these questions:

1. What is the goal of this project, and how does that affect what we want from the data?
2. What do we want each row to represent?
3. What do we want each column to look like? Pick a few columns from the dataset and try creating an example in excel.

<!----------------------
1. We want shorter column names.
2. We want responses in the columns.
3. We need to create numeric columns out of any text/category columns.
----------------------------->

<br>

## Cleaning data takes time

**Maybe not 80% of your time, but it does take time!**

> Data science is frequently about doing bespoke analysis which means creating and labelling unique datasets. No matter how cleanly formatted or standardized a dataset is, it likely needs some work. 
>
>
>
> I would argue that spending time working with data to transform, explore and understand it better is absolutely what data scientists should be doing. This is the medium they are working in. Understand the material better and you'll get better insights. [ref](https://blog.ldodds.com/2020/01/31/do-data-scientists-spend-80-of-their-time-cleaning-data-turns-out-no/)

<br>

## Structure your project, structure your thinking

### Tableau on tidying data

1. [Think about your data holistically](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#think)
2. [Know the basic structure of your data](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#know)
3. [Keep track of your steps](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#track)
4. [Spot check throughout](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#spot)

<br>

### Compartmentalize and organize your scripts and data

- [Best practices for organizing data science projects](https://www.thinkingondata.com/how-to-organize-data-science-projects/)
- [How to organize your Python data science project](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510#directory-structure)
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/#directory-structure)
- [Data Science Project Folder Structure](https://dzone.com/articles/data-science-project-folder-structure)
<!---- > - [BYU=I DSS](https://github.com/BYUIDSS/blank_project_repository) ----->

<br>

<!----------------------------------
### Structured Thinking

Here is how to read this graph:

- Red line in the graph shows how time to complete a project (in weeks) has come down with experience
- With in each of three blocks (< 1 year; 1 – 3 year; 3+ years), the area of color shows the factor responsible for drop in time.
- For example, during the first block, time required to complete the project comes down from 12+ weeks to 3 weeks and 75% of this drop is because of structured thinking. [ref](https://www.analyticsvidhya.com/blog/2013/06/art-structured-thinking-analyzing/)

![](https://www.analyticsvidhya.com/wp-content/uploads/2013/06/time-required-project-completion.jpg)

<br>
---------------------------------->


### What are codecs and encodings?

- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Python Unicode Basics](http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html#unicode-basics)
- [pd.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1)

<br>

### The `.str` functions in pandas

- `.strip`: [Strip white space](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html)
- `.replace`: [replace one string of characters with another.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
- `.split`: [Separate a character string into two values.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html)
- `.join`: [Join two lists together](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.join.html#pandas.Series.str.join)
- [Python for Data Science: Strings](https://byuidatascience.github.io/python4ds/strings.html)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html)
