import random

import uvicorn
from fastapi import FastAPI, Depends
from booksapi_core import actions
from booksapi_core.models import Book
from booksapi_rest.requests import CreateBookRequest, GetBookRequest, ListBooksRequest

app = FastAPI()


@app.get("/books")
def list_books(request: ListBooksRequest = Depends()):
    return actions.list_books(page_size=request.page_size)


@app.put("/books")
def create_book(request: CreateBookRequest):
    book_id = random.randint(1, 100000000)
    book = Book(name=request.name, author=request.author, year=request.year, pages=request.pages, id=book_id)
    return actions.save_book(book)


@app.get("/book")
def get_book(request: GetBookRequest = Depends()):
    return actions.get_book_by_id(request.book_id)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=6464)
