import subprocess
from finance_crew.cli.main import cli
from finance_crew.app.app import app

def run_app():
    subprocess.run(["streamlit", "run", "src/finance_crew/app/app.py"])

def run_cli():
    cli()

if __name__ == "__main__":
    # You can add logic here to determine whether to run the CLI or the app
    # For example:
    # import sys
    # if len(sys.argv) > 1 and sys.argv[1] == "cli":
    #     cli()
    # else:
    #     app()
    app()  # Default to running the app