from agents import Tool
from src.agents.researcher_agent import get_researcher
from src.templates.prompt_templates import research_tool


async def get_researcher_tool(mcp_servers) -> Tool:
    researcher = await get_researcher(mcp_servers)
    return researcher.as_tool(tool_name="Researcher", tool_description=research_tool())