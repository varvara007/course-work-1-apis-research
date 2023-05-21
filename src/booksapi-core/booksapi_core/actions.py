import sqlite3
from booksapi_core.database import DB_NAME, BooksDB
from booksapi_core.models import Book
from typing import List
from typing import Optional


def save_book(book: Book) -> Book:
    with BooksDB() as cursor:  # type: sqlite3.Cursor
        query = f"""
            INSERT INTO books VALUES ('{book.name}', '{book.author}', {book.id}, {book.year}, {book.pages}) 
            """
        cursor.execute(query)
        return book


def list_books(page_size: int) -> List[Book]:
    with BooksDB() as cursor:
        query = f"""
        SELECT name,author,id,year,pages FROM books
        """
        cursor.execute(query)
        rows = cursor.fetchmany(page_size)
        result = []
        for row in rows:
            book = Book(name=row[0], author=row[1], id=row[2], year=row[3], pages=row[4])
            result.append(book)
        return result


def get_book_by_id(book_id: int) -> Optional[Book]:
    with BooksDB() as cursor:  # type: sqlite3.Cursor
        query = f"""
              SELECT name,author,id,year,pages FROM books WHERE id = {book_id}
              """
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            return None
        return Book(name=row[0], author=row[1], id=row[2], year=row[3], pages=row[4])
