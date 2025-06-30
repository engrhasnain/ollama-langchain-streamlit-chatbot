import streamlit as st


from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please responsed to the question asked"),
        ("user", "Question {question}")
    ]
)


st.title("Langchain Demo w.r.t to Gemma Model")
input_text = st.text_input("What is question on your mind?")


llm = Ollama(model = "gemma2:2b")

chain = prompt|llm|StrOutputParser()

if input_text:
    st.write(chain.invoke({"question": input_text}))

