---
title: "Project 5: The war with Star Wars"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 5
draft: false
# search related keywords
keywords: [""]
---

### Background


Survey data is notoriously difficult to munge.  Even when the data is recorded cleanly the options for ‘write in questions’, ‘choose from multiple answers’, ‘pick all that are right’, and ‘multiple choice questions’ makes storing the data in a tidy format difficult.

In 2014, FiveThirtyEight surveyed over 1000 people to write the article titled, [America’s Favorite ‘Star Wars’ Movies (And Least Favorite Characters)](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/). They have provided the data on [GitHub](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey). 

For this project, your client would like to use the Star Wars survey data to figure out if they can predict an interviewing job candidate’s current income based on a few responses about Star Wars movies.  

### Data

__Download:__ [StarWars.csv](https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv)   
__Information:__ [Article](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/)


### Readings

* [Python for Data Science: Tidy Data](https://byuidatascience.github.io/python4ds/tidy-data.html)
* [Python for Data Science: Graphics for Communication](https://byuidatascience.github.io/python4ds/graphics-for-communication.html)
* [Python for Data Science: Strings](https://byuidatascience.github.io/python4ds/strings.html)

### Questions and Tasks

1. __Shorten the column names and clean them up for easier use with pandas. Provide a table or list that exemplifies how you fixed the names.__
2. __Clean and format the data so that it can be used in a machine learning model. As you format the data, you should complete each item listed below. In your final report provide example(s) of the reformatted data with a short description of the changes made.__
    <ol type="a">
        <li><b>Filter the dataset to respondents that have seen at least one film.</b></li>
        <li><b>Create a new column that converts the age ranges to a single number. Drop the age range categorical column.</b></li>
        <li><b>Create a new column that converts the education groupings to a single number. Drop the school categorical column</b></li>
        <li><b>Create a new column that converts the income ranges to a single number. Drop the income range categorical column.</b></li>
        <li><b>Create your target (also known as “y” or “label”) column based on the new income range column.</b></li>
        <li><b>One-hot encode all remaining categorical columns.</b></li>
    </ol>
3. __Validate that the data provided on GitHub lines up with the article by recreating 2 of the visuals from the article.__
5. __Build a machine learning model that predicts whether a person makes more than $50k. Describe your model and report the accuracy.__


### Deliverables

_Use this [template](../../template/ds250_project_template_clean.qmd) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/ds250_project_template.qmd)):_

1. _A short summary that highlights key that describes the results describing insights from  metrics  of the project and the tools you used (Think “elevator pitch”)._
2. _Answers to the questions from the "Questions and Tasks" section above. Each answer should include a written description of your results, code snippets, charts, and tables._
