---
title: "Project 3: Finding relationships in baseball."
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---


### Background

When you hear the word “relationship” what is the first thing that comes to mind? Probably not baseball. But a relationship is simply a way to describe how two or more objects are connected. There are many relationships in baseball such as those between teams and managers, players and salaries, even stadiums and concession prices. The graphs on [Data Visualizations from Best Tickets](https://web.archive.org/web/20200804101201/http://www.besttickets.com/blog/mlb-players-census/) show many other relationships that exist in baseball.

For this project, your client would like developed SQL queries that they can use to retrieve data for use on their website without needing Python. They would also like to see example Altair charts.

### Data

__Data Conection:__ [lahmansbaseballdb](../../data/lahmansbaseballdb.sqlite)   
__Connection Instructions:__ [See SQL for Data Science](../../course-materials/sql-for-data-science/)

### Readings

- [SQL for Data Science Readings (read all links)](../../course-materials/sql-for-data-science/)

#### Optional References

- [Why SQL is beating NoSQL, and what this means for the future of data](https://blog.timescale.com/blog/why-sql-beating-nosql-what-this-means-for-future-of-data-time-series-database-348b777b847a/)
- [Lahman Data Dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt)


### Questions and Tasks

1. __Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.__

2. __This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)__

    <ol type="a">
        <li> <b>Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.</b></li>
        <li><b>Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.</b></li>
        <li><b>Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.</b></li>
    </ol>   

3. __Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc). Write an SQL query to get the data you need, then make a graph in Altair to visualize the comparison. What do you learn?__  


### Deliverables

_Use this [template](../../template/ds250_project_template_clean.qmd) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/ds250_project_template.qmd)):_

1. _A short summary that highlights key that describes the results describing insights from  metrics  of the project and the tools you used (Think “elevator pitch”)._
2. _Answers to the questions from the "Questions and Tasks" section above. Each answer should include a written description of your results, code snippets, charts, and tables._

