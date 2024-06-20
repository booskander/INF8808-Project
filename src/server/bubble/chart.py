import plotly.graph_objects as go
import plotly.io as pio
import bubble.bubble as bubble
import plotly.express as px
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
    df['x'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    df['y'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(df)
    fig = px.scatter(
        df,
        x='x',
        y='y',
        size='size',
        color='color',
        hover_name='label',
        log_x=True,
        log_y=True,
        size_max=30,
        color_discrete_sequence=px.colors.qualitative.Set1,
        hover_data=['label', 'value']
    )

    # for label, value, size,color in zip(df['label'], df['value'], bubble.SIZES, bubble.COLORS):
    #     fig.add_trace(go.Scatter(
    #         x=[label],
    #         y=[value],
    #         mode='markers+text',
    #         marker=dict(size=size, color=color, sizemode='area'),
    #         text=f"{label}<br>{value}",
    #         textposition="middle center",
    #         showlegend=False
    #     ))
        
    # fig.update_layout(
    #     xaxis=dict(showgrid=False, zeroline=False),
    #     yaxis=dict(showgrid=False, zeroline=False),
    #     paper_bgcolor='rgba(0,0,0,0)',
    #     plot_bgcolor='rgba(0,0,0,0)',     
    # )
    
    return fig
