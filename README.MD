# Python MCP Server and Client Example

### Installation
1. Install Python 3.12+
2. python -m pip install -r requirements.txt

### Run server:
> uvicorn test_mcp_server:app --host 0.0.0.0 --workers 1 --port 8000

### Run client to test the server:
> python test_mcp_client.py


### Experience
- Better not to enable `json_response`, because it will trigger server error while client closing.
  > Example `mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)`

