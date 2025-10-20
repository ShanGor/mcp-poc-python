"""
Start with
  uvicorn test_mcp_server:app --host 0.0.0.0 --port 8000
"""

from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

# Stateless server (no session persistence)
mcp = FastMCP("StatelessServer", stateless_http=True)


# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


# Run server with streamable_http transport
# if __name__ == "__main__":
#     mcp.run(transport="streamable-http")

# with Uvicorn to run the service
app = mcp.streamable_http_app()

async def app_health_check(request):
    return JSONResponse({"status": "ok"})

app.add_route("/health", app_health_check, methods=["GET"])

