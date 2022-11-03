---
title: "Day 2: Intro to Machine Learning"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-01T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

<!-----------
Day 2: Training a Classifier
----------->

## Welcome to class!

#### Announcements
#### Spiritual thought

<br>

## Splitting the Data

#### 1. Start with packages and data set

We'll be using some parts of SKLEARN package and the Seaborn package.

```python
from types import GeneratorType
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
```

What is the difference between `dwellings_denver.csv` and `dwellings_ml.csv`?

#### 2. Choose which variables to use

How do we know which variables to use out of `dwellings_ml.csv`?

**Question 1** will help you identify patterns (or lack of patterns) in the data.

#### 3. Separate into features and target

## Which Features?

```python
# %%
h_subset = dwellings_ml.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)

sns.pairplot(h_subset, hue = 'before1980')

corr = h_subset.drop(columns = 'before1980').corr()
# %%
sns.heatmap(corr)
```

#### 4. Split into training and testing sets

### What does the "train_test_split()" function do?

```python
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = #???, random_state = #???)
```

__Read the documentation and tell me what is returned?__

__[Function documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)__   

> Why do we use "test_size" and "random_state"?

> What is "x" and "y"  in the above function example?

We need to take our data and build the feature and target data objects.

> What columns should we remove from our features (X)?   

> What column should we use as our target (y)?


```python
x = dwellings_ml.filter([#what variables will you use as "features"?])
y = dwellings_ml[#what variable is the "target"?]
```

<br>

<br>

## Training a Classifier

#### Decision Tree Example

```python
# create the model
classifier = DecisionTreeClassifier()

# train the model
classifier.fit(x_train, y_train)

# make predictions
y_predictions = classifier.predict(x_test)

# test how accurate predictions are
metrics.accuracy_score(y_test, y_predictions)
```

#### How to Improve Accuracy

To improve the accuracy of your model, you could:

- Change what variables are used in the features (x) data set
- Change what type of model you are using
- Tune (aka, "change" or "tweak") the parameters of the model

#### Other Classification Models

Here are some other models you could try. 

```python
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
```
<br>

<br>

## Make Progress on Project 4

{{< faq "Do the project readings">}}

