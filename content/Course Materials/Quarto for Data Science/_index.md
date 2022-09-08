---
title: "Quarto for Data Science"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 7
draft: false
# search related keywords
keywords: [""]
---

## Quarto

Quarto is an open-source scientific and technical publishing system built on [Pandoc](https://pandoc.org/). You can create dynamic content with [Python](https://quarto.org/docs/computations/python.html), [R](https://quarto.org/docs/computations/r.html), [Julia](https://quarto.org/docs/computations/julia.html), and [Observable](https://quarto.org/docs/computations/ojs.html).

We use this perfect union of Jupyter Notebooks and RMarkdown for reporting on our projects. It leverages Markdown and Python code chunks to create dynamic HTML content.

## Markdown

Markdown is a plain text formatting syntax aimed at making writing more accessible. The philosophy behind Markdown is that plain text documents should be readable without tags making a mess, but there should still be ways to add text modifiers like lists, bold, italics, etc. It is an alternative to WYSIWYG (what you see is what you get) editors, which use rich text that later gets converted to proper HTML.[^1]

## Quarto Basics

You will need to install the Quarto CLI and then go through the VS Code directions on using Quarto with Python.

1. Install [Quarto CLI](https://quarto.org/docs/get-started/)
2. [Setup your VS Code](https://quarto.org/docs/get-started/hello/vscode.html)
3. [Really read the VS Code setup entirely](https://quarto.org/docs/get-started/hello/vscode.html)


## Class template

We have built a [template](../../template/ds250_project_template_clean.qmd) to provide an example of you will submit your project reports (for additional details please see the [instructional template](../../template/ds250_project_template.qmd)). As you use the template, the following items may help you understand how to write your report.

1. The template is a guide. Don't feel responsible for including every item beyond sections for each question.
2. Your appendix should have properly highlighted Python code that doesn't run off the page (other than file paths).
3. You can see examples of the html output [here](../../template/ds250_project_template_clean.html) and [here](../../template/ds50_project_template.html)


## Markdown Examples

You can read the complete syntax guide [at the daringfireball.net website](https://daringfireball.net/projects/markdown/syntax). The code chunk below highlights the standard syntax[^2]

```Markdown
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

You can make bulleted lists.

* Item 1
* Item 2
  * Item 2a
  * Item 2b

Or numbered lists.

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

Place an image in the document.

![GitHub Logo](/images/logo.png)

or a link in a document

[GitHub](http://github.com)

You can even blockquote Kanye West said:

> We're living the future so
> the present is our past.

Finally, you can create tables. Check out `print(df.to_markdown())` to get tables from pandas.

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column


Every once in a while, you may want strikethrough.

~~this~~
```
### Getting tables out of Pandas

You can create tables using Markdown in your reports. You can use the `.to_markdown()` method on your `DataFrame` object. You would use `print(df.to_markdown(index=False))` to get tables from pandas. They would print out in your interactive window as;

```markdown
name  | gender
----- | ------
J.    | Male
Katie | Female
```

You would then copy the output from your interactive window and paste it into your `.md` report.

[^1]: https://www.ultraedit.com/company/blog/community/what-is-markdown-why-use-it.html

[^2]: https://guides.github.com/features/mastering-markdown/