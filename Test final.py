import dash

from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, )
#--------------------------------------------------------
#import data

# read the content.md file
with open('content.md') as file:
    markdown_content = file.read()


with open('Spec_quiz.html') as file:
    Spectroscopyquiz = file.read()

with open('Methyl ethyl ketone.html') as file:
    Methyl_ethyl_ketone = file.read()

with open('Remdesivir.html') as file:
    Remdesivir = file.read()

with open('Leflunomide.html') as file:
    Leflunomide = file.read()

with open('1,3-Propanediol.html') as file:
    Propanediol = file.read()

with open('Difluromethane.html') as file:
    Difluromethane = file.read()

with open('Butonoic acis.html') as file:
    Butonoic_acid = file.read()

with open('water.html') as file:
    water = file.read()

with open('1,5-Pentanedicarboxylic acid.html') as file:
    Pentanedicarboxylic_acid = file.read()

with open('Benzene.html') as file:
    Benzene = file.read()

with open('Fluorobiphenyl.html') as file:
    Fluorobiphenyl = file.read()

with open('Beta-Alanine.html') as file:
    BetaAlanine = file.read()

with open('Dichloromethane.html') as file:
    Dichloromethane = file.read()

with open('1,2,3,5-Tetrahydroxybenzene.html') as file:
    Tetrahydroxybenzene = file.read()

with open('Hydrogen cyanide.html') as file:
    Hydrogencyanide = file.read()

with open('1,5-Diiodopentane.html') as file:
    Diiodopentane = file.read()

with open('Triphenylphosphine.html') as file:
    Triphenylphosphine = file.read()

with open('Exampl 1.md') as file:
    Example1 = file.read()

with open('Exampl 2.md') as file:
    Example2 = file.read()

with open('Example 3.md') as file:
    Example3 = file.read()
#-------------------------------------------------------
#app layout



tab1 = html.Div([
    html.H3('Tab 1'),
    dcc.Dropdown(
        id='tab1-input',
        options=[
            {'label': 'IR spectrocopy', 'value':   markdown_content},
            {'label': 'Example 1', 'value': Example1},
            {'label': 'Example 2', 'value': Example2},
            {'label': 'Example 3', 'value': Example3},
        ],

    ),
    html.Div(id='tab1-output'),
])

tab2 = html.Div([
    html.H3('Tab 2'),
    html.Iframe(
        id="my-specoutput",
        style={"height": "495px", "width": "200%"},
        ),
        dcc.Dropdown(
            id='tab2-input',
            options=[
            {'label': ' Welcome to CH2200', 'value': Spectroscopyquiz},
            {'label': 'b ', 'value': 'physics'},
        ],

    ),

    html.Div(id='tab2-output'),
])

tab3 = html.Div([
    html.H3('Tab 3'),
    dcc.Dropdown(
        id='tab3-input',
        options=[
            {'label': ' 3D visulaisation', 'value': ''},
        ],

    ),

    html.Div(id='tab3-output'),
])

app.layout = html.Div([
    html.H1('Pranay Lodhia BSc Project'),
    dcc.Tabs(id='tabs', value='1', children=[
        dcc.Tab(
            label='NMR',
            id='markdown nmr',
            value='1',
            children=[
                tab1,
                # dcc.Markdown(markdown_content),
                # dcc.Markdown(Example1),
            ]),
        dcc.Tab(
            label='Spectroscopy',
            value='2',
            children=[
                tab2,
                ]),


        dcc.Tab(
            label ='3D',
            value='3',
            children=[
                tab3,
                html.Iframe(
                    id="my-output",
                    style={"height": "495px", "width": "200%"},
                ),
                    dcc.Dropdown(
                        id="input",
                        options=[
                    {"label": "Benzene", "value":Benzene},
                    {"label": "Triphenylphosphine", "value":Triphenylphosphine},
                    {"label": "Hydrogen cyanide", "value":Hydrogencyanide},
                    {"label": "1,2,3,5-Tetrahydroxybenzene", "value":Tetrahydroxybenzene},
                    {"label": "1,5-Diiodopentane", "value":Diiodopentane},
                    {"label": "Dichloromethane", "value":Dichloromethane},
                    {"label": "Beta-Alanine", "value":BetaAlanine},
                    {"label": "Fluorobiphenyl", "value":Fluorobiphenyl},
                    {"label": "1,5-Pentanedicarboxylic acid", "value":Pentanedicarboxylic_acid},
                    {"label": "water", "value":water},
                    {"label": "Butanoic acid", "value":Butonoic_acid},
                    {"label": "Difluromethane", "value":Difluromethane},
                    {"label": "1,3-Propanediol", "value":Propanediol},
                    {"label": "Leflunomide", "value":Leflunomide},
                    {"label": "Remdesivir", "value":Remdesivir},
                    {"label": "Methly ethyl ketone", "value": Methyl_ethyl_ketone},
                    ]
                )
            ])
        ])
    ])



#2
@app.callback(
    Output("tab2-output", "children"),
    Input("tab2-input", "value")
)
#1
@app.callback(
    Output("tab1-output", "children"),
    Input("tab1-input", "value")
)
#3
@app.callback(
    Output("input", "value"),
    Input("tab3-input", "value")
)
@app.callback(
    Output("my-output", "srcDoc"), Input("input", "value"), prevent_initial_call=True
)
def update_output_div(input_value):
    print(f"{input_value}")
    if input_value is not None and input_value != "":
        if(input_value[0] == "#"):
            return dcc.Markdown(input_value)
        else:
            return input_value






#-------------------
if __name__ == '__main__':
    app.run_server(debug=True)