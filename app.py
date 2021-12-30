from datetime import date
import math
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
import warnings
import pandas as pd
warnings.filterwarnings('ignore')


frame_style = {'backgroundColor': '#B8D9F4', "padding": "4px"}


def radiobutton(id):
    button = dbc.RadioItems(
        id=f"{id}",
        options=[
            {"label": "DONE", "value": 2},
            {"label": "ABSENT", "value": 1},
            {"label": "-", "value": 0}
        ],
        inline=True,
        value=0,
        labelStyle={'display': 'inline-block'}
    )
    return button


def result_boxy(i):
    return dbc.Card(
        html.Div(id=f'style{i}')
    )


def boxes(i):
    return dbc.Col(dbc.Card([
        radiobutton(f'name{i}'),
        result_boxy(str(i))
    ], style=frame_style))


def automize(i, k):
    return dbc.CardBody([
        dbc.Row([
            boxes(i) for i in range((i*k)+1, (i+1)*k+1)
        ])
    ], style={'backgroundColor': '#232323', 'margin-bottom': '-15px'})


k = 4

p1Layout = html.Div(
    [automize(i, k) for i in range(math.ceil(21/k))], style={'background-color': '#FFFFFF'})


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = p1Layout


names = pd.read_excel('names.xlsx')
NAMES = names['NAMES']


def color_status(status, name):
    if (status == 0):
        color = '#F6AE2D'
    elif (status == 1):
        color = "#FF2222"
    else:
        color = "#22FF22"
    result = dbc.CardBody([
        html.H2(f"{name}")
    ], style={'backgroundColor': f'{color}'})
    return result


yellow = {'backgroundColor': '#66FF44'}
green = {'backgroundColor': '#22FF22'}
red = {'backgroundColor': '#FF2222'}


@app.callback([Output(f'style{str(i+1)}', 'children') for i in range(21)],
              [Input(f'name{str(i+1)}', 'value') for i in range(21)])
def booknames_by_auhor(names1, names2, names3, names4, names5, names6, names7, names8, names9,
                       names10, names11, names12, names13, names14, names15, names16, names17,
                       names18, names19, names20, names21):
    print(names1, names2, names3)
    return color_status(names1, NAMES[1]), color_status(names2, NAMES[2]), color_status(names3, NAMES[3]), color_status(names4, NAMES[4]), color_status(names5, NAMES[5]), color_status(names6, NAMES[6]),            color_status(names7, NAMES[7]), color_status(names8, NAMES[8]), color_status(names9, NAMES[9]), color_status(names10, NAMES[10]), color_status(names11, NAMES[11]), color_status(names12, NAMES[12]),            color_status(names13, NAMES[13]), color_status(names14, NAMES[14]), color_status(names15, NAMES[15]), color_status(names16, NAMES[16]), color_status(names17, NAMES[17]), color_status(names18, NAMES[18]),            color_status(names19, NAMES[19]), color_status(names20, NAMES[20]), color_status(names21, NAMES[21])


if __name__ == "__main__":
    # app.run_server(debug=True, port=1111)
    app.run_server(debug=True, port=8050, host="0.0.0.0")
