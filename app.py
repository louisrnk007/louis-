import streamlit as st
import openai

st.title("🤖 CoachBot - Assistant Sportif avec IA")
st.write("Pose une question sur l'entraînement ou la nutrition 💪")

message = st.text_input("Que veux-tu savoir ?")

def repondre_ia(question):
    openai.api_key = st.secrets["openai"]["api_key"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un coach sportif motivant, clair, et bienveillant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message["content"]

if message:
    with st.spinner("Je réfléchis à ton plan... 🧠"):
        reponse = repondre_ia(message)
        st.success(reponse)