[**Machine Learning Introduction**](https://byuistats.github.io/CSE250-Larson/course-materials/machine-learning/)

- Step-by-step guide (mostly) for training a GaussianNB classifier. (The steps will be the same for any algorithm you use.) 

[**Visual Introduction to Machine Learning**](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

1. Machine learning identifies patterns using statistical learning and computers by unearthing boundaries in data sets. You can use it to make predictions.
2. One method for making predictions is called a decision trees, which uses a series of if-then statements to identify boundaries and define patterns in the data.
3. Overfitting happens when some boundaries are based on distinctions that don't make a difference. You can see if a model overfits by having test data flow through the model.

{{</ faq >}}


{{< faq "Start working on Question 1">}}

The goal of Grand Question 1 is to help us with "feature selection".

- "Overfitting" happens when some boundaries are based on on _distinctions that don't make a difference_.
- More data does not always lead to better models. ([Occam's Razor](https://www.google.com/search?q=Occam%E2%80%99s+Razor&rlz=1C1GCEJ_enUS882US882&oq=Occam%E2%80%99s+Razor&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8))

Common questions:

- [Why it may be better to have fewer predictors in Machine Learning models?](https://www.kdnuggets.com/2017/04/must-know-fewer-predictors-machine-learning-models.html)
- [What is Feature Selection and why do we need it in Machine Learning?](https://blog.contactsunny.com/data-science/what-is-feature-selection-and-why-do-we-need-it-in-machine-learning)

{{</ faq >}}

{{< faq "What is the 5000 rows error with Altair?">}}

The best way around this is to look at a sub-sample of the data for exploratory purposes.  For example, you can use "sample(500)".  But there are ways to expand VS Code's limits.  

[MaxRowsError: How can I plot Large Datasets?](https://altair-viz.github.io/user_guide/faq.html#maxrowserror-how-can-i-plot-large-datasets)

You may also save data to a local filesystem and reference the data by file path. Altair has a JSON data transformer that will do this transparently when enabled:

```python
alt.data_transformers.enable('json')
```

{{</ faq >}}

{{< faq "scikit-learn resources">}}

- [Home page](https://scikit-learn.org/stable/)
- [Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [Getting Started](https://scikit-learn.org/stable/getting_started.html): _What do you notice about the header portion of each of the script chunks?_
  - [`import` vs `from ... import`](https://scikit-learn.org/stable/getting_started.html)

{{</ faq >}}

<br>







<!------------------------------------------------------------

## Welcome to class!

#### Announcements
#### Spiritual thought

- [Elder Bednar on Rewards and Motivation](https://www.youtube.com/watch?v=mxz5udihf60)

#### Just for fun

{{< faq "My favorite  comic">}}

![](machine_learning.png)

[xkcd](https://xkcd.com/948/)
{{</ faq >}}

<br>

## Searching for patterns

What ideas do you have for charts?

<br>

## Understanding the data

What differences do you notice between these two data sets?

```python
dwellings = pd.read_csv()
dwellings_ml = pd.read_csv()
```
<br>
------------------------------------------------------------------->
<!-------------------------
### Searching For Patterns

{{< faq "What is the 5000 rows error with Altair?">}}

[MaxRowsError: How can I plot Large Datasets?](https://altair-viz.github.io/user_guide/faq.html#maxrowserror-how-can-i-plot-large-datasets)

You may also save data to a local filesystem and reference the data by file path. Altair has a JSON data transformer that will do this transparently when enabled:

```python
alt.data_transformers.enable('json')
```

{{</ faq >}}


{{< faq "What features of homes might have changed a bit over time?">}}

Some ideas:
- square footage
- number of bathrooms
- basement size

**Let's create one chart using some of these variables.**

{{</ faq >}}
----------------------------------------->

<!-----------------------------------------------------------------------------
## Choose a model

{{< faq "What is scikit-learn?">}}

> `Scikit-learn` is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities.

[About scikit-learn](https://scikit-learn.org/stable/about.html) helps us see the history and funding.  It should stay "king of the hill" for a long time.

- Simple and efficient tools for predictive data analysis
- Accessible to everybody, and reusable in various contexts
- Built on NumPy, SciPy, and matplotlib
- Open source, commercially usable - BSD license

{{</ faq >}}

{{< faq "Should I import scikit-learn?">}}

scikit-learn is very large, with many [submodules](https://scikit-learn.org/stable/user_guide.html).  To help the user of your `.py` script understand your code, the consensus is to use `from .... import ....`.

![](falin_from.png)

![](falin_general.png)


```python
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
```

{{</ faq >}}

{{< faq "After choosing a machine learning method, what do we do?">}}

1. Fit (or "train") the model using the features (also called "X")
2. Predict the target (also called "y")
3. Evaluate model performance (using many different metrics)

{{</ faq >}}

<br>

## Train the model

{{< faq "What does the `train_test_split()` function do?">}}

**Your turn:** Read the [documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) and tell me what is returned from the `train_test_split()` function.

**How to save the output:** Use a [destructuring assignment](https://riptutorial.com/python/example/14981/destructuring-assignment)

```python
x_train, x_test, y_train, y_test = train_test_split(
    x, 
    y, 
    test_size = .3, 
    random_state = 76)   
```

**Your turn:**
- Why would we want to use the `test_size` and `random_state` arguments?
- What is `x` and `y`  in the above example?
- Why do we care about splitting our data?

{{</ faq >}}

{{< faq "The next step">}}

We need to take our data and build the feature and target data objects. Think about:
- What column(s) should we remove from our features (x)?   
- What column(s) should we use as our target (y)?


{{</ faq >}}

<br>

## Predicting targets and evaluating model performance

{{< faq "What metrics should we use?">}}

##### Do your reading!

Read [How to evaluate your ML model](https://ranvir.xyz/blog/how-to-evaluate-your-machine-learning-model-like-a-pro-metrics/) and try googling other ideas.

##### Accuracy

Question 2 is looking for a model that has "at least 90% accuracy". 

##### Confusion Matrix

A confusion matrix is a quick way to see the strengths and weaknesses of your model. 

**Your turn:** Look at the confusion matrix for our GaussianNB model. Where the model is doing well and where it might be falling short?

**Your turn:** Now look at the confusion matrix for our Decision Tree model. What differences do you notice?

```python
# a confusion matrix
print(metrics.confusion_matrix(y_test, y_predicted_GNB))

# this one might be easier to read
print(pd.crosstab(y_test.flatten(), y_predicted_GNB, rownames=['True'], colnames=['Predicted'], margins=True))

# visualize a confusion matrix
# requires 'matplotlib' to be installed
metrics.plot_confusion_matrix(classifier_GNB, x_test, y_test)
```

{{</ faq >}}
------------------------------------------------------------------------->










<!---------------------------------


## The big picture

> AI is able to learn 'rules' from highly repetitive data. [Sebastian Thrun](https://www.youtube.com/watch?v=ZJixNvx9BAc)   
> The single most important thing for AI to accomplish in the next ten years is to free us from the burden of repetitive work. [Sebastian Thrun](https://www.youtube.com/watch?v=ZJixNvx9BAc)   

<iframe width="560" height="315" src="https://www.youtube.com/embed/asmXyJaXBC8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/XZDLbbfT9_Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### [Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

> 1. Machine learning identifies patterns using statistical learning and computers by unearthing boundaries in data sets. You can use it to make predictions.
> 2. One method for making predictions is called a decision trees, which uses a series of if-then statements to identify boundaries and define patterns in the data.
> 3. Overfitting happens when some boundaries are based on distinctions that don't make a difference. You can see if a model overfits by having test data flow through the model.

#### [Bias-Variance Tradeoff](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/)

> 1. Models approximate real-life situations using limited data.
> 2. In doing so, errors can arise due to assumptions that are overly simple (bias) or overly complex (variance).
> 3. Building models is about making sure there's a balance between the two.

#### But what is the 'Pavlovian bell' in the machine learning model?

![](../../images/ml/test.png)

Some mathematical penalty/reward equation.

> - __[Regression](https://setosa.io/ev/ordinary-least-squares-regression/)__
> - __[Variance, RMSE, SD](../../interactive/threshold_histogram.html)__
> - __proportions__

## Using our project data to understand features, targets, and samples.

> 1. Import `dwellings_ml.csv` and write a short sentence describing your data. Remember to explain an observation and what measurements we have on that observation.
> 2. Now try describing the modeling (machine learning) we are going to do in terms of features and targets.
>    A. Are there any columns that are the target in disguise?
>    B. _Are the observational units unique in every row?_

![](../../images/ml/iris_description.png)

### If your model is near perfect in its predictability, you might be cheating.

### Watch out for [transactional data](http://localhost:1313/CSE250-Course/images/ml/iris_description.png)!

> - Financial: orders, invoices, payments
> - Work: plans, activity records
> - School: Grades

### [scikit learn](https://scikit-learn.org/stable/)

> - [Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
> - [Getting Started](https://scikit-learn.org/stable/getting_started.html): _What do you notice about the header portion of each of the script chunks?_
>    - [`import` vs `from ... import`](https://scikit-learn.org/stable/getting_started.html)


## Setting up Live Share

----------------------------------->

<br>
