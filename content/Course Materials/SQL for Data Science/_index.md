---
title: "SQL for Data Science"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

We will be using [data.world](https://data.world/) as our remote server. They have a [Python package](https://github.com/datadotworld/data.world-py) that we will use to connect to their environment and process our SQL commands.

- [Data.World SQL Guide](https://docs.data.world/documentation/sql/concepts/basic/intro.html)

## Specific Data.World links

* [Install data.world](https://datadotworld.github.io/data.world-py/python.html)
* [SELECT and FROM clauses](https://docs.data.world/documentation/sql/concepts/basic/SELECT_and_FROM.html)
* [WHERE and comparison operators](https://docs.data.world/documentation/sql/concepts/basic/WHERE.html)
* [ORDER BY](https://docs.data.world/documentation/sql/concepts/basic/ORDER_BY.html)
* [Joins](https://docs.data.world/documentation/sql/concepts/intermediate/Joins.html)
* [Aggregations](https://docs.data.world/documentation/sql/concepts/intermediate/aggregations.html)
* [GROUP BY](https://docs.data.world/documentation/sql/concepts/intermediate/GROUP_BY.html)

## Baseball Instructions for data.world

To access the data, complete the following steps:

1. Make an account on [data.world](https://data.world/login) and click on the [join now](dataworld_join.png)
2. Install the data.world Python package using `pip install datadotworld` or `pip3 install datadotworld` (see [the package installation help](../../python-for-data-science/))
3. The data.world package needs your API token in order to query data. In the console, type `dw configure` and then entire your API token when prompted.
4. Follow the link provided in your terminal to get your API token (<https://data.world/settings/advanced>).
5. Paste the token into your terminal.
6. If you are on Windows and `dw configure` doesn't work, see below for guidance.

You are now ready to query the baseball relational database. This [data dictionary](http://www.seanlahman.com/files/database/readme2017.txt) will tell you what tables are available and help you understand the relationships between tables. 

Here is an example showing the first 5 rows of the `AllstarFull` table. Note that when using `dw.query` the first argument will always be `byuidss/cse-250-baseball-database` and the second argument will be your SQL query.

```python
import datadotworld as dw

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM allstarfull LIMIT 5')

print(results.dataframe)
```

### `dw configure` issues

Some Windows users will not be able to use `dw configure`.  You will get an error such as

```sh
dw : The term 'dw' is not recognized as the name of a cmdlet, function, 
script file, or operable program. Check the spelling of the name, or if 
a path was included, verify that the path is correct and try again.
At line:1 char:1
```

If you get this issue, you can manually create the `config` file in the right location on your computer to get the datadotworld python package to work.

1. Make sure you have your Folder view settings changed so you can see `File name extensions` and `Hidden items`.
1. Navigate to `C:/Users/<YOURUSER>/` and create a folder `.dw` if it isn't already there.
1. In that folder, create a `config` file with no extension.
1. Open that `config` file in VS code.
1. Put the following information in the `config` file and save.

```sh
[DEFAULT]
auth_token = eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJwcm9kLXVzZXI
```
