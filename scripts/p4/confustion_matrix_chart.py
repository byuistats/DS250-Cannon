# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Confusion matrix chart
- https://github.com/SorenLaursen/confusion_matrix_chart
# %% [markdown]
# Content: This notebook implements the confusion matrix chart i.e. the confusion matrix with a number of graphical decorators. 
# 
# Author: Søren Laursen (https://www.linkedin.com/in/soren02laursen/)
# 
# Further reading: The confusion matrix chart is the subject of an article on Towards Data Science: https://towardsdatascience.com/the-confusion-matrix-visualized-e778584c8834.
# %% [markdown]
# ## Imports

# %%
import pandas as pd
import numpy as np
import altair as alt

# %% [markdown]
# ## Odss Ratio calculations

# %%
critical_value_dict = {70:1.04, 75:1.15, 80:1.28, 85:1.44, 90:1.64 , 95:1.96 , 98:2.33 , 99:2.58}

def odds_ratio(a, b, c, d):
    if a==0 or np.isnan(a) or b==0 or np.isnan(b) or c==0 or np.isnan(c) or d==0 or np.isnan(d):
        a = 0.5 if np.isnan(a) else a + 0.5
        b = 0.5 if np.isnan(b) else b + 0.5
        c = 0.5 if np.isnan(c) else c + 0.5
        d = 0.5 if np.isnan(d) else d + 0.5

    return (a*d)/(b*c)

def odds_ratio_lower_ci(OR, a, b, c, d, confidence_level):
    if a==0 or np.isnan(a) or b==0 or np.isnan(b) or c==0 or np.isnan(c) or d==0 or np.isnan(d):
        a = 0.5 if np.isnan(a) else a + 0.5
        b = 0.5 if np.isnan(b) else b + 0.5
        c = 0.5 if np.isnan(c) else c + 0.5
        d = 0.5 if np.isnan(d) else d + 0.5

    return np.exp(np.log(OR) - critical_value_dict[confidence_level]*np.sqrt(1/a + 1/b + 1/c + 1/d))

def odds_ratio_upper_ci(OR, a, b, c, d, confidence_level):
    if a==0 or np.isnan(a) or b==0 or np.isnan(b) or c==0 or np.isnan(c) or d==0 or np.isnan(d):
        a = 0.5 if np.isnan(a) else a + 0.5
        b = 0.5 if np.isnan(b) else b + 0.5
        c = 0.5 if np.isnan(c) else c + 0.5
        d = 0.5 if np.isnan(d) else d + 0.5

    return np.exp(np.log(OR) + critical_value_dict[confidence_level]*np.sqrt(1/a + 1/b + 1/c + 1/d))

# %% [markdown]
# ## Derive confusion matrix data

