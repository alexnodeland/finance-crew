import streamlit as st

def reference_links():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.page_link("https://github.com/alexnodeland/finance-crew", label="View GitHub Repository", icon="🚀")
    with col2:
        st.page_link("https://www.linkedin.com/feed/update/urn:li:activity:7211752576269062146/", label="View on LinkedIn", icon="🔗")