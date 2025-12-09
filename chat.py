import streamlit as st
from langchain_openai import ChatOpenAI

st.title("LangChain × Streamlit Chatbot")

openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

    user_input = st.text_input("質問を入力してください")

    if st.button("送信"):
        result = llm.invoke(user_input)
        st.write("回答：", result.content)
