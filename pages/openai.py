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
- add context

"""

from openai import OpenAI
import streamlit as st
from utils.logger import custom_logger

if "logger" not in st.session_state:
    logger = st.session_state["logger"] = custom_logger()


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

model_list = client.models.list()
print(f"model_list :")
print(f"{[model.id for model in model_list.data]}")
model_list = sorted([model.id for model in model_list.data if "gpt" in model.id])

with st.sidebar:
    st.session_state["openai_model"] = st.selectbox(
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
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})