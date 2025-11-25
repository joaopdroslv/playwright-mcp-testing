from typing import Any, Dict, List

import pandas as pd


def write_into_xlsx(
    output: List[Dict[str, Any]], filename: str = "output.xlsx"
) -> None:
    df = pd.DataFrame(output)
    df.to_excel(filename, index=False)
