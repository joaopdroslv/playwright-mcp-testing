import asyncio
from code.gpt_model import gpt_model
from code.mcp import BrowserMCP, simple_implementation

from langchain_core.messages import AIMessage


async def main():

    async with BrowserMCP() as browser_mcp:
        snapshot = await browser_mcp.extract_snapshot(url="https://www.kabum.com.br/")

        response: AIMessage = gpt_model.invoke(
            f"""
        Here is a page snapshot. Identify the search input bar
        (where the user types the product name) and return ONLY the "ref"
        value, nothing else.

        Respond only the ref ID (ex: e315). No explanation.

        Snapshot:
        ```yaml
            {snapshot}
        ```
        """
        )

        ref = response.content
        print(f"Element ref={ref}")

        snapshot = await browser_mcp.query_product(
            url="https://www.kabum.com.br/",
            input_ref=ref,
            query="AMD Ryzen 7 5800X3D",
        )

        response: AIMessage = gpt_model.invoke(
            f"""
        You will receive a page snapshot from an ecommerce website.
        Extract every product listed on the page.

        Return a JSON array where each item has:
        - name (string)
        - price (number)

        If the price is not present, omit the item.

        Respond ONLY with valid JSON, nothing else.

        Here's the snapshot:
        {snapshot}
        """
        )

        print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
