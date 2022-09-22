---
title: "Day 2: Seeing names with Altair"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Announcements

#### Project Submissions
1. Don't leave example text/documentation from the Template in your writeup
1. Change the Project Title (don't have to call it Client Report)
1. Code can be adjacent to the relevant output as long as it's not distracting, but please include your complete code in an Appendix
1. Be sure to save the QMD file _before_ rendering
  * Autosave


# Project 0 Wrap-up

1. If you still cannot render a document in Quarto, let me know
1. Is python, at least up and running?  able to plot graphs and make tables?
1. Finishing up a report
  * [Markdown](https://byuistats.github.io/DS250-Cannon/course-materials/markdown/)
    * Tables - want to have the printed table in Markdown area, not a code area
  * HTML submissions

Other hints: 
1. Tutoring Lab Slack Channel:  #tutoring_lab


<!------------------
#### Thoughts about reading notes

It's a good idea to keep track of new skills you learn! Try taking notes in a `.py` or `.ipynb` file. This makes it easy to include examples of code.
--------------->
<br>

## Methods Checkpoint

<!------------------
<br>

## Create your own cheat sheet!
------------------>
<br>

<!----------------------------------

#### Coding "methods and calculations" quizzes

Let's review canvas and make sure we understand the checkpoints.

<br>

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


{{< faq "Understanding your data" >}}

You should be able to introduce your data sets to people, the same way you introduce a friend.

- If you can't describe what a row is in your data, then you don't understand what groups you can analyze.
- If you can'r describe what a column is in your data, then you don't understand what information you can evaluate for each group.

Being able to explain your data out loud to someone else follows the same principles as [rubber duck debugging](https://rubberduckdebugging.com/).

{{</ faq >}}


{{< faq "Let's practice!" >}}

#### Understanding column values

**How many unique names does the `names` dataset contain?** Work with a partner to find the answer. I recommend searching the [Pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).
1. pull the name column out as a series
1. Use the pandas unique function `pd.unique()`
1. find the size of the series

**What is the range of years in the `names` dataset?** Again, work with a partner and use the Pandas cheat sheet.

1. pull the year column as a series
1. Find the max
1. Find the min

{{</ faq >}}
----------------------------------------------------->

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

## Getting started with Altair

### Why are we using Altair?

#### It is built on the VEGA and D3 which are fast and web based.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AAuPPorsmJc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Grammar of Graphics: Vega-Lite

![](altair_grammar_graphics.png)

> - [Technical Paper](https://www.domoritz.de/papers/2017-VegaLite-InfoVis.pdf)
> - [Website](https://vega.github.io/vega-lite/)
> - [Endorsment](https://medium.com/@robin.linacre/why-im-backing-vega-lite-as-our-default-tool-for-data-visualisation-51c20970df39)

#### Grand Grand Question 1

What does a chart need to look like to answer Question 1?

What data do we need to build that chart?

<br>

#### Making our chart look good.

- Size of chart
- Title and subtitle
- Size and color of line
- Axis formatting
- Reference marks

<br>

## Extra Practice

{{< faq "Altair (and Vega and Vega-Lite and D3!)" >}}

#### What is the difference between a "high-level" and "low-level" programming language or tool? 

Here's what [Google has to say.](https://www.google.com/search?q=high+level+vs+low+level+programming&sxsrf=ALeKk00ZSifsXMTELe5ak1ossS-70RsgXg:1610515315933&tbm=isch&source=iu&ictx=1&fir=ycpdmOoII1RcDM%252Cekx1Wkmyah4tuM%252C_&vet=1&usg=AI4_-kTiopVeLLBbeXMuNvtNgPuThj2Abg&sa=X&ved=2ahUKEwjGvr6KlZjuAhXiHTQIHUL7AqYQ_h16BAgTEAE#imgrc=E6D0vvL8F5YDdM)

- [Altair](https://altair-viz.github.io/) is a Python library built on Vega and Vega-Lite
- [Vega](https://vega.github.io/vega/about/vega-and-d3/) is a "higher-level visualization specification language on top of D3" that creates charts with json files
- [D3](https://d3js.org/) is a JavaScript library

{{</ faq >}}


{{< faq "Altair: Removing commas from years" >}}

#### Remember, Altair builds on Vega, which builds on D3.

Sometimes to answer a question about Altair, you will have to read Vega or D3 documentation. For example:

- [Altair's guide](https://altair-viz.github.io/user_guide/customization.html#adjusting-axis-labels) for customizing axis labels. (Scroll down to the second code example.)
- [D3 options](https://github.com/d3/d3-format/blob/master/README.md#format) for different axis formats.

```
(alt.Chart(my_data)
   .mark_line()
   .encode(
      x = alt.X('year', axis = alt.Axis(format = 'd', title = "Year")), 
      y = alt.Y('Total', axis = alt.Axis(title = "Children with Name"))
    )
)
```

{{</ faq >}}

{{< faq "Altair: Adding a reference line" >}}

#### You may want to include a point or line of reference to help your chart answer the question "compared to what?".

Let's say you have your chart for Grand Question 1 saved as `question_1`. The easiest way I have found to add a reference line is to create a new DataFrame with a single number:

```
line_df = pd.DataFrame({'year': [1990]})
line_df
```

And use the new DataFrame to create a chart with a single line that has a specific value of x (for example, your birth year) but spans the entire y-axis. 

In Altair, this is done with the the `mark_rule()` geometry. You can then "layer" the two charts together.

```
line = alt.Chart(line_df).mark_rule(color="red").encode(x = "year")

final_chart = question_1 + line
final_chart
```
Additional references:
- [Using layered charts](https://altair-viz.github.io/user_guide/compound_charts.html)
- [Altair Marks](https://altair-viz.github.io/user_guide/marks.html)
- [Add a horizontal line to an existent chart](https://github.com/altair-viz/altair/issues/2059)

{{</ faq >}}




<!--------------------

### Discovering a new data relationship.

{{< faq "Look at the names data and write a short paragraph in your notes describing the data set" >}}

We have a row for each name-year.  Excluding the name and year columns we have a column for each state and DC. Finally there is a Total column that sums over the other columns.

> - __If you can't describe what a row is in your table then you don't understand what groups you can talk about with your data.__
> - __The columns tell you what information you will be able to evaluate on each 'group' or 'observation' in your data.__

 __We want [tidy data](https://byuidatascience.github.io/python4ds/tidy-data.html).__

{{</ faq >}}

----------------------->

<!-------------------

{{< faq "Which name has been given the most and the least?" >}}

> 1. Sum all the years for each name (`groupby()`).
> 2. Create a new DataFrame for the totals.
> 3. Write a query that filters the total data to the max and min.
> 4. Create a markdown table with the information.    
>     A. `to_markdown()` requires the `tabulate` package.    
>     B. `to_markdown()` with arguments `showindex` and `floatformat`    
>     C. [Guidance on `floatformat`](https://stackoverflow.com/questions/37079957/pythons-tabulate-number-of-decimal/37080063)    

```
dat_total = dat.groupby('name').agg(n = ('Total', 'sum')).reset_index()
print(dat_total
    .query('n in [@dat_total.n.max(), @dat_total.n.min()]')
    .to_markdown(showindex = False, floatfmt=".0f"))
```

{{</ faq >}}
-------------------------------->
