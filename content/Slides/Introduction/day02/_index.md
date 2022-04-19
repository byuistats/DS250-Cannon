---
title: "Day 2: Welcome and Project 0"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-17T10:42:26+06:00
weight: 1
draft: true
# search related keywords
keywords: [""]
---

<!---------- note: modified for a one-day first week -------->
<!---------- scroll to bottom for original 2-day second day slides ------>

## Welcome to DS 250!

#### Syllabus Questions?

#### Are we all on the Slack channel?

Follow the Slack invitation that is waiting in your student email. If you don't see an invite, you can join through [this link](https://join.slack.com/t/byuidss/signup) and then ask Brother Cannon to add you to the class channel.

<br>

## Methods Checkpoint

All the answers will be in the assigned reading or in these slides. 

You will also need to install a package in Python before you answer the last question.

<br>

## Notes on Project 0

#### Installing Packages and Extensions

Learn how to install packages by reading the assigned material and by watching the video tutorial on [this page](https://byuistats.github.io/DS250-Cannon/course-materials/python-for-data-science/).

The readings mention a lot of different packages. For Project 0, you need to install at least `pandas`, `altiar`, `altair-saver`, `numpy`, `tabulate`, and `jupyter`.

The readings will also mention two VS Code extensions you need to install.

#### Jupyter Notebooks vs. Interactive Python Window

Should you decide to use Juypyter Notebooks this semester within VS Code, [this is a great guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to get you started. 

Or you can choose to stick with the [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py) like the textbook does.

#### Use Your Resources!

- Technical documentation
- Google searches
- Asking for help on Slack
- Don't forget the [data science lab](https://byuidatascience.github.io/lab.html)! (Starts next week.)
- Question that cannot be answered by the textbook and documentation? Google it.
- A function you have never seen before? Google it.
- An error in your code? Google it.

#### Jupyter Notebooks

You can use Juypyter Notebooks this semester within VS Code. [This is a great guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to get you started. 

Or you can choose to stick with the [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py) like the textbook does.

#### Markdown

# What is Markdown?  
- A clean, human readable way to make slick html and pdf documents
- Used widely among programmers for clean documentation 
- Used widely by Data Scientists to publish results and communicate with stakeholders

[Here's a good summary](https://byuistats.github.io/DS250-Cannon/course-materials/markdown/)

<!----!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!------>
<!-------- UNEDITED second-day slides ----------------->


<!---------------------------------------------------------------------
## Welcome to class!

<br>

## Using Your Resources

- Technical documentation
- Google searches
- Asking for help on Slack
- Don't forget the [data science lab](https://byuidatascience.github.io/lab.html)! (Starts next week.)
- Question that cannot be answered by the textbook and documentation? Google it.
- A function you have never seen before? Google it.
- An error in your code? Google it.

<br>

## Project 0

#### VS Code and Python

#### Packages (Libraries?)

#### Jupyter Notebooks

I'll be using Juypyter Notebooks this semester within VS Code. [This is a great guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to get you started. 

Or you can choose to stick with the [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py) like the textbook does.

#### Let's make a chart!

#### Creating a report.

------------------------------------------------------------------------------>



<!----------------------------------



  - Question that cannot be answered by the textbook and documentation? Google it.
  - A function you have never seen before? Google it.
  - An error in your code? Google it.





## Finishing some setup

{{< faq "Any issues with getting Python installed?">}}

- [Python](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- [Altair in VS Code](https://altair-viz.github.io/user_guide/display_frontends.html)

{{</ faq >}}


{{< faq "Does everyone have `pandas`, `altiar`, `numpy`, `scikit-learn` installed?">}}

- [Video tutorial: how to install packages.](../../course-materials/python-for-data-science/)

One way to install packages:

```
pip install pandas altair
```
Maybe a better way to do it: run this in an interactive window.

```
import sys
!{sys.executable} -m pip install pandas altair
```

{{</ faq >}}

{{< faq "Does everyone have `altair-saver` working?">}}

- [altair_saver](https://github.com/altair-viz/altair_saver)
- [Video tutorial](../../course-materials/altiar/)

{{</ faq >}}

---------------------------------------------------->





<!--------------------
{{< faq "Why are we using Altair?">}}

## It is built on the VEGA and D3 which are fast and web based.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AAuPPorsmJc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Grammar of Graphics: Vega-Lite

![](altair_grammar_graphics.png)

> - [Technical Paper](https://www.domoritz.de/papers/2017-VegaLite-InfoVis.pdf)
> - [Website](https://vega.github.io/vega-lite/)
> - [Endorsment](https://medium.com/@robin.linacre/why-im-backing-vega-lite-as-our-default-tool-for-data-visualisation-51c20970df39)


{{</ faq >}}

{{< faq "What are we not learning in this course?">}}

## Indexing, `.loc[]` and `.iloc[]`

I may not be experienced enough to understand why I should teach you these. I think they all add complexity to what we are learning in the course and we have elected to avoid it.  We will use `reset_index()` a lot.  I think [MultiIndex](https://towardsdatascience.com/how-to-use-multiindex-in-pandas-to-level-up-your-analysis-aeac7f451fce) features create complication. I have also elected to use `.filter()` instead of `.loc[]` because I like it.

## Virtual Environments

[Virtual Environments](https://towardsdatascience.com/virtual-environments-for-data-science-running-python-and-jupyter-with-pipenv-c6cb6c44a405#:~:text=The%20primary%20purpose%20of%20Python,dependencies%20every%20other%20project%20has.) appear to be an important tool as you continue to use Python.  We will not be teaching these or supporting these in our course.

## matplotlib (and any tool leveraging it)

It feels old, [has a bad api](https://ryxcommar.com/2020/04/11/why-you-hate-matplotlib/), and isn't declarative.

{{</ faq >}}

----------------------------->



<!---------------

## Coming Up:

#### Can we practice making a chart in Altair with VS Code?


{{< faq "What can Python Interactive do?">}}

## Let's review the power of [Python Interactive](https://code.visualstudio.com/docs/python/jupyter-support-py)

- `# %%` in my `.py` script is much better than Jupyter notebooks (`.ipynb`). 
  - If we hope to have our code work in a production environment then Jupyter is problematic.
  - Caching and code chunks are problematic
  - https://medium.com/@_orcaman/jupyter-notebook-is-the-cancer-of-ml-engineering-70b98685ee71 

{{</ faq >}}


{{< faq "Set-up your `py` script">}}

## Setting up your script

A good data science `.py` script will have packages and data loaded at the top. Usually you have a few short commented sentences that descibe the script purpose.

   ```python
   # %%
   # import pandas, altair, numpy
   import pandas as pd
   import altair as alt
   import numpy as np

   # %%
   # load data
   # handgrenade data https://github.com/byuidatascience/data4soils/blob/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv
   
   url = 'https://github.com/byuidatascience/data4soils/raw/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv'
   
   dat = pd.read_csv(url)

   ```

{{</ faq >}}


{{< faq "Make a scatter plot with `hmx` on the x and `rdx` on the y">}}

To get you started: 

```python
alt.Chart(dat).encode()
```

{{</ faq >}}


{{< faq "Make a spatial plot with `hmx` colored">}}

1. Encode the `row` and `column` to the axes.
2. Color the `hmx` points using the 'goldorange' color scheme.
3. Use `mark_square()` and make the square sizes 500.

{{</ faq >}}


-------------------->




<!-----------------
alt.Chart(dat).encode(x='hmx', y='rdx').mark_circle()

(alt.
  Chart(dat).
  encode(
    x='column', 
    y='row', 
    size=alt.value(500),
    color=alt.Color('hmx', scale=alt.Scale(scheme='goldorange'))).
  mark_square()
)
----------------->





<!----------------------
{{< faq "Create a histogram of `hmx`">}}

1. Encode the x-axis as binned.
2. Encode the y-axis as counts.
3. Configure the title to a `fontSize` of 20.
4. Use properties to place the title.

{{</ faq >}}
----------------------------->




<!-------------
{{< faq "How can I get help?">}}

- Make sure you __read the reading assignments__ once or twice or five times.
- Read the guides on the [Course Materials](../../../course-materials/) page.
- Post questions in our #cse250_s21_larson slack channel (and try to help others!)
- Attend the [Data Science Lab](https://byuidatascience.github.io/lab.html).
- Google is your best friend.

{{</ faq >}}
-------------------------->


<br>
