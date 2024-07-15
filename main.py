"""
Menu : 
    - manage chat_list/params/credentials/prompt
    - chat
    - open/search logs

Comparatif des offres : 
- Google : 1er modele a priori gratuit pour usage raisonnable
- OpenAI : min 5€
- Mistral : 1 mois gratuit, puis abonnement

TODO : 
- logger

"""

import os
import subprocess as sp
import yaml
import streamlit as st
import ollama
from utils.ollama_utils import (
    preprocess_stream,
)
from config.config import ROOT_DIR
from utils.logger import custom_logger

if "logger" not in st.session_state:
    st.session_state["logger"] = custom_logger()

logger = st.session_state["logger"]

if "config.yaml" not in os.listdir(
    os.path.join(ROOT_DIR, "config")
    ):
    sp.run(args=["ollama", "pull", "llama3:latest"])
    config={"initialized":True}
    with open(os.path.join(ROOT_DIR, "config", "config.yaml"),"w") as f:
        yaml.dump(config, f)

print(f"model_list :")
try:
    print([model["model"] for model in ollama.list()["models"]])
    model_list = sorted(
        model["model"] for model in ollama.list()["models"]
        )
except:
    model_list = ["llama3", ]


with st.sidebar:
    st.session_state["ai_model"] = st.selectbox(
        label="Model to use", 
        options=model_list, index=0,   
        placeholder="Choose an option"
        )
    st.text(body="get a new model :")
    st.page_link(
        label="available models", 
        page="https://ollama.com/library"
        )
    
    if new_model := st.text_input(
        label="download new model",
        placeholder="indiquer ici le modele à télécharger"
        ):
        sp.Popen(args=["ollama", "pull", new_model])
        logger.info(f"sending 'olama pull {new_model}' command")

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
