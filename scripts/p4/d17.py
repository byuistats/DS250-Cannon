# %%
import pandas as pd 
import altair as alt 
import numpy as np 

# %%
# Load modules
from sklearn.model_selection import train_test_split
from sklearn import tree

from sklearn import metrics

# from sklearn.naive_bayes import GaussianNB
# from sklearn.ensemble import GradientBoostingClassifier

# %%
# Load data
dwellings = pd.read_csv('https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv')
dwellings_ml = pd.read_csv('https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv')
neighborhood = pd.read_csv('https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv')
alt.data_transformers.enable('json')

# %%
X_pred = dwellings_ml.drop(dwellings_ml.filter(regex = 'before1980|yrbuilt').columns, axis = 1)
y_pred = dwellings_ml.filter(regex = "before1980")
X_train, X_test, y_train, y_test = train_test_split(
    X_pred, y_pred, test_size = .34, random_state = 76)  

# %%
# https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_probs = clf.predict_proba(X_test)

# %%
print(metrics.classification_report(y_pred, y_test))

# %%
metrics.plot_roc_curve(clf, X_test, y_test)

# %%
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': clf.feature_importances_}).sort_values('f_values', ascending = False)

(alt.Chart(df_features.query('f_values > .011'))
    .encode(
        alt.X('f_values'),
        alt.Y('f_names', sort = '-x'))
    .mark_bar())

