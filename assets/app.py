import os
import streamlit as st
from secret_key import key
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"]=key

llm=ChatGroq(temperature=0.6,model="openai/gpt-oss-120b")

def prompt(CountryName):
    question=f"what is the capital city of {CountryName}? Give me single answer"
    response= llm.invoke(question)
    return response.content.strip()

st.title("Groq Capital City Name Generator Chatbot")

country=st.text_input("Type country name:")

if st.button("Get Capital City"):
    if country:
        capital = prompt(country)

        st.success(f"The capital city of **{country}** is:\n")

        st.markdown(f"""
            <div style="font-family: monospace; font-size: 24px; padding: 10px; background-color: #000000; border-radius: 5px;">
                {capital}
            </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please enter a valid country name.")


