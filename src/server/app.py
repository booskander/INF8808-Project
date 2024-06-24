# app.py
import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask, send_from_directory, jsonify
from server.bubble import chart, bubble, preprocess
import plotly.io as pio
import pandas as pd
server = Flask(__name__)

df_match_stats = pd.read_excel(
    './assets/EURO_2020_DATA.xlsx', sheet_name='Match Stats')
df_player_stats = pd.read_excel(
    './assets/EURO_2020_DATA.xlsx', sheet_name='Players stats')
df_viz_1 = preprocess.preprocess_data(df_match_stats, df_player_stats)
# create_template()
bubble_chart_figure = chart.init_figure()

bubble_chart_figure = chart.make_bubble_chart(df_viz_1)

bubble_graph = dcc.Graph(
    id='bubble-chart',
    figure=bubble_chart_figure
)


def to_html(component):
    return pio.to_html(component, full_html=False, include_plotlyjs='cdn')


@server.route('/pages/vis-1/bubble')
def serve_bubble():
    html = to_html(bubble_graph)
    return jsonify(dict(bubble_graph=html))


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

if __name__ == '__main__':
    app.run_server(debug=True)
