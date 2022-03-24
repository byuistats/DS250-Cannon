# %%
# Loading in packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# %%
# Loading in data
url = ""
data = pd.read_csv(url)

# Getting familiar with data
data.head()  # Taking a peek
data.dtypes  # What kind of data types do we have?
data.isna().sum()  # Any missing values?
data.describe()  # Summary statistics
data.survived.value_counts(normalize=True)  # Is there a class imbalance? Yes...

# %%
#### Exercise 1 ####
title = "Does age affect whether a passenger survived?"
chart1 = alt.Chart(data, title=title).transform_density(
    "age",
    as_=["age", "density"],
    groupby=["survived"]
).mark_area(opacity=.5).encode(
    alt.X("age:Q"),
    alt.Y("density:Q"),
    alt.Color("survived:N")
).configure_title(anchor="start")

chart1.save("titanic.svg")

# %%
#### Exercise 2 ####

# Step 0
X = data.drop("survived", axis=1)  # Drops the target column
y = data['survived']  # Selects the target columns

# %%
# Step 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=24, stratify=y)
# %%
# Step 2
rf = RandomForestClassifier(random_state=24)  # Creating random forest object
rf.fit(X_train, y_train)  # Fit with the training data

# %%
# Step 3
y_pred = rf.predict(X_test)  # Using the features in the test set to make predictions

# %%
# Step 4
accuracy_score(y_test, y_pred)  # Comparing predictions to actual values

# %%
#### Exercise 3 ####
feat_imports = (pd.DataFrame({"feature names": X_train.columns,
                              "importances": rf.feature_importances_})
                .sort_values("importances", ascending=False))

print(feat_imports.to_markdown(index=False))
