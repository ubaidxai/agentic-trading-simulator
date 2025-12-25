import os
import json
from dotenv import load_dotenv
from contextlib import AsyncExitStack
from openai import AsyncOpenAI
from agents import Agent, Tool, Runner, OpenAIChatCompletionsModel, trace
from src.mcp.accounts_mcp_client import read_accounts_resource, read_strategy_resource
from src.utils.tracers import make_trace_id
from agents.mcp import MCPServerStdio
from src.templates.prompt_templates import researcher_instructions, trader_instructions, trade_message, rebalance_message, research_tool
from src.mcp.mcp_params import get_trader_mcp_params, get_researcher_mcp_params
from src.tools.researcher_tool import get_researcher_tool

load_dotenv(override=True)

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
grok_api_key = os.getenv("GROK_API_KEY")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
GROK_BASE_URL = os.getenv("GEMINI_BASE_URL")
GEMINI_BASE_URL = os.getenv("GROK_BASE_URL")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

MAX_TURNS = int(os.getenv("MAX_TURNS") or 10)
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
deepseek_client = AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
grok_client = AsyncOpenAI(base_url=GROK_BASE_URL, api_key=grok_api_key)
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=gemini_api_key)





class Trader:
    def __init__(self, name: str, lastname="Trader", model_name=model_name):
        self.name = name
        self.lastname = lastname
        self.agent = None
        self.model_name = model_name
        self.do_trade = True

    async def create_agent(self, trader_mcp_servers, researcher_mcp_servers) -> Agent:
        tool = await get_researcher_tool(researcher_mcp_servers)
        self.agent = Agent(
            name=self.name,
            instructions=trader_instructions(self.name),
            model=self.model_name,
            tools=[tool],
            mcp_servers=trader_mcp_servers,
        )
        return self.agent

    async def get_account_report(self) -> str:
        account = await read_accounts_resource(self.name)
        account_json = json.loads(account)
        account_json.pop("portfolio_value_time_series", None)
        return json.dumps(account_json)

    async def run_agent(self, trader_mcp_servers, researcher_mcp_servers):
        self.agent = await self.create_agent(trader_mcp_servers, researcher_mcp_servers)
        account = await self.get_account_report()
        strategy = await read_strategy_resource(self.name)
        message = (
            trade_message(self.name, strategy, account)
            if self.do_trade
            else rebalance_message(self.name, strategy, account)
        )
        await Runner.run(self.agent, message, max_turns=MAX_TURNS)

    async def run_with_mcp_servers(self):
        async with AsyncExitStack() as stack:
            trader_mcp_servers = [
                await stack.enter_async_context(MCPServerStdio(params, client_session_timeout_seconds=120))
                for params in get_trader_mcp_params()
            ]
            async with AsyncExitStack() as stack:
                researcher_mcp_servers = [
                    await stack.enter_async_context(MCPServerStdio(params, client_session_timeout_seconds=120))
                    for params in get_researcher_mcp_params(self.name)
                ]
                await self.run_agent(trader_mcp_servers, researcher_mcp_servers)

    async def run_with_trace(self):
        trace_name = f"{self.name}-trading" if self.do_trade else f"{self.name}-rebalancing"
        trace_id = make_trace_id(f"{self.name.lower()}")
        with trace(trace_name, trace_id=trace_id):
            await self.run_with_mcp_servers()

    async def run(self):
        try:
            await self.run_with_trace()
        except Exception as e:
            print(f"Error running trader {self.name}: {e}")
        self.do_trade = not self.do_trade
