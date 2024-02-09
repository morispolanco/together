import streamlit as st
import requests

# Configuración de la página de Streamlit
st.set_page_config(page_title="Together API Playground", layout="wide")

# Título de la página
st.title("Together API Playground")

# Input para el prompt
prompt = st.text_input("Ingrese su prompt aquí")

# Botón para enviar el prompt
if st.button("Enviar"):
    # Endpoint de la API
    endpoint = 'https://api.together.xyz/v1/completions'

    # Datos del prompt
    data = {
        "model": "Qwen/Qwen1.5-72B",
        "max_tokens": 512,
        "prompt": prompt,
        "request_type": "language-model-inference",
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "promptObj": {
            "prompt": prompt
        }
    }

    # Headers de la petición
    headers = {
        "Authorization": "Bearer 5b454cb09f602c2a2dbf5f04380d62c027dd26689a962fde4b10bc21b2624abd",
    }

    # Enviar la petición a la API
    res = requests.post(endpoint, json=data, headers=headers)

    # Mostrar la respuesta de la API
    st.write(res.json())
