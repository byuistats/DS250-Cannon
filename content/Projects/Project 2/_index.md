---
title: "Project 2: Late flights and missing data (JSON files)"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---


### Background

Delayed flights are not something most people look forward to. In the best case scenario you may only wait a few extra minutes for the plane to be cleaned. However, those few minutes can stretch into hours if a mechanical issue is discovered or a storm develops. Arriving hours late may result in you missing a connecting flight, job interview, or your best friend’s wedding.

In 2003 the Bureau of Transportation Statistics (BTS) began collecting data on the causes of delayed flights. The categories they use are Air Carrier, National Aviation System, Weather, Late-Arriving Aircraft, and Security. You can visit the [BTS website](https://www.bts.gov/topics/airlines-and-airports/understanding-reporting-causes-flight-delays-and-cancellations) to read definitions of these categories.

The JSON file for this project contains information on delays at 7 airports over 10 years. Your task is to clean the data, search for insights about flight delays, and communicate your results using the provided template. If you have completed the checkpoints for Unit 5, then you are ready to answer the Grand Questions listed below. Refer to the readings for additional help.


### Data

__Download:__ [JSON File](https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json)   
__Information:__ [Data Description](https://github.com/byuidatascience/data4missing/blob/master/data.md)

### Readings

- [P4DS: Section 12.1 & 12.2 Tidy data](https://byuidatascience.github.io/python4ds/tidy-data.html#tidy-data-1)
- [P4DS: Chapter 5 Data transformation](https://byuidatascience.github.io/python4ds/transform.html)
- [P4DS: Section 7.4 Missing Values](https://byuidatascience.github.io/python4ds/exploratory-data-analysis.html#missing-values-2)
- [Python Data Science Handbook: Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html)
- [Wikipedia Missing Data](https://en.wikipedia.org/wiki/Missing_data)

#### Optional References

- [isin method](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin)
- [where method](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-where-method-and-masking)
- [np.where method](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- [replace method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)
- [An introduction to JSON](https://towardsdatascience.com/an-introduction-to-json-c9acb464f43e) _(May need to open in ingognito to read.)_
- [The key word in 'Data Science' is not Data...](https://simplystatistics.org/posts/2013-12-12-the-key-word-in-data-science-is-not-data-it-is-science/)
- [How to Handle Missing Data](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4) _(May need to open in ingognito to read.)_

### Questions and Tasks

1. __Which airport has the worst delays?__ Discuss the metric you chose, and why you chose it to determine the “worst” airport. Your answer should include a summary table that lists (for each airport) the total number of flights, total number of delayed flights, proportion of delayed flights, and average delay time in hours.

2. __What is the best month to fly if you want to avoid delays of any length?__ Discuss the metric you chose and why you chose it to calculate your answer. Include one chart to help support your answer, with the x-axis ordered by month. (To answer this question, you will need to remove any rows that are missing the `Month` variable.)

3. According to the BTS website, the “Weather” category only accounts for severe weather delays. Mild weather delays are not counted in the “Weather” category, but are actually included in both the “NAS” and “Late-Arriving Aircraft” categories. __Your job is to create a new column that calculates the total number of flights delayed by weather (both severe and mild).__ You will need to replace all the missing values in the Late Aircraft variable with the mean. Show your work by printing the first 5 rows of data in a table. Use these three rules for your calculations:__

    <ol type="a">
        <li> <b>100% of delayed flights in the Weather category are due to weather</b></li>
        <li> <b>30% of all delayed flights in the Late-Arriving category are due to weather.</b></li>
        <li><b>From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.</b></li>
    </ol>   

4. __Using the new weather variable calculated above, create a barplot showing the proportion of all flights that are delayed by weather at each airport. Discuss what you learn from this graph.__

5. __Fix all of the varied missing data types in the data to be consistent (all missing values should be displayed as “NaN”).__ In your report include one record example (one row) from your new data, in the raw JSON format. Your example should display the "NaN" for at least one missing value.__

### Deliverables

_Use this [template](../../template/ds250_project_template_clean.qmd) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/ds250_project_template.qmd)):_

1. _A short summary that highlights key that describes the results describing insights from  metrics  of the project and the tools you used (Think “elevator pitch”)._
2. _Answers to the grand questions. Each answer should include a written description of your results, code snippets, charts, and tables._

