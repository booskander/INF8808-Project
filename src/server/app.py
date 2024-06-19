# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Noe Jager
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''


import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import bubble.preprocess as preprocess


app = dash.Dash(__name__)
app.title = 'SportsAI Project'
df_match_stats = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Match Stats')
df_player_stats = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Players stats')
df_viz_1 = preprocess.preprocess_data(df_match_stats,df_player_stats)
app.layout = html.Div([
    html.H1('Welcome to the SportsAI Project!'),
    html.H2('This is the home page of the project.'),
    html.P('Please navigate to the other pages to see the content.'),
    dcc.Link('Go to the NBA page', href='/nba'),
    html.Br(),
    dcc.Link('Go to the NHL page', href='/nhl'),
    html.Br(),
    dcc.Link('Go to the NFL page', href='/nfl'),
    html.Br(),
    dcc.Link('Go to the MLB page', href='/mlb'),
    html.Br(),
    dcc.Link('Go to the MLS page', href='/mls'),
])
server = app.server