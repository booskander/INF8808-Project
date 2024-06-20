import pandas as pd
import utils
excel_file = './assets/EURO_2020_DATA.xlsx'
sheet_name = 'Players stats'
df = pd.read_excel(excel_file, sheet_name=sheet_name)

player_data = {}

def convert_to_minutes(time_obj):
    if pd.isnull(time_obj):
        return 0
    else:
        return time_obj.hour * 60 + time_obj.minute
    
def get_player_info(player, data_type):
    player_info = {}
    player_name_split = player.split(' ', 1)
    
    if len(player_name_split) == 2:
        player_name, player_surname = player_name_split
    elif len(player_name_split) == 1:
        player_name = ''
        player_surname = player_name_split[0]    
    
    player_rows = df[(df['PlayerName'] == player_name) & (df['PlayerSurname'] == player_surname)]

    player_info = {} 

    for stat_name in data_type:
        if not player_rows.empty:
            if stat_name == 'Played Time':
                filtered_rows = player_rows[player_rows['StatsName'] == stat_name]
                if not filtered_rows.empty:
                    total_minutes = filtered_rows['Value'].apply(convert_to_minutes).sum()
                    player_info[stat_name] = total_minutes
                else:
                    player_info[stat_name] = None
            else:
                filtered_rows = player_rows[player_rows['StatsName'] == stat_name]
                if not filtered_rows.empty:
                    stat_sum = filtered_rows['Value'].sum()
                    player_info[stat_name] = stat_sum
                else:
                    player_info[stat_name] = None
        else:
            player_info[stat_name] = None

    return {player: player_info}

for player in utils.defense_players:
    player_data[player] = get_player_info(player, utils.defense_data_type)

for player in utils.goalkeeper_players:
    player_data[player] = get_player_info(player, utils.goalkeeper_data_type)

for player in utils.midfield_players:
    player_data[player] = get_player_info(player, utils.midfield_data_type)

for player in utils.attacker_players:
    player_data[player] = get_player_info(player, utils.attacker_data_type)

def get_players_info():
    return player_data
