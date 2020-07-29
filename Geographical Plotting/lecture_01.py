import plotly.offline as py
from plotly.offline import iplot,plot
import plotly.graph_objects as go
import pandas as pd

## Choropleth US Maps

# data = dict(type = 'choropleth',
#             locations = ['AZ','CA','NY'],
#             locationmode = 'USA-states',
#             colorscale= 'Portland',
#             text= ['text1','text2','text3'],
#             z=[1.0,2.0,3.0],
#             colorbar = {'title':'Colorbar Title'})
#
# layout = dict(geo = {'scope':'usa'})
# go.Figure(data = [data],layout = layout)
# choromap = go.Figure(data = [data],layout = layout)
# iplot(choromap)


### Real Data US Map Choropleth

# df = pd.read_csv('https://github.com/plotly/datasets/blob/master/2011_us_ag_exports.csv')
# df.head()
# data = dict(type='choropleth',
#             colorscale = 'YIOrRd',
#             locations = df['code'],
#             z = df['total exports'],
#             locationmode = 'USA-states',
#             text = df['text'],
#             marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
#             colorbar = {'title':"Millions USD"}
#             )
# layout = dict(title = '2011 US Agriculture Exports by State',
#               geo = dict(scope='usa',
#                          showlakes = True,
#                          lakecolor = 'rgb(85,173,240)')
#              )
# choromap = go.Figure(data = [data],layout = layout)
# iplot(choromap)
#


