import streamlit as st

st.title("🤖 CoachBot - Assistant Sportif")
st.write("Salut Louis ! Pose-moi une question d'entraînement ou de nutrition 👇")

message = st.text_input("Que veux-tu savoir ?")

if message:
    st.write("Réponse automatique : tu as dit →", message)
