---
title: "Day 3: Making your name stand out"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-22T10:42:26+06:00
weight: 2
draft: true
# search related keywords
keywords: [""]
---

## Welcome to class!

<br>

## Reminder about resources

- Download Slack
- "Potluck" prep assignment
- Make your own cheat sheet
- Project 0 Summary

<br>

## Let's practice!

#### Goal: With your neighbor, make a chart that compares the popularity of your two names over time.

**What do you want the chart to look like?**

```python
alt.Chart()
   .mark_*()
   .encode()
```

<br>

**What data do you need to make that chart?**

```python
# names[] vs. names.query()
```


<br>

{{< faq "Work with your partner to create a line chart that includes both of your names?">}}

> - Can you include total and data for the state in which you were born?
> - Work together to make the code as eloquent as possible.
> - [compound charts](https://altair-viz.github.io/user_guide/compound_charts.html)

{{</ faq >}}


<br>

**What can you add to your chart to help tell a story?**

Remember this advice [from Edward Tufte](https://medium.com/@AnyChart/advices-by-edward-tufte-importance-of-context-for-charts-819396300255).

> To be truthful and revealing, data graphics must bear on the question at the heart of quantitative thinking: "Compared to what?" The emaciated, data-thin design should always provoke suspicion, for graphics often lie by omission, leaving out data sufficient for comparisons.


<!--------------------
{{< faq "What are some charts types we could use to answer this question?">}}

__There is a clear first choice, but I think there are a few other choices that could provide insight.__

> - [Visualization Catalog](https://datavizcatalogue.com/)
> - [Altair Example Gallery](https://altair-viz.github.io/gallery/index.html)

<iframe src="http://ipadstopwatch.com/timer-fullscreen.html" frameborder="0" scrolling="no" width="425" height="340"></iframe>


{{</ faq >}}


{{< faq "Use the `query()` method and `filter()` method to get your name and years in the rows with and include the `name`, `year`, and `Total` columns">}}

1. filter the data down to your names (`query`)
2. select the pertinent columns (`filter()`)
3. Create a new data object for your name. 

{{</ faq >}}

{{< faq "Create a line chart with your name.">}}

```python
base = (alt.Chart()
    .encode(
        x = alt.X(''),
        y = alt.Y('')
    )
    .mark_line()
)
```

{{</ faq >}}


{{< faq "Create a new DataFrame with your birthday information in the row">}}

Create a `DataFrame` with `x`, `y`, and `label` as columns. [How to create a dataframe.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

{{</ faq >}}


{{< faq "Add the vertical rule mark to show your birthday">}}

These references can help:

- [Using layered charts](https://altair-viz.github.io/user_guide/compound_charts.html)
- [Altair Marks](https://altair-viz.github.io/user_guide/marks.html)
- [Add a horizontal line to an existent chart](https://github.com/altair-viz/altair/issues/2059)

{{</ faq >}}


{{< faq "Work with your partner to create a line chart that includes both of your names?">}}

> - Can you include total and data for the state in which you were born?
> - Work together to make the code as eloquent as possible.

{{</ faq >}}


{{< faq "Can you modify your previous chart to include your birth state?">}}

- Can you include `Total` and your birth state?
- Is there a better metric than raw counts that you could calculate?
- Are there good labels that you could include on the chart ([`mark_text()`](https://altair-viz.github.io/gallery/bar_chart_with_labels.html#gallery-bar-chart-with-labels))?

{{</ faq >}}


{{< faq "Now come up with a different chart than a line chart">}}

Just use your state count or the `Total` count for your name.

{{</ faq >}}
--------------------------------->

<br>
