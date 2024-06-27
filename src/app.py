import pandas as pd
import plotly.io as pio
from flask import Flask, send_from_directory, jsonify
from bubble import preprocess as bubble_preprocess
from bubble import chart as bubble_chart
from field import chart as field_chart
from field import preprocess as field_preprocess
from field import chart as field_chart
from tournament import chart as tournament_chart
from tournament import preprocess as tournament_preprocess

import dash_core_components as dcc
import dash_html_components as html
import dash

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

# bubble_graph.show()
# """ Field chart """
players_data = field_preprocess.get_italian_players_positions(df_lineups)
players = field_preprocess.get_filter_italian_final_players(df_lineups)
players_names = players['OfficialSurname'].tolist()
players_stats = field_preprocess.get_italian_players_stats(
    df_player_stats, players_names)

field_graph = field_chart.make_field_chart(players_data, players_stats)

""" Tournament chart """

tournament_figure = tournament_chart.make_tournament_chart()


def to_html(component):
    return pio.to_html(component, full_html=False, include_plotlyjs='cdn')


@server.route('/pages/vis-1/bubble')
def serve_bubble():
    html = to_html(bubble_graph)
    return jsonify(dict(bubble_graph=html))


@server.route('/pages/vis-2/field')
def serve_field():
    html = to_html(field_graph)
    return jsonify(dict(field_graph=html))


@server.route('/pages/vis-3/tournament')
def serve_tournament():
    html = to_html(tournament_figure)
    return jsonify(dict(tournament_graph=html))


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
