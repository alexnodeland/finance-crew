from .utils import BOLD, UNDERLINE, END

def display_inputs(inputs):
    print(f"\n{UNDERLINE}Inputs received:{END}")
    for key, value in inputs.items():
        print(f"{BOLD}{key.replace('_', ' ').title()}:{END} {value}")
    print()

def save_result(result):
    with open("output/analysis.md", "w") as file:
        file.write(result if result is not None else "")