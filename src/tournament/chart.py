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



def make_tournament_figure(df, italian_matchs_infos):
    fig = init_figure()
    matches = italian_matchs_infos.to_dict(orient='records')
    print(type(matches))
    for match in matches:
        print( match['RoundName'], match['HomeTeamName'], match['AwayTeamName'])
        fig.add_trace(go.Scatter(
            x=[match['RoundName'], match['RoundName']],
            y=[match['HomeTeamName'], match['AwayTeamName']],
            mode='lines+markers+text',
            text=[f"{match['HomeTeamName']} ({match['ScoreHome']})", f"{match['AwayTeamName']} ({match['ScoreAway']})"],
            textposition='top center',
            line=dict(color='blue', width=4)
        ))


        fig.update_layout(
            title="EURO 2020 Knockout Phase",
            xaxis=dict(title='Competition level', tickvals=['Group stage', 'Round of 16', 'Quarter-finals', 'Semi-finals', 'Final']),
            yaxis=dict(title='Teams', tickmode='array', tickvals=[match['HomeTeamName'] for match in matches] + [match['AwayTeamName'] for match in matches]),
            showlegend=False
        )

    return fig
