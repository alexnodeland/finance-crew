import streamlit as st
from finance_crew.utils.load_configs import load_task_config, save_task_config
from finance_crew.app.components.content.fstring_warning import fstring_warning

def render_task_settings():
    task_config = load_task_config()
    
    # with st.expander("Task Config"):        
    #     st.write(task_config)

    task_tabs = st.tabs([task.replace("_", " ").title() for task in task_config.keys()])
    
    for task, tab in zip(task_config.keys(), task_tabs):
        with tab:
            render_individual_task_settings(task, task_config)

def render_individual_task_settings(task, task_config):
    task_config_data = task_config.get(task, {})
    
    # Use session state to track changes
    if f"{task}_changed" not in st.session_state:
        st.session_state[f"{task}_changed"] = False

    def mark_changed():
        st.session_state[f"{task}_changed"] = True

    with st.container(border=True):
        st.write(f"#### Configure your {task.replace('_', ' ').title()} task")
        with st.expander("Instructions"):
            st.markdown(f"""
            ##### How to configure the {task.replace("_", " ").title()} task

            This section allows you to configure the settings for the {task.replace("_", " ").title()} task. Follow the steps below to update the configurations:

            1. **{task.replace("_", " ").title()} Task Details**:
                - **Description**: Provide a detailed description of the {task.replace("_", " ").title()} task.
                - **Expected Output**: Specify the expected output or result of the {task.replace("_", " ").title()} task.

            2. **Saving Changes**:
                - After making changes, click the "Save" button to update the configurations. A success message will confirm that the settings have been saved.
            """)
            
            fstring_warning()

        description = st.text_area("Description", 
                                   value=task_config_data.get("description", ""), 
                                   key=f"{task}_description", 
                                   on_change=mark_changed,
                                   help="""Provide a detailed description of the task. 
                                   Include the purpose, scope, and any specific details 
                                   that are important for understanding what this task entails.""")
        
        expected_output = st.text_area("Expected Output", 
                                       value=task_config_data.get("expected_output", ""), 
                                       key=f"{task}_expected_output", 
                                       on_change=mark_changed,
                                       help="""Specify the expected output or result of the task. 
                                       Describe what the successful completion of this task looks like, 
                                       including any deliverables or measurable outcomes.""")

    if st.session_state[f"{task}_changed"]:
        if st.button("Save", key=f"{task}_save"):
            # Update task config for this specific task
            updated_task_config = {
                "description": description,
                "expected_output": expected_output,
            }
            save_task_config(task, updated_task_config)
            
            st.success(f"Configuration for {task} saved successfully.")
            st.session_state[f"{task}_changed"] = False