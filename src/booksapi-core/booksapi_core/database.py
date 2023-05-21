import sqlite3

DB_NAME = "C:\\Users\\user\\Documents\\course-work-1-apis-research\\src\\booksapi-core\\booksapi_core\\books.db"


class BooksDB:
    def __init__(self):
        self.connection = None  # type: sqlite3.Connection
        self.cursor = None  # type: sqlite3.Cursor

    def __enter__(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()


def create_tables():
    """ Метод создает таблицу в базе данных. """

    with BooksDB() as cursor:  # контекст-менеджер
        query = """
                CREATE TABLE IF NOT EXISTS  books (
                    name TEXT,
                    author TEXT,
                    id INTEGER  PRIMARY KEY, 
                    year INTEGER,
                    pages INTEGER
                )
            """
        cursor.execute(query)
