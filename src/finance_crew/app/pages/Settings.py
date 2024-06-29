import streamlit as st
from finance_crew.utils.utils import load_agent_config

def render_ai_provider_settings():
    ai_provider = st.selectbox("AI Provider", options=["-", "OpenAI", "Anthropic"], index=0)

    if ai_provider == "OpenAI":
        render_openai_settings()
    elif ai_provider == "Anthropic":
        render_anthropic_settings()

def render_openai_settings():
    st.subheader("OpenAI Settings")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    
    render_manager_settings()
    render_agent_settings()

def render_manager_settings():
    with st.expander("Manager"):
        st.selectbox("Model", options=["gpt-4o", "gpt-3.5-turbo"], key="manager_model")
        st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, key="manager_temperature")

def render_agent_settings():
    st.subheader("Agents")
    agent_roles = ["data_analyst", "trading_strategy_developer", "trade_advisor", "risk_advisor"]
    
    for role in agent_roles:
        render_agent_role_settings(role)

def render_agent_role_settings(role):
    agent_config = load_agent_config()
    with st.expander(role.replace("_", " ").title()):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("Settings")
        with col2:
            render_agent_info_popover(role, agent_config)
        st.selectbox("Model", options=["gpt-3.5-turbo", "gpt-4o"], key=f"{role}_model")
        st.slider("Temperature", 0.0, 1.0, 0.5, 0.1, key=f"{role}_temperature")

def render_agent_info_popover(role, agent_config):
    with st.popover("ℹ️", use_container_width=True):
        st.markdown(f"""
        **Role:** {agent_config[role]['role']}
        
        **Goal:** {agent_config[role]['goal']}
        
        **Backstory:** {agent_config[role]['backstory']}
        
        **Tools:**
        - Scrape Website Tool
        - SerperDev Tool
        """)

def render_anthropic_settings():
    st.subheader("Anthropic Settings")
    st.write("Support for Claude 3.5 Sonnet coming soon!")

def main():
    st.title("Settings")
    st.write("Configure your AI providers and agent settings here.")

    render_ai_provider_settings()

    if st.button("Save Settings", use_container_width=True):
        # Implement logic to save settings
        st.success("Settings saved successfully!")

if __name__ == "__main__":
    main()