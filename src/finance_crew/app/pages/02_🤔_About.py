import streamlit as st
from finance_crew.app.components.content.reference_links import reference_links
from finance_crew.app.components.content.project_description import project_description
from finance_crew.app.components.content.mermaid_diagram import mermaid_diagram

st.set_page_config(page_title="Finance Crew - About", page_icon="💹", layout="wide")

def About():
    st.title("🤔 About Finance Crew")
    reference_links()
    project_description()
    mermaid_diagram()

if __name__ == "__main__":
    About()
