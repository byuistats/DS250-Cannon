---
title: "Day 1: Intro to Project 3"
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

<br>

<!-------------
![](https://imgs.xkcd.com/comics/so_bad_its_worse.png)

## My history with SQL and NoSQL

> 1. In 2005 I started work at Pacific Northwest National Laboratory, having a master's in statistics completed and never having seen the SQL language.
> 2. In late 2005, I had to pull data from a SQL database for use in R related to our airline network.  It wasn't fun building a tidy table from a SQL database with no background in SQL. I am on the team that wins the [R&D 100 Award](https://www.pnnl.gov/about/rd100awards.asp). 
> 3. In 2012 Ryan Hafen and Jeremiah Rounds introduced me to Hadoop and the concept of [key-value databases](https://aws.amazon.com/nosql/key-value/), and I am enamored. 
> 4. From 2013 - 2015, I am in deep with Hadoop, using it to answer climate science problems using data well over terabytes in size.
> 5. I start developing the data science degree in 2016 with Scott Burton and Brent Morring, and I wonder if SQL is needed in the program. Upon researching, I realize that SQL as a language is having a resurgence regardless of the back-end database.
> 6. In 2017 we used CIT 111 and CIT 225 in the DS program to give students a SQL background.  
> 7. In 2020 we introduce CSE 250 and CSE 451 to provide DS students more access to the SQL language for data science applications.

#### [Google's influence on Big Data](https://medium.com/@garyorenstein/did-google-send-the-big-data-industry-on-a-10-year-head-fake-9c94d553925a)

__Big Data timeline__   

> 1. 2004 Paper on MapReduce released by Google
> 2. 2012 Hadoop 1.0 released for use.
> 3. 2017 Hadoop hype has come and gone.
> 4. Beyond 2017 the rise of new scalable databases that embrace SQL.

![](https://blog.timescale.com/content/images/2018/12/image-112.png)
--------------->

## What is Structured Query Language (SQL)?

<iframe width="560" height="315" src="https://www.youtube.com/embed/T8ngx84oHFY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/27axs9dO7AE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br>

<!-----------------------------------------
### History of SQL

![](https://blog.timescale.com/content/images/2018/12/image-107.png)

<br>

From [Early History of SQL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6359709):

> Ray and I were impressed by how compactly Codd’s languages could represent complex queries. However, at the same time, we believed that it should be possible to design a relational language that would be more accessible to users without formal training in mathematics or computer programming. We believed that barriers to widespread acceptance of Codd’s languages existed on two levels.    
>   .
>   
> 1. The first barrier came from the mathematical notation, which was hard to enter at a keyboard. This barrier was superficial and could be easily dealt with by replacing symbols with keywords.
>
> 2. The more difficult barrier was at the semantic level. The basic concepts of Codd’s languages were adapted from set theory and symbolic logic. This was natural given Codd’s background as a mathematician, _but Ray and I hoped to design a relational language based on concepts that would be familiar to a wider population of users._ We also hoped to extend the language to encompass database updates and administrative tasks such as the creation of new tables and views, which had traditionally been outside the scope of a query language.

<br>

SQL is "a relational language based on concepts that would be familiar to a wider population of users."

> When we moved to the San Jose Research Laboratory in 1973 to join the System R project, we began work on another new language that we called Sequel. Sequel allowed the well-paid-employee query to be represented in a readable form free from mathematical concepts and symbols. ... In 1977, because of a trademark issue, the name Sequel was shortened to SQL.
>
------------------------------------->

<br>

### Ok, but how does it work?

SQL uses keywords to pull (or "fetch", "extract") the data we want from a database. The computer reads those keywords in a specific order. 

From [EverSQL](https://www.eversql.com/sql-order-of-operations-sql-query-order-of-execution/) we can get some more background:

> This is the logical order of operations, also known as the order of execution, for an SQL query:
>
> </br>
>
> 1. FROM, including JOINs
> 1. WHERE
> 1. GROUP BY
> 1. HAVING
> 1. WINDOW functions
> 1. SELECT
> 1. DISTINCT
> 1. UNION
> 1. ORDER BY
> 1. LIMIT and OFFSET
>
> </br>
>
> But the reality isn't that easy nor straight forward. As we said, the SQL standard defines the order of execution for the different SQL query clauses. Said that, modern databases are already challenging that default order by applying some optimization tricks which might change the actual order of execution, though they must end up returning the same result as if they were running the query at the default execution order.

__For CSE 250: Don't think too hard about optimization at this point.  Let the database figure out the optimized routine.__  
<!--------------- 
(If we were in Pandas, we would need to [think about the optimized order](https://medium.com/swlh/reproducing-sql-queries-in-python-codes-35d90f716b1a).)
--------------->

Most SQL queries are typed in the following pattern:

```SQL
SELECT -- <columns> and <column calculations>
FROM -- <table name>
  JOIN -- <table name>
  ON -- <columns to join>
WHERE -- <filter condition>
GROUP BY -- <subsets for column calculations>
HAVING -- <grouped filter condition>
ORDER BY -- <how the output is returned in sequence>
LIMIT -- <number of rows to return>
```
<br>

## Project 3 - what are our goals?

Do we understand the questions being asked in Project 3?


<br>

## The baseball data

Let's start exploring the baseball data!

- You'll need to download the [SQLite Databse](https://byuistats.github.io/CSE250-Course/data/lahmansbaseballdb.sqlite)
- And review the [data dictionary](https://www.seanlahman.com/files/database/readme2017.txt)

```python
import pandas as pd
import sqlite3

con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query("SELECT * FROM fielding LIMIT 5", con)
df
```


<!---------------------------
### Let's make the connection

[Class reading](../../../course-materials/sql-for-data-science/)

### Let's view our tables

[data.world basebal data](https://data.world/byuidss/cse-250-baseball-database/workspace)


```python
import datadotworld as dw

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM batting LIMIT 5')

batting5 = results.dataframe
```
----------------------------->

<br>

## Understanding SQL queries

Make sure you do the project readings!

<!-------------------------------
#### I want to do a calculation in SQL and return it in a new column in Python?

__Use the batting table to show the player and his team with his at batts and runs together with a calculated value of `ab / r` that is called `runs_atbat`.__

- __Try do complete the above statement without using the info in the questions below.__

{{< faq "What table do we want to use?">}}

```python
q = '''
SELECT *
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}




{{< faq "What columns do we want to select?">}}

```python
q = '''
SELECT playerid, teamid, ab, r
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}


{{< faq "What calculation do we want to perform?">}}


```python
q = '''
SELECT playerid, teamid, ab, r, ab/r 
FROM batting
LIMIT 5
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

```


{{</ faq >}}


{{< faq "What name do we give our calculated column?">}}


```python
q = '''
SELECT playerid, teamid, ab, r, ab/r as runs_atbat
FROM batting
LIMIT 5
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

```


{{</ faq >}}
-------------------------------------------->


