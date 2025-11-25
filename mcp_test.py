import asyncio
import base64

from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport


async def main():

    transport = StreamableHttpTransport("http://localhost:8931")

    async with Client(transport) as client:
        tools = await client.list_tools()
        print("Available tools:", [t.name for t in tools])

        await client.call_tool(
            "browser_navigate",
            {
                # "url": "https://www.zapimoveis.com.br/"
                "url": "https://www.kabum.com.br/"
            },
        )

        await client.call_tool("browser_wait_for", {"time": 10})

        snapshot = await client.call_tool("browser_snapshot", {})

        print(snapshot.content)

        # result = await client.call_tool(
        #     "browser_take_screenshot", {"fullPage": True, "type": "png"}
        # )

        # image_content = None
        # for item in result.content:
        #     if getattr(item, "type", None) == "image":
        #         image_content = item
        #         break

        # raw_bytes = base64.b64decode(image_content.data)
        # with open("screenshot.png", "wb") as f:
        #     f.write(raw_bytes)


asyncio.run(main())
