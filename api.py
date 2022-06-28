from flask import Flask, jsonify
from db_management import get_books, get_book_by_isbn

app = Flask(__name__)


@app.get('/')
def say_hello():
    return "Hello World!"


@app.get('/books')
def show_books():
    return jsonify(get_books())


@app.get('/books/<isbn>')
def show_book(isbn):
    return jsonify(get_book_by_isbn(isbn))


if __name__ == '__main__':
    app.run(debug=True)