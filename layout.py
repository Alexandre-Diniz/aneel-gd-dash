import dash_core_components as dcc
import dash_html_components as html

from map import fig

layout = html.Div(children=[
    html.H3(children="A Dash Application"),
    html.Div(children="Os dados utilizados foram obtidos dos dados públicos disponilizados pela ANEEL para Geração Distribuída."),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])