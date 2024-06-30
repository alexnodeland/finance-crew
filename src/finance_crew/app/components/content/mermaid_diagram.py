import streamlit as st
import streamlit.components.v1 as components

def render_mermaid(code: str) -> None:
    components.html(
        f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <div class="mermaid" style="width: 100%; height: auto;">
            {code}
        </div>
        <script>
            mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
        </script>
        <style>
            .mermaid svg {{ max-width: 100%; height: auto; }}
        </style>
        """,
        height=600,
        scrolling=True
    )

def mermaid_diagram():
    st.markdown("### How it works:")
    render_mermaid(
        """
        graph TB
            A((Start)) --> B[Data Analysis Task]
            B --> C[Strategy Development Task]
            B --> D[Execution Planning Task]
            B --> E[Risk Assessment Task]
            C --> D
            C --> E
            B -- Data Analyst --> F[[output/data_analysis.md]]
            C -- Trading Strategy Developer --> G[[output/strategy_development.md]]
            D -- Trade Advisor --> H[[output/execution_planning.md]]
            E -- Risk Advisor --> I[[output/risk_assessment.md]]
            F --> J((End))
            G --> J
            H --> J
            I --> J
        """
    )