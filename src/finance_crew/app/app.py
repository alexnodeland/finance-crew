import streamlit as st
from datetime import datetime
from finance_crew.crew import FinanceCrew
from finance_crew.utils.utils import load_agent_config, load_example_inputs

def app():
    def run_analysis(finance_crew, inputs, result_placeholder):
        result = finance_crew.crew().kickoff(inputs=inputs)
        with open("output/analysis.md", "w") as file:
            file.write(result if result is not None else "")
        st.session_state.analysis_complete = True
        result_placeholder.success("Financial analysis generated successfully! 🎉")
        st.set_page_config(page_title="Finance Crew", page_icon="💹")

    # Load agent configurations
    agent_config = load_agent_config()

    with st.sidebar:
        st.header("Settings")
        ai_provider = st.selectbox("AI Provider", options=["-", "OpenAI", "Anthropic"], index=0)

        if ai_provider == "OpenAI":
            st.subheader("OpenAI Settings")

            openai_api_key = st.text_input("OpenAI API Key", type="password")
            
            with st.expander("Manager"):
                st.selectbox("Model", options=["gpt-4o", "gpt-3.5-turbo"], key="manager_model")
                st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, key="manager_temperature")

            st.subheader("Agents")
            agent_roles = ["data_analyst", "trading_strategy_developer", "trade_advisor", "risk_advisor"]
            
            for role in agent_roles:
                with st.expander(role.replace("_", " ").title()):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write("Settings")
                    with col2:
                        with st.popover("ℹ️", use_container_width=True):
                            st.markdown(f"""
                            **Role:** {agent_config[role]['role']}
                            
                            **Goal:** {agent_config[role]['goal']}
                            
                            **Backstory:** {agent_config[role]['backstory']}
                            
                            **Tools:**
                            - Scrape Website Tool
                            - SerperDev Tool
                            """)
                    st.selectbox("Model", options=["gpt-3.5-turbo", "gpt-4o"], key=f"{role}_model")
                    st.slider("Temperature", 0.0, 1.0, 0.5, 0.1, key=f"{role}_temperature")
        if ai_provider == "Anthropic":
            st.subheader("Anthropic Settings")
            st.write("Support for Claude 3.5 Sonnet coming soon!")

    st.title("Welcome to Finance Crew! 💹📊")

    # Initialize session state
    if 'files_generated' not in st.session_state:
        st.session_state.files_generated = False

    # Load example inputs
    example_inputs = load_example_inputs()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Parameters")
        stock_selection = st.text_input("Stock Selection", value=example_inputs["stock_selection"], help="Enter stock symbols separated by commas")
        initial_capital = st.number_input("Initial Capital ($)", value=float(example_inputs["initial_capital"]), min_value=0.0, help="Enter your initial investment amount")
        risk_tolerance = st.select_slider("Risk Tolerance", options=["Low", "Medium", "High"], value=example_inputs["risk_tolerance"], help="Select your risk tolerance level")
        trading_strategy_preference = st.selectbox("Trading Strategy", 
                                                   options=["Day Trading", "Swing Trading", "Position Trading", "Scalping"],
                                                   index=0,
                                                   help="Choose your preferred trading strategy")
        news_impact_consideration = st.checkbox("Consider News Impact", value=example_inputs["news_impact_consideration"], help="Include news analysis in the trading strategy")

    with col2:
        st.subheader("Analysis Generation")
        if st.button("Generate Financial Analysis", use_container_width=True):
            financial_trading_inputs = {
                "stock_selection": stock_selection,
                "initial_capital": initial_capital,
                "risk_tolerance": risk_tolerance,
                "trading_strategy_preference": trading_strategy_preference,
                "news_impact_consideration": news_impact_consideration,
                "current_date": datetime.now().strftime("%Y-%m-%d"),
            }

            with st.spinner("Generating financial analysis... 📈"):
                finance_crew = FinanceCrew()
                result = finance_crew.crew().kickoff(inputs=financial_trading_inputs)

                with open("output/analysis.md", "w") as file:
                    file.write(result if result is not None else "")

            st.success("Financial analysis generated successfully! 🎉")
            st.session_state.files_generated = True


    if st.session_state.get('files_generated', False):
        # Display analysis.md content
        with open("output/analysis.md", "r") as file:
            analysis_content = file.read()
        st.markdown(analysis_content)

        # Provide download buttons for the generated files
        col1, col2, col3 = st.columns(3)

        file_names = [
            "analysis.md", "data_analysis.md", "strategy_development.md",
            "execution_planning.md", "risk_assessment.md", "log.txt"
        ]

        for i, file_name in enumerate(file_names):
            with open(f"output/{file_name}", "r") as file:
                file_content = file.read()
            
            with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
                st.download_button(
                    label=f"Download {file_name}",
                    data=file_content,
                    file_name=file_name,
                    mime="text/markdown" if file_name.endswith(".md") else "text/plain",
                )