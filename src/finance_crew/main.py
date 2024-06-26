import json
import time
from datetime import datetime
from finance_crew.crew import FinanceCrew


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


if __name__ == "__main__":
    cli()
