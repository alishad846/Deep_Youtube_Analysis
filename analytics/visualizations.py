import plotly.express as px
import pandas as pd

def create_channel_stat_plot(channel_data):
    """
    Create a bar plot for channel statistics like views, subscribers, etc.
    """
    df = pd.DataFrame([channel_data])
    fig = px.bar(df, x="title", y=["subscribers", "views", "videos"],
                 title="YouTube Channel Statistics")
    return fig
