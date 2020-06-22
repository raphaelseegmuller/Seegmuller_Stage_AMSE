import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
import pandas as pd

import data as dt
import OxCGRT_definition as oxd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###

fig = make_subplots(rows=1, cols=1)
fig.update_layout(
    title={
        'text': "OxCGRT - COVID 19 France",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_size=30)

fig.add_scatter(
    x=dt.Time_ext,
    y=oxd.France_GR, name="Government response index - France")

fig.add_scatter(
    x=dt.Time_ext,
    y=oxd.France_CH, name="Containment and health index - France")

fig.add_scatter(
    x=dt.Time_ext,
    y=oxd.France_S, name="Stringency index - France")

fig.add_scatter(
    x=dt.Time_ext,
    y=oxd.France_ES, name="Economic support index - France")

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
