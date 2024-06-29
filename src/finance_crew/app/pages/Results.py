import streamlit as st
import os

def display_analysis_results():
    st.title("Analysis Results")

    if not os.path.exists("output/analysis.md"):
        st.warning("No analysis results found. Generate an analysis first!")
        return

    with open("output/analysis.md", "r") as file:
        analysis_content = file.read()
    st.markdown(analysis_content)

    render_download_buttons()

def render_download_buttons():
    st.subheader("Download Results")
    col1, col2, col3 = st.columns(3)

    file_names = [
        "analysis.md", "data_analysis.md", "strategy_development.md",
        "execution_planning.md", "risk_assessment.md", "log.txt"
    ]

    for i, file_name in enumerate(file_names):
        file_path = f"output/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_content = file.read()
            
            with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
                st.download_button(
                    label=f"Download {file_name}",
                    data=file_content,
                    file_name=file_name,
                    mime="text/markdown" if file_name.endswith(".md") else "text/plain",
                )

def main():
    display_analysis_results()

if __name__ == "__main__":
    main()