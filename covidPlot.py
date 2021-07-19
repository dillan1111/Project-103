import pandas as pd;
import plotly_express as px;
df = pd.read_csv("covid_Data.csv")
#fig = px.scatter(df, x = 'date', y = 'cases', size = 'pop', theme='plotly_dark', orientation='h', color = 'country', title = 'Cases of Covid per date for many countries.')

for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig = px.scatter(df,
                     x='date', y='cases', color='country',
                     size_max=60,
                     template=template, title="Cases of Covid per date for many countries: '%s' theme" % template)
    fig.show()

fig.show()