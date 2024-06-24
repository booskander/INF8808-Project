import pandas as pd

def preprocess_data(match_stats, player_stats, line_ups):
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
            get_filter_italian_final_players(line_ups),
            get_filter_all_italian_players_on_field(line_ups),
            get_italian_players_stats(match_stats)
        ]
    }
    return pd.DataFrame(data)


# Define a function to filter the players for Italy who are not staff and not bench
def get_filter_all_italian_players_on_field(df):
    filtered_all_italian_players = df[(df['Country'] == 'Italy') & (df['IsStaff'] == False) & (df['IsBench'] == False)]
    return filtered_all_italian_players

def get_filter_italian_final_players(df):
    filtered_final_italian_players = df[(df['Country'] == 'Italy') & (df['IsStaff'] == False) & (df['IsBench'] == False) & (df['AwayTeamName'] == 'England')]
    return filtered_final_italian_players


def get_italian_players_positions(df):
    filtered_players = get_filter_italian_final_players(df)
    players_positions = filtered_players[['OfficialSurname', 'TacticX', 'TacticY']]
    players_positions['TacticX'] = players_positions['TacticX'].astype(float) / 10  # Scaling the X position
    players_positions['TacticY'] = players_positions['TacticY'].astype(float) / 10  # Scaling the Y position
    return players_positions.to_dict(orient='records')

def get_italian_players_stats(df, playerNameList):
    stats_to_include = [
        'Goals', 'Fouls committed', 'Yellow cards', 'Red cards', 'Passes accuracy',
        'Dribbling', 'Clearances successful', 'Lost balls', 'Assists', 'Distance covered (Km)', 'Big Chances'
    ]
    filtered_stats = df[(df['HomeTeamName'] == 'Italy') & (df['AwayTeamName'] == 'England') & (df['PlayerSurname'].isin(playerNameList)) & (df['StatsName'].isin(stats_to_include))]
    
    player_stats = {}
    for _, row in filtered_stats.iterrows():
        player = row['PlayerSurname']
        if player not in player_stats:
            player_stats[player] = {'ShortName': player}
        player_stats[player][row['StatsName']] = row['Value']
 
    return list(player_stats.values())


