import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd 
import sqlite3

import os
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, '..\DataBase\wine_data.sqlite')
conn = sqlite3.connect(filename)
c = conn.cursor()

df = pd.read_sql("Select * from wine_data", conn)
df = df[['country', 'description', 'rating',
        'price', 'province', 'title', 
        'variety', 'winery', 'color']]