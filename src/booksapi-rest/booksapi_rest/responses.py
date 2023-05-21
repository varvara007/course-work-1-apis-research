from typing import List

from pydantic import BaseModel


class CreateBookResponse(BaseModel):
    name: str
    author: str
    id: int
    year: int
    pages: int


class GetBookResponse(BaseModel):
    name: str
    author: str
    id: int
    year: int
    pages: int


class ListBooksResponse(BaseModel):
    books = List[GetBookResponse]
