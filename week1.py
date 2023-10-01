#%%

import pandas as pd 
import altair as alt 

#%%

mpg = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/mpg/mpg.csv")

mpg
# %%
alt.Chart(data = mpg).mark_point().encode(
    x = "year", 
    y = "hwy"
)

# %%
a = "Her name is "
b = "Isabella"
c = a + b
# %%
