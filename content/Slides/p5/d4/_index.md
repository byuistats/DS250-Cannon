---
title: "Day 4: May the ML columns be with you"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 1
draft: False
# search related keywords
keywords: [""]
---

## Welcome to class!

#### Spiritual Thought

#### Announcements

<br>

## Getting the data ready for machine learning.

<br>

### What are machine learning algorithms expecting to see?

> We need to handle missing values and categorical features before feeding the data into a machine learning algorithm, because the mathematics underlying most machine learning models assumes that the data is numerical and contains no missing values. To reinforce this requirement, scikit-learn will return an error if you try to train a model using data that contain missing values or non-numeric values when working with models like linear regression and logistic regression. [ref](https://www.dataquest.io/blog/machine-learning-preparing-data/)

We have some options when converting categorical features (columns) to numeric.

- If the **category contains numeric information** (like a range of numbers) we can convert it to a  numeric variable by taking the minimum, average, or maximum of the range.
- **Factorization:** If the category is an **"ordinal"** variable (meaning, [there is an order to the categories](https://www.questionpro.com/blog/nominal-ordinal-interval-ratio/#:~:text=Nominal%20scale%20is%20a%20naming,each%20of%20its%20variable%20options.)) we can assign each category to an integer. (For example, good = 1, better = 2, best = 3.) 
- **One-hot Encoding or Dummy Variables:** If the category is a **"nominal"** variable (without an order) then we need to use one-hot encoding (sometimes called "[dummy variable encoding](https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/)").
- If the **category is some version of True/False or Yes/No** then we can simply convert the values to zeros and ones.

<br>

# What's our game plan for the Star Wars columns?

### Break into Groups

#### Strategize + Code + Share

- Group 1:  How are you going to turn Age, Income and Education into numbers?
- Group 2:  How are you going to encode 
    - Who Shot First
    - Gender
    - Location
    - All the Yes/No responses
- Group 3:  How are you going to deal with the character rankings?  

#### Combine all the factors into one big X dataframe
#### Define Y as those making > $50k

**First:** Limit the data to only people who answered "Yes" to the question "Have you seen any of the 6 films in the Star Wars franchise?".

**Then:** Use the table below as a guide to prepare your data for machine learning.

| Column            | Original Format                    | Convert To |
|-------------------|------------------------------------|------------|
| age               | category (ordinal, age ranges)     | number     |
| income            | category (ordinal, income ranges)  | number     |
| education         | category (ordinal, name of degree) | number     |
| shot_first        | category (nominal)                 | one-hot    |
| gender            | category (nominal)                 | one-hot    |
| location          | category (nominal)                 | one-hot    |
| fan_star_wars     | Yes/No                             | 0/1        |
| expanded_universe | Yes/No                             | 0/1        |
| fan_exapanded     | Yes/No                             | 0/1        |
| fan_star_trek     | Yes/No                             | 0/1        |
| seen_i            | Yes/No (name of movie/NaN)         | 0/1        |
| seen_ii           | Yes/No (name of movie/NaN)         | 0/1        |
| seen_iii          | Yes/No (name of movie/NaN)         | 0/1        |
| seen_iv           | Yes/No (name of movie/NaN)         | 0/1        |
| seen_v            | Yes/No (name of movie/NaN)         | 0/1        |
| seen_vi           | Yes/No (name of movie/NaN)         | 0/1        |
| movie rankings    | number                             | -          |
| character rankings| category (ordinal)                 | one-hot or factorize |

<br>

### What functions can we use to convert the categorical columns to numeric?

- Range of numbers: [str.split()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html) and [astype()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html)
- Ordinal: [str.replace()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
- Ordinal: [pd.factorize()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html) (can also be used for True/False)
- Nominal: [pd.get_dummies()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html)

{{< faq "Using the `drop_first = True` option in `get_dummies()`">}}

Question: When and why would we drop the first column when we convert a category using `pd.get_dummies()`?

Answer: Whenever your algorithm needs to calculate a matrix inverse.

> The one-hot encoding creates one binary variable for each category.
>
> <br>
>
> The problem is that this representation includes redundancy. For example, if we know that [1, 0, 0] represents "blue" and [0, 1, 0] represents "green" we don't need another binary variable to represent "red", instead we could use 0 values for both "blue" and "green" alone, e.g. [0, 0].
>
> <br>
>
> This is called a dummy variable encoding, and always represents C categories with C-1 binary variables. In addition to being slightly less redundant, a dummy variable representation is required for some models.
>
> <br>
>
> For example, in the case of a linear regression model (and other regression models that have a bias term), a one hot encoding will case the matrix of input data to become singular, meaning it cannot be inverted and the linear regression coefficients cannot be calculated using linear algebra. For these types of models a dummy variable encoding must be used instead.

[Source](https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/)

{{</ faq >}}

<br>

<!--------------------------------------------
### Let's get started!

Begin by filtering the data.

```python
dat = starwars_data.query('have_seen_any == "Yes"')
dat.shape
```
And then convert the age, income, and education categories into numbers.

```python
# Create a column that converts the income ranges to a number.
(dat.age
    .str.split("-", expand = True)
    .rename(columns = {0: 'age_min', 1: 'age_max'})
    .apply(lambda x: x.str.replace("> ", ""))
    .astype('float')
    .age_min)
```
You can combine the different features (columns) together using [pd.concat()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html).

```python
dat_numeric = pd.concat([
    (dat.age
        .str.split("-", expand = True)
        .rename(columns = {0: 'age_min', 1: 'age_max'})
        .apply(lambda x: x.str.replace("> ", ""))
        .astype('float').age_min),
    (dat.household_income
        .str.split("-", expand = True)
        .rename(columns = {0: 'income_min', 1: 'income_max'})
        .apply(lambda x: x.str.replace("\$|,|\+", ""))
        .astype('float').income_min),
    (dat.education
        .str.replace('Less than high school degree', '9')
        .str.replace('High school degree', '12')
        .str.replace('Some college or Associate degree', '14')
        .str.replace('Bachelor degree', '16')
        .str.replace('Graduate degree', '20')
        .astype('float'))], 
    axis = 1
)
```
Use `pd.get_dummies()` or other functions from these slides to finish preparing the columns for machine learning. Below is one example witih `pd.get_dummies()`. What difference does the `drop_first` option make?

```python
dat_onehot = pd.get_dummies(dat.filter(['shot_first']))

dat_onehot = pd.get_dummies(dat.filter(['shot_first']), drop_first = True)
```

When you're done, you can use `pd.concat()` again to combine all your features.

```python
dat_ml = pd.concat([
    # all of the movie rankings (already numbers, no conversion needed),
    # age, income, and education variables
    # all the "one-hot" encoded variables
    # all the 0/1 encoded variables
    ], axis = 1).dropna()
```

<br>
----------------------------------------->

## Predicting income.

**Grand Question 4** wants us to "build a machine learning model that predicts whether a person makes more than $50k".

{{< faq "What is the target we're interested in?">}}

Aka, what is our "outcome" or "response" that we want to predict?

```python
dat_ml.income > 50000
```

{{</ faq >}}

{{< faq "How to format the features (x) and target (y)">}}

Remember not to include the answer (income) in your features!

```python
x = dat_ml.drop(['income'], axis = 1)
```
The response needs to be saved as a 0/1 variable (at least, for binary classification algorithms).

```python
y = (dat_ml.income > 50000) / 1
```

{{</ faq >}}

<!-------------------------------------------------
{{< faq "One example of a model">}}

First we need to build and train the model.

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

# split the data (x) and response (y) into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .33, random_state = 2020)  

# build and train the model
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=5)
decision_tree = decision_tree.fit(x_train, y_train)

# what does the decision tree look like?
r = export_text(decision_tree, feature_names=x_train.columns.to_list())
print(r)
```

Then we can test it to see how well it does.

```python
from sklearn import metrics

# make predictions with the test data
predict_y = decision_tree.predict(x_test)

# how well did our model do?
metrics.plot_confusion_matrix(decision_tree, x_test, y_test)
print(metrics.accuracy_score(y_test, predict_y))
```
{{</ faq >}}
----------------------------------------------->

<br>
