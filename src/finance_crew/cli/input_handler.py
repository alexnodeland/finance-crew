from .utils import BOLD, END

def get_user_input(prompt, default_value):
    return input(f"{BOLD}{prompt} (leave blank for default): {END}") or default_value

def get_financial_trading_inputs(example_inputs):
    return {
        "stock_selection": get_user_input("Enter stock selection", example_inputs["stock_selection"]),
        "initial_capital": get_user_input("Enter initial capital", example_inputs["initial_capital"]),
        "risk_tolerance": get_user_input("Enter risk tolerance", example_inputs["risk_tolerance"]),
        "trading_strategy_preference": get_user_input("Enter trading strategy preference", example_inputs["trading_strategy_preference"]),
        "news_impact_consideration": get_user_input("Consider news impact? (True/False)", example_inputs["news_impact_consideration"]),
    }