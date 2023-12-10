from langchain.chat_models import ChatOpenAI
chat_models = ChatOpenAI()

import streamlit as st

st.title("AI Poem Generator")
theme = st.text_input('Type your poem theme here')

if st.button('Generate'):
    with st.spinner("Generating..."):
        result = chat_models.predict("write a poem about " + theme)
        st.write(result)




