# %%

import pandas as pd 
import altair as alt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

# %%

url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
dat_home = pd.read_csv(url).sample(n=4500, random_state=15)

# %%

pdat = dat_home.query("""
    yrbuilt > 0 and \
    livearea > 0 and \
    arcstyle in ["ONE-STORY", "TWO-STORY", "SPLIT LEVEL"]
    """)


chart = alt.Chart(pdat, 
    title = "Thank goodness the 21st century doesn't have split levels").encode(
    alt.X('yrbuilt', 
        scale=alt.Scale(zero=False), 
        axis=alt.Axis(format=".0f"),
        title = "Year home was built"),
    alt.Y('livearea', 
        scale=alt.Scale(zero=False, type = 'log'),
        title = "Square footage of home (log)"),
    color = alt.Color('arcstyle', 
        legend=alt.Legend(title="Standard house types", orient="bottom"),
        scale=alt.Scale(scheme='dark2'))
).mark_circle(size=50)

chart.save('split_entry.png', scale_factor=2.0)

# %%

# %%
# Programmatically replace all the `lost` values with 125 and make a boxplot. 

mister = pd.Series(["lost", 15, 22, 45, 31, "lost", 85, 38, 129, 80, 21, 2])

alt.Chart(pd.DataFrame({'values':mister.replace("lost", 125), "x":"x"})).encode(x = "x" , y = 'values').mark_boxplot()

# %%
# Programmatically replace all the `lost` values with 125 and report the mean rounded to two decimals. 
mister.replace("lost", 125).mean().round(2)

# %%
# Programmitcally read in the following JSON file, keep only the cases column and return a markdown table that has country in the rows and cases for 1999 and 2000 in the columns. Your table will have six cells with values.

url = 'https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/table1/table1.json'

print(pd.read_json(url)
    .filter(['country', 'year', 'cases'])
    .pivot(index='country', columns = 'year')
    .to_markdown())


# %%
# Use our cleaned example of the star wars data from project 6 to predict 
# the gender of the respondent to the survey respondent. Report your precision and a feature importance plot.
url = "http://byuistats.github.io/CSE250-Course/data/clean_starwars.csv"
dat = pd.read_csv(url)

# %%
X_pred = dat.drop(['gender'], axis = 1)
y_pred = pd.get_dummies(dat.gender, drop_first = True)

X_train, X_test, y_train, y_test = train_test_split(
    X_pred, y_pred, test_size = .20, random_state = 2020)   

# %%
classifier = GradientBoostingClassifier()
classifier.fit(X_train, y_train)

y_predict = classifier.predict(X_test)

metrics.accuracy_score(y_test, y_predict)

# metrics.plot_confusion_matrix(classifier, X_test, y_test)
# print(metrics.confusion_matrix(y_test, y_predict))
# print(metrics.classification_report(y_test, y_predict))

# %%
dat_import = (pd.DataFrame({
        "fnames": X_train.columns, 
        "fimport": classifier.feature_importances_})
    .sort_values('fimport', ascending = False)
    .head(12))

(alt.Chart(dat_import)
    .encode(
        x = 'fimport', 
        y = alt.Y('fnames', sort = "-x")).mark_bar())
# %%
