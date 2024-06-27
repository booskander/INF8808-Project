import os, sys
sys.path.append(os.path.dirname(__file__))
import pandas as pd
import plotly.graph_objects as go
from preprocess import get_stages_data, load_match_data



def add_match(fig, x, y, match, stage_height):
    fig.add_shape(
        type="rect",
        x0=x, y0=y, x1=x + 0.2, y1=y + stage_height,
        line=dict(color="black", width=2),
        fillcolor="lightblue"
    )
    fig.add_annotation(
        x=x + 0.1, y=y + stage_height / 2 + 0.025, text=f"{match.get('team1', '')} {match.get('team1_score', '')}",
        showarrow=False, font=dict(size=12), yanchor="middle", xanchor="center"
    )
    fig.add_annotation(
        x=x + 0.1, y=y + stage_height / 2 - 0.025, text=f"{match.get('team2', '')} {match.get('team2_score', '')}",
        showarrow=False, font=dict(size=12), yanchor="middle", xanchor="center"
    )
    if "penalties" in match:
        fig.add_annotation(
            x=x + 0.1, y=y + stage_height / 2 - 0.1, text=f"(P {match.get('penalties', '')})",
            showarrow=False, font=dict(size=12, color="red"), yanchor="middle", xanchor="center"
        )



def make_tournament_chart():
    file_path = "../assets/EURO_2020_DATA.xlsx"
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    absolute_path = os.path.join(base_dir, file_path)
    df_match_infos = load_match_data(absolute_path)
    stages_data = get_stages_data(df_match_infos)
    fig = go.Figure()

    fig.update_layout(
        xaxis=dict(range=[-0.05, 1.25], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, 1.2], showgrid=False, zeroline=False, showticklabels=False),
        width=1200,
        height=800,
        title="Tournament Chart",
        template='plotly_white',
        margin=dict(t=100, b=20, l=20, r=20)
    )

    
    stage_height = 0.1
    x = 0
    y_base_group = 0.9  
    y_base_knockout = y_base_group - (stage_height * 1.5) * 1  
    y_base = [y_base_group, y_base_knockout, y_base_knockout, y_base_knockout, y_base_knockout]

    x_positions = []
    y_positions = []

    for i, stage_name in enumerate(stages_data.keys()):
        fig.add_annotation(x=x + i * 0.25 + 0.1, y=1.05, text=stage_name, showarrow=False,
                           font=dict(size=14, color="blue"), xanchor="center")

    for i, (stage_name, y) in enumerate(zip(stages_data.keys(), y_base)):
        for match in stages_data[stage_name]:
            add_match(fig, x, y, match, stage_height)
            if i != 0:  
                x_positions.append(x)
                y_positions.append(y + stage_height / 2)
            if i == 0:  
                y -= stage_height * 1.5  
        x += 0.25  

    for i in range(1, len(x_positions)):
        fig.add_shape(
            type="line",
            x0=x_positions[i - 1] + 0.2, y0=y_positions[i - 1],
            x1=x_positions[i], y1=y_positions[i],
            line=dict(color="black", width=2)
        )

    return fig
