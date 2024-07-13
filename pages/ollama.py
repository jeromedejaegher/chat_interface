from utils.logger import custom_logger
import streamlit as st

if "logger" not in st.session_state:
    logger = st.session_state["logger"] = custom_logger()

with st.sidebar:
    model = st.selectbox(
        label="Model to use", 
        options=[elem for elem in "abc"], index=0,   
        placeholder="Choose an option"
        )