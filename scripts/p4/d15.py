# %% 
# install packages
import sys
!{sys.executable} -m pip install seaborn scikit-learn

# %%
# libraries
import pandas as pd 
import altair as alt
import numpy as np
import seaborn as sns

# %% 
# scikit learn froms
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
# %%
# load data
dwellings_denver = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv")
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")
dwellings_neighborhoods_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv")   

alt.data_transformers.enable('json')

# %%
h_subset = dwellings_ml.filter(['livearea', 'finbsmnt', 'basement', 
    'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 'before1980', 'stories', 'yrbuilt']).sample(500)
sns.pairplot(h_subset, hue = 'before1980')

# %%
corr = h_subset.drop(columns = 'before1980').corr()
# %%
sns.heatmap(corr)
# %%
