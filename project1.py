import pandas as pd
import altair as alt


#%%
import pandas as pd
import altair as alt
names = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv")
names
# %%

Avishek = names.query("name == 'Jake'")

#%%
Avishek


# %%
Avi_chart = alt.Chart(Avishek).encode(
            x = alt.X('year', axis= alt.Axis(format='d', title="Year")),
            y = alt.Y('Total',axis= alt.Axis(title='number of Jake') )
     ).mark_line()
# %%
Avi_chart
# %%
line_df = pd.DataFrame({'year': [2003]})

# %%
line_df
# %%
line = alt.Chart(line_df).mark_rule(color='yellow').encode(x='year')
# %%
Avi_chart + line
# %%
# Question 2 starts here
brittany = names.query("name == 'Brittany'")
# %%
her_age = 2023 - brittany['year']
# %%
her_age
# %%
brittany.insert(2, 'age', her_age)
# %%
brittany
# %%
alt.Chart(brittany).mark_bar().encode(
    x= 'age',
    y= 'Total'
)
# %%
## Question 3 starts here

Christian_names = ["Mary", "Martha", "Peter", "Paul"]
new_data = (names.query('name in @Christian_names'))
new_data = (new_data.query("year>1919"))
new_data= (new_data.query("year<2001"))
# %%
christian_chart = alt.Chart(new_data).encode(
     x = alt.X('year', axis = alt.Axis(format ='d', title = "Year")),
     y = alt.Y('Total'),
    color = alt.Color('name')
)
# %%
christian_chart.mark_line()
# %%
#Question 4 starts here

Barry = names.query("name == 'Barry' ")
# %%
Barry
# %%
barry_chart = alt.Chart(Barry).encode(
    x = alt.X('year', axis=alt.Axis(format='d',title="year")),
    y = alt.Y('Total')
).mark_line()
# %%
barry_chart
# %%
line_fd = pd.DataFrame({'year':[1939]})
line_2 = alt.Chart(line_fd).mark_rule(color='black').encode(
    x = 'year'
)

# %%
barry_chart+line_2

