import pandas as pd
import plotly.io as pio
from flask import Flask, send_from_directory, jsonify, request
from bubble import preprocess as bubble_preprocess
from bubble import chart as bubble_chart
from field import chart as field_chart
from field import preprocess as field_preprocess
from field import chart as field_chart
from tournament import chart as tournament_chart
import dash_core_components as dcc
import dash_html_components as html
import dash
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

import tournament.chart
server = Flask(__name__)

""" Bubble chart """
df_match_stats = pd.read_excel(
    './assets/EURO_2020_DATA.xlsx', sheet_name='Match Stats')
df_player_stats = pd.read_excel(
    './assets/EURO_2020_DATA.xlsx', sheet_name='Players stats')
df_viz_1 = bubble_preprocess.preprocess_data(df_match_stats, df_player_stats)
df_lineups = pd.read_excel(
    "./assets/EURO_2020_DATA.xlsx", sheet_name="Line-ups")


bubble_graph = bubble_chart.make_bubble_chart(df_viz_1)

""" Field chart """

def get_field_chart(team, opposite_team):
    if team is None:
        team = 'Italy'
    if opposite_team is None:
        opposite_team = 'England'
    players_data = field_preprocess.get_italian_players_positions(df_lineups, team, opposite_team)
    players = field_preprocess.get_filter_italian_final_players(df_lineups, team, opposite_team)
    players_names = players['OfficialSurname'].tolist()
    players_stats = field_preprocess.get_italian_players_stats(
        df_player_stats, players_names, team, opposite_team)

    field_graph = field_chart.make_field_chart(players_data, players_stats)
    return field_graph

""" Tournament chart """
tournament_figure = tournament_chart.get_figure()



def to_html(component):
    return pio.to_html(component, full_html=False, include_plotlyjs='cdn')


@server.route('/pages/vis-1/bubble')
def serve_bubble():
    html = to_html(bubble_graph)
    return jsonify(dict(bubble_graph=html))


@server.route('/pages/vis-2/field')
def serve_field():
    team = request.args.get('team', 'Italy')
    opposite_team = request.args.get('opposite_team', 'England')
    field_graph = get_field_chart(team, opposite_team)
    html = to_html(field_graph)
    return jsonify(dict(field_graph=html))


@server.route('/pages/vis-3/tournament')
def serve_tournament():
    html = to_html(tournament_figure)
    return jsonify(dict(tournament_graph=html))

# New routes for dropdown data
@server.route('/data/team')
def get_team():
    team = field_preprocess.get_country_team_(df_lineups)
    return jsonify(team.tolist())

@server.route('/data/teams/<team_country>')
def get_teams(team_country):
    teams = field_preprocess.get_opposite_team_(df_lineups, team_country)
    return jsonify(teams)

@server.route('/')
def serve_index():
    return send_from_directory('website', 'index.html')


@server.route('/index.css')
def serve_css():
    return send_from_directory('website', 'index.css')


@server.route('/index.js')
def serve_js():
    return send_from_directory('website', 'index.js')


@server.route('/pages/<path:path>')
def serve_pages(path):
    return send_from_directory('website/pages', path)


@server.route('/scripts/<path:path>')
def serve_scripts(path):
    return send_from_directory('website/scripts', path)


@server.route('/styles/<path:path>')
def serve_styles(path):
    return send_from_directory('website/styles', path)


@server.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('website/assets', path)


app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.Iframe(src='/index.html',
                style={'width': '100%', 'height': '100vh', 'border': 'none'})
])

if __name__ == '__main':
    app.run_server(debug=True)
