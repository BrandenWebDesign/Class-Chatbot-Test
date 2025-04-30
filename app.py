import streamlit as st
import openai

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = st.secrets["openrouter_key"]

st.title("Free Chatbot (OpenRouter)")

with st.form("chat_form"):
    user_input = st.text_input("Ask anything:")
    submitted = st.form_submit_button("Get Response")

if submitted and user_input:
    response = openai.ChatCompletion.create(
        model="mistral-7b",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write("Bot:", response.choices[0].message["content"])
