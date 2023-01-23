---
title: "Day 2: Transforming Data"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: true
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Spiritual Thought

#### Announcements

1. Code chunk options:  
    * Locally:  #| warning:  false
    * Globally:  in the YAML:  execute: warning: false
2. Something to be said for consistency (in graphs)...and variation
3. Slack me when you resubmit a project

<br>

## Loading JSON files into pandas

Let's load in some practice data! [Data link.](https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json)

Here's a description of the data:  [Data Description.](https://rstudio-pubs-static.s3.amazonaws.com/61800_faea93548c6b49cc91cd0c5ef5059894.html)

```python
import pandas as pd   # to load and transform data
import numpy as np    # for math/stat calculations

# from url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)

# or from file to pandas dataframe
cars = pd.read_json("mtcars_missing.json")
```

Look at the data for the first two cars. What is different about the format? 

```JS
[
  {
    "car": "Mazda RX4",
    "mpg": 21,
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.62,
    "qsec": 16.46,
    "vs": 0,
    "am": 1,
    "gear": 4,
    "carb": 4
  },
  {
    "car": "Mazda RX4 Wag",
    "mpg": 21,
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.875,
    "qsec": 17.02,
    "am": 1,
    "gear": 4,
    "carb": 4
  }
]
```

<br>

## Your Turn: Transforming Data

With your group, research these functions and create an example using the `cars` data. Post your example in Slack. Be prepared to teach the class about your functions.

You can use the [Data Transformation textbook chapter](https://byuidatascience.github.io/python4ds/transform.html) and the [pandas documentation](https://pandas.pydata.org/docs/) to help you.

### Recreate the following output to the best of your abilities: 

<!-------------------------------------
[LINK](https://htmlpreview.github.io/?https://github.com/byuistats/DS250-Cannon/blob/master/content/Slides/p2/d2/cars.html)
--------------------------------------------------->


#####  Group 1:  Working with rows

- `.query()` allows you to subset observations (rows)
- `.sort_values()` arranges rows in a particular order

#####  Group 2:  Working with columns

- `.filter()` (as well as `[]` and `.loc[]`) allow you to select columns
- `.assign()` is one way to add new columns to a dataframe

#####  Group 3:  Counting items

- `.value_counts()` summarizes a column by counting the values inside
- `.crosstab()` creates a "cross tabulation" of two or more variables

#####  Group 4:  Summarizing data

- Using `.groupby()` and `.agg()` together allows you to calculate group summaries

<br>

## Your Turn: Summarizing the cars data

Write code to calculate the mean weight `wt` for each cylinder type `cyl`.

{{< faq "Answer 1">}}
```
cars.groupby('cyl').agg(mean_weight = ('wt', np.mean)).reset_index()
```
{{</ faq >}}

Can you print the answer as a markdown table?

{{< faq "Answer 2">}}
```
print(cars.groupby('cyl').agg(mean_weight = ('wt', np.mean)).reset_index().to_markdown(index = False))
```
{{</ faq >}}

<!-------------------------------------
<br>

## Project 2: Late Flights and Missing Data

#### Introduce the data

Load the JSON file and spend a few minutes studying it. Can you learn enough about it to describe the columns and rows?

<br>

#### Question 1 Brainstorming

What is our goal? How can we get there?

<br>

#### Question 2 Brainstorming

What is our goal? How can we get there?

<br>

#### Question 3 Brainstorming

What is our goal? How can we get there?
--------------------------------------------------->


## Project 2 FAQs

{{< faq "Why are we using assign()">}}

One main reason: 
> You can create multiple columns within the same `assign()` where one of the columns depends on another one defined within the same assign. [*source:* Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)

Other resources:
- [Why use pandas.assign rather than simply initialize new column?](https://stackoverflow.com/questions/48177914/why-use-pandas-assign-rather-than-simply-initialize-new-column)
- [3 Ways to Add New Columns to Pandas Dataframe](https://cmdlinetips.com/2019/01/3-ways-to-add-new-columns-to-pandas-dataframe/)

Not related, but also fun: [Should you use "dot notation" or "bracket notation" with pandas?](https://www.dataschool.io/pandas-dot-notation-vs-brackets/#:~:text=Dot%20notation%20is%20three%20fewer,it%20makes%20a%20real%20difference!)

{{</ faq >}}

{{< faq "Lambda functions">}}

Two ways to define the same function:
```python
def square(x):
     return x**2

square = lambda x:x**2
```

There are some difference between them as listed below.
>   1. lambda is a keyword that returns a function object and does not create a 'name'. Whereas def creates name in the local namespace
>   2. lambda functions are good for situations where you want to minimize lines of code as you can create function in one line of python code. It is not possible using def
>   3. lambda functions are somewhat less readable for most Python users.
>   4. lambda functions can only be used once, unless assigned to a variable name.
>
> [*source*](https://www.listendata.com/2019/04/python-lambda-function.html)

{{</ faq >}}

{{< faq "Conditional operations">}}

What if you want to create a new column, whose values depend on another column? There are a lot of ways to accomplish this (see [this stackoverflow answer](https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column)). Some functions I use:

- [isin() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin)
- [where() method](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- You can also use an if else statement [inside a lambda function](https://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda)

{{</ faq >}}

{{< faq "Missing data">}}

We will learn how to identify and deal with missing data next week. For now, we can drop rows we don't want using square brackets `[]` or `.query()`.

{{</ faq >}}



# API's and JSON: A Primer

## Application Programming Interfaces (APIs)

#### Representational State Transfer (REST APIs)

> Over the course of the ’00s, another Web services technology, called __Representational State Transfer, or REST__, began to overtake [all other tools] for the purpose of transferring data. One of the big advantages of programming using REST APIs is that you can use multiple data formats — not just XML, but JSON and HTML as well. As web developers came to prefer JSON over XML, so too did they come to favor REST over SOAP. As Kostyantyn Kharchenko put it on the Svitla blog, “In many ways, the success of REST is due to the JSON format because of its easy use on various platforms.”   
> Today, JSON is the de-facto standard for exchanging data between web and mobile clients and back-end services. [ref](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html)

<br>

#### JavaScript Object Notation

> Well, when you’re writing frontend code in Javascript, getting JSON data back makes it easier to load that data into an __object tree__ and work with it. And JSON formats data in a more __succinct way__, which saves bandwidth and improves response times when sending messages back and forth to a server.    
> In a world of APIs, cloud computing, and ever-growing data, JSON has a big role to play in greasing the wheels of a modern, open web. [ref](https://blog.sqlizer.io/posts/json-history/)

<br>

#### Other Resources

- [RESTful APIs in 100 Seconds (video)](https://www.youtube.com/watch?v=-MTSQjw5DrM)
- [Python API Tutorial: Getting Started with APIs](https://www.dataquest.io/blog/python-api-tutorial/)
- [Big List of Free and Open Public APIs (No Auth Needed)](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)


<br>

<br>

<br>




<!-------------------------------------
{{< faq "How could we leverage numpy's `where()` to address the different month proportions in question 3?">}}

[reference](https://numpy.org/doc/stable/reference/generated/numpy.where.html)

{{</ faq >}}


{{< faq "How many rows have missing months?">}}

```python
flights.month.value_counts()
```

{{</ faq >}}

{{< faq "Can we figure out any patterns in the missingness?">}}

- [`pd.crosstab()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.crosstab.html)   
- [groupby](https://byuidatascience.github.io/python4ds/transform.html#grouped-summaries-or-aggregations-with-agg)

{{</ faq >}}
-------------------------------------------------->

<br>
