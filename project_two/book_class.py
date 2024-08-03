from pydantic import BaseModel, Field
from typing import Optional


class Book:
    id: int
    title: str
    author: str
    description: str
    published_year: str
    rating: int

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        published_year: str,
        rating: int,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.published_year = published_year
        self.rating = rating


class NewBook(BaseModel):
    id: Optional[int] = Field(description="ID is optional", default=None)
    title: str = Field(min_length=1, max_length=20)
    author: str = Field(min_length=1, max_length=20)
    description: str = Field(min_length=1, max_length=100)
    published_year: str = Field(min_length=4, max_length=4)
    rating: int = Field(gt=0, lt=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book Title",
                "author": "Author Name",
                "description": "Description of the book",
                "published_year": "YYYY",
                "rating": 3,
            }
        }
    }