# %%
def confusion_matrix_data(Yy, Yn, Ny, Nn):
    CM = pd.DataFrame({'label':['Yy','Yn','Ny','Nn', 
                                'y|Y','n|Y','n|N','y|N',
                                'Y|y','N|y','N|n','Y|n',
                                'Y','N','y','n',
                                'Y*','N*','y*','n*',
                                'OR_lci90','OR_lci95','OR_lci99','OR','OR_uci90','OR_uci95','OR_uci99', '1',
                                'ACC','ACC-','F1','F1-'], 
                       'value':[Yy,  Yn,  Ny,  Nn,   
                                0 if Yy+Yn==0 else Yy/(Yy+Yn), 
                                0 if Yy+Yn==0 else Yn/(Yy+Yn), 
                                0 if Ny+Nn==0 else Nn/(Ny+Nn), 
                                0 if Ny+Nn==0 else Ny/(Ny+Nn),
                                0 if Yy+Ny==0 else Yy/(Yy+Ny), 
                                0 if Yy+Ny==0 else Ny/(Yy+Ny), 
                                0 if Yn+Nn==0 else Nn/(Yn+Nn), 
                                0 if Yn+Nn==0 else Yn/(Yn+Nn),
                                Yy+Yn, Ny+Nn, Yy+Ny, Yn+Nn, 
                                (Yy+Yn)/(Yy+Yn+Ny+Nn), (Ny+Nn)/(Yy+Yn+Ny+Nn), 
                                (Yy+Ny)/(Yy+Yn+Ny+Nn), (Yn+Nn)/(Yy+Yn+Ny+Nn),
                                odds_ratio_lower_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 90), 
                                odds_ratio_lower_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 95), 
                                odds_ratio_lower_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 99), 
                                odds_ratio(Yy, Yn, Ny, Nn), 
                                odds_ratio_upper_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 90), 
                                odds_ratio_upper_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 95), 
                                odds_ratio_upper_ci(odds_ratio(Yy, Yn, Ny, Nn), Yy, Yn, Ny, Nn, 99), 
                                1,
                                (Yy+Nn)/(Yy+Yn+Ny+Nn), (Yn+Ny)/(Yy+Yn+Ny+Nn),
                                0 if Yy==0 or Yy+Yn==0 or Yy+Ny==0 else 2 * ((Yy/(Yy+Yn)) * (Yy/(Yy+Ny))) / ((Yy/(Yy+Yn)) + (Yy/(Yy+Ny))),
                                1 if Yy==0 or Yy+Yn==0 or Yy+Ny==0 else 1 - (2 * ((Yy/(Yy+Yn)) * (Yy/(Yy+Ny))) / ((Yy/(Yy+Yn)) + (Yy/(Yy+Ny))))
                               ]})


    colours = alt.Scale(domain=['Yy','Yn','Ny','Nn', 
                                'y|Y','n|Y','n|N','y|N',
                                'Y|y','N|y','N|n','Y|n',
                                'Y','N','y','n',
                                'Y*','N*',
                                'y*','n*',
                                'OR_lci90','OR_lci95','OR_lci99','OR','OR_uci90','OR_uci95','OR_uci99', '1',
                                'ACC','ACC-','F1','F1-'], 
                        range =['snow', 'snow','snow', 'snow',
                                'forestgreen','palegreen','powderblue','cadetblue',
                                'forestgreen','cadetblue','powderblue','palegreen',
                                'goldenrod','gold','goldenrod','gold',
                                'goldenrod','gold',
                                'goldenrod','gold',
                                'dodgerblue','deepskyblue','lightskyblue','blue',
                                'dodgerblue','deepskyblue','lightskyblue','darkorange',
                                'goldenrod','gold','goldenrod','gold'
                               ])
    return CM, colours

# %% [markdown]
# ## Create confusion matrix chart

# %%
def cf_v_bar(CM, colours, label_list, sort_order, w_factor, h_factor, sf):
    bar = alt.Chart(CM.loc[CM['label'].isin(label_list)]).mark_bar(size=w_factor*sf).encode(
        y=alt.Y('sum(value)', stack='normalize', title=None, axis=None),
        color=alt.Color('label', scale = colours, legend=None),
        order=alt.Order('label', sort=sort_order),
        tooltip=['value']
    ).properties(width=w_factor*sf, height=h_factor*sf) 
    
    return bar

def cf_h_bar(CM, colours, label_list, sort_order, w_factor, h_factor, sf):
    bar = alt.Chart(CM.loc[CM['label'].isin(label_list)]).mark_bar(size=h_factor*sf).encode(
        x=alt.X('sum(value)', stack='normalize', title=None, axis=None),
        color=alt.Color('label', scale = colours, legend=None),
        order=alt.Order('label', sort=sort_order),
        tooltip=['value']
    ).properties(width=w_factor*sf, height=h_factor*sf) 
    
    return bar


def cf_text(CM, label, format, font_size, w_factor, dy_factor, sf):
    text = alt.Chart(CM.loc[CM['label']==label]).mark_text(fontSize=font_size, color='black').encode(
        text=alt.Text('sum(value)', format=format)
    ).properties(width=w_factor*sf, height=w_factor*sf) 

    return text


