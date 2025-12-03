import os
from typing import Any, Dict, List, Literal

import pandas as pd


def write_dataframe_into_file(
    output: List[Dict[str, Any]],
    filename: str,
    extension: Literal["xlsx", "csv"] = "csv",
) -> None:
    """Writes a list of dicts into an Excel file.

    Note:
        Although the `extension` parameter supports `"csv"` or `"xlsx"`,
        the current implementation always writes an Excel file.

    Args:
        output: List of rows to convert into a DataFrame.
        filename: File name without extension.
        extension: Desired file extension (currently ignored for CSV).
    """

    file_path = filename + "." + extension
    df = pd.DataFrame(output)
    df.to_excel(file_path, index=False)


def make_dir(dir_name: str, root_dir: str = "./output") -> str:
    """Creates a directory under a given root, ignoring if it already exists.

    Args:
        dir_name: Name of the directory to create.
        root_dir: Base path where the directory will be created.

    Returns:
        The full path to the created directory.
    """

    path = os.path.join(root_dir, dir_name)
    os.makedirs(path, exist_ok=True)
    return path
