### Edits once you use the template.

In the [config.toml](config.toml) file you will need to change a few settings

#### First Section

```YAML
################################# Default configuration ###################
# provide your domain here
baseURL = "https://byuistats.github.io/CSE250-Course"
# https:byuistats.github.io/CSE250-Course
# theme
theme = "Dot"
# site title
title = "DS250"
# disable language
disableLanguages = [true]
# google analytics
googleAnalytics = "UA-132356198-4" 
publishDir = 'docs'
# unsafe html
[markup.goldmark.renderer]
unsafe= true
```

#### End Section

You can set the copyright to have your name but please keep BYU-I.  You can change the title to have your name in it.

```YAML
################################ English Language ######################
[Languages.en]
languageName = "En"
languageCode = "en-us"
weight = 1
home = "Home"
copyright = "J. Hathaway and BYU-I ©"

# banner
[Languages.en.params.banner]
title = "DS 250: Data Science Programming"
subtitle = "Using pandas, Altiar, scikit-learn, and NumPy to program with data"
bg_image = "images/banner.png"
placeholder = "Have a question? Just ask here or enter terms"
```

Finally, you can change the colors in the __Default Parameters__ section.  Maybe tweaking the `primary_color` for the banner color.
