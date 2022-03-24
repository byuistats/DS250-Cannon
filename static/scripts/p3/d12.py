# %%
import pandas as pd 
import altair as alt
import numpy as np
import datadotworld as dw


# %%
# See d15.py for the first set of examples.
con_url = 'byuidss/cse-250-baseball-database'

# %%
# allstar table

dw.query(con_url, 
'''
SELECT *
FROM AllstarFull
WHERE yearid > 1999 
    AND gp != 1
LIMIT 5

''').dataframe

# %%
# Can you use a groupby to get 
# the counts of players per year?

dw.query(con_url, 
'''
SELECT yearid, COUNT(*) as num_players
FROM AllstarFull
WHERE yearid > 1999 
    AND gp != 1
GROUP BY yearid
ORDER BY yearid
''').dataframe



# %%
# join season game data and 
# calculate the total atbats and hits for each player by year.
dw.query(con_url, 
'''
SELECT *
FROM BattingPost as bp
LIMIT 5

'''
).dataframe

# %%
# Can you join the batting table and AllStar 
# information and keep only the at bats, 
# hits with the all star gp and gameid columns?

dw.query(con_url, 
'''
SELECT bp.playerid, bp.yearid, ab, h, asf.gp, asf.gameid
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp != 1
    AND ab > 0
LIMIT 15

'''
).dataframe

# %%
# Let's build the final table

# Which year had the most players players selected as All Stars 
# but didn't play in the All Star game after 1999?

# provide a summary of how many games, hits, and at bats 
# occured by those players had in that years post season.

dw.query('byuidss/cse-250-baseball-database', 
'''
SELECT bp.yearid, sum(ab) as ab, sum(h) as h,
    sum(g) as games, count(ab) as num_players, 
    asf.gp, asf.gameid
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp != 1
    AND ab > 0
GROUP BY bp.yearid
ORDER BY bp.yearid
'''
).dataframe
# %%
