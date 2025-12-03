from typing import List, Optional

from pydantic import BaseModel, Field


class PageItem(BaseModel):

    number: int
    url: str


class Pagination(BaseModel):

    total: int = 0
    pages: Optional[List[PageItem]] = []


# Model structured output
class PaginationOutput(BaseModel):

    first_page_number: int
    last_page_number: int

    page_url_pattern: str = Field(
        description='A URL template that represents the pagination pattern. It must include the literal string "PAGE_NUMBER" at the exact position where page numbers appear in the real URLs.'
    )
