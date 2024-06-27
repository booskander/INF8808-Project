import os, sys
sys.path.append(os.path.dirname(__file__))
import pandas as pd
import plotly.graph_objects as go
from preprocess import get_stages_data


def add_match(fig, x, y, match, stage_height):
    stats_text = "<br>".join([f"{key}: {value}" for key, value in match.get('stats', {}).items()])
    hovertext = (
        f"{match.get('team1', '')} {match.get('team1_score', '')} vs {match.get('team2', '')} {match.get('team2_score', '')}<br>"
        f"Stats:<br>{stats_text}"
    )

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

    fig.add_trace(go.Scatter(
        x=[x + 0.1], y=[y + stage_height / 2],
        mode="markers",
        marker=dict(size=20, opacity=0),
        hoverinfo="text",
        hovertext=hovertext,
        showlegend=False
    ))


def make_tournament_chart():
    stages_data = get_stages_data()
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
        fig.add_annotation(x=x + i * 0.25 + 0.1, y=1.05, text=f"<b>{stage_name}</b>", showarrow=False,
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

    # Ajouter des lignes entre les matchs du Group Stage et le Round 16
    for j in range(len(stages_data["Group Stage"])):
        fig.add_shape(
            type="line",
            x0=0.2, y0=y_base_group - j * stage_height * 1.5 + stage_height / 2,
            x1=0.25, y1=y_base_knockout + stage_height / 2,
            line=dict(color="black", width=2)
        )

    return fig
