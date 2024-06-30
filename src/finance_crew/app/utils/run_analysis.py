from finance_crew.crew import FinanceCrew
import streamlit as st

def run_analysis(finance_crew, inputs, result_placeholder):
    result = finance_crew.crew().kickoff(inputs=inputs)
    with open("output/analysis.md", "w") as file:
        file.write(result if result is not None else "")
    st.session_state.analysis_complete = True
    result_placeholder.success("Financial analysis generated successfully! 🎉")