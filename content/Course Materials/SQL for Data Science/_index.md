---
title: "SQL for Data Science"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

There are many [flavors of SQL](https://en.wikipedia.org/wiki/Database#Database_management_system) but most flavors have the same base commands. SQL queries are typed in the following pattern;

```SQL
SELECT -- <columns> and <column calculations>
FROM -- <table name>
  JOIN -- <table name>
  ON -- <columns to join>
WHERE -- <filter condition on rows>
GROUP BY -- <subsets for column calculations>
HAVING -- <filter conditions on groups>
ORDER BY -- <how the output is returned in sequence>
LIMIT -- <number of rows to return>
```

## Introductory SQL links

- [SQL Guide](https://docs.data.world/documentation/sql/concepts/basic/intro.html)
- [SELECT and FROM clauses](https://docs.data.world/documentation/sql/concepts/basic/SELECT_and_FROM.html)
- [WHERE and comparison operators](https://docs.data.world/documentation/sql/concepts/basic/WHERE.html)
- [ORDER BY](https://docs.data.world/documentation/sql/concepts/basic/ORDER_BY.html)
- [Joins](https://docs.data.world/documentation/sql/concepts/intermediate/Joins.html)
- [Aggregations](https://docs.data.world/documentation/sql/concepts/intermediate/aggregations.html)
- [GROUP BY](https://docs.data.world/documentation/sql/concepts/intermediate/GROUP_BY.html)


```python
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3

# %%
# careful to list your path to the file.
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)

results = pd.read_sql_query( 
    'SELECT * FROM allstarfull LIMIT 5',
    con)

results
```

You can see the list of tables available in the database;

```python
table = pd.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type='table'",
    con)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
print(table.sql[8])
```
