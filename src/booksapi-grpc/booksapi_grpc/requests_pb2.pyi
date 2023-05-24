from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["author", "name", "pages", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    name: str
    pages: int
    year: int
    def __init__(self, name: _Optional[str] = ..., author: _Optional[str] = ..., year: _Optional[int] = ..., pages: _Optional[int] = ...) -> None: ...

class GetBookByIDRequest(_message.Message):
    __slots__ = ["book_id"]
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    book_id: int
    def __init__(self, book_id: _Optional[int] = ...) -> None: ...

class ListBooksRequest(_message.Message):
    __slots__ = ["page_size"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    def __init__(self, page_size: _Optional[int] = ...) -> None: ...
