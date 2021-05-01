from dash import Dash
from flask import Flask
from layout import layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.run_server

app.layout = layout


if __name__=="__main__":
    server(debug=False,port=8050)