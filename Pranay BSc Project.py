import dash

from dash import dcc, html
from dash.dependencies import Input, Output

#stylesheet




app = dash.Dash(__name__)
#--------------------------------------------------------
#import data


#markdown

# read the content.md file
with open('Welcome.md') as file:
    welcome = file.read()


with open('content.md') as file:
    markdown_content = file.read()

with open('Example 1 Alkanes and alkenes.md') as file:
    Alkene_Alkane = file.read()

with open('Aromatics.md') as file:
    Aromatics = file.read()

with open('OH and COOH.md') as file:
    OH_and_COOH = file.read()

with open('COH and RCOR.md') as file:
    COH_and_RCOR = file.read()

with open('Esters.md') as file:
    Esters = file.read()

with open('NMR example 1.md') as file:
    NMR1 = file.read()

with open('Exampl 1.md') as file:
    worked_through_Example1 = file.read()

with open('Exampl 2.md') as file:
    worked_through_Example2 = file.read()

with open('Example 3.md') as file:
    worked_through_Example3 = file.read()
#-------------------------------------------

#Quiz


with open('Spec_quiz.html') as file:
    Spectroscopyquiz = file.read()

with open('Flash cards.html') as file:
    Flash_Cards = file.read()

with open('IR practice.html') as file:
    IR1 = file.read()

with open('nmr q2.html') as file:
    NMR_simple_1 = file.read()

with open('NMR practice q1.html') as file:
    NMRQ1 = file.read()

with open("NMR question 2.html") as file:
    NMRQ2 = file.read()

with open("Practice test 3.html") as file:
    NMRQ3 = file.read()


with open('NMR quiz 2.html') as file:
    NMRq3 = file.read()

with open("PointGroups.html") as file:
    pointgroup = file.read()

with open("game.js") as file:
    game = file.read()

with open("index.html") as file:
    index = file.read()

with open("styles.css") as file:
    style = file.read()

with open("test game.html") as file:
    test = file.read()
#--------------------------------------------

#3D

with open('Cubane.html') as file:
    Cubane = file.read()

with open('1,3,5 trimethyl benzene.html') as file:
    trimethylbenzene = file.read()

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



#-------------------------------------------------------
#app layout



tab1 = html.Div([
    html.H3(''),
        dcc.Dropdown(
            placeholder="Examples",
            id='tab1-input',
            options=[
                {'label': 'Welcome', 'value': welcome},
                {'label': 'Basic NMR and IR information', 'value': markdown_content},
                {'label': 'Alkenes, Alkanes and Alkynes', 'value': Alkene_Alkane},
                {'label': 'Aromatics', 'value': Aromatics},
                {'label': 'Alcohols and Carboxylic acids', 'value': OH_and_COOH},
                {'label': 'Aldehydes and Ketones ', 'value': COH_and_RCOR},
                {'label': 'Esters', 'value': Esters},
                {'label': 'Simple NMR example', 'value': NMR1},
                {'label': 'Example 1', 'value': worked_through_Example1},
                {'label': 'Example 2', 'value': worked_through_Example2},
                {'label': 'Example 3', 'value': worked_through_Example3},



            ],
        ),
    html.Div(id='tab1-output'),
    ])

tab2 = html.Div([
    html.H3(''),
        html.Iframe(
            id="my-specoutput",
            style={"height": "495px", "width": "100%"},
                ),
                dcc.Dropdown(
                    id='tab2-input',
                    options=[
                        {'label': 'Chemland ', 'value': test},
                        {'label': 'Spectroscopy quiz', 'value':Spectroscopyquiz},
                        {'label': 'Flash cards ', 'value': Flash_Cards},
        ],
    ),
    html.Div(id='tab2-output'),
])

tab3 = html.Div([
    html.H3(''),
    dcc.Dropdown(
        id='tab3-input',
        options=[
            {'label': ' 3D visulaisation', 'value': ''},
        ],
    ),
    html.Div(id='tab3-output'),
])
tab4=html.Div([
    html.H3(""),

    html.Iframe(
        id="my-Questions",
        style={"height": "495px", "width": "100%"},
    ),
    dcc.Dropdown(
        id="tab4-input",
        options=[
            {'label': 'IR practice question 1 ', 'value':IR1},
            {'label': 'NMR practice question 1 ', 'value':NMR_simple_1},
            {'label': 'NMR practice question 2 ', 'value':NMRq3},
            {'label': 'practice question 1 ', 'value':NMRQ1},
            {'label': 'Practice question 2 ', 'value': NMRQ2},
            {'label': 'Practice question 3 ', 'value': NMRQ3},
        ],
    ),
    html.Div(id="tab4_output"),
])


