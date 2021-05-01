import pandas as pd
import dash
import plotly.express as px
import plotly as plt
import json
from urllib.request import urlopen

with urlopen("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson") as response:
    BR = json.load(response)

file = 'PotenciaInstaladaPorEstadoPorAno.csv'
df = pd.read_csv(file, encoding='utf-8')

state_id_map = {}
for feature in BR["features"]:
    feature["id"] = feature["properties"]["name"]
    state_id_map[feature["properties"]["sigla"]] = feature["id"]

fig = px.choropleth_mapbox(
    df,
    locations="Estado",
    geojson=BR,
    color="mdaPotenciaInstaladakW",
    hover_name="Estado",
    #hover_data=["mdaPotenciaInstaladakW","longitude","latitude"],
    title="Potência Instalada - Geração Fotovoltaica",
    animation_frame="anoReferencia",
    mapbox_style = "carto-positron",
    center={"lat":-14, "lon": -55},
    zoom = 2,
    opacity=0.5,
    labels={
        "mdaPotenciaInstaladakW":"Potência Instalada",
        "anoReferencia":"Ano"
    },
    height=600
)