# chat_interface

1. Objective

A really simple chat interface to compare answers from some chat models on the market.


2. Installation

First, install ollama on your pc : 
[click here](https://ollama.com/download)

from the directory where you want to install if, run the following command lines :

~~~cmd
ollama pull llama3:latest
git clone https://github.com/jeromedejaegher/chat_interface.git
conda create --name <<NEW_ENV_NAME>> python=3.12
conda activate <<NEW_ENV_NAME>>
cd chat_interface
mkdir logs
pip install -r requirements.txt

~~~

2. Run the code

from the chat_interface directory, run the following command line :

```cmd
streamlit run main.py

```


