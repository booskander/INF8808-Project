import plotly.graph_objects as go
import pandas as pd

def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    return fig



def make_tournament_figure(df):
    fig = init_figure()
    knockout_rounds = df[df['RoundName'].str.contains('Round of 16|Quarter-finals|Semi-finals|Final')]
    matches = [
        {'round': 'Round of 16', 'home': 'Belgium', 'away': 'Portugal', 'home_score': 1, 'away_score': 0},
        {'round': 'Round of 16', 'home': 'Italy', 'away': 'Austria', 'home_score': 2, 'away_score': 1},
        {'round': 'Round of 16', 'home': 'France', 'away': 'Switzerland', 'home_score': 3, 'away_score': 3, 'penalties': '4-5'},
        {'round': 'Round of 16', 'home': 'Croatia', 'away': 'Spain', 'home_score': 3, 'away_score': 5},
        {'round': 'Round of 16', 'home': 'Sweden', 'away': 'Ukraine', 'home_score': 1, 'away_score': 2},
        {'round': 'Round of 16', 'home': 'England', 'away': 'Germany', 'home_score': 2, 'away_score': 0},
        {'round': 'Round of 16', 'home': 'Netherlands', 'away': 'Czech Republic', 'home_score': 0, 'away_score': 2},
        {'round': 'Round of 16', 'home': 'Wales', 'away': 'Denmark', 'home_score': 0, 'away_score': 4},
        {'round': 'Quarter-finals', 'home': 'Belgium', 'away': 'Italy', 'home_score': 1, 'away_score': 2},
        {'round': 'Quarter-finals', 'home': 'Switzerland', 'away': 'Spain', 'home_score': 1, 'away_score': 1, 'penalties': '1-3'},
        {'round': 'Quarter-finals', 'home': 'Ukraine', 'away': 'England', 'home_score': 0, 'away_score': 4},
        {'round': 'Quarter-finals', 'home': 'Czech Republic', 'away': 'Denmark', 'home_score': 1, 'away_score': 2},
        {'round': 'Semi-finals', 'home': 'Italy', 'away': 'Spain', 'home_score': 1, 'away_score': 1, 'penalties': '4-2'},
        {'round': 'Semi-finals', 'home': 'England', 'away': 'Denmark', 'home_score': 2, 'away_score': 1},
        {'round': 'Final', 'home': 'Italy', 'away': 'England', 'home_score': 1, 'away_score': 1, 'penalties': '4-2'}
    ]
    for match in matches:
        fig.add_trace(go.Scatter(
            x=[match['round'], match['round']],
            y=[match['home'], match['away']],
            mode='lines+markers+text',
            text=[f"{match['home']} ({match['home_score']})", f"{match['away']} ({match['away_score']})"],
            textposition='top center',
            line=dict(color='blue', width=2)
        ))


        fig.update_layout(
            title="EURO 2020 Knockout Phase",
            xaxis=dict(title='Niveau de la compétition', tickvals=['Round of 16', 'Quarter-finals', 'Semi-finals', 'Final']),
            yaxis=dict(title='Équipes', tickmode='array', tickvals=[match['home'] for match in matches] + [match['away'] for match in matches]),
            showlegend=False
        )

    return fig
