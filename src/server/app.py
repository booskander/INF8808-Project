import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, render_template

server = Flask(__name__)

# Initialize Dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/')

# Define route to render your index.html template


@server.route('/')
def index():
    return render_template('website/index.html')


# Define layout of the Dash app directly
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback to update page content based on URL


@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    # This callback renders your Flask-rendered HTML
    return render_template('website/index.html')


if __name__ == '__main__':
    server.run(port=8050, debug=True)
