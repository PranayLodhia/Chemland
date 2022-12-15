import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash import Input, Output

from dash import Dash, dcc, html
from dash.dependencies import Input, Output



app = Dash(__name__, )
#--------------------------------------------------------
#import data


#-------------------------------------------------------
#app layout

tab1 = html.Div([
    html.H3('Tab 1'),
    dcc.Dropdown(
        id='input',
        options=[
            {'label': 'How tow to assign NMR', 'value': 'well'},
            {'label': 'Practice question', 'value': 'this'},
        ],

    ),
    html.Div(id='output'),
])

tab2 = html.Div([
    html.H3('Tab 2'),
    dcc.Dropdown(
        id='my-input',
        options=[
            {'label': ' Welcome to CH2200', 'value': 'In this section we will cover the basics of Spectrocopy'},
            {'label': 'b ', 'value': 'physics'},
        ],

    ),

    html.Div(id='my-output'),
])

app.layout = html.Div([
    html.H1('Pranay Lodhia BSc Project',style={"color": "#011833"}),
    dcc.Tabs(id='tabs', value='1', children=[
        dcc.Tab(
            label='NMR',
            value='1',
            children=[
                tab1,
                dcc.Textarea(
                    id="example",
                    value="example1",
                    style={"width": "50%", "height": 300}
                )]),
        dcc.Tab(
            label='Spectroscopy',
            value='2',
            children=[
                tab2,
                dcc.Textarea(
                    id="test",
                    value="testrun",
                    style={"width": "50%", "height": 300}
                )]),
            ])
        ])

@app.callback(
    Output("test", "value"),
    Input("my-input", "value")
)
@app.callback(
    Output("example", "value"),
    Input("input", "value")
)

def update_textarea(input_value):
    return f'Dropdown says: {input_value}'


#-------------------
if __name__ == '__main__':
    app.run_server(debug=True)
