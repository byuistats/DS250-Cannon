---
title: "Project 5: The war with Star Wars (4 days)"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

### Background


Survey data is notoriously difficult to handle.  Even when the data is recorded cleanly the options for ‘write in questions’, ‘choose from multiple answers’, ‘pick all that are right’, and ‘multiple choice questions’ makes storing the data in a tidy format difficult.

In 2014, FiveThirtyEight surveyed over 1000 people to write the article titled, [America’s Favorite ‘Star Wars’ Movies (And Least Favorite Characters)](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/). They have provided the data on GitHub - &lt;[https://github.com/fivethirtyeight/data/tree/master/star-wars-survey](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey)>. 

A company would like to use this data to figure out if they can predict an interviewing job candidate's current income based on a few responses about Star Wars movies.  

### Data:

__Download:__ [StarWars.csv](https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv)   
__Information:__ [Article](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/)


### Readings:

* [Python for Data Science: Tidy Data](https://byuidatascience.github.io/python4ds/tidy-data.html)
* [Python for Data Science: Graphics for Communication](https://byuidatascience.github.io/python4ds/graphics-for-communication.html)
* [Python for Data Science: Strings](https://byuidatascience.github.io/python4ds/strings.html)

### Grand Questions:

1. __Shorten the column names and clean them up for easier use with pandas.__
2. __Filter the dataset to those that have seen at least one film.__
3. __Please validate that the data provided on GitHub lines up with the article by recreating 2 of their visuals and calculating 2 summaries that they report in the article.__
4. __Clean and format the data so that it can be used in a machine learning model. Please achieve the following requests and provide examples of the table with a short description the changes made in your report.__
   <ol type="a">
      <li><b>Create an additional column that converts the age ranges to a number and drop the age range categorical column.</b></li>
      <li><b>Create an additional column that converts the school groupings to a number and drop the school categorical column.</b></li>
      <li><b>Create an additional column that converts the income ranges to a number and drop the income range categorical column.</b></li>
      <li><b>Create your target (also known as label) column based on the new income range column.</b></li>
      <li> <b>One-hot encode all remaining categorical columns.</b> </li>
      

   </ol>   
5. __Build a machine learning model that predicts whether a person makes more than $50k.__


### Deliverables:

_Use this [template](../../template/cse250_project_template_clean.md) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/cse250_project_template.md)):_

1. _A 30 second elevator pitch as if you were in a job interview that describes the tools you used in this project._
1. _An “elevator pitch” that summarizes the entire case study._
1. _Answers to the grand questions that include text, pictures, and tables._
1. _An appendix that provides your commented code and justification for any programming that required you to choose an option._