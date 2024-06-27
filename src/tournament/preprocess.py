import pandas as pd

def preprocess_data(df):
    filtered_italian_match_infos = df[ ((df['HomeTeamName'] == 'Italy') | (df['AwayTeamName'] == 'Italy')) ]
    filtered_italian_match_infos = filtered_italian_match_infos[['HomeTeamName', 'AwayTeamName', 'ScoreHome', 'ScoreAway', 'RoundName']]
   
    return filtered_italian_match_infos

