---
title: "Project 4: Can you predict that? (4 days)"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

### Background

The clean air act of 1970 was the beginning of the end for the use of asbestos in home building.  By 1976, the U.S. Environmental Protection Agency (EPA) was given authority to restrict the use of asbestos in paint. Homes built during and before this period are known to have materials with asbestos <https://www.asbestos.com/mesothelioma-lawyer/legislation/ban/>.  

The state of Colorado has a large portion of their residential dwelling data that is missing the year built and they would like you to build a predictive model that can __classify__ if a house is built pre 1980.  They would also like you to build a model that __predicts__ (regression) the actual age of each home.

Colorado gave you home sales data for the city of Denver from 2013 on which to train your model. They said all the column names should be descriptive enough for your modeling and that they would like you to use the latest machine learning methods.

### Data:

__Download:__ [dwellings_denver.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv), [dwellings_ml.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv), [dwellings_neighborhoods_ml.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv)   
__Information:__ [Data description](https://github.com/byuidatascience/data4dwellings/blob/master/data.md)


### Readings:

- [Machine Learning Introduction](../../course-materials/machine-learning/)
- [A visual introduction to machine learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
- [How to choose a good evaluation metric for your Machine learning model](https://ranvir.xyz/blog/how-to-evaluate-your-machine-learning-model-like-a-pro-metrics/)  

#### Optional References

- [Decision Tree Classification in Python](https://www.datacamp.com/community/tutorials/decision-tree-classification-python)    
- [Boosted algorithms in scikit-learn](https://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting)
- [scikit-plot package](https://github.com/reiinakano/scikit-plot)   

### Grand Questions:

1. __Create 2-3 charts that evaluate potential relationships between the home variables and `before1980`.__
1. __Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state of Colorado to use (explain your model choice and which models you tried)?__
1. __Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?__
1. __Can you describe the quality of your classification model using 2-3 evaluation metrics? You need to provide an interpretation of each evaluation metric when you provide the value.__

### Deliverables:

_Use this [template](../../template/cse250_project_template_clean.md) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/cse250_project_template.md)):_

1. _An “elevator pitch” that summarizes the entire case study._
1. _Answers to the grand questions that include text, pictures, and tables._
1. _An appendix that provides your commented code and justification for any programming that required you to choose an option._