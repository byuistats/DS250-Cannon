# %%
import pandas as pd 
import altair as alt
import numpy as np
# %%
# create a number threshold that minimizes variance in two histograms

dat = pd.concat([
    pd.DataFrame({"value":np.random.normal(-5, 2, 300)}).assign(group="Negative"),
    pd.DataFrame({"value":np.random.normal(5, 2, 300)}).assign(group="Positive")])

# %%
slider = alt.binding_range(min=-15, max=15, step=1, name='Threshold:')

selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
                                bind=slider, init={'Threshold:': 4})

histogram = (alt.Chart()
    .mark_bar()
    .encode(
        x = 'binned_value:O',
        y = 'count()',
        color = alt.condition(
            alt.datum.binned_value < selector.cutoff,
            alt.value('red'), alt.value('blue')
        ))
    .transform_bin('binned_value', field = 'value', bin = alt.Bin(step = .5))
)

text = (alt.Chart()
    .mark_text()
    .encode(
        x = alt.value(500),
        y = alt.value(25),
        text = 'sdcalc:O',
        color = alt.value('red'),
        size = alt.value(25))
    .transform_filter((alt.datum.value < selector.cutoff))
    .transform_aggregate(sdcalc = 'stdev(value)'))

text_right = (alt.Chart()
    .mark_text()
    .encode(
        x = alt.value(500),
        y = alt.value(0),
        text = 'sdcalc:O',
        color = alt.value('blue'),
        size = alt.value(25))
    .transform_filter((alt.datum.value > selector.cutoff))
    .transform_aggregate(sdcalc = 'stdev(value)'))
    
chart = (alt.layer(
        histogram, 
        text, 
        text_right, 
        data=dat)
    .add_selection(selector)
    .properties(
        width = 1000,
        height = 500))

chart.save('threshold_histogram.html')

# %%



# # %%
# import pandas as pd 
# import altair as alt
# import numpy as np
# # %%
# # create a number threshold that minimizes variance in two histograms

# dat = pd.concat([
#         pd.DataFrame({"value":np.random.normal(-5, 2, 300)}).assign(group="Negative"),
#         pd.DataFrame({"value":np.random.normal(5, 2, 300)}).assign(group="Positive")]).sort_values('value')

# pd.concat([dat, pd.Series(['yes', 'no', 'yes']).repeat([150, 300, 150]).to_frame()], axis = 1)

# # %%
# slider = alt.binding_range(min=-15, max=15, step=1, name='Threshold:')

# selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
#                                 bind=slider, init={'Threshold:': 4})

# histogram = (alt.Chart()
#     .mark_bar()
#     .encode(
#         x = 'binned_value:O',
#         y = 'count()',
#         color = alt.condition(
#             alt.datum.binned_value < selector.cutoff,
#             alt.value('red'), alt.value('blue')
#         ))
#     .transform_bin('binned_value', field = 'value', bin = alt.Bin(step = .5))
# )

# text = (alt.Chart()
#     .mark_text()
#     .encode(
#         x = alt.value(500),
#         y = alt.value(25),
#         text = 'sdcalc:O',
#         color = alt.value('red'),
#         size = alt.value(25))
#     .transform_filter((alt.datum.value < selector.cutoff))
#     .transform_aggregate(sdcalc = 'stdev(value)'))

# text_right = (alt.Chart()
#     .mark_text()
#     .encode(
#         x = alt.value(500),
#         y = alt.value(0),
#         text = 'sdcalc:O',
#         color = alt.value('blue'),
#         size = alt.value(25))
#     .transform_filter((alt.datum.value > selector.cutoff))
#     .transform_aggregate(sdcalc = 'stdev(value)'))
    
# chart = (alt.layer(
#         histogram, 
#         text, 
#         text_right, 
#         data=dat)
#     .add_selection(selector)
#     .properties(
#         width = 1000,
#         height = 500))

# chart.save('threshold_histogram.html')

# # %%
