import streamlit as st
from datetime import datetime
from finance_crew.crew import FinanceCrew
from finance_crew.app.components.input.parameters import parameters
from finance_crew.app.components.output.analysis_result import analysis_result
from finance_crew.app.utils.run_analysis import run_analysis

st.set_page_config(page_title="Finance Crew - Analysis", page_icon="💹", layout="wide")

def Analysis():
    st.title("✨ Generate Financial Analysis")

    financial_trading_inputs = parameters()
    
    if st.button("Generate Financial Analysis", use_container_width=True):
        with st.spinner("Generating financial analysis... 📈"):
            finance_crew = FinanceCrew()
            result_placeholder = st.empty()
            run_analysis(finance_crew, financial_trading_inputs, result_placeholder)
        
        analysis_result(result_placeholder)

if __name__ == "__main__":
    Analysis()