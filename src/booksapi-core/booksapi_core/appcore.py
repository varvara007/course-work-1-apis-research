import sqlite3


if __name__ == '__main__':
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()  # Connection.cursor() returns a Cursor object. Cursor objects allow us to send SQL statements to a SQLite database using cursor.execute().
    # cursor.execute("CREATE TABLE IF NOT EXISTS  books (name TEXT, author TEXT, id INTEGER, year INTEGER)")
    # cursor.execute("ALTER TABLE books ADD COLUMN count_of_pages INTEGER")
    first_book = cursor.execute("INSERT INTO books VALUES ('Piece and War', 'Tolstoy', 1, 1800, 2000)")
    second_book = cursor.execute("INSERT INTO books VALUES ('Piece and War', 'Tolstoy', 1, 1800, 2000)")
    third_book = cursor.execute("INSERT INTO books VALUES ('Piece and War', 'Tolstoy', 1, 1800, 2000)")
    all_books = cursor.execute("SELECT * FROM books WHERE id = 1")
    print(all_books.fetchall()[0][0])
    connection.commit()
    pass
