import pandas as pd
import plotly.express as px


def plot_distance_by_week(df):
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['week'] = df['start_date'].dt.isocalendar().week
    df_week = df.groupby('week')['distance'].sum().reset_index()
    fig = px.bar(df_week, x='week', y='distance',
                 title="Distância pedalada por semana (km)")
    return fig
