import streamlit as st
from finance_crew.utils.load_configs import load_agent_config, save_agent_config, load_crew_config, save_crew_config

def render_agent_settings():
    agent_roles = ["data_analyst", "trading_strategy_developer", "trade_advisor", "risk_advisor"]

    agent_config = load_agent_config()
    crew_config = load_crew_config()
    
    with st.expander("Agent Config"):        
        st.write(agent_config)
    
    agent_tabs = st.tabs([role.replace("_", " ").title() for role in agent_roles])
    
    for role, tab in zip(agent_roles, agent_tabs):
        with tab:
            render_agent_role_settings(role, agent_config, crew_config)

def render_agent_role_settings(role, agent_config, crew_config):
    agent_config_role = agent_config.get(role, {})
    crew_config_role = crew_config.get("agents", {}).get(role, {})
    
    # Use session state to track changes
    if f"{role}_changed" not in st.session_state:
        st.session_state[f"{role}_changed"] = False

    def mark_changed():
        st.session_state[f"{role}_changed"] = True

    with st.expander("Model Settings"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("Settings")
        with col2:
            st.write("")  # Placeholder for alignment
        model = st.selectbox("Model", options=["gpt-3.5-turbo", "gpt-4o"], 
                             key=f"{role}_model", 
                             index=["gpt-3.5-turbo", "gpt-4o"].index(crew_config_role.get("llm", {}).get("model", "gpt-3.5-turbo")),
                             on_change=mark_changed)
        temperature = st.slider("Temperature", 0.0, 1.0, 
                                crew_config_role.get("llm", {}).get("temperature", 0.5), 0.1, 
                                key=f"{role}_temperature",
                                on_change=mark_changed)
        
    # Display agent config and tools
    goal = st.text_area("Role Goal", value=agent_config_role.get("goal", ""), 
                        key=f"{role}_goal", on_change=mark_changed)
    backstory = st.text_area("Role Description", value=agent_config_role.get("backstory", ""), 
                             key=f"{role}_backstory", on_change=mark_changed)
    allow_delegation = st.checkbox("Allow Delegation", value=crew_config_role.get("allow_delegation", False), 
                                   key=f"{role}_allow_delegation", on_change=mark_changed)

    if st.session_state[f"{role}_changed"]:
        if st.button("Save", key=f"{role}_save"):
            # Update agent config
            new_agent_config = {
                "goal": goal,
                "backstory": backstory,
            }
            save_agent_config(role, new_agent_config)
            
            # Update crew config
            crew_config["agents"][role] = {
                "allow_delegation": allow_delegation,
                "llm": {
                    "model": model,
                    "temperature": temperature
                }
            }
            save_crew_config(crew_config)
            
            st.success(f"Configuration for {role} saved successfully.")
            st.session_state[f"{role}_changed"] = False