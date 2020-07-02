import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import pandas as pd

import data as dt
from libs.models import logistique, richards, SIR, SEIR

### Défintion des paramètres ###

# Nombre initial d'infectés.
C0 = 2
# Nombre cumulatif final d'infectés.
K = 189670
# Taux de croissance exponentielle.
r_log = 0.14628805  # modèle logistique
r_rich = 0.16942401  # modèle de Richards
# Intervalles de temps.
t = np.arange(0, len(dt.Time), 1)
t1 = np.arange(2, len(dt.Time), 1)
# Coefficient du modèle de Richards.
alpha1 = 1.0685873
# Population totale.
N = 64081000
# Nombre initial d'individus infectés, infectieux et guéris.
E0, I0, R0 = 0, 2, 0
# Nombre d'individu susceptibles d'attrapper la maladie.
S0 = N - E0 - I0 - R0
# Taux de transmission et taux de guérison par jours.
beta_SIR, gamma_SIR = 9.24884336, 9.12660313  # modèle SIR
beta_SEIR, sigma_SEIR, gamma_SEIR = 44.3754473, 2.75653902, 41.72852292  # modèle SEIR

# Nombre cumulé d'infectés.
C1 = logistique(C0, K, r_log, t1)  # modèle logistique
C2 = richards(C0, K, r_rich, t1, alpha1)  # modèle de Richards
C3 = SIR(S0, I0, R0, t1, N, beta_SIR, gamma_SIR)  # modèle SIR
C4 = SEIR(S0, E0, I0, R0, t1, N, beta_SEIR, sigma_SEIR, gamma_SEIR)  # modèle SEIR

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###

fig = make_subplots(rows=1, cols=1)
fig.update_layout(
    title={
        'text': "COVID 19 France",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_size=30)

fig.add_scatter(
    x=dt.Time,
    y=dt.France_C, name="Données France")

fig.add_scatter(
    x=dt.Time[2:],
    y=C1, name="Modèle logistique")

fig.add_scatter(
    x=dt.Time[2:],
    y=C2, name="Modèle de Richards")

fig.add_scatter(
    x=dt.Time[2:],
    y=C3, name="Modèle SIR")

fig.add_scatter(
    x=dt.Time[2:],
    y=C4, name="Modèle SEIR")

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig
    ),
    html.Div(id='EGR_log_value', style={'margin-top': 20}),
    dcc.Slider(
        id='EGR_log_slider',
        min=0.1,
        max=0.2,
        step=0.0001,
        marks={
            0.1: {'label': '0,1'},
            0.15: {'label': '0,15'},
            0.2: {'label': '0,2'}
        },
        value=0.14628805
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
        value=0.16942401
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
        value=1.0685873
    ),
    html.Div(id='SIR_beta_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SIR_beta_slider',
        min=9,
        max=9.2,
        step=0.0001,
        marks={
            9: {'label': '9'},
            9.1: {'label': '9,1'},
            9.2: {'label': '9,2'}
        },
        value=9.13370681
    ),
    html.Div(id='SIR_gamma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SIR_gamma_slider',
        min=8.9,
        max=9.1,
        step=0.0001,
        marks={
            8.9: {'label': '8,9'},
            9: {'label': '9'},
            9.1: {'label': '9,1'}
        },
        value=9.01266501
    ),
    html.Div(id='SEIR_beta_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_beta_slider',
        min=43,
        max=46,
        step=0.0001,
        marks={
            43: {'label': '43'},
            44: {'label': '44'},
            45: {'label': '45'},
            46: {'label': '46'}
        },
        value=44.37642256
    ),
    html.Div(id='SEIR_sigma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_sigma_slider',
        min=2,
        max=4,
        step=0.0001,
        marks={
            2: {'label': '2'},
            3: {'label': '3'},
            4: {'label': '4'}
        },
        value=2.74638698
    ),
    html.Div(id='SEIR_gamma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='SEIR_gamma_slider',
        min=40,
        max=43,
        step=0.0001,
        marks={
            40: {'label': '40'},
            41: {'label': '41'},
            42: {'label': '42'},
            43: {'label': '43'}
        },
        value=41.72459742
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
    # Nombre cumulé d'infectés.
    C1 = logistique(C0, K, EGR_log, t1)  # modèle logistique
    C2 = richards(C0, K, EGR_rich, t1, Rcoeff)  # modèle de Richards
    C3 = SIR(S0, I0, R0, t1, N, b_SIR, g_SIR)  # modèle SIR
    C4 = SEIR(S0, E0, I0, R0, t1, N, b_SEIR, s_SEIR, g_SEIR)  # modèle SEIR

    new_fig = make_subplots(rows=1, cols=1)
    new_fig.update_layout(
        title={
            'text': "Nombre cumulatif d'infectés du COVID 19",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30)

    new_fig.add_scatter(
        x=dt.Time,
        y=dt.France_C, name="Données France")

    new_fig.add_scatter(
        x=dt.Time[2:],
        y=C1, name="Modèle logistique")

    new_fig.add_scatter(
        x=dt.Time[2:],
        y=C2, name="Modèle de Richards")

    new_fig.add_scatter(
        x=dt.Time[2:],
        y=C3, name="Modèle SIR")

    new_fig.add_scatter(
        x=dt.Time[2:],
        y=C4, name="Modèle SEIR")

    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)

"""
Exécution du programme :
- Rentrer dans le terminal : python models_interractive.py
- Cliquer sur le lien
"""
