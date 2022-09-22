---
title: "Project 4: Can you predict that?"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

### Background

The clean air act of 1970 was the beginning of the end for the use of asbestos in home building.  By 1976, the U.S. Environmental Protection Agency (EPA) was given authority to restrict the use of asbestos in paint. Homes built during and before this period are known to have materials with asbestos YOu can [read more about this ban](https://www.asbestos.com/mesothelioma-lawyer/legislation/ban/).  

The state of Colorado has a large portion of their residential dwelling data that is missing the year built and they would like you to build a predictive model that can __classify__ if a house is built pre 1980.  

Colorado gave you home sales data for the city of Denver from 2013 on which to train your model. They said all the column names should be descriptive enough for your modeling and that they would like you to use the latest machine learning methods.

### Data

__Download:__ [dwellings_denver.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv), [dwellings_ml.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv), [dwellings_neighborhoods_ml.csv](https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv)   
__Information:__ [Data description](https://github.com/byuidatascience/data4dwellings/blob/master/data.md)


### Readings

- [Machine Learning Introduction](../../course-materials/machine-learning/)
- [A visual introduction to machine learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
- [How to choose a good evaluation metric for your Machine learning model](https://ranvir.xyz/blog/how-to-evaluate-your-machine-learning-model-like-a-pro-metrics/)  

#### Optional References

- [Decision Tree Classification in Python](https://www.datacamp.com/community/tutorials/decision-tree-classification-python)    
- [Boosted algorithms in scikit-learn](https://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting)
- [scikit-plot package](https://github.com/reiinakano/scikit-plot)   

### Grand Questions

1. __Create 2-3 charts that evaluate potential relationships between the home variables and `before1980`.__ Explain what you learn from the charts that could help a machine learning algorithm.
1. __Build a classification model labeling houses as being built “before 1980” or “during or after 1980”. Your goal is to reach or exceed 90% accuracy. Explain your final model choice (algorithm, tuning parameters, etc) and describe what other models you tried.__
1. __Justify your classification model by discussing the most important features selected by your model. This discussion should include a chart and a description of the features.__
1. __Describe the quality of your classification model using 2-3 different evaluation metrics. You also need to explain how to interpret each of the evaluation metrics you use.__

### Deliverables

_Use this [template](https://byuistats.github.io/DS250-Course/template/ds250_project_template_clean.qmd) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](https://byuistats.github.io/DS250-Course/template/ds250_project_template.qmd)):_

1. _A short summary that highlights key that describes the results describing insights from  metrics  of the project and the tools you used (Think “elevator pitch”)._
2. _Answers to the questions from the "Questions and Tasks" section above. Each answer should include a written description of your results, code snippets, charts, and tables._
