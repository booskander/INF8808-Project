import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to load match data from Excel file
def load_match_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier n'existe pas à l'emplacement spécifié : {file_path}")

    print(f"Chargement des données depuis {file_path}...")
    df_match_infos = pd.read_excel(file_path, sheet_name='Match information', usecols=['HomeTeamName', 'AwayTeamName', 'RoundName', 'ScoreHome', 'ScoreAway'])
    print("Données chargées avec succès.")
    return df_match_infos

# Function to add a match to the figure
def add_match(fig, x, y, match, stage_height):
    fig.add_shape(
        type="rect",
        x0=x, y0=y, x1=x+0.2, y1=y+stage_height,
        line=dict(color="black", width=2)
    )
    fig.add_annotation(
        x=x+0.1, y=y+stage_height/2 + 0.02, text=f"{match['team1']} {match['team1_score']}",
        showarrow=False, font=dict(size=12), yshift=5
    )
    fig.add_annotation(
        x=x+0.1, y=y+stage_height/2 - 0.05, text=f"{match['team2']} {match['team2_score']}",
        showarrow=False, font=dict(size=12), yshift=-5
    )
    if "penalties" in match:
        fig.add_annotation(
            x=x+0.1, y=y+stage_height/2 - 0.1, text=f"(P {match['penalties']})",
            showarrow=False, font=dict(size=12, color="red")
        )

# Initialize and organize data into stages based on rounds
def initialize(df_match_infos):
    stages_data = {
        "Group Stage": [],
        "Round 16": [],
        "Quarterfinals": [],
        "Semifinals": [],
        "Final": []
    }

    for _, match in df_match_infos.iterrows():
        home_team = match['HomeTeamName']
        away_team = match['AwayTeamName']
        round_name = match['RoundName']
        score_home = match['ScoreHome']
        score_away = match['ScoreAway']
        # Keep only Italy matches 
        if away_team != 'Italy' and home_team != 'Italy':
            continue

        if round_name == 'final tournament':
            stages_data["Group Stage"].append({"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away})
        elif round_name == 'eighth finals':
            stages_data["Round 16"].append({"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away})
        elif round_name == 'quarter finals':
            stages_data["Quarterfinals"].append({"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away})
        elif round_name == 'semi finals':
            stages_data["Semifinals"].append({"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away})
        elif round_name == 'final':
            stages_data["Final"].append({"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away})

    # Create figure
    fig = go.Figure()

    # Set the layout
    fig.update_layout(
        xaxis=dict(range=[-0.05, 1.25], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, 1.2], showgrid=False, zeroline=False, showticklabels=False),
        width=1200,
        height=800,
        title="Tournament Chart",
        template='plotly_white',
        margin=dict(t=50, b=20, l=20, r=20)
    )

    # Add the matches and stage labels
    stage_height = 0.1
    x = 0
    y_base_group = 1.0
    y_base_knockout = y_base_group - (stage_height * 1.5) * 1  # Align with the second match of the group stage
    y_base = [y_base_group, y_base_knockout, y_base_knockout, y_base_knockout, y_base_knockout]

    x_positions = []
    y_positions = []

    for i, (stage_name, y) in enumerate(zip(stages_data.keys(), y_base)):
        # Add stage label
        if i == 0:  # Group Stage
            fig.add_annotation(x=x + 0.1, y=y + 0.05, text=stage_name, showarrow=False, font=dict(size=14, color="blue"), xanchor="center")
        else:  # Knockout Stages
            fig.add_annotation(x=x + 0.1, y=y_base_knockout + 0.05, text=stage_name, showarrow=False, font=dict(size=14, color="blue"), xanchor="center")

        for match in stages_data[stage_name]:
            add_match(fig, x, y, match, stage_height)
            if i != 0:  # Store positions for knockout stages to draw lines
                x_positions.append(x)
                y_positions.append(y + stage_height / 2)
            if i == 0:  # Group Stage
                y -= stage_height * 1.5  # Add some spacing between matches in the same stage
        x += 0.25  # Add spacing between stages

    # Draw connecting lines for knockout stages
    for i in range(1, len(x_positions)):
        fig.add_shape(
            type="line",
            x0=x_positions[i-1] + 0.2, y0=y_positions[i-1],
            x1=x_positions[i], y1=y_positions[i],
            line=dict(color="black", width=2)
        )

    # Show the figure
    return fig