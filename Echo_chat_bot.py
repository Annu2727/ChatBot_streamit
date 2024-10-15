import streamlit as st
import numpy as np

st.title("Echo Bot")

#Initialize chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat message from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        
#React to user input 
if prompt := st.chat_input("Hola you there! "):
    #Display user message in chat message contaner 
    with st.chat_message("user"):
        st.markdown(prompt)

#Add user message to chat history 
st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"
#Display assistant response ini chat message 

with st.chat_message("assistant"):
    st.markdown(response)

st.session_state.messages.append({"role": "assistant", "content": response})