import subprocess as sp
import streamlit as st
import ollama

from utils.ollama_utils import (
    preprocess_stream,
)
from utils.logger import custom_logger


if "logger" not in st.session_state:
    st.session_state["logger"] = custom_logger()

logger = st.session_state["logger"]

model_list = ["llama3", "codellama"]
print(f"model_list :")
print([model["model"] for model in ollama.list()["models"]])
model_list = sorted(
    model["model"] for model in ollama.list()["models"]
    )

with st.sidebar:
    st.session_state["ai_model"] = st.selectbox(
        label="Model to use", 
        options=model_list, index=0,   
        placeholder="Choose an option"
        )
    st.text(body="get a new model :")
    st.page_link(page="https://ollama.com/library")
    
    if new_model := st.text_input(placeholder="indiquer ici le modele à télécharger"):
        sp.Popen(args=["ollama", "run", new_model])

st.title("ChatGPT-like clone")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Posez votre question ici..."):
    
    logger.info(msg=f'role: user, content: {prompt}')

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
        )
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = ollama.chat(
    model=st.session_state["ai_model"],
    messages=[
        {'role': 'user', 'content': prompt}
        ],
    stream=True,
    )
    
    response = st.write_stream(preprocess_stream(stream))
    st.session_state.messages.append({"role": "assistant", "content": response})

    logger.info(msg=f'role: assistant, content: {response}')
