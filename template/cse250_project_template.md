# Client Report - [Insert Project Title]
__Course CSE 250__
__Student Name__

_THIS `.md` FILE SHOULD BE USED TO WRITE YOUR REPORT.  YOU WILL NEED TO EXPORT THE REPORT INTO A `.pdf` DOCUMENT AND SUBMIT IT ON CANVAS._

_USE THIS [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) VS CODE EXTENSION TO WORK WITH MARKDOWN FILES (`.md`). READ MORE ABOUT CODE CHUNKS (AKA CODE SNIPPETS) [HERE](https://shd101wyy.github.io/markdown-preview-enhanced/#/code-chunk). YOU WILL ALSO NEED THIS [VS CODE MARKDOWN PDF](https://github.com/yzane/vscode-markdown-pdf) ADD-ON TO EXPORT TO `.pdf` FOR SUBMISSION._

## Elevator pitch

_A SHORT (4-5 SENTENCES) PARAGRAPH THAT `SUMMARIZES` THE WORK REQUESTED INCLUDING THE TOP RESULTS._

_A Client has requested this analysis and  this is your one shot of  what you would say to your boss in a 2min elevator ride before he takes your report and hands it to the client._

### GRAND QUESTION 1
#### COPY PASTE GRAND QUESTION 1 FROM THE PROJECT
###### Add details here to answer the question but `NOT` like an assignment Q&A. You need to write your answers as a consulting solution report. A Client needs to understand the answer, but also needs to understand the decisions that went into the answer (when applicable). 

##### TECHNICAL DETAILS
`### START ### Delete or Replace everything below this comment until the ### END ###`

_IN THIS SECTION, YOU WILL PROVIDE ANY OR ALL OF THE FOLLOWING AS APPROPRIATE FOR EACH GRAND QUESTION_
` `
- _PROVIDE CHARTS THAT HELP ADDRESS THE GRAND QUESTIONS._
![](CHART.png)

Note: Save your chart `.png` file in the same folder as your `.md`. Use the \!\[]\(CHART.png) code above and replace the name to match your png file name.
` `
- _PROVIDE TABLES THAT HELP ADDRESS THE GRAND QUESTIONS._
```python 
s = pd.Series(["elk", "pig", "dog", "quetzal"], name="animal")
print(s.to_markdown()
```
|    | animal   |
|---:|:---------|
|  0 | elk      |
|  1 | pig      |
|  2 | dog      |
|  3 | quetzal  |
` `
Note: Leave one empty row after pasting a chart or it can shift your chart and text. Also `don't` put this | `OR BAR` output into a code snippet it will not convert it to the good looking table in the preview window.
` `
- _YOU SHOULD INCLUDE SMALL CODE SNIPPETS FOR CHARTS, TABLES, AND TO  HIGHLIGHT DECISIONS (SEE EXAMPLES ABOVE). EXAMPLES WOULD INCLUDE CALCULATIONS, AND FEATURES SELECTION FOR ML MODELS._

Note: Python `Snippets` include (3) \`\`\` followed by (3) more \`\`\`, each on their own line. These are not single quotes, they are the key left of the number 1 key on the keyboard. The top row can include the language of code that is pasted inbetween the \`\`\`  marks. 

Note: These also work in `Slack` and it is expected they are used for any code shared in that app. No screen shots allowed.

Note: There are additional parameters that can then be passed after python using a set of {}. Dont put any other text on the row with these marks \`\`\`. See more about these parameters [here](https://shd101wyy.github.io/markdown-preview-enhanced/#/code-chunk). We have not been able to sucessfully run python code from in the `.md` file.

Example:
```python {cmd=true matplotlib=true}
import matplotlib.pyplot as plt
plt.plot([1,2,3, 4])
plt.show() # show figure
```

Note: If you see a `<p data-line="49" class="sync-line" style="margin:0;">\</p>` its a glitch with the preview add-on. If you use the VS CODE Preview this will not show up. However, use the Markdown Preview Enhanced anyways. 
 
- _YOU SHOULD HAVE QUALITY WRITING THAT DESCRIBES YOUR CHARTS AND TABLES._

- _I HIGHLY RECOMMEND [GRAMMARLY](https://grammarly.com/) TO FIX YOUR SPELLING AND GRAMMAR. WRITING TAKES TIME TO BE CLEAR. SPEND THE TIME TO PRACITCE._ 

` ### END ### - Delete up to here `

### GRAND QUESTION 2

    Repete layout and content from GQ1 for GQ2 where applicable

### GRAND QUESTION 3

    Repete layout and content from GQ1 for GQ3 where applicable

### GRAND QUESTION 4

    RRepete layout and content from GQ1 for GQ4 where applicable

### GRAND QUESTION 5

    Repete layout and content from GQ1 for GQ5 where applicable

## APPENDIX A (PYTHON SCRIPT)

`### START ### Delete everything below this comment until the ### END ###`

- _YOU SHOULD HAVE QUALITY COMMENTS THAT DESCRIBES YOUR CODES. OFTEN CODEERS WORK IN TEAMS AND YOU NEED TO HAVE QUALTIY COMMENTS FOR YOUR TEAM AND YOURSELF. YOU MAY NEED TO REVISIT CODE YOU WROTE OVER A YEAR AGO, AND IF YOU DONT COMMENT IT NOW YOU WONT REMEMBER WHY YOU DID WHAT YOU DID._

` ### END ### - Delete up to here `

```python
commented python code from .py file
```
