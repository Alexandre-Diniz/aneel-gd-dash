from dash import Dash
from flask import Flask
from layout import layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.layout = layout


if __name__=="__main__":
    server.run(port=8050)