app.layout = html.Div([
    html.H1("CHEMLAND",
            style ={'textAlign' : 'center'} ),
    html.H2('Pranay Lodhia BSc Project',
            style = {'textAlign' : 'center'}),
    dcc.Tabs(id='tabs', value='1', children=[
        dcc.Tab(
            label='Spectroscopy practice',
            id='markdown nmr',
            value='1',
            children=[
                tab1,
            ]),
        dcc.Tab(
            label='Practice questions',
            id='practice questions',
            value="4",
            children=[
                tab4,
            ]),
        dcc.Tab(
            label='Spectroscopy theory',
            value='2',
            children=[
                tab2,
                ]),
        dcc.Tab(
            label ='Point groups and visualisation',
            value='3',
            children=[
                tab3,
                html.Iframe(
                    id="my-3D",
                    style={"height": "495px", "width":"50%", "align": "left%"},
                ),
                html.Iframe(
                    id="my-googleDoc",
                    style={"height": "495px","width": "49%", "align": "right"},
                ),

                    dcc.Dropdown(
                        id="input_3D_quiz",
                        style={"width":"50%", "align": "left"},
                        placeholder="pick the quiz",
                        options=[
                    {"label": "Point group quiz", "value": pointgroup},
                        ],
                    ),
                    dcc.Dropdown(
                        id="input",
                        style={"width":"50%", "align":"right"},
                        placeholder="pick a molecule",
                        options=[
                    {"label": "Benzene", "value":Benzene},
                    {"label": "Triphenylphosphine", "value":Triphenylphosphine},
                    #{"label": "Hydrogen cyanide", "value":Hydrogencyanide},
                    #{"label": "1,2,3,5-Tetrahydroxybenzene", "value":Tetrahydroxybenzene},
                    #{"label": "1,5-Diiodopentane", "value":Diiodopentane},
                    {"label": "Dichloromethane", "value":Dichloromethane},
                   # {"label": "Beta-Alanine", "value":BetaAlanine},
                   # {"label": "Fluorobiphenyl", "value":Fluorobiphenyl},
                   # {"label": "1,5-Pentanedicarboxylic acid", "value":Pentanedicarboxylic_acid},
                    {"label": "water", "value":water},
                   # {"label": "Butanoic acid", "value":Butonoic_acid},
                   # {"label": "Difluromethane", "value":Difluromethane},
                   # {"label": "1,3-Propanediol", "value":Propanediol},
                    #{"label": "Leflunomide", "value":Leflunomide},
                    #{"label": "Remdesivir", "value":Remdesivir},
                    #{"label": "Methly ethyl ketone", "value": Methyl_ethyl_ketone},
                    {"label": "Cubane", "value":Cubane},
                    {"label": "1,3,5-trimethylbenzene", "value":trimethylbenzene},
                    ]
                )
            ])
        ])
    ])



#2
@app.callback(
    Output("my-specoutput", "children"),
    Input("tab2-input", "value")
)
#1
@app.callback(
    Output("tab1-output", "children"),
    Input("tab1-input", "value")
)
#@app.callback(
 #   Output("my-NMRQ_output", "srcDoc"),
  #  Input("tab1_question_input","value")
#)
#3
@app.callback(
    Output("input", "value"),
    Input("tab3-input", "value")
)
@app.callback(
    Output("my-3D", "srcDoc"), Input("input", "value"), prevent_initial_call=True
)

@app.callback(
    Output("my-specoutput", "srcDoc"),
    Input("tab2-input", "value")
)

@app.callback(
    Output("my-Questions", "srcDoc"),
    Input("tab4-input", "value")
)
@app.callback(
    Output("my-googleDoc","srcDoc"),
    Input("input_3D_quiz","value")
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