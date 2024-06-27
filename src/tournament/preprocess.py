import pandas as pd

def get_stages_data(df_match_infos: pd.DataFrame):
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

        match_info = {"team1": home_team, "team1_score": score_home, "team2": away_team, "team2_score": score_away}

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

def preprocess_data(match_infos):
    '''
    This function preprocesses the data for the bubble chart.
    '''
    
    data = {
        'label': [
            'Goals', 'Goals Conceded', 'Assist', 'Yellow Cards', 'Red Card',
            'Goals Saved', 'Pass accuracy(%)', 'Matches Played',
            'Avg Possession (%)', 'Best Scorer', 'Free Kicks',
            'Total Attempts', 'Attempts on Target', 'Corners', 'Offsides',  
            'OfficialSurname'
        ],
        'value': [
            get_italian_match_infos(match_infos)
        ]
    }
    return pd.DataFrame(data)


# Define a function to filter the players for Italy who are not staff and not bench
def get_italian_match_infos(df):
    filtered_italian_match_infos = df[ ((df['HomeTeamName'] == 'Italy') | (df['AwayTeamName'] == 'Italy')) ]
    return filtered_italian_match_infos