import mysql.connector


# Function to connect to our database
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='instabook',
        user='instabook_admin',
        password='admin',
    )


# Function to view all the books in our books table
def get_books():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT *
                                FROM books AS b""")
            results = cursor.fetchall()
            return results


# Function to add a new book to the database
def add_book(title, author, isbn):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT
                                INTO books
                                     (title, author, isbn)
                              VALUES (%s, %s, %s)""", [title, author, isbn])
            connection.commit()


# Function to find a book with a particular isbn in the database
def get_book_by_isbn(isbn):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id,
                                     title,
                                     author,
                                     isbn
                                FROM books AS b
                               WHERE b.isbn = %s""", [isbn])
            result = cursor.fetchone()
            return result


