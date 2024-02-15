---
title: "Day 3: The end of baseball"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Spiritual Thought

#### Announcements

1. Practice Coding Challenge
2. Can I still get an "A"?
    * Profile of an "A" student
    * What if I fall behind? 
4. Reminders:
    * DS community assignment
    * Review and Request Letter

#### Coding Challenge:

How do I prepare?
What would your coding challenge look like?

#### Project 3 Questions

1. Integer Division
2. Career Batting Average
3. What have come up with for Q3?  Metrics? Visualizations? 

<br>

## Question 1

Ask yourself:

1. What do I want and expect the end table to look like?
2. What table(s) and calculations do I need?
3. What makes a row in my end table unique?
4. What problems can I anticipate?

<br>

## Question 2

Ask yourself:

1. What do I want and expect the end table to look like?
2. What table(s) and calculations do I need?
3. What makes a row in my end table unique?
4. What problems can I anticipate?

<br>

## Question 3

What are some ideas for Grand Question 3? Ask yourself:

1. What information will you use to compare the two baseball teams?
2. What table(s) and calculations do I need?
3. What makes a row in my end table unique?
4. What problems can I anticipate?






<!-----------------------------------------
### SQL queries are typed in the following pattern:

```SQL
SELECT -- <columns> and <column calculations>
FROM -- <table name>
  JOIN -- <table name>
  ON -- <columns to join>
WHERE -- <filter condition>
GROUP BY -- <subsets for column calculations>
ORDER BY -- <how the output is returned in sequence>
LIMIT -- <number of rows to return>
```
------------------------------------------->



<!-----------------------------------------------------------------
## Setting up Live Share

<iframe width="560" height="315" src="https://www.youtube.com/embed/oUcc2hp7fDM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Connecting to SQLite: [Lahman SQLite](https://byuistats.github.io/CSE250-Course/data/lahmansbaseballdb.sqlite)

__Download the sqlite file:__ [Lahman sqlite](https://byuistats.github.io/CSE250-Course/data/lahmansbaseballdb.sqlite)


### What is SQLite?

> - [Wikipedia](https://en.wikipedia.org/wiki/SQLite): SQLite is **a popular choice as embedded database software for local/client storage in application software such as web browsers.** It is arguably the most widely deployed database engine, as it is used today by several widespread browsers, operating systems, and embedded systems (such as mobile phones), among others. SQLite has bindings to many programming languages.

> - [SQLite.org](https://www.sqlite.org/about.html): **SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.** The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.

> - [Codecademy](https://www.codecademy.com/articles/what-is-sqlite): SQLite is a database engine. It is software that allows users to interact with a relational database. In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. This fact allows for a great deal of accessibility: copying a database is no more complicated than copying the file that stores the data, sharing a database can mean sending an email attachment.

### Working with SQLite files in Python

```python
# %%
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3

# %%
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)
# %%
# See the tables in the database
table = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'",
    con)
print(table)

```
------------------------------------------------------>




<!---------------------------------------------------------------------------

## Calculating New Columns

#### I want to do a calculation in SQL and return it in a new column in Python

__Use the batting table to show the player and his team, along with his at bats, runs, and a calculated value of `r / ab` that is called `runs_atbat`.__

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
SELECT playerid, teamid, ab, r, r/ab 
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```


{{</ faq >}}


{{< faq "What name do we give our calculated column?">}}


```python
q = '''
SELECT playerid, teamid, ab, r, r/ab as runs_atbat
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}

<br>

#### I want to join two tables to help in decision making

__For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?__

- Provide a summary of how many games, hits, and at bats all the players had in that year's post season.
- The [data dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt) might help.

```python
import pandas as pd 
import altair as alt
import numpy as np
import datadotworld as dw

baseball_url = 'byuidss/cse-250-baseball-database'
```

{{< faq "What table do we want for All Star information?">}}


```python
# %%
# allstar table

dw.query(baseball_url, 
'''
SELECT *
FROM AllstarFull
WHERE --?
    AND --?
LIMIT 5
''').dataframe

```

{{</ faq >}}



{{< faq "Can you use a groupby to get the counts of players per year?">}}

```python
dw.query(baseball_url, 
'''
SELECT yearid, -- <stuff to calculate>
FROM AllstarFull
WHERE yearid > 1999 
    AND gp != 1
GROUP BY --?
ORDER BY --?
''').dataframe
```

{{</ faq >}}



{{< faq "What table do we want for the post season at bats?">}}

```python
dw.query(baseball_url, 
'''
SELECT *
FROM BattingPost as bp
LIMIT 5
''').dataframe
```

{{</ faq >}}

{{< faq "Can you join the post season batting table and AllStar information?">}}

- __For each player, keep only the at bats, hits, the all star gp, and gameid columns.__
- __Let's only keep players with at least one at bat in the post season.__


```python
dw.query(baseball_url, 
'''
SELECT -- <columns to keep>
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  -- <two columns for the join>
WHERE bp.yearid > 1999
    AND gp != 1
    AND -- <at bat condition>
LIMIT 15

'''
).dataframe
```
{{</ faq >}}

{{< faq "Let's build the final table">}}


__For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?__

- Provide a summary of how many games, hits, and at bats all the players had in that year's post season.

```python
dw.query('byuidss/cse-250-baseball-database', 
'''
SELECT -- <lots of calculations>
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp != 1
    AND ab > 0
GROUP BY -- <column>
ORDER BY -- <column>
'''
).dataframe
```
{{</ faq >}}


<br>
--------------------------------------------------------------------->







<!----------------------------
## Work with a subset in pandas

Often, you can pull a small subset of the data and work through the logic in Python to make sure you are working out the logic correctly.

1. Only want to pull small parts of each table needed.
2. Small part should be a a complete division.  For example, lets use Idaho.
3. Then use Pandas to work out all the table join logic.
4. Check your work against the SQL call.

### How can we check our SQL logic?

> I want to see how much each college player from schools in the west and mountain west has made over their professional career. I want to know the full school name attended and the the Given name of each player.

_Is this query correct?_

```SQL
SELECT cp.playerID, nameGiven, birthYear
    ,cp.schoolID, name_full
    ,SUM(salary) as salary
FROM salaries as sal
JOIN people as p
    ON p.playerID = sal.playerID
JOIN CollegePlaying as cp
    ON p.playerID = cp.playerID
JOIN schools as sc
    ON sc.schoolID = cp.schoolID
WHERE sc.state = 'ID'
GROUP BY cp.playerID, cp.schoolID
ORDER BY name_full
```

```python
pd.read_sql_query(
'''
SELECT cp.playerID, nameGiven, birthYear
    ,cp.schoolID, name_full
    ,SUM(salary) as salary
FROM salaries as sal
JOIN people as p
    ON p.playerID = sal.playerID
JOIN CollegePlaying as cp
    ON p.playerID = cp.playerID
JOIN schools as sc
    ON sc.schoolID = cp.schoolID
WHERE sc.state = 'ID'
GROUP BY cp.playerID, cp.schoolID
ORDER BY name_full
''', con) 
```

#### Let's start here

```python
schools = pd.read_sql_query(
'''
SELECT *
FROM schools
WHERE state = 'ID'
''', con)
```
----------------------------------------------------->



<!--------------------

#### I get SQL and want to be challenged.

[Do this Math 335 task with SQL commands in Python](https://byuistats.github.io/M335/class_tasks/task12_details.html).

-------------------------->

<br>
