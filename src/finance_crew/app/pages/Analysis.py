import streamlit as st
from datetime import datetime
from finance_crew.crew import FinanceCrew
from finance_crew.utils.utils import load_example_inputs

def render_input_parameters():
    example_inputs = load_example_inputs()
    st.subheader("Input Parameters")
    stock_selection = st.text_input("Stock Selection", value=example_inputs["stock_selection"], help="Enter stock symbols separated by commas")
    initial_capital = st.number_input("Initial Capital ($)", value=float(example_inputs["initial_capital"]), min_value=0.0, help="Enter your initial investment amount")
    risk_tolerance = st.select_slider("Risk Tolerance", options=["Low", "Medium", "High"], value=example_inputs["risk_tolerance"], help="Select your risk tolerance level")
    trading_strategy_preference = st.selectbox("Trading Strategy", 
                                               options=["Day Trading", "Swing Trading", "Position Trading", "Scalping"],
                                               index=0,
                                               help="Choose your preferred trading strategy")
    news_impact_consideration = st.checkbox("Consider News Impact", value=example_inputs["news_impact_consideration"], help="Include news analysis in the trading strategy")
    
    return stock_selection, initial_capital, risk_tolerance, trading_strategy_preference, news_impact_consideration

def run_analysis(finance_crew, inputs, result_placeholder):
    result = finance_crew.crew().kickoff(inputs=inputs)
    with open("output/analysis.md", "w") as file:
        file.write(result if result is not None else "")
    st.session_state.analysis_complete = True
    result_placeholder.success("Financial analysis generated successfully! 🎉")

def main():
    st.title("Generate Financial Analysis")

    inputs = render_input_parameters()
    
    if st.button("Generate Financial Analysis", use_container_width=True):
        financial_trading_inputs = {
            **inputs,
            "current_date": datetime.now().strftime("%Y-%m-%d"),
        }

        with st.spinner("Generating financial analysis... 📈"):
            finance_crew = FinanceCrew()
            result_placeholder = st.empty()
            run_analysis(finance_crew, financial_trading_inputs, result_placeholder)
        
        st.success("Analysis complete! View the results in the 'Results' page.")

if __name__ == "__main__":
    main()