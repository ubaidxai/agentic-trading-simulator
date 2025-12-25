import os
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()
tavily_env = {"TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")}

 

## Set of MCP Servers for the Researcher: (fetch, tavily, Memory)
def get_researcher_mcp_params(name: str):
    return [
        {"command": "uvx", "args": ["mcp-server-fetch"]},
        {"command": "npx", "args": ["-y", "tavily-mcp@latest"], "env": tavily_env},
        {"command": "npx", "args": ["-y", "mcp-memory-libsql"], "env": {"LIBSQL_URL": f"file:./memory/{name}.db"}},

    ]

## Set of MCP Servers for the Trader: (Accounts, Push Notification and the Market)
def get_trader_mcp_params():
    return [
        {"command": "uv", "args": ["run", "python", "-m", "src.mcp.accounts_mcp_server"]},
        {"command": "uv", "args": ["run", "python", "-m", "src.mcp.push_mcp_server"]},
        {"command": "uv", "args": ["run", "python", "-m", "src.mcp.market_mcp_server"]}    
    ]