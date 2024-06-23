# app.py
import dash
import dash_html_components as html
from flask import Flask, send_from_directory

server = Flask(__name__)


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
