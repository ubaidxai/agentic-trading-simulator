import os
from agents import Agent, Tool
from dotenv import load_dotenv
from src.templates.prompt_templates import researcher_instructions, research_tool

load_dotenv(override=True)
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")


async def get_researcher(mcp_servers) -> Agent:
    researcher = Agent(
        name="Researcher",
        instructions=researcher_instructions(),
        model=model_name,
        mcp_servers=mcp_servers,
    )
    return researcher