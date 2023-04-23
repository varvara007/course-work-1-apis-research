from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    id: int
    year: int
    count_of_pages: int

