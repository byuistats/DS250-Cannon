# %%
import pandas as pd 
import numpy as np
import altair as alt 
import sqlite3

# %%
sqlite_file = '../data/lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)

# %%
table = pd.read_sql_query(
    "SELECT * FROM sqlite_schema WHERE type='table'",
    con)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
print(table.sql[0])
# %%

# Data check
# https://www.cbssports.com/mlb/news/the-14-all-stars-did-not-play-in-the-2017-mlb-all-star-game-and-why-they-did-not/

# Here is the final table query to answer the two statements.

# Which year had the most players players selected as All Stars 
# but didn't play in the All Star game after 1999?

# provide a summary of how many games, hits, and at bats 
# occured by those players had in that years post season.

pd.read_sql_query(
'''
SELECT bp.yearid, sum(ab) as ab, sum(h) as h,
    sum(g) as games, count( DISTINCT bp.playerid) as num_players, 
    asf.gp, asf.gameid
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp == 0
GROUP BY bp.yearid
ORDER BY bp.yearid
''',
con)


# %%
bp = pd.read_sql_query(
'''
SELECT *
FROM battingpost
WHERE yearid == 2017
''', con)

alst = pd.read_sql_query(
'''
SELECT *
FROM allstarfull
WHERE yearid == 2017
''', con)

bp_noals = (bp.merge(
        alst.filter(['playerID', 'yearID', "GP"]), 
        on = ['playerID', 'yearID'])
    .query('GP == 0'))

# %%

# %%

(bp_noals    
    .groupby(['yearID'])
    .agg(
        ab = ('AB', 'sum'),
        h = ('H', 'sum'),
        games = ('G', 'sum'),
        num_players = ('playerID', 'nunique')
    )
    .reset_index()
)
# %%
# check stuff
(bp.merge(
        alst.filter(['playerID', 'yearID', "GP"]), 
        on = ['playerID', 'yearID'])
    .query('GP == 0 & yearID == 2017'))


bp.query('@bp.playerID.isin(@noplay_alst)').query('yearID == 2017')
alst.query('GP == 0 & yearID == 2017')

alst.query('@alst.playerID.isin(@noplay_alst)').query('yearID == 2017')

# %%
