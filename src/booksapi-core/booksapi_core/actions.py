from booksapi_core.models import Book
from typing import List
from typing import Optional


def save_book(book: Book):
    book_name = book.name
    book_a = book.author


def get_all_books() -> List[Book]:
    pass


def get_book_by_id(book_id: int) -> Optional[Book]:
    pass
