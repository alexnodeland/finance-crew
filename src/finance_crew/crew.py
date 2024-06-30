import yaml
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


@CrewBase
class FinanceCrew:
    """FinanceCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    crew_config_file = "src/finance_crew/config/crew.yaml"

    def __init__(self):
        with open(self.crew_config_file, 'r') as file:
            self.crew_config = yaml.safe_load(file)
        self.tools = self._get_tools()

    def _get_tools(self):
        return {"search": SerperDevTool(), "scrape": ScrapeWebsiteTool()}

    def _get_agent_llm(self, agent_name):
        agent_config = self.crew_config['agents'].get(agent_name, {})
        llm_config = agent_config.get('llm')
        if llm_config is None:
            llm_config = self.crew_config['default_agent_llm']
        return ChatOpenAI(**llm_config)

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["data_analyst"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=self.crew_config['agents']['data_analyst'].get('allow_delegation', True),
            llm=self._get_agent_llm('data_analyst'),
        )

    @agent
    def trading_strategy_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["trading_strategy_developer"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=self.crew_config['agents']['trading_strategy_developer'].get('allow_delegation', True),
            llm=self._get_agent_llm('trading_strategy_developer'),
        )

    @agent
    def trade_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["trade_advisor"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=self.crew_config['agents']['trade_advisor'].get('allow_delegation', True),
            llm=self._get_agent_llm('trade_advisor'),
        )

    @agent
    def risk_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_advisor"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=self.crew_config['agents']['risk_advisor'].get('allow_delegation', True),
            llm=self._get_agent_llm('risk_advisor'),
        )

    @task
    def data_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["data_analysis"],
            output_file="output/data_analysis.md",
            create_directory=True,
            agent=self.data_analyst(),
            human_input=self.crew_config['tasks']['data_analysis'].get('human_input', False),
        )

    @task
    def strategy_development(self) -> Task:
        return Task(
            config=self.tasks_config["strategy_development"],
            agent=self.trading_strategy_developer(),
            output_file="output/strategy_development.md",
            create_directory=True,
            context=[self.data_analysis()],
            human_input=self.crew_config['tasks']['strategy_development'].get('human_input', False),
        )

    @task
    def execution_planning(self) -> Task:
        return Task(
            config=self.tasks_config["execution_planning"],
            agent=self.trade_advisor(),
            output_file="output/execution_planning.md",
            create_directory=True,
            context=[self.data_analysis(), self.strategy_development()],
            human_input=self.crew_config['tasks']['execution_planning'].get('human_input', False),
        )

    @task
    def risk_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["risk_assessment"],
            agent=self.risk_advisor(),
            output_file="output/risk_assessment.md",
            create_directory=True,
            context=[
                self.data_analysis(),
                self.strategy_development(),
            ],
            human_input=self.crew_config['tasks']['risk_assessment'].get('human_input', False),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FinceCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=self.crew_config['crew']['verbose'],
            process=Process[self.crew_config['crew']['process']],
            manager_llm=ChatOpenAI(**self.crew_config['manager_llm']),
            output_log_file="output/log.txt",
            # full_output=True,
        )
