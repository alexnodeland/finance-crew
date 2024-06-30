import streamlit as st

def disclaimer():
    with st.expander("⚠️ Disclaimer"):
        st.markdown("""
        **IMPORTANT**: Finance Crew is an experimental tool designed for educational and research purposes only. It should not be used for real-world trading or financial decision-making. The insights and recommendations provided by this tool do not constitute financial advice and should not be interpreted as such.

        >- This tool is not licensed or regulated by any financial authority.
        >- The accuracy and reliability of the AI-generated insights have not been independently verified.
        >- Trading in financial markets carries significant risks, including the potential loss of your invested capital.
        >- Always consult with a qualified financial advisor before making any investment decisions.

        By using Finance Crew, you acknowledge that you understand these risks and agree to use this tool solely for educational or experimental purposes.

        Get started by generating a new analysis or reviewing your previous results!
        """)