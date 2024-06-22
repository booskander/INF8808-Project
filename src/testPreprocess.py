import pandas as pd
from field.preprocess import get_filter_italian_final_players, get_italian_players_stats


player_stats = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Players stats')
line_ups = pd.read_excel('./assets/EURO_2020_DATA.xlsx',sheet_name='Line-ups')


# Filter the final Italian players
filtered_players = get_filter_italian_final_players(line_ups)
player_names = filtered_players['ShortName'].tolist()

# Get the stats for the filtered Italian players
italian_player_stats = get_italian_players_stats(player_stats, player_names)

# Display the results
print("Filtered Players:")
print(filtered_players[['ShortName', 'TacticX', 'TacticY', 'Role', 'JerseyNumber', 'IsCaptain']])

print("\nPlayer Stats:")
for stats in italian_player_stats:
    print(stats)
