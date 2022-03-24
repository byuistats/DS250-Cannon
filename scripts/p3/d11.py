# %%
import pandas as pd 
import numpy as np 
import altair as alt 

# %%
# Now our new packages
# https://byuistats.github.io/CSE250-Course/course-materials/sql-for-data-science/
import sys
!{sys.executable} -m pip install datadotworld

# %%
import datadotworld as dw

# %%
results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM batting LIMIT 5')

batting5 = results.dataframe
# %%
# What columns do we want to select?
q = '''
SELECT playerid, teamid, ab, r
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

# %%
# What calculation do we want to perform?

q = '''
SELECT playerid, teamid, ab, r, ab/r 
FROM batting
LIMIT 5
'''

batting_calc = (dw
    .query('byuidss/cse-250-baseball-database', q)
    .dataframe)

# %%

# What name do we give our calculated column?

q = '''
SELECT playerid, teamid, ab, r, ab/r as runs_atbat
FROM batting
LIMIT 5
'''

batting_calc = (dw
    .query('byuidss/cse-250-baseball-database', q)
    .dataframe)

# %%
