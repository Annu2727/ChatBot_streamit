import streamlit as st
from openai import OpenAI

st.title("ChatBot like chatgpt")

client = OpenAI(api_key=st.secrets["OpenAi_API_KEY"])

#set a model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    
#Initialize char history 
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#Display chat msg from histry on app rerum
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
     st.markdown(message["content"])
     
#Accept user input
if prompt := st.chat_input("Hilo there!"):
    #Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
#Display assistant responsse in chat message container 
with st.chat_message("assistant"):
    stream = client.chat.completions.create(
        model =  st.session_state["openai_model"],
        messages= [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )
    response = st.write_stream(stream)

st.session_state.messages.append({"role": "assitant", "content": response})