"""
Описание моделей данных (DTO).
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewsItemDTO(BaseModel):
    """
    Модель данных для представления новости.

    .. code-block::
        NewsItemDTO(
            source="BBC News",
            author="BBC News",
            title="Coronavirus: UK records 1,000 deaths in a day",
            description="The UK records its highest daily death toll since the start of the pandemic.",
            url="https://www.bbc.co.uk/news/uk-55510000",
            published_at="2021-01-08T00:00:00Z"
        )
    """

    source: str
    author: Optional[str]
    title: str
    description: Optional[str]
    url: Optional[str]
    published_at: datetime
