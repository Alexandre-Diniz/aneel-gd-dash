import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly as plt
import json
from urllib.request import urlopen
from map import fig
from layout import layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = layout

if __name__=="__main__":
    app.run_server(debug=False)