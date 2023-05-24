from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookResponse(_message.Message):
    __slots__ = ["author", "id", "name", "pages", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    id: int
    name: str
    pages: int
    year: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., author: _Optional[str] = ..., year: _Optional[int] = ..., pages: _Optional[int] = ...) -> None: ...

class ListBooksResponse(_message.Message):
    __slots__ = ["books"]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: _containers.RepeatedCompositeFieldContainer[BookResponse]
    def __init__(self, books: _Optional[_Iterable[_Union[BookResponse, _Mapping]]] = ...) -> None: ...
