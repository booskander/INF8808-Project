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

def make_field_chart(players=None, stats=None):
    fig = init_figure()
    
    # Create the pitch
    # Pitch Outline
    fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100,
                  line=dict(color="black", width=3))
    
    # Left Penalty Area
    fig.add_shape(type="rect", x0=0, y0=30, x1=20, y1=70,
                  line=dict(color="black", width=3))

    # Right Penalty Area
    fig.add_shape(type="rect", x0=80, y0=30, x1=100, y1=70,
                  line=dict(color="black", width=3))
    
    # Left 6-yard Box
    fig.add_shape(type="rect", x0=0, y0=40, x1=6, y1=60,
                  line=dict(color="black", width=3))

    # Right 6-yard Box
    fig.add_shape(type="rect", x0=94, y0=40, x1=100, y1=60,
                  line=dict(color="black", width=3))
    
    # Prepare Circle
    fig.add_shape(type="circle", x0=45, y0=45, x1=55, y1=55,
                  line=dict(color="black", width=3))

    # Center Line
    fig.add_shape(type="line", x0=50, y0=0, x1=50, y1=100,
                  line=dict(color="black", width=3))

    
    # Add players if provided
    if players is not None:
        for player in players:
            # Initialize player_stats to an empty dictionary
            player_stats = {}
            
            # Iterate through the stats to find the corresponding player's stats
            for stat in stats:
                if stat['ShortName'] == player['OfficialSurname']:
                    player_stats = stat
                    break
            # Create the hover text for the player
            hover_text = f"{player['OfficialSurname']}<br>"
            for key, value in player_stats.items():
                if key != 'ShortName':
                    hover_text += f"{key}: {value}<br>"
            
            # Add the player to the plot
            fig.add_trace(go.Scatter(
                x=[player['TacticX']],
                y=[player['TacticY']],
                mode='markers+text',
                marker=dict(size=22, color='blue'),
                text=[player['OfficialSurname']],
                textposition="top center",
                name=player['OfficialSurname'],
                hoverinfo="text",
                hovertext=hover_text
            ))

    # Update layout
    fig.update_layout(
        xaxis=dict(range=[-10, 110], showgrid=False, zeroline=False, title="TacticX"),
        yaxis=dict(range=[-10, 110], showgrid=False, zeroline=False, title="TacticY"),
        height=600,
        width=1000,
        margin=dict(t=80, b=50, l=50, r=50),
        plot_bgcolor='#4CAF50',  # Set the background color to green
        title={
            'text': "Team formation and players statistics",
            'y':0.97,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        font=dict(
            family="Arial, sans-serif",
            size=18,
            color="black"
        )
    )

    return fig


