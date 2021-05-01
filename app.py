from dash import Dash
from flask import Flask
from layout import layout
from flask_caching import Cache

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = Dash(__name__, external_stylesheets=external_stylesheets, server=server)

cache = Cache(server, config={
    "CACHE_TYPE":"filesystem",
    "CACHE_DIR":"cache-directory"
})

app.layout = layout


if __name__=="__main__":
    server.run(port=8050)