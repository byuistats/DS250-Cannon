---
title: "Python for Data Science"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

[Python for Data Science](https://byuidatascience.github.io/python4ds/) is a port of [R for Data Science](https://r4ds.had.co.nz/index.html) into Python. We are keeping Garrett Grolemund and Hadley Wickham’s writing and examples as much as possible while demonstrating Python instead of R. We have focused on [pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) and [Altair](https://altair-viz.github.io/) in our Python code snippets.

This book will teach you how to do data science with Python: You’ll learn how to get your data into Python, get it into the most useful structure, transform it, visualise it and model it. In this book, you will find a practicum of skills for data science. Just as a chemist learns how to clean test tubes and stock a lab, you’ll learn how to clean data and draw plots—and many other things besides. These are the skills that allow data science to happen, and here you will find the best practices for doing each of these things with Python. You’ll learn how to use the grammar of graphics, literate programming, and reproducible research to save time. You’ll also learn how to manage cognitive resources to facilitate discoveries when wrangling, visualising, and exploring data.

### Installing and Importing Packages

We want to install the following three packages;

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/install.html#installation-instructions). The Apple Silicon is still more difficult to get installed.  You can use the following links to get it installed - [Link 1](https://scikit-learn.org/stable/install.html#installing-on-apple-silicon-m1-hardware), [Link 2](https://github.com/scikit-learn/scikit-learn/issues/19137), [Link 3](https://github.com/conda-forge/miniforge).

We can get packages installed for this course using one of the two methods below.
#### Using your terminal

```python
# default way
pip install numpy pandas scikit-learn
```

If you are using a Mac

```python
# Mac method with Python 2 and 3 installed
pip3 install numpy pandas scikit-learn
```

#### Using your interactive Python (Jupyter server)

```python
import sys
!{sys.executable} -m pip install numpy pandas scikit-learn
```

{{< youtube UnkLhsI3ycg >}}