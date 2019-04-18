
# coding: utf-8

# In[19]:


#http://www.intervalfundtracker.com
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

#import the data
df = pd.read_csv('total_net_asset_growth.csv')  #change this depending on directory where you store csv file


#chart data source and layout
trace1 = go.Bar(
                    x=df['Filing Date'], y=df['Net Assets'], name='Net Assets', yaxis='y'# Data
                    
                   )
trace2 = go.Scatter(
    x=df['Filing Date'],
    y=df['QOQ'],name='%Change QOQ',
    yaxis='y2'
)

layout = go.Layout(
    title='Interval Fund Net Asset Growth', legend=dict(orientation="h"), 
    yaxis=dict(
        title='Aggregate Net Assets($)', side ='left', range=[0, 30000000000]
    ),
    yaxis2=dict(       
       overlaying='y', side='right',tickformat="%", showgrid=False, range=[-.005, .20])
)
#df.head()


# In[20]:


data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='net_asset_growth')

