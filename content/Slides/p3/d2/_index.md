---
title: "Day 2: SQL Calculations"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Gratitude Journal

#### Announcements

<br>

## Class Activity in Slack

### Part 1

**Goal:** Describe in words (NOT using code) how to get from your *starting data* to your *ending data*. 

Post your answer in your group's Slack thread. You have 7 minutes, and are allowed to ask me 1 question.

### Part 2

**Goal:** Now try to write a SQL query to get your ending data.

Post your SQL query in your group's Slack thread. You have 7 minutes, and are allowed to ask me 1 question.

Here is the SQL template for your use.

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

<br>

<!-------------------------
## Connecting to data.world in Python

#### Make the connection

[Class reading](../../../course-materials/sql-for-data-science/)

```python
import datadotworld as dw

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM batting LIMIT 5')

results.dataframe
```
<br>

#### What information is available?

- [data.world baseball data](https://data.world/byuidss/cse-250-baseball-database/workspace)

- [Data dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt)


<br>
------------------------------------>

<!-------------------
## Working with SQL

### Group activity

1. With your group, create an example for your SQL keyword using the assigned data set. 
2. Your group will use this example to teach the class more about SQL and more about the baseball data.
3. Your group needs to post your code example in Slack.

> - Group 1: [SELECT and FROM](https://docs.data.world/documentation/sql/concepts/basic/SELECT_and_FROM.html) with the `people` table (called "master" in the data dictionary). Include examples of `SELECT AS` and `SELECT DISTINCT`.
> - Group 2: [WHERE](https://docs.data.world/documentation/sql/concepts/basic/WHERE.html) with the `schools` table. Try using different types of comparison operators, or making multiple comparisons with `AND`.
> - Group 3: [ORDER BY](https://docs.data.world/documentation/sql/concepts/basic/ORDER_BY.html) with the `salaries` table. Try sorting in different orders (ascending or descending) and with multiple columns.
> - Group 4: [JOIN](https://docs.data.world/documentation/sql/concepts/intermediate/Joins.html) with the `schools` and `collegeplaying` tables (focus on "inner" joins).
> - Group 5: [Aggregations](https://docs.data.world/documentation/sql/concepts/intermediate/aggregations.html) with the `batting` table.
> - Group 6: [GROUP BY](https://docs.data.world/documentation/sql/concepts/intermediate/GROUP_BY.html) with the `batting` table.

<br>
-------------------------->

## Getting started

**Question One:** Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

Think about:
- What tables (data) do you need?
- What SQL commands do you need?

<br>

<!---------------------------
## More for Project 3

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


#### I want to join two tables to help in decision making

__Which year had the most players players selected as All Stars but didn't play in the All Star game after 1999?__

- __provide a summary of how many games, hits, and at bats occured by those players had in that years post season.__


```python
import pandas as pd 
import altair as alt
import numpy as np
import datadotworld as dw

con_url = 'byuidss/cse-250-baseball-database'
```

{{< faq "What table do we want for All Star information?">}}


```python
# %%
# allstar table

dw.query(con_url, 
'''
SELECT *
FROM AllstarFull
WHERE 
    AND 
LIMIT 5
''').dataframe

```

{{</ faq >}}



{{< faq "Can you use a groupby to get the counts of players per year?">}}

```python
dw.query(con_url, 
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
dw.query(con_url, 
'''
SELECT *
FROM BattingPost as bp
LIMIT 5
''').dataframe
```

{{</ faq >}}

{{< faq "Can you join the batting table and AllStar information and keep only the at bats, hits with the all star gp and gameid columns?">}}

__Let's only keep players with at least one at bat in the post season__

```python
dw.query(con_url, 
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


__Which year had the most players players selected as All Stars but didn't play in the All Star game after 1999?__

- __provide a summary of how many games, hits, and at bats occured by those players had in that years post season.__

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


--------------------------------------------------------->

## Extra Practice

#### "I get SQL and want to be challenged."

[Do this Math 335 task with SQL commands in Python](https://byuistats.github.io/M335/class_tasks/task12_details.html).