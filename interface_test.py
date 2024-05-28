#git clone https://github.com/sychhq/llama-cpp-setup.git && cd llama-cpp-setup && chmod +x setup.sh &&./setup.sh
#https://github.com/sychhq/llama-cpp-setup

import streamlit as st
import pandas as pd
from streamlit_chat import message
from langchain_community.llms import CTransformers

# Set the title of the Streamlit application
st.title("Llama2 Chat CSV - 🦜🦙")

# Create a sidebar with a file uploader
uploaded_file = st.sidebar.file_uploader("Upload File", type="csv")

# Create a chat box
user_input = st.text_input("Enter a command:")

# Create a submit button
submit_button = st.button("Send")

# Create a container to hold the chat history
response_container = st.container()

# Initialize the chat history
if "past" not in st.session_state:
    st.session_state["past"] = []
if "generated" not in st.session_state:
    st.session_state["generated"] = []

# Define a function to load the language model
# def load_llm():
    # Load the locally downloaded model here
    # llm = CTransformers(
    #     model="llama-2-7b-chat.ggmlv3.q8_0.bin",
    #     model_type="llama",
    #     max_new_tokens=512,
    #     temperature=0.5
    # )



def load_llm():
    from ctransformers import AutoModelForCausalLM
    llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML", model_file="llama-2-7b-chat.ggmlv3.q2_K.bin", hf=True)

    return llm
    return llm

# Load the language model
llm = load_llm()

# Define a function to handle user input and generate responses
def conversational_chat(user_input):
    # Call the language model to generate a response
    output = llm.generate_response(user_input)
    return output

# Handle user input and generate responses
if submit_button and user_input:
    output = conversational_chat(user_input)
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)

# Display the chat history
if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user", avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")