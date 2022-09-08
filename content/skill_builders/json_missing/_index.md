---
title: "JSONs & missing"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

# UFO Sightings

### Data
[Link to json file](json_missing.json)

### Exercise 1 

Read in the json file as a pandas dataframe. After reading in the data, you'll want to explore it and gain some intuition. Exploring data is a very important step &mdash; the more you know about your data the better! Answer the following questions to gain some insight into this dataset.

- How many rows are there?
- How many columns?
- What does a row represent in this dataset?
- What are the different ways missing values are encoded?
- How many np.nan in each column?

__Some useful code for exploring data__
```python
# Object/Categorical Columns
data.column_name.value_counts(dropna=False)
data.column_name.unique()

# Numeric Columns
data.column_name.describe()

# Counting missing values
data.isna().sum()  # Creates boolean dataframe and sums each column
```

<hr>

### Exercise 2

After learning different ways our data encodes missing values, now we will neatly manage them. There are many techniques we can use to handle missing values; for example, we can drop all rows that contain a missing value, impute with mean or median, or replace missing values with a new `missing` category. We will use some of these techniques in this exercise.

- `shape_reported` - replace missing values with `missing` string.
- `distance_reported` - change -999 values to np.nan. (-999 is a typical way of encoding missing values.)
- `distance_reported` - fill in missing values with the mean (imputation)
- `were_you_abducted` - replace `-` string with `missing` string.

The first 10 rows of your data should look like this after completion of the above steps.

|    | city                 | shape_reported   |   distance_reported | were_you_abducted   |   estimated_size |
|---:|:---------------------|:-----------------|--------------------:|:--------------------|-----------------:|
|  0 | Ithaca               | TRIANGLE         |             8521.9  | yes                 |          5033.9  |
|  1 | Willingboro          | OTHER            |             7438.64 | no                  |          5781.03 |
|  2 | Holyoke              | OVAL             |             7438.64 | no                  |        697203    |
|  3 | Abilene              | DISK             |             7438.64 | no                  |          5384.61 |
|  4 | New York Worlds Fair | LIGHT            |             6615.78 | missing             |          3417.58 |
|  5 | Valley City          | DISK             |             7438.64 | no                  |          4280.1  |
|  6 | Crater Lake          | CIRCLE           |             7377.89 | no                  |        528289    |
|  7 | Alma                 | DISK             |             7438.64 | missing             |          4772.75 |
|  8 | Eklutna              | CIGAR            |             5214.95 | no                  |          4534.03 |
|  9 | Hubbard              | CYLINDER         |             8220.34 | missing             |          4653.72 |

__Some useful code for filling in missing data__
```python
data.column_name.replace(..., ..., inplace=True)
data.column_name.fillna(..., inplace=True)
```

<hr>

### Exercise 3 
Create a table that contains the following summary statistics.
- median estimated size by shape
- mean distance reported by shape
- count of reports belonging to each shape

Your table should look like this:

| shape_reported   |   median_est_size |   mean_distance_reported |   group_count |
|:-----------------|------------------:|-------------------------:|--------------:|
| CIGAR            |           5899.68 |                  6520.21 |             3 |
| CIRCLE           |         266002    |                  7408.26 |             2 |
| CYLINDER         |           4550.58 |                  8039.49 |             2 |
| DISK             |           4581.8  |                  7516.39 |            16 |
| FIREBALL         |           5407.22 |                  7097.78 |             3 |
| FLASH            |           6108.34 |                  7438.64 |             1 |
| FORMATION        |           5104.4  |                  8708.32 |             2 |
| LIGHT            |           3850.25 |                  7636.09 |             2 |
| OTHER            |           4699.4  |                  7473.98 |             4 |
| OVAL             |           4943.63 |                  7787.24 |             4 |
| RECTANGLE        |           3668.1  |                  6054.62 |             2 |
| SPHERE           |           5076.78 |                  7206.55 |             6 |
| TRIANGLE         |           5033.9  |                  8521.9  |             1 |
| missing          |         250153    |                  7438.64 |             2 |

__Some useful code for grouping and getting summary statistics__
```python
(data.groupby(...)
     .agg(...,
          ...,
          ...))
```

<hr>

### Exercise 4 

The cities listed below reported their estimated size in square inches, not square feet. Create a new column named `estimated_size_sqft` in the dataframe, that has all the estimated sizes reported as sqft. (Hint: divide by 144 to go from sqin -> sqft)

- Holyoke
- Crater Lake
- Los Angeles
- San Diego
- Dallas

The head of your data should look like this.

|    | city                 | shape_reported   |   distance_reported | were_you_abducted   |   estimated_size |   estimated_size_sqft |
|---:|:---------------------|:-----------------|--------------------:|:--------------------|-----------------:|----------------------:|
|  0 | Ithaca               | TRIANGLE         |             8521.9  | yes                 |          5033.9  |               5033.9  |
|  1 | Willingboro          | OTHER            |             7438.64 | no                  |          5781.03 |               5781.03 |
|  2 | Holyoke              | OVAL             |             7438.64 | no                  |        697203    |               4841.69 |
|  3 | Abilene              | DISK             |             7438.64 | no                  |          5384.61 |               5384.61 |
|  4 | New York Worlds Fair | LIGHT            |             6615.78 | missing             |          3417.58 |               3417.58 |
|  5 | Valley City          | DISK             |             7438.64 | no                  |          4280.1  |               4280.1  |
|  6 | Crater Lake          | CIRCLE           |             7377.89 | no                  |        528289    |               3668.68 |
|  7 | Alma                 | DISK             |             7438.64 | missing             |          4772.75 |               4772.75 |
|  8 | Eklutna              | CIGAR            |             5214.95 | no                  |          4534.03 |               4534.03 |
|  9 | Hubbard              | CYLINDER         |             8220.34 | missing             |          4653.72 |               4653.72 |

__Some useful code to fix the rows reported in sqin__

```python
np.where(...,  # Condition
         ...,  # If condition is true
         ...)  # If condition is false
```

{{< faq "After you have completed this skill builder with your team (or on your own) then compare your work to our script" >}}

__See the [script](json_missing.py).__

{{</ faq >}}