from datetime import datetime
from finance_crew.crew import FinanceCrew
from finance_crew.utils.load_configs import load_example_inputs
from .ui import print_welcome_message, print_ascii_logo, loading_animation
from .input_handler import get_financial_trading_inputs
from .output_handler import display_inputs, save_result
from .utils import GREEN, BOLD, END

def cli():
    print_welcome_message()
    print_ascii_logo()

    example_inputs = load_example_inputs()
    financial_trading_inputs = get_financial_trading_inputs(example_inputs)
    financial_trading_inputs["current_date"] = datetime.now().strftime("%Y-%m-%d")

    display_inputs(financial_trading_inputs)

    loading_animation("Initializing Finance Crew...")

    finance_crew = FinanceCrew()
    result = finance_crew.crew().kickoff(inputs=financial_trading_inputs)

    save_result(result)

    print(f"\n{GREEN}Process completed. Here are the results:{END}")
    print(result)

    print(f"\n{BOLD}{GREEN}🎉 Your financial analysis is ready! Check 'analysis.md' for details! 🚀{END}")

if __name__ == "__main__":
    cli()