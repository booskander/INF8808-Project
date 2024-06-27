import os
import pandas as pd


def load_match_stats(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier n'existe pas à l'emplacement spécifié : {file_path}")

    print(f"Chargement des données depuis {file_path}...")
    df_match_stats = pd.read_excel(file_path, sheet_name='Match Stats',
                                   usecols=['MatchID', 'StatsName', 'Value'])
    print("Données chargées avec succès.")
    return df_match_stats


def load_match_info(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier n'existe pas à l'emplacement spécifié : {file_path}")

    print(f"Chargement des données depuis {file_path}...")
    df_match_infos = pd.read_excel(file_path, sheet_name='Match information',
                                   usecols=['MatchID', 'HomeTeamName', 'AwayTeamName', 'RoundName', 'ScoreHome', 'ScoreAway'])
    print("Données chargées avec succès.")
    return df_match_infos

def get_stages_data():
    file_path = "../assets/EURO_2020_DATA.xlsx"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(base_dir, file_path)
    df_match_infos = load_match_info(absolute_path)
    df_match_stats = load_match_stats(absolute_path)

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
        match_id = match['MatchID']

        # Keep only Italy matches
        if away_team != 'Italy' and home_team != 'Italy':
            continue

        match_stats = df_match_stats[df_match_stats['MatchID'] == match_id]
        stats_dict = {}
        for _, stat in match_stats.iterrows():
            stat_name = stat['StatsName']
            stat_value = stat['Value']
            if stat_name in ["Ball Possession", "Passes accuracy", "Total Attempts", "Recovered balls", "Yellow cards", "Red cards"]:
                stats_dict[stat_name] = stat_value

        match_info = {
            "ID" : match_id,
            "team1": home_team,
            "team1_score": score_home,
            "team2": away_team,
            "team2_score": score_away,
            "stats": stats_dict
        }

        if round_name == 'final tournament':
            stages_data["Group Stage"].append(match_info)
        elif round_name == 'eighth finals':
            stages_data["Round 16"].append(match_info)
        elif round_name == 'quarter finals':
            stages_data["Quarterfinals"].append(match_info)
        elif round_name == 'semi finals':
            stages_data["Semifinals"].append(match_info)
        elif round_name == 'final':
            stages_data["Final"].append(match_info)

    return stages_data

def get_match_stats(matchID):
    stages_data = get_stages_data()
    for stage in stages_data.values():
        for match in stage:
            if match["ID"] == matchID:
                return match.get("stats", {})
    return {}
