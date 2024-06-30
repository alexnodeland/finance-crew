import streamlit as st
from finance_crew.app.components.content.disclaimer import disclaimer
from finance_crew.app.components.content.home_grid import home_grid

st.set_page_config(page_title="Finance Crew", page_icon="💹", layout="wide")

def Home():
    st.title("Welcome to Finance Crew 💹")
    st.info("Your AI-powered financial analysis assistant")

    disclaimer()
    home_grid()
    
if __name__ == "__main__":
    Home()