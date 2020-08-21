import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from libs.useful_fcts import fig_creator_death_comparator

days_around = 30

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig_creator_death_comparator(["France"], 'Non', 'Non', days_around)
    ),
    html.Div(id='Country_value', style={'margin-top': 20}),
    dcc.Dropdown(
        id='Country_choice',
        options=[
            # {'label': 'Afghanistan', 'value': 'Afghanistan'},
            # {'label': 'Afrique du Sud', 'value': 'Afrique du Sud'},
            # {'label': 'Albanie', 'value': 'Albanie'},
            # {'label': 'Algérie', 'value': 'Algérie'},
            {'label': 'Allemagne', 'value': 'Allemagne'},
            # {'label': 'Andorre', 'value': 'Andorre'},
            # {'label': 'Angola', 'value': 'Angola'},
            # {'label': 'Arabie sahoudite', 'value': 'Arabie sahoudite'},
            # {'label': 'Argentine', 'value': 'Argentine'},
            # {'label': 'Aruba', 'value': 'Aruba'},
            # {'label': 'Australie', 'value': 'Australie'},
            {'label': 'Autriche', 'value': 'Autriche'},
            # {'label': 'Azerbaïdjan', 'value': 'Azerbaïdjan'},
            # {'label': 'Bangladesh', 'value': 'Bangladesh'},
            # {'label': 'Barbades', 'value': 'Barbades'},
            # {'label': 'Barheïn', 'value': 'Barheïn'},
            {'label': 'Belgique', 'value': 'Belgique'},
            # {'label': 'Belize', 'value': 'Belize'},
            # {'label': 'Bénin', 'value': 'Bénin'},
            # {'label': 'Bermudes', 'value': 'Bermudes'},
            # {'label': 'Bhoutan', 'value': 'Bhoutan'},
            # {'label': 'Biélorussie', 'value': 'Biélorussie'},
            # {'label': 'Birmanie', 'value': 'Birmanie'},
            # {'label': 'Bolivie', 'value': 'Bolivie'},
            # {'label': 'Bosnie-Herzégovine', 'value': 'Bosnie-Herzégovine'},
            # {'label': 'Botswana', 'value': 'Botswana'},
            # {'label': 'Brésil', 'value': 'Brésil'},
            # {'label': 'Brunei', 'value': 'Brunei'},
            # {'label': 'Bulgarie', 'value': 'Bulgarie'},
            # {'label': 'Burkina Faso', 'value': 'Burkina Faso'},
            # {'label': 'Burundi', 'value': 'Burundi'},
            # {'label': 'Cambodge', 'value': 'Cambodge'},
            # {'label': 'Cameroun', 'value': 'Cameroun'},
            # {'label': 'Canada', 'value': 'Canada'},
            # {'label': 'Cap-Vert', 'value': 'Cap-Vert'},
            # {'label': 'Chili', 'value': 'Chili'},
            # {'label': 'Chine', 'value': 'Chine'},
            # {'label': 'Chypre', 'value': 'Chypre'},
            # {'label': 'Colombie', 'value': 'Colombie'},
            # {'label': 'Congo', 'value': 'Congo'},
            # {'label': 'Corée du Sud', 'value': 'Corée du Sud'},
            # {'label': 'Costa Rica', 'value': 'Costa Rica'},
            # {'label': 'Côte d\'Ivoire', 'value': 'Côte d\'Ivoire'},
            # {'label': 'Croatie', 'value': 'Croatie'},
            # {'label': 'Cuba', 'value': 'Cuba'},
            {'label': 'Danemark', 'value': 'Danemark'},
            # {'label': 'Djibouti', 'value': 'Djibouti'},
            # {'label': 'Dominique', 'value': 'Dominique'},
            # {'label': 'Égypte', 'value': 'Égypte'},
            # {'label': 'Émirats arabes unis', 'value': 'Émirats arabes unis'},
            # {'label': 'Équateur', 'value': 'Équateur'},
            # {'label': 'Érythrée', 'value': 'Érythrée'},
            {'label': 'Espagne', 'value': 'Espagne'},
            # {'label': 'Estonie', 'value': 'Estonie'},
            # {'label': 'Eswatini', 'value': 'Eswatini'},
            # {'label': 'États-Unis', 'value': 'États-Unis'},
            # {'label': 'Éthiopie', 'value': 'Éthiopie'},
            # {'label': 'Fidji', 'value': 'Fidji'},
            # {'label': 'Finlande', 'value': 'Finlande'},
            {'label': 'France', 'value': 'France'},
            # {'label': 'France2', 'value': 'France2'},
            # {'label': 'Gabon', 'value': 'Gabon'},
            # {'label': 'Gambie', 'value': 'Gambie'},
            # {'label': 'Géorgie', 'value': 'Géorgie'},
            # {'label': 'Ghana', 'value': 'Ghana'},
            # {'label': 'Gibraltar', 'value': 'Gibraltar'},
            # {'label': 'Grèce', 'value': 'Grèce'},
            # {'label': 'Groenland', 'value': 'Groenland'},
            # {'label': 'Guam', 'value': 'Guam'},
            # {'label': 'Guatemala', 'value': 'Guatemala'},
            # {'label': 'Guinée', 'value': 'Guinée'},
            # {'label': 'Guyana', 'value': 'Guyana'},
            # {'label': 'Haïti', 'value': 'Haïti'},
            # {'label': 'Honduras', 'value': 'Honduras'},
            # {'label': 'Hong Kong', 'value': 'Hong Kong'},
            # {'label': 'Hongrie', 'value': 'Hongrie'},
            # {'label': 'Îles Salomon', 'value': 'Îles Salomon'},
            # {'label': 'Inde', 'value': 'Inde'},
            # {'label': 'Indonésie', 'value': 'Indonésie'},
            # {'label': 'Irak', 'value': 'Irak'},
            # {'label': 'Iran', 'value': 'Iran'},
            # {'label': 'Irlande', 'value': 'Irlande'},
            {'label': 'Islande', 'value': 'Islande'},
            # {'label': 'Israël', 'value': 'Israël'},
            {'label': 'Italie', 'value': 'Italie'},
            # {'label': 'Jamaïque', 'value': 'Jamaïque'},
            # {'label': 'Japon', 'value': 'Japon'},
            # {'label': 'Jordanie', 'value': 'Jordanie'},
            # {'label': 'Kazakhstan', 'value': 'Kazakhstan'},
            # {'label': 'Kenya', 'value': 'Kenya'},
            # {'label': 'Kirghizistan', 'value': 'Kirghizistan'},
            # {'label': 'Kosovo', 'value': 'Kosovo'},
            # {'label': 'Koweït', 'value': 'Koweït'},
            # {'label': 'Laos', 'value': 'Laos'},
            # {'label': 'Lesotho', 'value': 'Lesotho'},
            # {'label': 'Lettonie', 'value': 'Lettonie'},
            # {'label': 'Liban', 'value': 'Liban'},
            # {'label': 'Libéria', 'value': 'Libéria'},
            # {'label': 'Libye', 'value': 'Libye'},
            # {'label': 'Lituanie', 'value': 'Lituanie'},
            # {'label': 'Luxembourg', 'value': 'Luxembourg'},
            # {'label': 'Macao', 'value': 'Macao'},
            # {'label': 'Madagascar', 'value': 'Madagascar'},
            # {'label': 'Malaisie', 'value': 'Malaisie'},
            # {'label': 'Malawi', 'value': 'Malawi'},
            # {'label': 'Mali', 'value': 'Mali'},
            # {'label': 'Maroc', 'value': 'Maroc'},
            # {'label': 'Maurice', 'value': 'Maurice'},
            # {'label': 'Mauritanie', 'value': 'Mauritanie'},
            # {'label': 'Mexique', 'value': 'Mexique'},
            # {'label': 'Moldavie', 'value': 'Moldavie'},
            # {'label': 'Mongolie', 'value': 'Mongolie'},
            # {'label': 'Mozambique', 'value': 'Mozambique'},
            # {'label': 'Namibie', 'value': 'Namibie'},
            # {'label': 'Népal', 'value': 'Népal'},
            # {'label': 'Nicaragua', 'value': 'Nicaragua'},
            # {'label': 'Niger', 'value': 'Niger'},
            # {'label': 'Nigéria', 'value': 'Nigéria'},
            # {'label': 'Norvège', 'value': 'Norvège'},
            # {'label': 'Nouvelle-Zélande', 'value': 'Nouvelle-Zélande'},
            # {'label': 'Oman', 'value': 'Oman'},
            # {'label': 'Ouganda', 'value': 'Ouganda'},
            # {'label': 'Ouzbékistan', 'value': 'Ouzbékistan'},
            # {'label': 'Pakistan', 'value': 'Pakistan'},
            # {'label': 'Palestine', 'value': 'Palestine'},
            # {'label': 'Panama', 'value': 'Panama'},
            # {'label': 'Papouasie-Nouvelle-Guinée', 'value': 'Papouasie-Nouvelle-Guinée'},
            # {'label': 'Paraguay', 'value': 'Paraguay'},
            {'label': 'Pays-Bas', 'value': 'Pays-Bas'},
            # {'label': 'Pérou', 'value': 'Pérou'},
            # {'label': 'Philippines', 'value': 'Philippines'},
            # {'label': 'Pologne', 'value': 'Pologne'},
            # {'label': 'Porto Rico', 'value': 'Porto Rico'},
            # {'label': 'Portugal', 'value': 'Portugal'},
            # {'label': 'Qatar', 'value': 'Qatar'},
            # {'label': 'République centrafricaine', 'value': 'République centrafricaine'},
            # {'label': 'République démocratique du Congo', 'value': 'République démocratique du Congo'},
            # {'label': 'République dominicaine', 'value': 'République dominicaine'},
            # {'label': 'Roumanie', 'value': 'Roumanie'},
            {'label': 'Royaume-Uni', 'value': 'Royaume-Uni'},
            # {'label': 'Russie', 'value': 'Russie'},
            # {'label': 'Rwanda', 'value': 'Rwanda'},
            # {'label': 'Saint-Marin', 'value': 'Saint-Marin'},
            # {'label': 'Salvador', 'value': 'Salvador'},
            # {'label': 'Sénégal', 'value': 'Sénégal'},
            # {'label': 'Serbie', 'value': 'Serbie'},
            # {'label': 'Seychelles', 'value': 'Seychelles'},
            # {'label': 'Sierra Leone', 'value': 'Sierra Leone'},
            # {'label': 'Singapour', 'value': 'Singapour'},
            # {'label': 'Slovaquie', 'value': 'Slovaquie'},
            # {'label': 'Slovénie', 'value': 'Slovénie'},
            # {'label': 'Somalie', 'value': 'Somalie'},
            # {'label': 'Soudan', 'value': 'Soudan'},
            # {'label': 'Soudan du Sud', 'value': 'Soudan du Sud'},
            # {'label': 'Sri Lanka', 'value': 'Sri Lanka'},
            {'label': 'Suède', 'value': 'Suède'},
            {'label': 'Suisse', 'value': 'Suisse'},
            # {'label': 'Suriname', 'value': 'Suriname'},
            # {'label': 'Syrie', 'value': 'Syrie'},
            # {'label': 'Taiwan', 'value': 'Taiwan'},
            # {'label': 'Tajikistan', 'value': 'Tajikistan'},
            # {'label': 'Tanzanie', 'value': 'Tanzanie'},
            # {'label': 'Tchad', 'value': 'Tchad'},
            # {'label': 'Tchéquie', 'value': 'Tchéquie'},
            # {'label': 'Thaïlande', 'value': 'Thaïlande'},
            # {'label': 'Timor oriental', 'value': 'Timor oriental'},
            # {'label': 'Togo', 'value': 'Togo'},
            # {'label': 'Trinité-et-Tobago', 'value': 'Trinité-et-Tobago'},
            # {'label': 'Tunisie', 'value': 'Tunisie'},
            # {'label': 'Turkmenistan', 'value': 'Turkmenistan'},
            # {'label': 'Turquie', 'value': 'Turquie'},
            # {'label': 'Ukraine', 'value': 'Ukraine'},
            # {'label': 'Uruguay', 'value': 'Uruguay'},
            # {'label': 'Vanuatu', 'value': 'Vanuatu'},
            # {'label': 'Vénézuela', 'value': 'Vénézuela'},
            # {'label': 'Viêt Nam', 'value': 'Viêt Nam'},
            # {'label': 'Yémen', 'value': 'Yémen'},
            # {'label': 'Zambie', 'value': 'Zambie'},
            # {'label': 'Zimbabwe', 'value': 'Zimbabwe'}
        ],
        value=["Allemagne", "Autriche", "Belgique", "Danemark", "Espagne", "France", "Islande", "Italie", "Pays-Bas",
               "Royaume-Uni", "Suède", "Suisse"],
        multi=True
    ),
    html.Div(id='Normalize_value', style={'margin-top': 20}),
    dcc.Dropdown(
        id='Normalize_choice',
        options=[
            {'label': 'Oui', 'value': 'Oui'},
            {'label': 'Non', 'value': 'Non'}
        ],
        value='Oui'
    ),
    html.Div(id='Normalize2_value', style={'margin-top': 20}),
    dcc.Dropdown(
        id='Normalize2_choice',
        options=[
            {'label': 'Oui', 'value': 'Oui'},
            {'label': 'Non', 'value': 'Non'}
        ],
        value='Non'
    )
])


### Mise à jour de la figure ###

@app.callback(Output('Country_value', 'children'),
              [Input('Country_choice', 'value')])
def country(name):
    return 'Pays : '


@app.callback(Output('Normalize_value', 'children'),
              [Input('Normalize_choice', 'value')])
def country(answer):
    return 'Normaliser ? : '


@app.callback(Output('Normalize2_value', 'children'),
              [Input('Normalize2_choice', 'value')])
def country(answer):
    return 'Normaliser 2 ? : '


@app.callback(
    Output('graph', 'figure'),
    [Input('Country_choice', 'value'),
     Input('Normalize_choice', 'value'),
     Input('Normalize2_choice', 'value')])
def update_graph(name_list, normalize, normalize2):
    return fig_creator_death_comparator(name_list, normalize, normalize2, days_around)


if __name__ == '__main__':
    app.run_server(debug=True)
