import pandas as pd
import utils
excel_file = '../assets/EURO_2020_DATA.xlsx'
df = pd.read_excel(excel_file)

player_data = {}

def get_player_info(player, category, data_type):
    player_info = {}
    player_name, player_surname = player.split()  
    player_row = df[(df['PlayerName'] == player_name) & (df['PlayerSurname'] == player_surname)]

    player_info = {}

    for type in data_type:
        if not player_row.empty:
            player_info[type] = player_row[type].values[0]  
        else:
            player_info[type] = None 

    return {category: player_info}

for player in utils.defense_players:
    player_data[player] = get_player_info(player, 'defense', utils.defense_data_type)

for player in utils.goalkeeper_players:
    player_data[player] = get_player_info(player, 'goalkeeper', utils.goalkeeper_data_type)

for player in utils.midfield_players:
    player_data[player] = get_player_info(player, 'midfield', utils.midfield_data_type)

for player in utils.attacker_players:
    player_data[player] = get_player_info(player, 'attacker', utils.attacker_data_type)

print(player_data)
