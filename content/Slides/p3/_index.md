---
title: "Week 6-7: Project 3 - Baseball"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---


{{% notice info %}}
We will use a baseball relational database to explore SQL in Python for data science applications. [Finding relationships in baseball](../../projects/project-4/)
{{% /notice %}}


{{% notice note %}}

**Completed Readings:** [SQL for Data Science Readings (read all links)](../../course-materials/sql-for-data-science/)
 and [Why SQL is beating NoSQL, and what this means for the future of data](https://blog.timescale.com/blog/why-sql-beating-nosql-what-this-means-for-future-of-data-time-series-database-348b777b847a/)


{{% /notice %}}

{{% notice tip %}}
Use the [data.world baseball url](https://data.world/byuidss/cse-250-baseball-database) for the __Data Conneection__. You can read the    
__Connection Instructions__ [for data.world here](../../course-materials/sql-for-data-science/)
{{% /notice %}}

### Grand Questions

1. __Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.__

2. __This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)__

    1. __Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.__
    2. __Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.__
    3. __Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.__

3. __Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and the compiled Vega script that would build the visualization.__
