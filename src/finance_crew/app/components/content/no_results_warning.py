import streamlit as st

def no_results_warning():
    with st.container(border=True):
        st.warning(
            """
            **It looks like you haven't generated any analysis results yet.**
            
            Get started by generating a new analysis or configuring your settings!
            """
        )
        col1, col2 = st.columns([1, 3])
        with col1:
            st.page_link("pages/03_✨_Analysis.py", label="Start Custom Analysis", icon="✨")
        with col2:
            st.page_link("pages/05_⚙_Settings.py", label="Configure Settings", icon="🎛️")