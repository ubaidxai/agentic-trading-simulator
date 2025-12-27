# 📈Agentic Trading Simulator
<!--
![Orchestration Diagram](assets/orchestration_diagram.png)
-->
Agentic Trading Simulator is a multi-agent AI system that simulates equity trading with autonomous traders and researcher agents. 

## 🚀 Key Features:
- **Autonomous Traders & Researchers:** multiple agents operate simultaneously.
- **Agentic Decision-Making:** traders act based on account data, strategies, and insights.
- **Portfolio Management:** track holdings, balances, and strategy changes.
- **Extensible & Modular:** easily add new agents, tools, and data sources.
- **Simulated Market Environment:** fully contained for safe testing.
- **Multi-Server Architecture:** uses MCP servers for web search, accounts, market, memory, and notifications.

## 🤖 Agents, Tools & MCP Servers:
- Build with OpenAI Agents SDK.
- Multi-Agent Architecture with 5 agents:
  - One Researcher agent used as tool by trading agents.
  - Four trading agents with different trading stretegies.
- Uses 6 different MCP servers with dozens of tools, with three self-made in-house MCP servers:
  - MCP-Fetch ()
  - Tavily (Internet Search)
  - LIBSQL (Graph-Based Memory)
  - Massive (Stock Market Data)
  - Accounts (User Account Details - Self-Made)
  - Push (NTFY for Push Notification)
- Multiple models options (OpenAI, Gemini, DeepSeek, Grok, OpenRouter). 

## 📁 Project Folder Structure 
```
agentic-trading-simulator/
│
├── assets/
├── db/
├── memory/
├── notebooks/  --> Some practice Stuff
|
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── researcher_agent.py
│   │   └── trader_agent.py
│   │
│   ├── mcp/
│   │   ├── __init__.py
│   │   ├── mcp_params.py
│   │   ├── accounts_mcp_server.py
│   │   ├── accounts_mcp_client.py
│   │   ├── market_mcp_server.py
│   │   └── push_mcp_server.py
│   │
│   ├── portfolio/
│   │   ├── __init__.py
│   │   ├── accounts.py
│   │   ├── db_operations.py
│   │   └── market.py
│   │
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── prompt_templates.py
│   │   └── trader_strategies.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── researcher_tool.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── reset_traders.py
│   │   ├── tracers.py
│   │   └── ui_utils.py
│   │
│   ├── __init__.py
│   └── orchestrator.py
│
├── .env
├── .gitignore
├── app.py --> Main Gradio UI
├── config.py
├── memory-tool.db
├── pyproject.toml
├── README.md
├── setups.md
└── LICENSE
```

## ⚙️ Setup Instructions
0. Setup WSL (For Windows only):

Follow the instructions in <a href="setups.md">setups.md</a> to setup WSL (Windows Subsystem for Linux).
Skip this step if working with Linux or MAC.

2. Clone the repository
```
> git clone https://github.com/Ubadi-The-Data-Scientist/agentic-trading-simulator.git
> cd agentic-trading-simulator
```
2. Install environment & dependencies (single uv command)
   - create the .venv
   - install all dependencies
   - sync them with your pyproject.toml
```
> uv sync
```
3. Activate the virtual environment (Optional)
```
> source .venv/bin/activate    # Mac/Linux
> .venv\Scripts\activate       # Windows
```
4. Configure environment variables
```
> cp .env.example .env      # Mac/Linux
> copy .env.example .env    # Windows
```
Then open .env and fill in the required fields.

5. Create folders for DB and memory:
```
> mkdir db
> mkdir memory
```

## ▶️ Usage Example
Run with scheduler
```
> uv run app.py
```
It will run the gradio app and Scheduler runs the simulation every 60 minutes when market is on.

If want to run the traders manually:
```
> uv run python -m src.orchestrator
```

## 🤝 Contributing

Contributions, feature ideas, and PRs are welcome!
Please open an issue to discuss major changes before submitting PRs.

## 📜 License

MIT License — free for personal and commercial use.
