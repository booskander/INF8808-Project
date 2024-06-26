import plotly.graph_objects as go
import plotly.io as pio

THEME = {
    'bar_colors': [
        '#861388',
        '#d4a0a7',
        '#dbd053',
        '#1b998b',
        '#A0CED9',
        '#3e6680'
    ],
    'background_color': '#061b22', 
    'font_family': 'Montserrat',
    'font_color': '#ffffff',
    'font_size': 25,
    'label_font_size': 16,
    'label_background_color': 'rgb(255, 128, 128)'
}


def create_template():
    pio.templates['my_theme'] = go.layout.Template(
        layout=go.Layout(
            font=dict(
                family=THEME['font_family'],
                color=THEME['font_color'],
                size = THEME['font_size'] 
            ),
            plot_bgcolor=THEME['background_color'],
            paper_bgcolor=THEME['background_color'],
            
            hoverlabel=dict(
                bgcolor=THEME['label_background_color'],
                font=dict(
                    size=THEME['label_font_size'],
                    color=THEME['font_color']
                )
            ),
            hovermode='closest'
        ),
        data_bar=[go.Bar(marker_color=x) for x in THEME['bar_colors']]
    )