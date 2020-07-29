# International World Maps
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objects as go

df = pd.read_csv('https://pkgstore.datahub.io/core/gdp/gdp_csv/data/0048bc8f6228d0393d41cac4b663b90f/gdp_csv.csv')
print(df.head())

data = dict(
        type = 'choropleth',
        locations = df['Code'],
        z = df['Value'],
        text = df['Country'],
        colorbar = {'title' : 'GDP Value'},
      )
layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'Mercator'}
    )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)