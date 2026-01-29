import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM
from crewai_tools import SerperDevTool

BASE_DIR = Path(__file__).resolve().parent
CONFIG_DIR = BASE_DIR / "config"
OUTPUT_DIR = BASE_DIR / "output"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    load_dotenv()

    domain = sys.argv[1] if len(sys.argv) > 1 else input(
        "Enter a company domain (e.g., shopify.com): "
    ).strip()

    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("Missing GEMINI_API_KEY in .env")
    if not os.getenv("SERPER_API_KEY"):
        raise RuntimeError("Missing SERPER_API_KEY in .env (required for web search)")

    OUTPUT_DIR.mkdir(exist_ok=True)

    agents_cfg = load_yaml(CONFIG_DIR / "agents.yaml")
    tasks_cfg = load_yaml(CONFIG_DIR / "tasks.yaml")

    # Use a model that is much more likely to work with quota than 2.5-pro.
    gemini_llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.1,
    )

    search_tool = SerperDevTool()

    researcher = Agent(
        **agents_cfg["researcher"],
        llm=gemini_llm,
        tools=[search_tool],
    )

    research_task = Task(
        description=tasks_cfg["research_task"]["description"].format(domain=domain),
        expected_output=tasks_cfg["research_task"]["expected_output"],
        agent=researcher,
    )

    report_path = OUTPUT_DIR / f"{domain.replace('.', '_')}_market_research_report.md"
    research_task.output_file = str(report_path)

    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True,
    )

    crew.kickoff()

    print("\n✅ Done!")
    print("📄 Report saved to:", report_path)


if __name__ == "__main__":
    main()
