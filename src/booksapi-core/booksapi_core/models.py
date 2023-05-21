from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    id: int
    year: int
    pages: int

