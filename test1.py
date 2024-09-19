## Run this file to start the Streamlit app: stremlit run test1.py
# This simple app allows you to ask questions from llama2 large language model
# The language model will be running locally inside a docker container
# before running the app please start the docker container by running the following commands
# docker pull ollama/ollama
# docker run -d -p 11434:11434 ollama/ollama

import streamlit as st
from langchain_community.llms import Ollama

# Initialize the Ollama object
ollama = Ollama(base_url='http://localhost:11434', model='llama2')


#App Framework
st.title("Ollama Streamlit app with LangChain 🦜🔗")

prompt=st.text_input("Insert in your prompt here")



#Show stuff to the screen if there is a prompt
if prompt:
    response = ollama.invoke(prompt)
    st.write(response)
