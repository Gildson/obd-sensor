import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

from matplotlib import pyplot as plt

#Criação do modelo de rede neural para uma regressão
              
obd_sensor = pd.read_csv('trackLog-2022-set-03_08-26-06.csv')

#Criar análise de vendas
                                            
#Criar dados geojson dos estados brasileiros
brazil_states = json.load(open("brazil_geo.json", "r"))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

colorscale = [
[0, 'rgb(38, 53, 113)'], 
[0.5, 'rgb(100, 127, 225)'],
[1, 'rgb(234, 32, 41)']
]
#Criando mapa da análise das vendas
fig = px.choropleth_mapbox(df12, locations="Estado", color="Quantidade",
                            center={"lat": -15.95, "lon": -46.78}, zoom=3,
                            geojson=brazil_states, color_continuous_scale=colorscale,
                            opacity=0.4, hover_data={"Preço_total":True, "Preço_min": True, "Preço_max": True,
                            "Preço_médio": True, "Frete_total": True, "Frete_médio": True, "Estado": True})
fig.update_layout(
    paper_bgcolor="#242424",
    autosize=True,
    margin=go.Margin(l=0, r=0, t=0, b=0),
    showlegend=False,
    mapbox_style="carto-darkmatter"
)