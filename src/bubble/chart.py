import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import random
from bubble.template import create_template
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


def make_bubble_chart(df):
    '''
        This function creates a bubble chart from the given dataframe.

        Args:
            df: The dataframe containing the data to be displayed in the bubble chart

        Returns:
            fig: The figure which will display the bubble chart
    '''
    fig = init_figure()
    df['size'] = [100, 20, 70, 30, 10, 55, 70,
                  50, 90, 55, 60, 90, 85, 45, 35]
    
    df['color'] = '#ff9999'
    random.seed(0)
    df['x'] = [20, 45, 65, 95, 172, -10, 65, 115, 150, 165, 12, 35, 95, 125, 140]
    df['y'] = [0, -40, -5, -20, 115, 60, 160, -15, 150, 25, 145, 155, 110, 100, -10]
    df['text'] = df['label'] + '<br>' + df['value'].astype(str)
    red_gradient = [
    [0, 'rgb(255, 230, 230)'],  # Light red
    [0.5, 'rgb(255, 128, 128)'], # Medium red
    [1, 'rgb(255, 0, 0)']       # Pure red
    ]
    
    fig = px.scatter(
        df,
        x='x',
        y='y',
        size='size',
        color='size',
        color_continuous_scale= red_gradient,
        hover_name='label',
        size_max=200,
        text='text',
        labels= {'x': '', 'y': ''},
        custom_data=['label','value'],
        
    )
    create_template()
    fig.update_layout(
        xaxis=dict(range=[-50, 200],
                  showgrid=False, 
                  zeroline=False, 
                  showticklabels=False
                   ),
        yaxis=dict(range=[-110,255],
                   showticklabels=False,
                   showgrid=False,
                   showline=False,
                   zeroline=False,
                   ),
        title='Italy statistics',
        template=pio.templates['my_theme'],
        showlegend=False,
        height=700,
        coloraxis_colorbar = dict(
            title = 'Impact',
            tickvals = [],
            ticktext = ['Low', 'Medium', 'High']
        ) 
    )
    fig.update_traces(
        textposition='middle center',
        hovertemplate=hover_template('%{customdata[0]}', '%{customdata[1]}'),
        marker=dict(line=dict(width=0))
    )

    return fig

def hover_template(label, value):
    hover_template = f'<b>{label}<br>' + \
                     f'<b>Value:</b> {value}<br>' + \
                     '<extra></extra>'

    return hover_template   
