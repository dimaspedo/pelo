import streamlit as st
from groq import Groq


st.set_page_config(page_title='Mi primer CHATBOT', page_icon='smile')


MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def congif_chatbot():
    st.sidebar.title('Elección de modelos IA')
    elejirModelo = st.sidebar.selectbox('',options=MODELOS,index=0)

    if elejirModelo == 'llama3-8b-8192':
        st.header(f'llama3-8b-8192')
    elif elejirModelo == 'llama3-70b-8192':
        st.header(f'llama3-70b-8192')
    elif elejirModelo == 'mixtral-8x7b-32768':
        st.header(f'mixtral-8x7b-32768')

    return elejirModelo


modelo = congif_chatbot()


def config_user_groq():
    api_key = st.secrets["API_KEY"]
    return Groq(api_key=api_key)


def config_model(cliente,modelo, mensajeRecibo):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensajeRecibo}],
        stream=True
    )



clienteUsuario = config_user_groq()

mensaje = st.chat_input('ENVIA UN MENSAJE A CHATGPT')

print(mensaje)

if mensaje:
    config_model(clienteUsuario,modelo,mensaje)
    print(mensaje)
