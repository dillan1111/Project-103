import pandas as pd;
import plotly_express as px;
df = pd.read_csv("covid_Data.csv")
fig = px.scatter(df, x = 'date', y = 'cases', color = 'country', title = 'Cases of Covid per date for many countries.')
fig.show()