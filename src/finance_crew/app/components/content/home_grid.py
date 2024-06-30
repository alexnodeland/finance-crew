import streamlit as st

def home_grid():
    st.markdown("## What would you like to do?")

    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("📊 Market Analysis")
            st.write("Generate comprehensive market analysis using a multi-agent LLM system")
            st.page_link("pages/03_✨_Analysis.py", label="Start Custom Analysis", icon="✨")
        
        with st.container(border=True):
            st.subheader("⚙️ Settings")
            st.write("Configure your API keys and AI agent settings for optimal performance")
            st.page_link("pages/05_⚙_Settings.py", label="Configure Settings", icon="🎛️")
    
    with col2:
        with st.container(border=True):
            st.subheader("📈 Results")
            st.write("View your analysis results and download detailed reports from your AI agents")
            st.page_link("pages/04_👀_Results.py", label="View Results", icon="👀")
        
        with st.container(border=True):
            st.subheader("❓ Help & Resources")
            st.write("Learn more about Finance Crew and how to maximize its potential")
            st.page_link("pages/02_🤔_About.py", label="About Finance Crew", icon="ℹ️")