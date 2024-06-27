from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI()

st.title('chatbot')

content = st.text_input('시의 주제를 제시해 주세요')

result = "" 

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성중'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
st.write(result)

