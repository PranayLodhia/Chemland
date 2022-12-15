from dash import Dash, dcc
from sympy import symbols, Eq
app = Dash(__name__)


app.layout = dcc.Markdown('''

    # Spectroscopy main ideas and revision points:
    
    
    ## This is an <h2> tag

    ###### This is an <h6> tag
''')


if __name__ == '__main__':
    app.run_server(debug=True)