from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio

endpoint = "http://localhost:8000/mcp"

async def main():
    async with streamablehttp_client(endpoint) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("== Available tools:")
            for tool in tools.tools:
                print(f"{tool.name}: {tool}")

                if tool.name == "greet":
                    result = await session.call_tool(name='greet', arguments={"name": "Samuel"})
                    print(f"    Greeting Result: {result.structuredContent['result']}")

if __name__ == "__main__":
    asyncio.run(main())
