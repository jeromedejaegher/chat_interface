"""
WIP : to be tested with billing plan    

"""


from utils.logger import custom_logger
import google.generativeai as genai
# from openai import OpenAI
import streamlit as st

if "logger" not in st.session_state:
    logger = st.session_state["logger"] = custom_logger()

st.title("ChatGPT-like clone")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
client = genai.configure(api_key=st.secrets["GOOGLEAI_API_KEY"])


if "ai_model" not in st.session_state:
    st.session_state["ai_model"] = 'gemini-1.0-pro'

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

model=genai.GenerativeModel(st.session_state["ai_model"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = model.generate_content(
            prompt)
            
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})