def confusion_matrix_chart(Yy, Yn, Ny, Nn):
    
    # Scaling factor
    sf = 15  
    
    
    # Derive chart data
    CM, colours = confusion_matrix_data(Yy, Yn, Ny, Nn)
    
    
    # FIRST ROW

    text_Yy = cf_text(CM, label='Yy', format='.0f', font_size=36, 
                      w_factor=10, dy_factor=5, sf=sf)

    bar_Y = cf_v_bar(CM, colours,
                     label_list=['n|Y','y|Y'], sort_order='descending', 
                     w_factor=2, h_factor=10, sf=sf)
    
    text_Yn = cf_text(CM, label='Yn', format='.0f', font_size=36, 
                      w_factor=10, dy_factor=5, sf=sf)

    # SECOND ROW
    
    bar_y = cf_h_bar(CM, colours,
                     label_list=['Y|y','N|y'], sort_order='ascending', 
                     w_factor=10, h_factor=2, sf=sf)
    
    bar_a = cf_v_bar(CM, colours,
                     label_list=['ACC','ACC-'], sort_order='ascending', 
                     w_factor=2, h_factor=2, sf=sf)
    
    bar_n = cf_h_bar(CM, colours,
                     label_list=['N|n','Y|n'], sort_order='ascending', 
                     w_factor=10, h_factor=2, sf=sf)
    
    # THIRD ROW
    
    text_Ny = cf_text(CM, label='Ny', format='.0f', font_size=36, 
                      w_factor=10, dy_factor=5, sf=sf)

    bar_N = cf_v_bar(CM, colours,
                     label_list=['n|N','y|N'], sort_order='descending', 
                     w_factor=2, h_factor=10, sf=sf)
    
    text_Nn = cf_text(CM, label='Nn', format='.0f', font_size=36, 
                      w_factor=10, dy_factor=5, sf=sf)

    
    # FRAMING BARS
    
    # Left bar
    bar_L = cf_v_bar(CM, colours,
                     label_list=['Y*','N*'], sort_order='ascending', 
                     w_factor=2, h_factor=25, sf=sf)
    
    # Top left corner bar
    bar_0 = cf_v_bar(CM, colours,
                     label_list=['F1','F1-'], sort_order='ascending', 
                     w_factor=2, h_factor=2, sf=sf)
    
    # Top bar
    bar_T = cf_h_bar(CM, colours,
                     label_list=['y*','n*'], sort_order='descending', 
                     w_factor=25, h_factor=2, sf=sf)
    
    # Top right corner text
    text_R = cf_text(CM, label='OR', format='.1f', font_size=12, w_factor=2, dy_factor=1, sf=sf)

    # Right bar
    bar_R = alt.Chart(CM.loc[
        CM['label'].isin(['1','OR_lci90','OR_lci95','OR_lci99','OR','OR_uci90','OR_uci95','OR_uci99'])]
                     ).mark_circle(opacity=0.8, stroke='black', strokeWidth=1, size=10*sf).encode(
        y=alt.Y('value', title=None, axis=None),
        color=alt.Color('label', scale = colours, legend=None),
        order=alt.Order('label', sort='descending'),
        tooltip=['value']
    ).properties(width=2*sf, height=25*sf) 


    # BUILD COMBINED CHART
    
    return (bar_0 | bar_T | text_R) & ( 
        bar_L | ( ( (text_Yy) | bar_Y | text_Yn) & (bar_y | bar_a | bar_n) & (text_Ny | bar_N | text_Nn) ) 
     | bar_R )

# %% [markdown]
# ## Instantiate the confusion matrix chart

# %%
Yy = 100 ; Yn = 200 ; Ny = 150 ; Nn = 550

confusion_matrix_chart(Yy, Yn, Ny, Nn)


