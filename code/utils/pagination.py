from code.schemas.pagination import PageItem, Pagination


def handle_pagination() -> Pagination:
    """Extracts pagination information from the current page and returns it in a
    structured format.

    Returns:
        Pagination: Object containing the total number of pages and the list of
        page items, each with its page number and URL.
    """
