import streamlit as st
import yaml

def load_config():
    with open("src/finance_crew/config/crew.yaml", "r") as file:
        return yaml.safe_load(file)

def save_config(config):
    with open("src/finance_crew/config/crew.yaml", "w") as file:
        yaml.safe_dump(config, file)

def render_manager_settings():
    config = load_config()
    manager_model_default = config['manager_llm']['model']
    manager_temperature_default = config['manager_llm']['temperature']

    with st.container(border=True):
        st.write("#### Configure Manager Agent")
        with st.expander("Instructions"):
            st.markdown(f"""
            ##### How to configure your Manager agent

            This section allows you to configure the settings for the Manager. The Manager is responsible for overseeing the operations of the AI crew and coordinating the tasks assigned to each agent. Follow the steps below to update the manager agent configuration:

            1. **Model Settings**:
                - **Model**: Select the language model to be used by the Manager (e.g., `gpt-3.5-turbo` or `gpt-4o`).
                - **Temperature**: Adjust the temperature setting for the model, which controls the randomness of the output.

            2. **Saving Changes**:
                - After making changes, click the "Save" button to update the configurations. A success message will confirm that the settings have been saved.
            """)
        
        with st.container(border=True):
            st.write("#### Model Settings")
            
            manager_model = st.selectbox("Model", options=["gpt-4o", "gpt-3.5-turbo"], key="manager_model", index=["gpt-4o", "gpt-3.5-turbo"].index(manager_model_default))
            manager_temperature = st.slider("Temperature", 0.0, 1.0, manager_temperature_default, 0.1, key="manager_temperature")

            if manager_model != manager_model_default or manager_temperature != manager_temperature_default:
                if st.button("Save Changes"):
                    config['manager_llm']['model'] = manager_model
                    config['manager_llm']['temperature'] = manager_temperature
                    save_config(config)
                    st.success("Configuration updated successfully.")