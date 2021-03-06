from plotly.express import choropleth_mapbox
from json import load
from urllib.request import urlopen

with open(r"brazil-states.json") as file:
    BR = load(file)

with open(r'potencia-instalada.json') as file:
    df = load(file)

state_id_map = {}
for feature in BR["features"]:
    feature["id"] = feature["properties"]["name"]
    state_id_map[feature["properties"]["sigla"]] = feature["id"]

fig = choropleth_mapbox(
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