import plotly.graph_objects as go
import plotly.io as pio
import bubble.bubble as bubble
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
    fig = go.Figure()
    df['size'] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    df['color'] = '#ff9999'
    random.seed(0)
    df['x'] = generate_values(0, 200, 5, 15)
    df['y'] = generate_values(0, 200, 5, 15)
    df['text'] = df['label'] + '<br>' + df['value'].astype(str) 
    fig = px.scatter(
        df,
        x='x',
        y='y',
        size='size',
        color='color',
        hover_name='label',       
        color_discrete_sequence=px.colors.qualitative.Set1,
        hover_data=['label', 'value'],
        size_max=200,
        text='text' 
        
    )
  
    fig.update_layout(
        xaxis=dict(range=[-50, 250], 
                   showgrid=False,
                   showline=False, 
                   zeroline=False, 
                   showticklabels=False,
                   ),
        yaxis=dict(range=[-50, 250], 
                   showgrid=False, 
                   showline=False, 
                   zeroline=False, 
                   showticklabels=False, 
                   ),
        title='Bubble Chart',
        template='plotly_dark',
        showlegend=False
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