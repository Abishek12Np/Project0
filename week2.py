import pandas as pd 
import altair as alt 

#%%
import pandas as pd 
import altair as alt 
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})


# %%
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})
df

# %%
df.sort_values("a")


#%%
df.head(n=2)

# %%
df["b"].mean()

# %%
df.rename(columns= {'a':'duck'})

# %%
df.filter(["duck", "b"])
df.query("b<9")


# %%

names = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv")
# %%
names["name"].nunique()
# %%
names.filter(["name, year"]).nunique()
# %%
names

#%%
oliver = names.query("name == 'Oliver' ")
oliver

oliver.filter(["UT"]).sum()  # assignment part


#%%
hans = names.query("name == 'Hans' ")
Felisha = names.query("name == 'Felisha' ")

Felisha.filter(['year']).min()  #assignment part

# %%
import altair as alt 
#pick a name
hans_chart = alt.Chart(hans).encode(
    x = 'year',
    y = 'Total'
).mark_bar()


Felisha_chart = alt.Chart(Felisha).encode(
    x = 'year',
    y = 'Total'
).mark_bar(color="green")
# %%
Felisha_chart
# %%
hans_chart + Felisha_chart
# %%
h_f = names.query("name == 'Felisha' | name == 'Hans' ")

#%%
h_f

# %%
alt.Chart(h_f).encode(
    x = 'year',
    y = 'Total',
    color = 'name'
).mark_line()
# %%
