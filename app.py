import streamlit as st
import google.generativeai as genai

st.title("GenAI Common Project 1 - Simple chat-bot")

API_KEY = st.secrets["API_KEY"]

genai.configure(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    st.session_state.chat = model.start_chat(history=[])
    
with st.sidebar:
    if st.button("Clear History"):
        st.session_state.messages = []
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_text = st.chat_input("Ask your query here...")

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    response = st.session_state.chat.send_message(user_text)
    st.session_state.messages.append({"role": "assisstant", "content": response.text})
    st.rerun()