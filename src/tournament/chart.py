import pandas as pd
import plotly.graph_objects as go
import os


def init_figure():
    fig = go.Figure()
    return fig


def make_tournament_bracket(df_match_infos):
    fig = init_figure()

    rounds = df_match_infos['RoundName'].unique()
    rounds.sort()

    teams = list(set(df_match_infos['HomeTeamName'].tolist() + df_match_infos['AwayTeamName'].tolist()))
    y_positions = {team: i for i, team in enumerate(teams)}

    for _, match in df_match_infos.iterrows():
        fig.add_trace(go.Scatter(
            x=[match['RoundName'], match['RoundName']],
            y=[y_positions[match['HomeTeamName']], y_positions[match['AwayTeamName']]],
            mode='lines+markers+text',
            text=[f"{match['HomeTeamName']} ({match['ScoreHome']})", f"{match['AwayTeamName']} ({match['ScoreAway']})"],
            textposition='top center',
            line=dict(color='blue', width=4)
        ))

    fig.update_layout(
        title="EURO 2020 Knockout Phase",
        xaxis=dict(title='Competition level', tickvals=list(range(len(rounds))), ticktext=rounds),
        yaxis=dict(title='Teams', tickvals=list(y_positions.values()), ticktext=list(y_positions.keys())),
        showlegend=False
    )
    fig.show()
    return fig


try:
    file_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'EURO_2020_DATA.xlsx')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier n'existe pas à l'emplacement spécifié : {file_path}")

    print(f"Chargement des données depuis {file_path}...")

    df_match_infos = pd.read_excel(file_path, sheet_name='Match information',
                                   usecols=['RoundName', 'HomeTeamName', 'AwayTeamName', 'ScoreHome', 'ScoreAway'])

    print("Données chargées avec succès.")

    make_tournament_bracket(df_match_infos)

except Exception as e:
    print(f"An error occurred: {e}")
