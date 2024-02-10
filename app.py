import streamlit as st
import requests

endpoint = 'https://api.together.xyz/v1/chat/completions'
headers = {
    "Authorization": "Bearer 5b454cb09f602c2a2dbf5f04380d62c027dd26689a962fde4b10bc21b2624abd" 
}

def get_chat_completion(prompt):
    res = requests.post(endpoint, json={
        "model": "meta-llama/Llama-2-70b-chat-hf",
        "max_tokens": 512,
        "prompt": "[INST] {prompt} [/INST]".format(prompt=prompt),
        "request_type": "language-model-inference",
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stream_tokens": True,
        "stop": [
            "[/INST]".format(prompt=prompt),
            ""
        ],
        "promptObj": {
            "prompt": ""
        }
    }, headers=headers)
    return res.json()

prompt = st.text_input("Enter a prompt:")
chat_completion = get_chat_completion(prompt)
st.write(chat_completion)
