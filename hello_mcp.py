from fastmcp import FastMCP

# MCPサーバーを作成
mcp = FastMCP("Hello MCP Server")

@mcp.tool
def say_hello(name: str = "World") -> str:
    """指定された名前で挨拶します"""
    return f"Hello, {name}! MCPの世界へようこそ!"

if __name__ == "__main__":
    mcp.run()