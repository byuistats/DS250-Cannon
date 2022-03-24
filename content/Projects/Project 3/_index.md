---
title: "Project 3: Finding relationships in baseball. (4 days)"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---


### Background

When you hear the word “relationship” what is the first thing that comes to mind? Probably not baseball. But a relationship is simply a way to describe how two or more objects are connected. There are many relationships in baseball such as those between teams and managers, players and salaries, even stadiums and concession prices. The graphs on [Data Visualizations from Best Tickets](https://web.archive.org/web/20200804101201/http://www.besttickets.com/blog/mlb-players-census/) show many other relationships that exist in baseball.

Your client would like developed SQL queries that they can use to retreive data for use on their website without needing Python.  They expect to use [Vega](https://vega.github.io/vega/) and [Vega-LIte](https://vega.github.io/vega-lite/) on their website. They would also like to see an example Vega Script with a Vega visualization.

### Data:

__Data Conneection:__ [data.world baseball url](https://data.world/byuidss/cse-250-baseball-database)   
__Connection Instructions:__ [See Baseball Instructions for data.world](../../course-materials/sql-for-data-science/)

### Readings:

- [SQL for Data Science Readings (read all links)](../../course-materials/sql-for-data-science/)
- [Why SQL is beating NoSQL, and what this means for the future of data](https://blog.timescale.com/blog/why-sql-beating-nosql-what-this-means-for-future-of-data-time-series-database-348b777b847a/)

#### Optional References

- [data.world Python package](https://help.data.world/hc/en-us/articles/360039429733-Python-SDK)
- [Lahman Data Dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt)


### Grand Questions:

1. __Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.__

2. __This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)__

    <ol type="a">
        <li> <b>Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.</b></li>
        <li><b>Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.</b></li>
        <li><b>Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.</b></li>
    </ol>   

3. __Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and its description.__  


### Deliverables:

_Use this [template](../../template/cse250_project_template_clean.md) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/cse250_project_template.md)):_

1. _An “elevator pitch” that summarizes the entire case study._
1. _Answers to the grand questions that include text, pictures, and tables._
1. _An appendix that provides your commented code and justification for any programming that required you to choose an option._
