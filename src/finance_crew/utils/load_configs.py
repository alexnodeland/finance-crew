import json
import yaml

def load_task_config():
    with open("src/finance_crew/config/tasks.yaml", "r") as file:
        return yaml.safe_load(file)

def save_task_config(task, config):
    current_config = load_task_config()
    current_config[task] = config
    with open("src/finance_crew/config/tasks.yaml", "w") as file:
        yaml.safe_dump(current_config, file)

def load_agent_config():
    with open("src/finance_crew/config/agents.yaml", "r") as file:
        return yaml.safe_load(file)
    
def save_agent_config(role, config):
    with open("src/finance_crew/config/agents.yaml", "r") as file:
        agent_configs = yaml.safe_load(file)
    
    agent_configs[role] = config
    
    with open("src/finance_crew/config/agents.yaml", "w") as file:
        yaml.safe_dump(agent_configs, file)
    
def load_crew_config():
    with open("src/finance_crew/config/crew.yaml", "r") as file:
        return yaml.safe_load(file)
    
def save_crew_config(config):
    with open("src/finance_crew/config/crew.yaml", "w") as file:
        yaml.safe_dump(config, file)

def load_example_inputs():
    with open("data/cli-default.json", "r") as file:
        return json.load(file)