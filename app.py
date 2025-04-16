import streamlit as st
import openai

st.set_page_config(page_title="CoachBot IA", page_icon="🏋️‍♂️")
st.title("🤖 CoachBot - Assistant Sportif avec IA")
st.write("Pose-moi une question sur l'entraînement ou la nutrition 👇")

message = st.text_input("Que veux-tu savoir ?")

def repondre_ia(question):
    openai.api_key = st.secrets["openai"]["api_key"]  # 🔐 Ta clé est sécurisée

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # tu peux aussi essayer "gpt-4"
        messages=[
            {"role": "system", "content": "Tu es un coach sportif motivant et bienveillant. Tu aides les gens à s'entraîner et bien manger."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message["content"]

if message:
    with st.spinner("CoachBot réfléchit à ta question... 🧠"):
        reponse = repondre_ia(message)
        st.success(reponse)
