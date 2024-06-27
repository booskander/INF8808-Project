import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os
import random

# Create a custom Plotly template
def create_template():
    THEME = {
        'background_color': '#f2f2f2',
        'font_family': 'Arial, sans-serif',
        'font_color': '#333333',
        'label_font_size': 16,
        'label_background_color': '#ffffff',
        'line_color': '#666666'
    }

    pio.templates['tournament_bracket'] = go.layout.Template(
        layout=go.Layout(
            font=dict(
                family=THEME['font_family'],
                color=THEME['font_color']
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
        )
    )

# Function to load match data from an Excel file
def load_match_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist at the specified location: {file_path}")

    print(f"Loading data from {file_path}...")
    df_match_infos = pd.read_excel(file_path, sheet_name='Match information', usecols=['HomeTeamName', 'AwayTeamName', 'RoundName', 'ScoreHome', 'ScoreAway'])
    print("Data loaded successfully.")
    return df_match_infos

# Function to simulate match outcomes
def simulate_match(home_team, away_team):
    score1 = random.randint(0, 3)
    score2 = random.randint(0, 3)
    if score1 > score2:
        return home_team
    elif score2 > score1:
        return away_team
    else:
        return random.choice([home_team, away_team])

# Function to create the tournament bracket
def make_tournament_bracket(df_match_infos):
    rounds = df_match_infos['RoundName'].unique()
    rounds.sort()

    teams = list(set(df_match_infos['HomeTeamName'].tolist() + df_match_infos['AwayTeamName'].tolist()))
    y_positions = {team: i for i, team in enumerate(teams)}

    fig = go.Figure()

    for _, match in df_match_infos.iterrows():
        home_team = match['HomeTeamName']
        away_team = match['AwayTeamName']
        round_name = match['RoundName']
        score_home = match['ScoreHome']
        score_away = match['ScoreAway']

        fig.add_trace(go.Scatter(
            x=[round_name, round_name],
            y=[y_positions[home_team], y_positions[away_team]],
            mode='lines+markers',
            line=dict(color='#666666', width=2),
            marker=dict(symbol='line-ew', color='blue', size=10),
            text=[f"{home_team} ({score_home})", f"{away_team} ({score_away})"],
            hoverinfo='text',
            showlegend=False
        ))

    fig.update_layout(
        title="Champions League Knockout Phase",
        xaxis=dict(title='Competition Level', tickvals=list(range(len(rounds))), ticktext=rounds),
        yaxis=dict(title='Teams', tickvals=list(y_positions.values()), ticktext=list(y_positions.keys())),
        template='tournament_bracket'
    )

    return fig

# Function to generate the final figure
def get_figure():
    file_path = 'path_to_your_excel_file.xlsx'  # Replace with your file path

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist at the specified location: {file_path}")

    print(f"Loading data from {file_path}...")

    df_match_infos = pd.read_excel(file_path, sheet_name='Match information', usecols=['RoundName', 'HomeTeamName', 'AwayTeamName', 'ScoreHome', 'ScoreAway'])

    print("Data loaded successfully.")

    return make_tournament_bracket(df_match_infos)


