import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import sqlite3

import plotly.graph_objs as go

import os
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'DataBase\wine_data.sqlite')
conn = sqlite3.connect(filename)
c = conn.cursor()

df = pd.read_sql("Select * from wine_data", conn)
df = df[['country', 'description', 'rating', 
'price', 'province', 'title', 
'variety', 'winery', 'color']]

print(df.head(1))
