---
title: "SQL & databases"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---


# Skill builder (relational database)

For this skill builder, we are exploring some important topics in relational databases. This exercise will require you to create SQL queries through python. You may want to at least scan the readings before beginning this task since this serves as an assessment of your understanding of the assigned readings. 

A competent student should be able to finish the exercises within 75 minutes. 

## Before you start

Make sure you have installed VS-code, pandas, and Altair on your computer.  

Also make sure you have gone through the tutorial on under course materials called [SQL for Data Science](../../course-materials/sql-for-data-science/):
we assume that you have a connection to your data.

## Exercise 1

### Readme file

A database can consist of more than one table/data set. A relational database consists of tables/data sets that share columns. These shared columns then establish the relationship between the tables, thus the name relational database. The relations are sometimes not easily found and they require careful investigations.

To understand what is in a relational database, we can start with understanding the tables and the columns within.

Here is a link to the [readme file of the baseball database](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt).

> What is the name of the table that records data about pitchers in the regular seasons?

> What do the HR and HBP columns mean in that table respectively?

## Excercise 2 SELECT and FROM

The simplest SQL query is a query with `SELECT` and `FROM`. These are the keywords you will see again and again in SQL. Usually, when constructing a more complex query, it is easier to identify what goes into these two clauses first.

> Create a query that shows all columns from the table you found in Exercise 1, save the dataframe in a variable "pitch"

You script should look something like:

```{python}
result = pd.read_sql_query(
    'SELECT _______ FROM _______',
    con)

results
```

## Excercise 2 WHERE 

The `WHERE` keyword allows us to filter down the table horizontally (fewer rows).

It goes after `SELECT` and `FROM`.

> Using a SQL query, select all rows in the same table where HR is lesser than 10 and gs is greater than 25. 

> Find out what the columns mean and explain your query in words

## Excercise 3 ORDER BY

`ORDER BY` sort the table you select by one or more columns and goes after `WHERE`

> Using the same query in exercise 2, edit it so that the table is ordered by the year of the season(nearest to furthermost) and the player ID(alphabetically).

## Excercise 4 Joins

Joins are used when you wish to create a new table through two different tables. Keep in mind that you have to identify the relationship between two tables before you can correctly join them.

`JOIN` goes between `FROM` and `WHERE`.

> Identify the shared columns (keys) and join the table in exercise 2 with the salaries table, then filter the data so that it shows only pitchers in the year 1986.

You should get a dataframe with 306 rows.

## Exercise 5 Group by
`Group by` is a keyword we use to lower the level of granularity of a table. Meaning we are combining rows into one by the given column(s). 


`Create a query that captures the number of pitchers the Washington Nationals used in each year, then sort the table by year`

You should get a dataframe with 23 rows.
# For the overachievers
## Excercise 6

Research the order of operations for SQL and put the following keywords in that order.

- `SELECT`
- `FROM`
- `JOIN` 
- `WHERE` 
- `HAVING`
- `ORDER BY`
- `GROUP BY`
- `LIMIT`

{{< faq "After you have completed this skill builder with your team (or on your own) then compare your work to our script" >}}

__See the [script](relational_data.py).__

{{</ faq >}}