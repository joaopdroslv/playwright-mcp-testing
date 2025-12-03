def concat_prompt_n_snapshot(initial_prompt: str, snapshot: str) -> str:
    """Helper function to concat partial prompts with it's relevant snapshot."""

    return (
        initial_prompt
        + f"""
    \nHere is the snapshot:
    {snapshot}
    """
    )
