import pandas as pd

def preprocess_data(match_stats, player_stats, line_ups):
    
    data = {
        'label': [
            'Goals', 'Goals Conceded', 'Assist', 'Yellow Cards', 'Red Card',
            'Goals Saved', 'Pass accuracy(%)', 'Matches Played',
            'Avg Possession (%)', 'Best Scorer', 'Free Kicks',
            'Total Attempts', 'Attempts on Target', 'Corners', 'Offsides',  
            'OfficialSurname'
        ],
        'value': [
            get_country_team_(line_ups),
            get_opposite_team_(line_ups),
            get_filter_final_players(line_ups),
            get_filter_all_players_on_field(line_ups),
            get_players_stats(match_stats)
        ]
    }
    return pd.DataFrame(data)

def get_country_team_(df):
    unique_countries = df['Country'].unique()
    return unique_countries

def get_opposite_team_(df, country_team):
    filtered_home_teams = df[(df['Country'] == country_team) & ((df['HomeTeamName'] == country_team) | (df['AwayTeamName'] == country_team))]['HomeTeamName'].unique()
    filtered_away_teams = df[(df['Country'] == country_team) & ((df['HomeTeamName'] == country_team) | (df['AwayTeamName'] == country_team))]['AwayTeamName'].unique()
    filtered_opposite_teams = set(filtered_home_teams).union(set(filtered_away_teams))
    if country_team in filtered_opposite_teams:
        filtered_opposite_teams.remove(country_team)
    return list(filtered_opposite_teams)

def get_filter_all_players_on_field(df, country_team):
    if country_team is None:
        country_team = 'Italy'
    filtered_all_italian_players = df[(df['Country'] == country_team) & (df['IsStaff'] == False) & (df['IsBench'] == False)]
    return filtered_all_italian_players

def get_filter_final_players(df, country_team, opposite_team):
    if country_team is None:
        country_team = 'Italy'
    if opposite_team is None:
        opposite_team = 'England'
    filtered_final_italian_players = df[(df['Country'] == country_team) & (df['IsStaff'] == False) & (df['IsBench'] == False) & ((df['AwayTeamName'] == opposite_team) | (df['HomeTeamName'] == opposite_team))]
    return filtered_final_italian_players


def get_players_positions(df, country_team, opposite_team):
    if country_team is None:
        country_team = 'Italy'
    if opposite_team is None:
        opposite_team = 'England'
    filtered_players = get_filter_final_players(df, country_team, opposite_team)
    players_positions = filtered_players[['OfficialSurname', 'TacticX', 'TacticY']]
    players_positions['TacticX'] = players_positions['TacticX'].astype(float) / 10  # Scaling the X position
    players_positions['TacticY'] = players_positions['TacticY'].astype(float) / 10  # Scaling the Y position
    return players_positions.to_dict(orient='records')

def get_players_stats(df, playerNameList, team, opposite_team):
    if team is None:
        team = 'Italy'
    if opposite_team is None:
        opposite_team = 'England'
    stats_to_include = [
        'Goals', 'Fouls committed', 'Yellow cards', 'Red cards', 'Passes accuracy',
        'Dribbling', 'Clearances successful', 'Lost balls', 'Assists', 'Distance covered (Km)', 'Big Chances'
    ]
    filtered_stats = df[(df['HomeTeamName'] == team) & (df['AwayTeamName'] == opposite_team) & (df['PlayerSurname'].isin(playerNameList)) & (df['StatsName'].isin(stats_to_include))]
    if filtered_stats.empty:
        filtered_stats = df[(df['HomeTeamName'] == opposite_team) & (df['AwayTeamName'] == team) & (df['PlayerSurname'].isin(playerNameList)) & (df['StatsName'].isin(stats_to_include))]
    player_stats = {}
    for _, row in filtered_stats.iterrows():
        player = row['PlayerSurname']
        if player not in player_stats:
            player_stats[player] = {'ShortName': player}
        player_stats[player][row['StatsName']] = row['Value']
 
    return list(player_stats.values())


