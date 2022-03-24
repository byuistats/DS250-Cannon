# Exercise 1
# What is the name of the table that records data about pitchers in the regular seasons?'''

## the ptiching table

# What do the HR and HBP columns mean in that table respectively?

## HR stands for Homeruns
## HBP Batters Hit by Pitch

#%%
# Exercise 2
## Create a query that shows all columns from the table you found in Exercise 1, save the dataframe in a variable "pitch"

import pandas as pd
import altair as alt
import datadotworld as dw

# %%
db = 'byuidss/cse-250-baseball-database'
query1 = '''SELECT *
            FROM pitching'''

result = dw.query(db, query1)

pitch = result.dataframe

#%%
#Exercise 3
## Using a SQL query, select all rows in the same table where HR is less than 10 and gs is greater than 25. 
query2 = '''SELECT *
            FROM pitching
            WHERE HR < 10
                AND gs > 25'''

result = dw.query(db, query2)
print(result.dataframe)

## Find out what the columns mean and explain your query in words
# Select the pitchers that allowed less than 10 homeruns and started more than 25 games in a team for that season. 

# %%
#Exercise 4
## Identify the shared columns (keys) and join the table in exercise 2 with the salaries table.
query3 = '''SELECT *
            FROM pitching
            JOIN salaries 
                USING (playerid, yearid, teamid)
            WHERE yearid = 1986'''

result = dw.query(db, query3)
result.dataframe.shape
# We need to join using teamid because some pitchers transfered to another team 
# mid-season, and they are getting paid differently.

#%%
# Exercise 5

## Create a query that captures the number of pitchers the Washington Nationals used in each year.

query4 = '''SELECT COUNT(DISTINCT playerid), yearid
            FROM pitching
            WHERE teamid = 'WAS'
            GROUP BY yearid
            ORDER BY yearid'''


#%%
# Exercise 6

## Research the order of operations for SQL and put the following keywords in that order.

# The order is FROM JOIN WHERE GROUP BY HAVING SELECT ORDER BY LIMIT

