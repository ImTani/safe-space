from ollama import Client
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
ollama_host = os.getenv("ollama_host")

client = Client(host=ollama_host)
model = "qwen2.5:14b"

def generate_message(prompt: str):
    response = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": "start"},
            {"role": "user", "content": prompt},
        ],
        options={
            "temperature": 0.8,
        },
        stream=False
    )

    return response["message"]["content"]

def main():
    st.title("Ollama Chatbot")
    prompt = st.text_area("Enter your message here:")
    if st.button("Generate"):
        response = generate_message(prompt)
        st.write(response)

if __name__ == "__main__":
    main()