from pydantic import BaseModel


class CreateBookRequest(BaseModel):
    name: str
    author: str
    year: int
    pages: int


class ListBooksRequest(BaseModel):
    page_size: int = 100


class GetBookRequest(BaseModel):
    book_id: int
