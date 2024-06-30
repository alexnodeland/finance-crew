import streamlit as st
from finance_crew.app.components.settings.keys import render_key_settings
from finance_crew.app.components.settings.manager import render_manager_settings
from finance_crew.app.components.settings.agent import render_agent_settings
from finance_crew.app.components.settings.tasks import render_task_settings

st.set_page_config(page_title="Finance Crew - Settings", page_icon="💹", layout="wide")

def Settings():
    st.title("Settings")
    st.write("Configure your AI providers, agent settings, and tasks here.")

    tabs = st.tabs(["API Keys", "Manager Settings", "Agent Settings", "Task Settings"])  # Add "Task Settings" tab

    with tabs[0]:
        render_key_settings()

    with tabs[1]:
        render_manager_settings()

    with tabs[2]:
        render_agent_settings()

    with tabs[3]:
        render_task_settings()

if __name__ == "__main__":
    Settings()