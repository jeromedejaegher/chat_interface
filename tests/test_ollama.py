"""LLM generated tests... of course ;)
"""
import pytest
import logging, sys, os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config.config import ROOT_DIR
from utils.ollama_utils import preprocess_stream
from utils.logger import custom_logger
import streamlit as st
import ollama

def test_preprocess_stream():
    # Test that the preprocess_stream function works correctly with a given stream
    stream = [
        {
            "message": {"content": "Hello,"}
        },
        {
            "message": {"content": "world!"} 
        },
    ]

    processed_stream = preprocess_stream(stream)
    assert " ".join(processed_stream) == "Hello, world!"

def test_custom_logger():
    # Test that the custom logger is created and used correctly
    logger = custom_logger()
    assert isinstance(logger, logging.Logger)

def test_ollama_list():
    # Test that the ollama.list() function works correctly and returns a list of models
    models = ollama.list()["models"]
    assert isinstance(models, list)
    for model in models:
        assert "model" in model

def test_st_sidebar():
    # Test that the st.sidebar module is imported correctly and can be used to create a select box
    ai_model = st.selectbox("Model to use", ["llama3", "codellama"])
    assert ai_model in ("llama3", "codellama")



def test_ollama_chat():
    # Test that the ollama.chat function is imported correctly and can be used to get a response from an AI model
    stream = ollama.chat(model="llama3", messages=[{"role": "user", "content": "Please give me only one word"}], stream=True)
    for elem in stream:
        assert isinstance(elem, dict)
    response = ' '.join(preprocess_stream(stream))
    assert isinstance(response, str)