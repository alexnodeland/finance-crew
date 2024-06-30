import streamlit as st
from datetime import datetime
from finance_crew.utils.load_configs import load_example_inputs

def parameters():
    st.info("Please fill in the input parameters below to generate a comprehensive financial analysis report. This tool helps you make informed investment decisions based on your preferences and risk tolerance.")
    example_inputs = load_example_inputs()
    st.subheader("User Inputs")
    stock_selection = st.text_input("Stock Selection", value=example_inputs["stock_selection"], help="Enter stock symbols separated by commas")
    initial_capital = st.number_input("Initial Capital ($)", value=float(example_inputs["initial_capital"]), min_value=0.0, help="Enter your initial investment amount")
    risk_tolerance = st.select_slider("Risk Tolerance", options=["Very Low", "Low", "Medium", "High", "Very High"], value=example_inputs["risk_tolerance"], help="Select your risk tolerance level")
    trading_strategy_preference = st.selectbox("Trading Strategy", 
                                               options=["Day Trading", "Swing Trading", "Position Trading", "Scalping"],
                                               index=0,
                                               help="Choose your preferred trading strategy")
    news_impact_consideration = st.checkbox("Consider News Impact", value=example_inputs["news_impact_consideration"], help="Include news analysis in the trading strategy")
    
    return {
        "stock_selection": stock_selection,
        "initial_capital": initial_capital,
        "risk_tolerance": risk_tolerance,
        "trading_strategy_preference": trading_strategy_preference,
        "news_impact_consideration": news_impact_consideration,
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }