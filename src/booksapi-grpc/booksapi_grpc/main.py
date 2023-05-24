import random
from concurrent import futures
import grpc
from booksapi_core.models import Book
from grpc_reflection.v1alpha import reflection
from booksapi_grpc import service_pb2
from booksapi_grpc.requests_pb2 import CreateBookRequest, ListBooksRequest, GetBookByIDRequest
from booksapi_grpc.responses_pb2 import BookResponse, ListBooksResponse
from service_pb2_grpc import BooksServiceServicer, add_BooksServiceServicer_to_server
from booksapi_core import actions


class BooksService(BooksServiceServicer):
    def CreateBook(self, request: CreateBookRequest, context) -> BookResponse:
        book_id = random.randint(1, 100000000)
        book = Book(request.name, request.author, book_id, request.year, request.pages)
        actions.save_book(book)
        response = BookResponse(id=book_id, name=book.name, author=book.author, year=book.year, pages=book.pages)
        return response

    def GetBook(self, request: GetBookByIDRequest, context) -> BookResponse:
        book = actions.get_book_by_id(request.book_id)
        response = BookResponse(name=book.name, author=book.author, id=book.id, year=book.year, pages=book.pages)
        return response

    def ListBooks(self, request: ListBooksRequest, context) -> ListBooksResponse:
        books = actions.list_books(request.page_size)
        response = []
        for book in books:
            response.append(
                BookResponse(name=book.name, author=book.author, id=book.id, year=book.year, pages=book.pages))
        return ListBooksResponse(books=response)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port('localhost:6464')

    add_BooksServiceServicer_to_server(BooksService(), server)

    reflection.enable_server_reflection(
        [
            service_pb2.DESCRIPTOR.services_by_name["BooksService"].full_name,
            reflection.SERVICE_NAME
        ], server
    )

    server.start()
    server.wait_for_termination()
