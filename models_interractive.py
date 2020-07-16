import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

import data as dt
from libs.useful_fcts import fig_creator_md_inter

country = "France"

### Défintion des paramètres ###

# Taux de croissance exponentielle.
r_log = 0.10786183  # modèle logistique
r_rich = 0.12764188  # modèle de Richards
# Coefficient du modèle de Richards.
alpha = 1.0732281
# Taux de transmission et taux de guérison par jours.
beta_SIR, gamma_SIR = 43.01327559046377, 42.96070458702876  # modèle SIR
beta_SEIR, sigma_SEIR, gamma_SEIR = 397.86333590847744, 49.17696647366713, 397.3828531005903  # modèle SEIR

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###

fig = fig_creator_md_inter(country, [r_log, r_rich, alpha, beta_SIR, gamma_SIR, beta_SEIR, sigma_SEIR, gamma_SEIR])

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig
    ),
    html.Div(id='EGR_log_value', style={'margin-top': 20}),
    dcc.Slider(
        id='EGR_log_slider',
        min=0.1,
        max=0.15,
        step=0.0001,
        marks={
            0.1: {'label': '0,1'},
            0.125: {'label': '0.125'},
            0.15: {'label': '0,15'}
        },
        value=r_log
    ),
    html.Div(id='EGR_rich_value', style={'margin-top': 20}),
    dcc.Slider(
        id='EGR_rich_slider',
        min=0.1,
        max=0.2,
        step=0.0001,
        marks={
            0.1: {'label': '0,1'},
            0.15: {'label': '0,15'},
            0.2: {'label': '0,2'}
        },
        value=r_rich
    ),
    html.Div(id='Rcoeff_value', style={'margin-top': 20}),
    dcc.Slider(
        id='Rcoeff_slider',
        min=0.5,
        max=1.5,
        step=0.0001,
        marks={
            0.5: {'label': '0,5'},
            1: {'label': '1'},
            1.5: {'label': '1,5'}
        },
        value=alpha
    ),
    html.Div(id='SIR_beta_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SIR_beta_slider',
        min=42,
        max=44,
        step=0.0001,
        marks={
            42: {'label': '42'},
            43: {'label': '43'},
            44: {'label': '44'}
        },
        value=beta_SIR
    ),
    html.Div(id='SIR_gamma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SIR_gamma_slider',
        min=42,
        max=44,
        step=0.0001,
        marks={
            42: {'label': '42'},
            43: {'label': '43'},
            44: {'label': '44'}
        },
        value=gamma_SIR
    ),
    html.Div(id='SEIR_beta_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_beta_slider',
        min=397,
        max=399,
        step=0.0001,
        marks={
            397: {'label': '397'},
            398: {'label': '398'},
            399: {'label': '399'}
        },
        value=beta_SEIR
    ),
    html.Div(id='SEIR_sigma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_sigma_slider',
        min=48,
        max=50,
        step=0.0001,
        marks={
            48: {'label': '48'},
            49: {'label': '49'},
            50: {'label': '50'}
        },
        value=sigma_SEIR
    ),
    html.Div(id='SEIR_gamma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_gamma_slider',
        min=396,
        max=398,
        step=0.0001,
        marks={
            396: {'label': '396'},
            397: {'label': '397'},
            398: {'label': '398'}
        },
        value=gamma_SEIR
    )
])


### Mise à jour de la figure ###

@app.callback(Output('EGR_log_value', 'children'),
              [Input('EGR_log_slider', 'value')])
def EGR_value(EGR_log):
    return 'Taux de croissance exponentielle du modèle logistique : ', EGR_log


@app.callback(Output('EGR_rich_value', 'children'),
              [Input('EGR_rich_slider', 'value')])
def EGR_value(EGR_rich):
    return 'Taux de croissance exponentielle du modèle de Richards : ', EGR_rich


@app.callback(Output('Rcoeff_value', 'children'),
              [Input('Rcoeff_slider', 'value')])
def Rcoeff_value(Rcoeff):
    return 'Coefficient du modèle de Richards : ', Rcoeff


@app.callback(Output('SIR_beta_value', 'children'),
              [Input('SIR_beta_slider', 'value')])
def beta_value(b_SIR):
    return 'Taux de transmission par individu infecté du modèle SIR : ', b_SIR


@app.callback(Output('SIR_gamma_value', 'children'),
              [Input('SIR_gamma_slider', 'value')])
def gamma_value(g_SIR):
    return 'Taux de guérison du modèle SIR : ', g_SIR


@app.callback(Output('SEIR_beta_value', 'children'),
              [Input('SEIR_beta_slider', 'value')])
def beta_value(b_SEIR):
    return 'Taux de transmission par individu infecté du modèle SEIR : ', b_SEIR


@app.callback(Output('SEIR_sigma_value', 'children'),
              [Input('SEIR_sigma_slider', 'value')])
def sigma_value(s_SEIR):
    return 'Taux d\'individus devenant transmetteur du modèle SEIR : ', s_SEIR


@app.callback(Output('SEIR_gamma_value', 'children'),
              [Input('SEIR_gamma_slider', 'value')])
def gamma_value(g_SEIR):
    return 'Taux de guérison du modèle SEIR : ', g_SEIR


@app.callback(
    Output('graph', 'figure'),
    [Input('EGR_log_slider', 'value'),
     Input('EGR_rich_slider', 'value'),
     Input('Rcoeff_slider', 'value'),
     Input('SIR_beta_slider', 'value'),
     Input('SIR_gamma_slider', 'value'),
     Input('SEIR_beta_slider', 'value'),
     Input('SEIR_sigma_slider', 'value'),
     Input('SEIR_gamma_slider', 'value')])
def update_graph(EGR_log, EGR_rich, Rcoeff, b_SIR, g_SIR, b_SEIR, s_SEIR, g_SEIR):
    new_fig = fig_creator_md_inter(country, [EGR_log, EGR_rich, Rcoeff, b_SIR, g_SIR, b_SEIR, s_SEIR, g_SEIR])
    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)

"""
Exécution du programme :
- Rentrer dans le terminal : python models_interractive.py
- Cliquer sur le lien
"""
