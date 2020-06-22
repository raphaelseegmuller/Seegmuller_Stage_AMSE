import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from scipy.integrate import odeint
import pandas as pd
from libs.models import *

import data as dt


### Fonctions ###

# Les équations différentielles du modèle SIR.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


### Défintion des paramètres ###

# Nombre initial d'infectés.
C0 = 2
# Nombre cumulatif final d'infectés.
K = 189670
# Taux de croissance exponentielle.
r_log = 0.15011031  # modèle logistique
r_rich = 0.17434972 # modèle de Richards
# Intervalles de temps.
t = np.arange(0, len(dt.Time), 1)
t1 = np.arange(2, len(dt.Time), 1)
# Coefficient du modèle de Richards.
alpha1 = 1.06988692
# Population totale.
N = 64081000
# Nombre initial d'individus infectés et guéris.
I0, R0 = 2, 0
# Nombre d'individu susceptibles d'attrapper la maladie.
S0 = N - I0 - R0
# Taux de transmission et taux de guérison par jours.
beta, gamma = 9.13370681, 9.01266501


# Nombre cumulé d'infectés.
C1 = logistique(C0, K, r_log, t1)  # modèle logistique
C2 = richards(C0, K, r_rich, t1, alpha1)  # modèle de Richards
C3 = SIR(S0, I0, R0, t1, N, beta, gamma)    # modèle SIR


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
            0.2: {'label': '0,2'}
        },
        value=0.15011031
    ),
    html.Div(id='EGR_rich_value', style={'margin-top': 20}),
    dcc.Slider(
        id='EGR_rich_slider',
        min=0.1,
        max=0.2,
        step=0.0001,
        marks={
            0.1: {'label': '0,1'},
            0.2: {'label': '0,2'}
        },
        value=0.17434972
    ),
    html.Div(id='Rcoeff_value', style={'margin-top': 20}),
    dcc.Slider(
        id='Rcoeff_slider',
        min=0.5,
        max=1.5,
        step=0.0001,
        marks={
            0.5: {'label': '0.5'},
            1: {'label': '1'},
            1.5: {'label': '1.5'}
        },
        value=1.06988692
    ),
    html.Div(id='beta_value', style={'margin-top': 20}),
    dcc.Slider(
        id='beta_slider',
        min=9,
        max=9.2,
        step=0.0001,
        marks={
            9: {'label': '9'},
            9.2: {'label': '9,2'}
        },
        value=9.13370681
    ),
    html.Div(id='gamma_value', style={'margin-top': 20}),
    dcc.Slider(
        id='gamma_slider',
        min=8.9,
        max=9.1,
        step=0.0001,
        marks={
            8.9: {'label': '8,9'},
            9: {'label': '9'},
            9.1: {'label': '9,1'}
        },
        value=9.01266501
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


@app.callback(Output('beta_value', 'children'),
              [Input('beta_slider', 'value')])
def beta_value(b):
    return 'Taux de transmission par individu infecté : ', b


@app.callback(Output('gamma_value', 'children'),
              [Input('gamma_slider', 'value')])
def gamma_value(g):
    return 'Taux de guérison : ', g


@app.callback(
    Output('graph', 'figure'),
    [Input('EGR_log_slider', 'value'),
     Input('EGR_rich_slider', 'value'),
     Input('Rcoeff_slider', 'value'),
     Input('beta_slider', 'value'),
     Input('gamma_slider', 'value')])
def update_graph(EGR_log, EGR_rich, Rcoeff, b, g):
    # Nombre cumulé d'infectés.
    C1 = logistique(C0, K, EGR_log, t1)  # modèle logistique
    C2 = richards(C0, K, EGR_rich, t, Rcoeff)  # modèle de Richards
    C3 = SIR(S0, I0, R0, t1, N, b, g)  # modèle SIR


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

    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)

"""
Exécution du programme :
- Rentrer dans le terminal : python models_interractive.py
- Cliquer sur le lien
"""
