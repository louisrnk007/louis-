import streamlit as st
import openai

openai.api_key = st.secrets["openai"]["api_key"]

st.title("🤖 CoachBot - Assistant Sportif avec IA")
st.write("Pose-moi une question sur l'entraînement ou la nutrition 👇")

message = st.text_input("Que veux-tu savoir ?")

def repondre_ia(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou gpt-4 si tu veux tester
        messages=[
            {"role": "system", "content": "Tu es un coach sportif professionnel, spécialiste en nutrition et musculation."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

if message:
    with st.spinner("Réflexion..."):
        reponse = repondre_ia(message)
        st.success(reponse)
