---
title: "Day 3: Missing Data"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
draft: true
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Gratitude Journal

#### Announcements

<br>

## Questions 1 and 2

What issues are we still running into?

<br>

## How to work with missing data

#### What counts as missing data?
<!---------------- 
Check the reading assignments, or try this article: [The Weird World of Missing Values in Pandas: NaN, NaT, None](https://dev.to/discdiver/the-weird-world-of-missing-values-in-pandas-3kph)   

Pandas has an experimental [pd.NA](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#experimental-na-scalar-to-denote-missing-values) 
-------------------->

<br>

#### How to identify missing data

<!----- You can use these methods to identify missing values or strange values in your data set:---->
- `df.isnull().sum()`
- `df.describe()`
- `df.column.value_counts(dropna=False)`
<!---- You can also look for patterns within the missing values: ------->
- `pd.crosstab()`   


<br>

#### Option 1: Remove missing values

Be careful with `.dropna()`, and make sure you know what it is doing to your data!

Let's use the [pandas example](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html):


```python
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
```

{{< faq "Q: When would we ever use `dropna()`?">}}
A: Almost never! Why do you think it is a bad idea? `df.dropna()`
{{</ faq >}}

{{< faq "Q: What argument do we use to drop rows where all values are `NA`?">}}
A: `df.dropna(how='all')` [reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
{{</ faq >}}

{{< faq "Q: What if we want to drop `NA` rows based on one column?">}}
A: `df.dropna(subset=['toy'])` [reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
{{</ faq >}}

<br>

#### Option 2: Replacing missing values

Again, let's use the [pandas example](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html):

```python
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
```

{{< faq "Q: What if we want to replace all the `NA` in the `wt` column with the mean weight?">}}
A: `fillna()` [reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)
{{</ faq >}}

{{< faq "Q: What if we want to replace all the `999` with a 4?">}}
A: `replace()` [reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)
{{</ faq >}}

{{< faq "Q: What if we want to replace all the `NAs` with a linear interpolation?">}}
A: `interpolate()` [reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html)
{{</ faq >}}

<br>

## Question 3

#### What columns do we need to use for question 3 (total number of flights delayed by weather)?

- `num_of_delays_weather`
- `num_of_delays_late_aircraft`
- `num_of_delays_nas`

```python
weather = flights.assign(
    severe = #????,
    mild_late = #????,
    mild_nas = np.where(#????),
    total_weather = # add up severe and mild,
).filter(['airport_code','month','severe','mild_late','mild_nas',
    'total_weather', 'num_of_delays_total'])
```

#### Other resources for question 3

- [isin() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin)
- [where() method](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- [Adding new variables with assign()](https://byuidatascience.github.io/python4ds/transform.html#add-new-variables-with-.assign)
- [assign() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html)

<!-------------------------------------
<br>

## Your Turn: Filling in the cars data

Suppose that the missing car names should be the value preceding it in the table. __Write the code to do the replacement using functions mentioned above.__

<br>
--------------------------------->

<br>
