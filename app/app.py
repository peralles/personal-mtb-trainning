import streamlit as st
from app.pages import dashboard, planejamento
from app.services.strava_api import authenticate_strava
from app.db.db import init_db

st.set_page_config(page_title="Controle MTB Caminho da Fé", layout="wide")
st.title("Controle de Treinamento MTB - Caminho da Fé")

# Inicializar banco
init_db()

# Menu lateral
menu = st.sidebar.selectbox(
    "Menu", ["Dashboard", "Planejamento", "Autenticação Strava"])

if menu == "Dashboard":
    dashboard.show()
elif menu == "Planejamento":
    planejamento.show()
else:
    st.header("Autenticação Strava")
    auth_url = authenticate_strava()
    st.markdown(f"[Clique aqui para autenticar com Strava]({auth_url})")
    auth_code = st.text_input("Cole aqui o código de autorização do Strava:")
    if st.button("Buscar treinos"):
        from app.services.strava_api import fetch_activities, save_activities
        if auth_code:
            activities = fetch_activities(auth_code)
            save_activities(activities)
            st.success("Treinos sincronizados com sucesso!")
        else:
            st.error("Código inválido.")
