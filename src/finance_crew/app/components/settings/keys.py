import os
import streamlit as st
from finance_crew.app.utils.api_validators import validate_openai_key, validate_serper_key

def render_key_settings():
    st.subheader("API Keys")
    status_message_placeholder = st.container()
    st.write("Please enter your keys below:")

    get_api_key_input("OpenAI API Key", validate_openai_key, "OPENAI_API_KEY")
    get_api_key_input("SerperDev API Key", validate_serper_key, "SERPER_API_KEY")

    display_warning_or_success(status_message_placeholder)

def get_api_key_input(label, validator, env_var):
    api_key = st.text_input(label, type="password")
    if api_key:
        if validator(api_key):
            os.environ[env_var] = api_key
            st.success(f"{label} validated and set successfully!")
        else:
            st.error(f"Invalid {label}. Please check and try again.")
    return api_key

def display_warning_or_success(status_message_placeholder):
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("SERPER_API_KEY"):
        status_message_placeholder.warning("""
        To use the features of this application, you need to provide API keys for the following services:
        
        - **OpenAI API Key**: 
            - This key is required to access OpenAI's API services, which provide powerful LLMs like `gpt-3.5-turbo` and `gpt-4o`. 
            - You can generate a key by creating an account and navigating to the API keys section [here](https://platform.openai.com/account/api-keys).
        - **SerperDev API Key**: 
            - This key is needed to use SerperDev's API, which offers search and scraping capabilities. 
            - You can create a free account and obtain your API key [here](https://serper.dev/).
        """)
    else:
        status_message_placeholder.success("API keys have been successfully set and validated!")