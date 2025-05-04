import streamlit as st
from app.db.db import load_activities_from_db
from app.utils.charts import plot_distance_by_week


def show():
    st.header("Dashboard de Treinamento")

    df = load_activities_from_db()

    if df.empty:
        st.warning("Nenhum treino encontrado.")
        return

    st.subheader("Volume Semanal (km)")
    fig = plot_distance_by_week(df)
    st.plotly_chart(fig, use_container_width=True)
