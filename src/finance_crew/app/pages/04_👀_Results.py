import os
import streamlit as st
from finance_crew.app.components.output.download_buttons import download_buttons
from finance_crew.app.components.content.no_results_warning import no_results_warning


st.set_page_config(page_title="Finance Crew - Results", page_icon="💹", layout="wide")

def Results():
    st.title("👀 Analysis Results")

    if not os.path.exists("output/analysis.md"):
        no_results_warning()
        return
    
    download_buttons()

if __name__ == "__main__":
    Results()
