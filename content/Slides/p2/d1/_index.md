---
title: "Day 1: Intro to Flights Data"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

### How about General Conference?

### Short

[Link](https://youtu.be/qol2X_8JF9I)

### Project 1 Comments

1. Don't include data as a table.  Only include tables that add useful information.  If I have to scroll up and down it isn't useful.
2. Reports should be readable by an intelligent, but non-technical audience (Meaningful titles and section names)
3. Make it like something you'd like to read 
4. Clean out any code output, logs, that distract from the message ("My Useless Chart")


<br>

## Project 2: Late Flights and Missing Data

#### JSON files (JavaScript Object Notation)

> Today, JSON is the de-facto standard for exchanging data between web and mobile clients and back-end services. [*source*](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html)

<br>

##### What is JSON?

#### Introduce the data

Load the JSON file and spend a few minutes studying it. Can you learn enough about it to describe the columns and rows?

Hints:

- You can use `.describe()` to learn about the distribution of a numeric variable.
- You can use `.value_counts()` to learn about the distribution of a categorical variable.
- `.crosstab()` creates a "cross tabulation" of two or more categorical variables.

<br>

#### Can you trust the data?

Do you notice anything interesting about the flights data?

<br>

#### Question Brainstorming

In your group, try to answer the following questions about your assigned "Grand Question":

- What is our goal? 
- How can we get there?
- What will the answer look like when we're done?

<br>

<br>

<br>

## Project 2 FAQs

{{< faq "Missing data">}}

Not all missing data is represented as `np.nan`. For an example, look at the column that counts delays due to late aircraft.

We will learn how to identify and deal with missing data next week. For now, we can drop rows we don't want using square brackets `[]` or `.query()`.

{{</ faq >}}

{{< faq "What columns do we need to use for question 3 (total number of flights delayed by weather)?">}}

> - `num_of_delays_weather`
> - `num_of_delays_late_aircraft`
> - `num_of_delays_nas`

{{</ faq >}}

<!-----------------------------------------------------------------
#### Handling JSON data in Python

Let's load in some practice data! [Data link.](https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json)

```python
import pandas as pd   # to load and transform data
import numpy as np    # for math/stat calculations

# from url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)

# or from file to pandas dataframe
cars = pd.read_json("mtcars_missing.json")
```
--------------------------------------------------------------------------------->

<!--------------------------------------------
### If you're using an API:

[Web requests in Python](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul)

__Internal Packages__

- [urlib](https://docs.python.org/3/library/urllib.html#module-urllib)
- [urlib3](https://urllib3.readthedocs.io/en/latest/)

__External Packages__   

- [Requests package](https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


__Our Path__   

[urllib3](https://urllib3.readthedocs.io/en/latest/user-guide.html)


__Example__

```python
#%%
import pandas as pd
import urllib3
import json

#%% get JSON file
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"

http = urllib3.PoolManager()
response = http.request('GET', url)
cars_json = json.loads(response.data.decode('utf-8'))

# convert it to Pandas dataframe
cars = pd.io.json.json_normalize(cars_json)
```
---------------------------------------------------------->

<!---------------------------------------------------------------
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
  },
  {
    "car": "Datsun 710",
    "mpg": 22.8,
    "cyl": 4,
    "disp": 108,
    "hp": 93,
    "drat": 3.85,
    "wt": 2.32,
    "qsec": 18.61,
    "vs": 1,
    "am": 1,
    "gear": 999,
    "carb": 1
  }
]
```
--------------------------------------------------------------------->
<!---------------------------
## Let's get our JSON files into Python.

#### The cars data

```python
url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)
```

#### The flight project data

```python
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
flights = pd.read_json(url_flights)
```
------------------------------------->

<br>
<!-------------------------------------------------------------------------------
## Your Turn: Transforming Data

#### Groups 1 and 5 - Working with rows

- `.query()` allows you to subset observations (rows)
- `.sort_values()` arranges rows in a particular order

#### Groups 2 and 6 - Working with columns

- `.filter()` (as well as `[]` and `.loc[]`) allow you to select columns
- `.assign()` is one way to add new columns to a dataframe

#### Groups 3 and 7 - Counting items

- `.value_counts()` summarizes a column by counting the values inside
- `.crosstab()` creates a "cross tabulation" of two or more variables

#### Groups 4 and 8 - Summarizing data

- Using `.groupby()` and `.agg()` together allows you to calculate group summaries

<br>

<hr>

<br>

## Your Turn: Summarizing the cars data

__Write the code to calculate the mean weight `wt` for each cylinder type `cyl`.__

{{< faq "Answer 1">}}
```
cars.groupby('cyl').agg(mean_weight = ('wt', np.mean)).reset_index()
```
{{</ faq >}}

__Can you print the answer as a markdown table?__

{{< faq "Answer 2">}}
```
cars.groupby('cyl').agg(mean_weight = ('wt', np.mean)).reset_index().to_markdown(index = False)
```
{{</ faq >}}

<br>
-------------------------------------------------------------------------->
<!-------------------------------------------------------------------

## The flights data

How are we going to answer Question 1 and Question 2?




{{< faq "Watch out for different forms of missing data!">}}

Not all missing data is represented as `np.nan`. For an example, look at the column that counts delays due to late aircraft.

{{</ faq >}}

{{< faq "What columns do we need to use for question 3 (total number of flights delayed by weather)?">}}

> - `num_of_delays_weather`
> - `num_of_delays_late_aircraft`
> - `num_of_delays_nas`

{{</ faq >}}


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








## Project 1: Names

In your groups, discuss:

- What did you learn about data and Altair?   
- What questions do you still have?   

## Connecting to Application Programming Interfaces (APIs)

### Representational State Transfer (REST APIs)

> Over the course of the ’00s, another Web services technology, called __Representational State Transfer, or REST__, began to overtake [all other tools] for the purpose of transferring data. One of the big advantages of programming using REST APIs is that you can use multiple data formats — not just XML, but JSON and HTML as well. As web developers came to prefer JSON over XML, so too did they come to favor REST over SOAP. As Kostyantyn Kharchenko put it on the Svitla blog, “In many ways, the success of REST is due to the JSON format because of its easy use on various platforms.”   
> Today, JSON is the de-facto standard for exchanging data between web and mobile clients and back-end services. [ref](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html)

### JavaScript Object Notation

> Well, when you’re writing frontend code in Javascript, getting JSON data back makes it easier to load that data into an __object tree__ and work with it. And JSON formats data in a more __succinct way__, which saves bandwidth and improves response times when sending messages back and forth to a server.    
> In a world of APIs, cloud computing, and ever-growing data, JSON has a big role to play in greasing the wheels of a modern, open web. [ref](https://blog.sqlizer.io/posts/json-history/)
------------------------------------------------------------>




<!-------------------------------------------------------------
## What is missing data?

### And why would data be missing?

{{< faq "What does missing data look like?">}}

How many missing values do you see in the first ten rows? (The `mtcars` documentation [might help](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html).)

```python
cars.head(10)
```
{{</ faq >}}

{{< faq "How many missing values are there?">}}

```python
#%%
cars.isna().sum()

#%%
cars.isin(['']).sum()

#%%
cars.describe()
```
[reference 1](https://www.geeksforgeeks.org/count-nan-or-missing-values-in-pandas-dataframe/) and [reference 2](https://stackoverflow.com/questions/22257527/how-do-i-get-a-summary-count-of-missing-nan-data-by-column-in-pandas)
{{</ faq >}}


### How Pandas handles missingness

Read ['Handling missing in pandas'](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

```python
import numpy as np

df = (pd.DataFrame(
    np.random.randn(5, 3), 
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three'])
  .assign(
    four = 'bar', 
    five = lambda x: x.one > 0,
    six = [np.nan, np.nan, 2, 2, 1],
    seven = [4, 5, 5, np.nan, np.nan])
  )
```


{{< faq "What happens when you add two pandas objects with missing values?">}}

```python
df.seven + df.six
```

[reference](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

{{</ faq >}}

{{< faq "What happens when you sum within a column?">}}

```python
df.seven.sum()
```

[reference](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

{{</ faq >}}

{{< faq "How could I add two columns treating NaN like zeros?">}}

```python
df.seven.fillna(0) + df.six.fillna(0)
```
[reference](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#filling-missing-values-fillna)

{{</ faq >}}
----------------------------------------------------------->
