import json
import yaml
import time
from datetime import datetime
import subprocess
import streamlit as st
from finance_crew.crew import FinanceCrew

def load_agent_config():
    with open("src/finance_crew/config/agents.yaml", "r") as file:
        return yaml.safe_load(file)

def load_example_inputs():
    with open("data/cli-default.json", "r") as file:
        return json.load(file)


def cli():
    # ANSI escape codes for styling
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"

    print(f"{BOLD}{BLUE}Welcome to the Finance Crew CLI!{END}")
    print(f"{BOLD}{BLUE}=============================={END}\n")

    # Add an ASCII art logo
    print(f"{YELLOW}")
    print(
        r"""

░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓█████████████▓▒░ 
    """
    )
    print(f"{END}\n")

    # Load example inputs from cli-default.json
    print(f"{YELLOW}Loading example inputs...{END}")
    example_inputs = load_example_inputs()
    print(f"{GREEN}Example inputs loaded successfully.{END}\n")

    # Prompt the user for inputs, using example inputs if left blank
    stock_selection = (
        input(f"{BOLD}Enter stock selection (leave blank for default): {END}")
        or example_inputs["stock_selection"]
    )
    initial_capital = (
        input(f"{BOLD}Enter initial capital (leave blank for default): {END}")
        or example_inputs["initial_capital"]
    )
    risk_tolerance = (
        input(f"{BOLD}Enter risk tolerance (leave blank for default): {END}")
        or example_inputs["risk_tolerance"]
    )
    trading_strategy_preference = (
        input(
            f"{BOLD}Enter trading strategy preference (leave blank for default): {END}"
        )
        or example_inputs["trading_strategy_preference"]
    )
    news_impact_consideration = (
        input(
            f"{BOLD}Consider news impact? (True/False, leave blank for default): {END}"
        )
        or example_inputs["news_impact_consideration"]
    )

    # Define the inputs for the financial trading process
    financial_trading_inputs = {
        "stock_selection": stock_selection,
        "initial_capital": initial_capital,
        "risk_tolerance": risk_tolerance,
        "trading_strategy_preference": trading_strategy_preference,
        "news_impact_consideration": news_impact_consideration,
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }

    print(f"\n{UNDERLINE}Inputs received:{END}")
    print(f"{BOLD}Stock Selection:{END} {stock_selection}")
    print(f"{BOLD}Initial Capital:{END} {initial_capital}")
    print(f"{BOLD}Risk Tolerance:{END} {risk_tolerance}")
    print(f"{BOLD}Trading Strategy Preference:{END} {trading_strategy_preference}")
    print(f"{BOLD}News Impact Consideration:{END} {news_impact_consideration}\n")

    # Add a loading animation
    print(f"\n{YELLOW}Initializing Finance Crew...{END}")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

    # Create the FinanceCrew instance
    #agentops.init()
    finance_crew = FinanceCrew()

    # Kickoff the process
    result = finance_crew.crew().kickoff(inputs=financial_trading_inputs)

    # Save the result to a file
    with open("output/analysis.md", "w") as file:
        file.write(result if result is not None else "")
    # You can add any post-processing or result handling here
    print(f"\n{GREEN}Process completed. Here are the results:{END}")
    print(result)

    # Add a fun message at the end
    print(
        f"\n{BOLD}{GREEN}🎉 Your financial analysis is ready! Check 'analysis.md' for details! 🚀{END}"
    )

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

def run_app():
    subprocess.run(["streamlit", "run", "src/finance_crew/main.py"])

if __name__ == "__main__":
    app()
