import streamlit as st
import random
import time

st.title("Simple chat")

#Initialize chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#Display chat message frm history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#Accept user input 
if prompt := st.chat_input("Howdyy!"):
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
#Add user message to chat historyb
st.session_state.messages.append({"role": "user", "content": prompt})

#Streamed response emulator 
def response_gentrator():
    response =  random.choice(
        [
            "Hilo there! How can i help you ?",
            "What can i do for you today ?",
            "Ksa chlriya h sb?",
            "Hilo biradar , kya haal h? ",
            "Hola amigo, kaise ho thik ho?",
            "Ghar pr kse h sb? Aunty ko bolna i'm sending my love<3",
        ]
    )
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
        
with st.chat_message("assistant"):
    response = st.write_stream(response_gentrator())
    
st.session_state.messages.append({"role":"assistant", "content" : response})
