from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
import streamlit as st
import os


st.title("Mini-chatgpt4.1")

def generate_response(input_text):
    model = AzureAIChatCompletionsModel(
    endpoint = "https://models.github.ai/inference",
    model = "openai/gpt-4.1",
    credential = os.environ["GITHUB_TOKEN"]

)
    
    response = model.invoke(input_text)

    st.info(response.content)

with st.form("chat_interface"):
    text = st.text_area(
        "Enter your message:",
        height=200,
    )
    
    submitted = st.form_submit_button("Send")
    generate_response(text)