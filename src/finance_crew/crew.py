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

    def __init__(self):
        self.llm_provider = "openai"
        self.llm = self._get_llm()
        self.tools = self._get_tools()

    def _get_llm(self):
        if self.llm_provider == "openai":
            return ChatOpenAI(model="gpt-4o", temperature=0.5)

    def _get_tools(self):
        return {"search": SerperDevTool(), "scrape": ScrapeWebsiteTool()}

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["data_analyst"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
        )

    @agent
    def trading_strategy_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["trading_strategy_developer"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
        )

    @agent
    def trade_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["trade_advisor"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
        )

    @agent
    def risk_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_advisor"],
            tools=[self.tools["scrape"], self.tools["search"]],
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
        )

    @task
    def data_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["data_analysis"],
            output_file="output/data_analysis.md",
            create_directory=True,
            agent=self.data_analyst(),
        )

    @task
    def strategy_development(self) -> Task:
        return Task(
            config=self.tasks_config["strategy_development"],
            agent=self.trading_strategy_developer(),
            output_file="output/strategy_development.md",
            create_directory=True,
            context=[self.data_analysis()],
        )

    @task
    def execution_planning(self) -> Task:
        return Task(
            config=self.tasks_config["execution_planning"],
            agent=self.trade_advisor(),
            output_file="output/execution_planning.md",
            create_directory=True,
            context=[self.data_analysis(), self.strategy_development()],
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
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FinceCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=2,
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-4o", temperature=0.7),
            output_log_file="output/log.txt",
            # full_output=True,
        )
