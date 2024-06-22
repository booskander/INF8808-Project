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
import bubble.chart as bubble
import field.chart as field
import field.preprocess as field_preprocess
from dash.dependencies import Input, Output, State
from bubble.template import create_template
app = dash.Dash(__name__)
app.title = 'SportsAI Project'

# Load the data
df_match_stats = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Match Stats')
df_player_stats = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Players stats')
df_Line_ups = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Line-ups')

df_viz_1 = preprocess.preprocess_data(df_match_stats,df_player_stats)
# create_template()
figure = bubble.init_figure()
field_figure = field.init_figure()

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
    html.Button('Click me', id='button'),
    dcc.Graph(
        id='bubble-chart',
        figure=figure 
    ),
    html.Button('Click not me', id='buttonField'),
    dcc.Graph(
        id='field-chart',
        figure=figure
    )
])

# Define the callback to update the bubble chart
@app.callback(
    Output('bubble-chart', 'figure'),
    [Input('button', 'n_clicks')],
    [State('bubble-chart', 'figure')]
)

def on_update(n_clicks, figure):
    # Update the figure based on some interaction
    figure = bubble.make_bubble_chart(df_viz_1)
    figure.show()
    return figure, f'Mode: {n_clicks}'

@app.callback(
    Output('field-chart', 'field_figure'),
    [Input('buttonField', 'n_clicks')],
    [State('field-chart', 'field_figure')]
)

def on_update_field_figure(n_clicks, figure):
    # Update the figure based on some interaction
    players_data = field_preprocess.get_italian_players_positions(df_Line_ups)
    filtered_players = field_preprocess.get_filter_italian_final_players(df_Line_ups)
    player_names = filtered_players['OfficialSurname'].tolist()
    player_stats = field_preprocess.get_italian_players_stats(df_player_stats, player_names)
    figure = field.make_field_chart(players_data, player_stats)
    figure.show()
    return figure, f'Mode: {n_clicks}'

server = app.server
