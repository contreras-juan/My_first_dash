import os

import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

os.chdir('/home/juan/Data_Science/dash/intro')
df = pd.read_csv('intro_bees.csv')

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace = True)
print(df[:5])

app.layout = html.Div([

    html.H1('Web Application Dashboards widh Dash', style = {'text-align', 'center'}),

    dcc.Dropdown(id='slct_year',
    options=[
        {'label': '2015', 'value': 2015},
        {'label': '2016', 'value': 2016},
        {'label': '2017', 'value': 2017},
        {'label': '2018', 'value': 2018}],

        multi=False,
        value=2015,
        style={'width':'40%'}
        ),

    html.Div(id='output-container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

if __name__ == '__main__':
    app.run_server(debug=True)