---
title: "VS Code for Data Science"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 6
draft: false
# search related keywords
keywords: [""]
---



{{< faq "What if my interactive Python window in VS Code is not using the same version of Python as my terminal?" >}}

You can set your Python version in VS Code by opening a `.py` script and then clicking on the Python text in the bottom left corner as shown below.

![](python_vscode_terminal.png)

Once you click, VS Code will open the command pallete where you can select your installation of Python that you would like to use with this workspace.

![](python_command_palet.png)

This setting will not fix what version your interactive Python window is using. You can get there by [opening settings](https://code.visualstudio.com/docs/getstarted/settings) by using  the `⌘,` shortcut.

You can then search your settings for _jupyter_ and you should see a section that has `Jupyter Command Line Arguments`.  Click on the `Edit in settings.json`.

![](ipython_settings.png)

Here you can set the jupyter path to Python to match the one you picked for your Terminal. An example for a Mac computer is shown below.

```
		"python.pythonPath": "/usr/local/opt/python/bin/python3",
```



{{</ faq >}}


{{< faq "What if I am not able to read in files from the GitHub links using `read_csv()?`" >}}

Most likely your Python SSl certificates are not installed.  Follow the answer in [this post](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)


{{</ faq >}}

{{< faq "How do I use VS Code to collaborate?" >}}

[Microsft's Live Share extension documentation](https://code.visualstudio.com/learn/collaboration/live-share) says, _'Live Share enables you to quickly collaborate with a friend, classmate, or professor on the same code without the need to sync code or to configure the same development tools, settings, or environment.'_  You can follow their guide or use our course created video.

{{< youtube oUcc2hp7fDM >}}

{{</ faq >}}



