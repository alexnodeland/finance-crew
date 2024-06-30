import streamlit as st
from finance_crew.utils.load_configs import load_agent_config, save_agent_config, load_crew_config, save_crew_config
from finance_crew.app.components.content.fstring_warning import fstring_warning

def render_agent_settings():
    agent_roles = ["data_analyst", "trading_strategy_developer", "trade_advisor", "risk_advisor"]

    agent_config = load_agent_config()
    crew_config = load_crew_config()
    
    # with st.expander("Agent Config"):        
    #     st.write(agent_config)
    
    agent_tabs = st.tabs([role.replace("_", " ").title() for role in agent_roles])
    
    for role, tab in zip(agent_roles, agent_tabs):
        with tab:
            render_agent_role_settings(role, agent_config, crew_config)

def render_agent_role_settings(role, agent_config, crew_config):
    agent_config_role = agent_config.get(role, {})
    crew_config_role = crew_config.get("agents", {}).get(role, {})
    
    # Use a consistent key format for session state
    role_key = role.lower().replace(" ", "_")
    
    # Initialize session state
    if f"{role_key}_changed" not in st.session_state:
        st.session_state[f"{role_key}_changed"] = False

    def mark_changed():
        st.session_state[f"{role_key}_changed"] = True

    with st.container(border=True):
        st.write(f"#### Configure your {role.replace('_', ' ').title()} agent")
        with st.expander("Instructions"):
            st.markdown(f"""
            ##### How to configure your {role.replace('_', ' ').title()} agent

            This section allows you to configure the settings for the {role.replace('_', ' ').title()}. Follow the steps below to update the configurations:

            1. **Model Settings**:
                - **Model**: Select the language model to be used by the {role.replace('_', ' ').title()} (e.g., `gpt-3.5-turbo` or `gpt-4o`).
                - **Temperature**: Adjust the temperature setting for the model, which controls the randomness of the output.

            2. **Agent Configuration**:
                - **Role**: Displays the specific role of the {role.replace('_', ' ').title()} within the crew.
                - **Goal**: Enter the primary objective or purpose of the {role.replace('_', ' ').title()}'s role. Describe what the {role.replace('_', ' ').title()} aims to achieve.
                - **Backstory**: Provide a detailed background and context for the {role.replace('_', ' ').title()}'s role and responsibilities. Include relevant experience, skills, and personality traits.
                - **Allow Delegation**: Check this box to enable the {role.replace('_', ' ').title()} to delegate tasks to other agents in the crew.

            3. **Saving Changes**:
                - After making changes, click the "Save" button to update the configurations. A success message will confirm that the settings have been saved.
            """)
            
            fstring_warning()

        # Display agent config and tools
        st.text(f"Role: {role.replace('_', ' ').title()}", help="The specific role this agent plays within the crew.")

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
        
        goal = st.text_area("Goal", value=agent_config_role.get("goal", ""), 
                            key=f"{role}_goal", on_change=mark_changed,
                            help="""The primary objective or purpose of this agent's role.
                            Describe what this agent aims to achieve within the crew.""")
        backstory = st.text_area("Backstory", value=agent_config_role.get("backstory", ""), 
                                key=f"{role}_backstory", on_change=mark_changed,
                                help="""Detailed background and context for this agent's role and responsibilities.
                                Include relevant experience, skills, and personality traits that shape the agent's approach.""")
        allow_delegation = st.checkbox("Allow Delegation", value=crew_config_role.get("allow_delegation", False), 
                                    key=f"{role}_allow_delegation", on_change=mark_changed,
                                    help="""Enable this agent to delegate tasks to other agents in the crew.
                                    When checked, this agent can assign subtasks to other agents for more efficient teamwork.""")

    if st.session_state[f"{role_key}_changed"]:
        if st.button("Save", key=f"{role_key}_save"):
            # Update agent config
            new_agent_config = {
                "role": role,
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
            st.session_state[f"{role_key}_changed"] = False