import streamlit as st

st.set_page_config(page_title="Finance Crew", page_icon="💹", layout="wide")

def main():
    st.title("Welcome to Finance Crew 💹")
    st.write("Your AI-powered financial analysis assistant")

    st.markdown("""
    ## What would you like to do?

    - [Generate Financial Analysis](/Analysis)
    - [Configure Settings](/Settings)
    - [View Previous Results](/Results)

    ### About Finance Crew

    Finance Crew is an AI-powered tool that helps you analyze financial trading strategies. 
    Our advanced AI agents work together to provide comprehensive insights into your 
    investment choices, risk assessment, and market trends.

    Get started by generating a new analysis or reviewing your previous results!
    """)

if __name__ == "__main__":
    main()