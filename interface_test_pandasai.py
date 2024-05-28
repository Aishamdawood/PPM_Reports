import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# ---------------
# st.set_page_config(layout="wide")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://github.com/Aishamdawood/images/blob/main/2.jpg?raw=true");
# background-size: cover;
# background-position: center center;
# background-repeat: no-repeat;
# background-attachment: local;
background: rgba(0,0,0,0);


}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
content: "Development Environment";

}}

[data-testid="stSidebarNav"] {{
background-image: url("https://github.com/Aishamdawood/images/blob/main/expro%20logo.PNG?raw=true");
content: "Development Environment";
background-repeat: no-repeat;
padding-top: 120px;
background-position: 20px 20px;
background-size: 90% auto;
background-color: dark grey;
}}
[data-testid="stSidebarNav"]::before {{
content: "Development Environment";
margin-left: 20px;
margin-top: 20px;
font-size: 20px;
position: relative;
top: 100px;
background-color: red;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#-----------------

# Set API key
os.environ['PANDASAI_API_KEY'] = "$2a$10$3lpg.RW0lsf63jzOdLm4XugvVLNAo.RKoCahPytqnpLS8Sk5e74ui"

# Create a Streamlit app
st.title("Report Automation use case: PPM_01")
st.text('29-5-2024')

# Upload dataframe
uploaded_file = st.file_uploader("Upload your dataframe (Excel file):", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Dataframe uploaded successfully!")

# Create a chat box
chat_input = st.text_input("Ask a question about your dataframe:")

# Create a button to submit the question
if st.button("Ask"):

    # Create a SmartDataframe object
    sdf = SmartDataframe(df)
    # Ask the question and display the output
    output = sdf.chat(chat_input+",Answerin arabic?")
    st.write(f"""{output}""")
