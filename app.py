import streamlit as st
from chatbot.chatbot_engine import Chatbot

# Initialize the chatbot (ensure the path to your text file is correct)
chatbot = Chatbot("knowledgebase.txt")

st.title("TradingBot")
st.write("Ask me anything about the financial Market!")

# Create a chat history list to store user and chatbot messages
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history with messenger-like interface
for index, message in enumerate(st.session_state.chat_history):
    if "user" in message:
        st.text_input(f"You {index + 1}:", value=message["user"], disabled=True)
    if "chatbot" in message:
        st.text_input(f"Chatbot {index + 1}:", value=message["chatbot"], disabled=True)

user_input = st.text_input("You: ")

if st.button('Send'):
    if user_input:
        # Get chatbot response
        response = chatbot.response(user_input)

        # Add user input and chatbot response to chat history
        st.session_state.chat_history.append({"user": user_input, "chatbot": response})
