import streamlit as st
from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

def chat():
    user_input = st.text_input('Enter your message:')
    response = chatbot.get_response(user_input)
    st.write('Chatbot:', response)

st.title('Chatbot')
chat()
