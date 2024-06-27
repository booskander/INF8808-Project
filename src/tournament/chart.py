import pandas as pd
import plotly.graph_objects as go
import os


def init_figure():
    fig = go.Figure()
    return fig


def make_tournament_bracket(df_match_infos):
    fig = init_figure()
    
    print(df_match_infos)
    return fig


def get_figure():
    file_path = os.path.join(os.path.dirname(
        __file__), '..', 'assets', 'EURO_2020_DATA.xlsx')

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Le fichier n'existe pas à l'emplacement spécifié : {file_path}")

    print(f"Chargement des données depuis {file_path}...")

    df_match_infos = pd.read_excel(file_path, sheet_name='Match information',
                                   usecols=['RoundName', 'HomeTeamName', 'AwayTeamName', 'ScoreHome', 'ScoreAway'])

    print("Données chargées avec succès.")

    return make_tournament_bracket(df_match_infos)
