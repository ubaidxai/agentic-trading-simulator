import os
from dotenv import load_dotenv
import requests
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

load_dotenv(override=True)
ntfy_url = os.getenv("NTFY_URL")

mcp = FastMCP("push_server")


class PushModelArgs(BaseModel):
    message: str = Field(description="A brief message to push")


@mcp.tool()
def push(args: PushModelArgs):
    """Send a push notification with this brief message"""
    print(f"Push: {args.message}")
    requests.post(
        ntfy_url, 
        data=args.message,
        headers={
            "Title": "Portfolio Agent Alert",
            "Priority": "urgent"
        }
    )
    return "Push notification sent"


if __name__ == "__main__":
    mcp.run(transport="stdio")