import streamlit as st
import pandas as pd


def show():
    st.header("Planejamento de Treinamento")

    df = pd.read_csv("app/data/planilha.csv")

    st.dataframe(df)
