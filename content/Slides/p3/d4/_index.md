---
title: "Day 4: Practice Coding Challenge"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---
<!-------------------------------------------------------------------------------------

## Calculating New Columns

#### I want to calculate a new column in SQL

Use the batting table to show the player and his team, along with his at bats, runs, and a calculated value of `r / ab` that is called `runs_atbat`.

- Try do complete the above statement without using the info in the questions below.

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

The [data dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt) might help.

- For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?
- Provide a summary of how many games, hits, and at bats all the players had in that year's post season.

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

- For each player, keep only the at bats, hits, the all star gp, and gameid columns.
- Let's only keep players with at least one at bat in the post season.


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

- For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?
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
------------------------------------------------------------------------------->

<!-----------------------------------------------
<br>

### Altair Examples

<br>

### Brainstorm

What are some ideas for Grand Question 3?

> Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison.

__In your group, answer the following questions and be prepared to share your answers with the class.__

1. What will you use to compare the two baseball teams?
2. What table(s) does this information come from?
3. Do you need to do any calculations?
4. Can you think of any problems you might run into?

<br>

### Open Programming Time
--------------------------------------------------->

<br>