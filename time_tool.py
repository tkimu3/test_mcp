from fastmcp import FastMCP
import datetime
import os

# MCPサーバーを作成
mcp = FastMCP("便利ツールサーバー")

@mcp.tool
def get_current_time() -> str:
    """現在の日時を取得します"""
    now = datetime.datetime.now()
    return f"現在の日時: {now.strftime('%Y年%m月%d日 %H時%M分%S秒')}"

@mcp.tool
def get_system_info() -> dict:
    """システム情報を取得します"""
    return{
        "OS": os.name,
        "作業ディレクトリ": os.getcwd(),
        "ユーザー名": os.environ.get('USER', os.environ.get('USERNAME','不明'))
    }

if __name__ == "__main__":
    mcp.run()