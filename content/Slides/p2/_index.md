---
title: "Week 4-5: Project 2 - Flights"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 6
draft: false
# search related keywords
keywords: [""]
---

<!-------------------------------------

{{% notice info %}}
  JSON files are the format of choice for sharing information and data between apps on the internet. When you hear someone explain that you can use an API to get the data, there is usually a JSON file involved. The history of [JSON](https://blog.sqlizer.io/posts/json-history/) is worth reading.  We will have another project analyzing data from JSON files that are missing values. [Are we missing JSON on our flight?](../../projects/project-3/)
{{% /notice %}}


{{% notice note %}}

**Completed Readings:** [P4DS: Chapter 5 Data tranformation](https://byuidatascience.github.io/python4ds/transform.html), [P4DS: Section 7.4 Missing Values](https://byuidatascience.github.io/python4ds/exploratory-data-analysis.html#missing-values-2), [Python Data Science Handbook: Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html), [How to Handle Missing Data](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4), and [Wikipedia Missing Data](https://en.wikipedia.org/wiki/Missing_data)


{{% /notice %}}

{{% notice tip %}}
The flights [JSON File](https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json)   
 and the [Data Description](https://github.com/byuidatascience/data4missing/blob/master/data.md) 
{{% /notice %}}

### Grand Questions

> 1. __Which airport has the worst delays? How did you choose to define "worst"? As part of your answer include a table that lists the total number of flights, total number of delayed flights, proportion of delayed flights, and average delay time in hours, for each airport.__
>
> 2. __What is the worst month to fly if you want to avoid delays? Include one chart to help support your answer, with the x-axis ordered by month. You also need to explain and justify how you chose to handle the missing `Month` data.__
>
> 3. __According to the BTS website the Weather category only accounts for severe weather delays. Other “mild” weather delays are included as part of the NAS category and the Late-Arriving Aircraft category. Calculate the total number of flights delayed by weather (either severe or mild) using these two rules:__
>
>    1. __30% of all delayed flights in the Late-Arriving category are due to weather.__
>    2. __From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.__
>
> 4. __Create a barplot showing the proportion of all flights that are delayed by weather at each airport. What do you learn from this graph (Careful to handle the missing `Late Aircraft` data correctly)?__
>
> 5. __Fix all of the varied `NA` types in the data and save the file back out in the same format that was provided. Provide one example from the file with the new `NA` values shown.__

--------------------------------------------------->