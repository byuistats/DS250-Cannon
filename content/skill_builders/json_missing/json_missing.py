# %%
# Loading in packages
import pandas as pd
import numpy as np

# %%
# Loading in data
url = ""
data = pd.read_json(url)

# %%
#### Exercise 1 ####

# How many rows are there? How many columns?
data.shape  # This returns (rows, columns)

# What does a row represent in this dataset?
# - A row is a reported ufo sighting

# What are the different ways missing values are encoded?
# Object columns
data.city.value_counts(dropna=False)  # No missing values here
data.shape_reported.value_counts(dropna=False)  # NaN are present
data.were_you_abducted.value_counts(dropna=False)  # - looks like a missing value
# Numeric columns
data.distance_reported.describe()  # -999 looks like a missing value encoding
data.distance_reported.isna().sum()  # 16 NaN in this column
data.estimated_size.isna().sum()  # No missing here

# How many np.nan in each column?
data.isna().sum()

# %%
#### Exercise 2 ####

# Shape reported replacing nan values with missing string
data.shape_reported.fillna("missing", inplace=True)
# Distance reported column replacing -999 values with nan value
data.distance_reported.replace(-999, np.nan, inplace=True)
# Imputing distance reported column with mean
data.distance_reported.fillna(data.distance_reported.mean(), inplace=True)
# Were you abducted replacing - with missing
data.were_you_abducted.replace("-", "missing", inplace=True)

# Printing first ten rows to paste in markdown
print(data.head(10).to_markdown())

# %%
#### Exercise 3 ####

# What is the median estimated size by shape, and mean distance reported by shape?
stats_table = (data.groupby("shape_reported")
               .agg(median_est_size=('estimated_size', 'median'),
                    mean_distance_reported=("distance_reported", 'mean'),
                    group_count=('were_you_abducted', 'count')))

# Printing table to markdown
print(stats_table.to_markdown())

# %%
#### Exercise 4 ####

# Changing all estimated size to sqft
cities_sqin = ["Holyoke", "Crater Lake", "Los Angeles", "San Diego", "Dallas"]

# Think of this as an if else statement
data = data.assign(estimated_size_sqft=np.where(data.city.isin(cities_sqin),  # Condition
                                                data.estimated_size / 144,  # If condition is true
                                                data.estimated_size))  # If condition is false

# Printing table to markdown
print(data.head(10).to_markdown())
