import streamlit as st
import os

def download_buttons():
    st.subheader("Download Results")

    col1, col2 = st.columns(2)
    for i, (file_name, info) in enumerate(output_file_info.items()):
        file_path = f"output/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_content = file.read()
            with (col1 if i % 2 == 0 else col2):
                with st.container(border=True, height=300):
                    st.markdown(
                        f"""
                        <div style="height: 200px; overflow-y: auto;">
                            <h1 style="font-size: 24px;">{info['icon']} {info['title']}</h1>
                            <p><strong>{info['description']}</strong></p>
                            <p><small>{info['content']}</small></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    c1, c2 = st.columns([1, 5])
                    with c1:
                        st.popover("👀").markdown(file_content)
                    with c2:
                        st.download_button(
                            label=f"Download {file_name}",
                            data=file_content,
                            file_name=file_name,
                            mime="text/markdown" if file_name.endswith(".md") else "text/plain",
                            use_container_width=True
                        )

output_file_info = {
        "analysis.md": {
            "icon": "📊",
            "title": "Complete Analysis Report",
            "description": "Comprehensive market analysis using AI-powered insights.",
            "content": "Technical indicators, fundamental analysis, and sentiment analysis results"
        },
        "data_analysis.md": {
            "icon": "📈",
            "title": "Detailed Data Analysis",
            "description": "In-depth examination of market data and trends.",
            "content": "Statistical analysis, visualizations, and interpretation of key metrics"
        },
        "strategy_development.md": {
            "icon": "🎯",
            "title": "Strategy Development Insights",
            "description": "AI-generated trading strategies based on market insights.",
            "content": "Proposed strategies, rationale, and potential impact"
        },
        "execution_planning.md": {
            "icon": "📅",
            "title": "Execution Plan and Timeline",
            "description": "Optimal trade execution plans considering market conditions.",
            "content": "Entry/exit points, position sizing, and liquidity considerations"
        },
        "risk_assessment.md": {
            "icon": "🛡️",
            "title": "Risk Assessment and Mitigation",
            "description": "Comprehensive analysis of potential risks and safeguards.",
            "content": "Market risks, operational risks, and proposed risk management techniques"
        },
        "log.txt": {
            "icon": "📝",
            "title": "Analysis Process Log",
            "description": "Detailed log of the entire AI-powered analysis process.",
            "content": "Timestamps, steps taken, and notable events during the CrewAI workflow execution"
        }
    }
