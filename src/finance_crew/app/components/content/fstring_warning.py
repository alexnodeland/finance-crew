import streamlit as st

def fstring_warning():
    st.warning(
        """
            Warning: 
            
            ```
            Do NOT modify the variable names inside curly braces {} in f-strings. 
                    
            Changing these variable names can break the analysis input page. 
                    
            Keep the variable names exactly as they are. 
                    
            You can change the surrounding text, reuse the variables, or use variables from other agents or tasks.
            ```
        """
    )