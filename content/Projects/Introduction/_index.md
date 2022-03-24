---
title: "Project: Introduction (2 days)"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---

### Background

{{% notice note %}}
We will complete six projects during the class that each take about four days of class.  The average student will take 2 hours per class for a total of 8 hours each project to complete the readings, submit any Canvas items, and complete the project. Each project will be structured into sections like this page. 
This section will provide some context to the project. Make sure you read the background carefully to see the big picture needs and purpose of the project.
{{% /notice %}}


During our first two days of class we need to get VS Code prepped for data science programming.  

### Data:

{{% notice note %}}
Every data science project should start with data.  We will keep to this model for our six projects. Each project will have links after the two items below.
{{% /notice %}}

__Download:__ [mpg data](https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv)   
__Information:__ [Data description](https://github.com/byuidatascience/data4python4ds/blob/master/data.md#fuel-economy-data-from-1999-to-2008-for-38-popular-models-of-cars)

### Readings:

{{% notice note %}}
This section will have links to the readings that you will need to complete the projects. Remember that we are reading this material to build skills. Reading to read will waste your time.  Take the time to comprehend the readings and the skills contained within.  We recommend that you read through the readings for a general understanding once before the first day of that project's class.  You will reread and reference the readings multiple times as you complete the projects. Those readings that are meant for a reference during the project are included under __Optional References__. You will see bulleted links to the required readings.
{{% /notice %}}


The readings listed below are required for the first two days of class.

- [Python for Data Science (P4DS): Introduction](https://byuidatascience.github.io/python4ds/introduction.html)
- [P4DS: Data Visualization Section 3.1 & 3.2 Only](https://byuidatascience.github.io/python4ds/data-visualisation.html)
- [Saving Altair charts](../../course-materials/altair/)
- [Markdown for DS](../../course-materials/markdown/)

#### Optional References

- [VS Code user interface](https://code.visualstudio.com/docs/getstarted/userinterface) 
- [Reading Technical Documentation](https://byui-cse.github.io/cse450-course/course/reading-technical-documentation.html)

### Grand Questions:

{{% notice note %}}
This section will have the project deliverables listed. These are the primary items that need to be completed for the project. You will need to submit your projects in Canvas by the weekend following the last class day for that project.  
{{% /notice %}}

1. __Finish the readings and come to class prepared with any questions to get your environment working smoothly.__
2. __Create a python script and use VS Code to create the example Altair chart in the assigned readings (note that you have to type `chart` to see the Altair chart after you run the code).  Save your Altair chart for submission.__
3. __Include the Markdown table created from the following code in your report (assuming you have `mpg` from question 2).__

```python
print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))
```

### Deliverables:

{{% notice note %}}
This section will be the same for all six projects. After this submission, you will be expected to submit a report using markdown within VSCode. Make sure you have your image ready. We will finalize the introduction project submission the class period following the due date. 
{{% /notice %}}

_Use this [template](../../template/cse250_project_template_clean.md) to submit your Client Report. The template has three sections (for additional details please see the [instructional template](../../template/cse250_project_template.md)):_

1. _An “elevator pitch” that summarizes the entire project._
2. _Answers to the grand questions that include text, pictures, and tables._
3. _An appendix that provides your commented code and justification for any programming that required you to choose an option._

<!-- 
{{% notice note %}}
  This is a simple note.
{{% /notice %}}

{{% notice tip %}}
  This is a simple tip.
{{% /notice %}}

{{% notice info %}}
  This is a simple info.
{{% /notice %}} -->