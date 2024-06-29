import json
import yaml

def load_task_config():
    with open("src/finance_crew/config/tasks.yaml", "r") as file:
        return yaml.safe_load(file)

def load_agent_config():
    with open("src/finance_crew/config/agents.yaml", "r") as file:
        return yaml.safe_load(file)
    
def load_crew_config():
    with open("src/finance_crew/config/crew.yaml", "r") as file:
        return yaml.safe_load(file)

def load_example_inputs():
    with open("data/cli-default.json", "r") as file:
        return json.load(file)