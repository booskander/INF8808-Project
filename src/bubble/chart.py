import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import random

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
    print(df)
    fig = px.scatter(
        df,
        x='x',
        y='y',
        size='size',
        color='color',
        hover_name='label',
        color_discrete_sequence=['#ff9999'],
        hover_data=['label', 'value'],
        size_max=200,
        text='text'

    )

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
        template='plotly_dark',
        showlegend=False,
        height=600
    )
    fig.update_traces(textposition='middle center')

    return fig


def generate_values(min_value, max_value, min_distance, max_distance):
    values = [min_value]
    current_value = min_value
    use_min_distance = True

    while True:
        # Alternate between min_distance and max_distance
        next_distance = min_distance if use_min_distance else max_distance
        next_value = current_value + next_distance

        if next_value > max_value:
            break

        values.append(next_value)
        current_value = next_value
        use_min_distance = not use_min_distance  # Alternate for next step
    random.shuffle(values)
    return values[:15]
