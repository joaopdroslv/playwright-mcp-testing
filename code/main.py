import asyncio
from code.gpt_model import gpt_model
from code.mcp import main

from langchain_core.messages import AIMessage

if __name__ == "__main__":

    page_snapshot = asyncio.run(main(page_url="https://www.kabum.com.br/"))

    response: AIMessage = gpt_model.invoke(
        f"""
    Here is a page snapshot. Identify the search input bar
    (where the user types the product name) and return ONLY the "ref"
    value, nothing else.

    Respond only the ref ID (ex: e315). No explanation.

    Snapshot:
    ```yaml
        {page_snapshot}
    ```
    """
    )

    print(f"Element ref={response.content}")
