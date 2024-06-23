import pandas as pd

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