from utils.ollama_utils import (
    preprocess_stream,
)
from utils.logger import custom_logger
import streamlit as st
import ollama

if "logger" not in st.session_state:
    logger = st.session_state["logger"] = custom_logger()

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

st.title("ChatGPT-like clone")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
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