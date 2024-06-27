import pandas as pd

def preprocess_data(match_stats, player_stats):
    '''
    This function preprocesses the data for the bubble chart.
    '''
    
    data = {
        'label': [
            'Goals', 'Goals Conceded', 'Assist', 'Yellow Cards', 'Red Card',
            'Goals Saved', 'Pass accuracy(%)', 'Matches Played',
            'Avg Possession (%)', 'Best Scorer', 'Free Kicks',
            'Total Attempts', 'Attempts on Target', 'Corners', 'Offsides'
        ],
        'value': [
            get_stats(match_stats, 'Goals'), 
            get_stats(match_stats,'Goals conceded'), 
            get_stats(match_stats, 'Assists'), 
            get_stats(match_stats, 'Yellow cards'), 
            get_stats(match_stats, 'Red cards'), 
            get_stats(match_stats, 'Saves'), 
            get_avg_stats(match_stats, 'Passes accuracy'),
            get_stats(match_stats, 'Matches played'), 
            get_avg_stats(match_stats,'Ball Possession'), 
            get_best_scorer(player_stats),
            get_free_kicks(match_stats),
            get_stats(match_stats, 'Total Attempts'),
            get_stats(match_stats, 'Attempts on target'),
            get_stats(match_stats, 'Corners'),
            get_stats(match_stats, 'Offsides')
        ]
    }
    return pd.DataFrame(data)

def get_avg_stats(df, stat_name):
    '''
    This function returns the average value of a given stat for a specific team.
    '''
    mean_value = df[(df['TeamName'] == 'Italy') & (df['StatsName'] == stat_name)]['Value'].mean()
    return round(mean_value, 2)


def get_stats(df, stat_name):
    '''
    This function returns the stats of Italy.
    '''
    return df[(df['TeamName'] == 'Italy') & (df['StatsName'] == stat_name)].sum()['Value']

def get_free_kicks(df):
    '''
    This function returns the free kicks on goal for Italy.
    '''
    direct_free_kicks = df[(df['TeamName'] == 'Italy') & (df['StatsName'] == 'Attempts on direct free kick')].sum()['Value']
    indirect_free_kicks = df[(df['TeamName'] == 'Italy') & (df['StatsName'] == 'Attempts on indirect free kick')].sum()['Value']
    return direct_free_kicks + indirect_free_kicks

def get_best_scorer(df):
    '''
    This function returns the best scorer for Italy.
    '''
    scorer_df = df[((df['HomeTeamName'] == 'Italy') | (df['AwayTeamName'] == 'Italy')) & (df['StatsName'] == 'Goals')]
    scorer_df['Value'] = pd.to_numeric(scorer_df['Value'], errors='coerce').fillna(0)
    scorer_goals = scorer_df.groupby('PlayerName')['Value'].sum()
    best_scorer_name = scorer_goals.idxmax()
    best_scorer_surname = df[df['PlayerName'] == best_scorer_name]['PlayerSurname'].values[0]
    best_scorer = best_scorer_name + ' ' + best_scorer_surname
    return best_scorer
