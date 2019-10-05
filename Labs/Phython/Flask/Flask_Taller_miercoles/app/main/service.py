from flask import Blueprint, request, jsonify  # , Response
from app.constants import GET, POST, PUT
from .plugins import db
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

urls = Blueprint('urls', __name__)

# define your routes here

@urls.route('/author', methods=POST)
def created_author():
    author_serializer = AuthorSerializer()
    new_author = author_serializer.load(request.json, partial=True)
    db.session.add(new_author)
    db.session.commit()
    # return Response(json.dumps({'message':'Author Created')}),status=201)
    return author_serializer.jsonify(new_author), 201


@urls.route('/author', methods=GET)
def get_author():
    author_serializer = AuthorSerializer()
    authors = Author.query.all()
    serialized_authors = author_serializer.dump(authors)
    return jsonify(serialized_authors)

##URI LIBROS

@urls.route('/book', methods=POST)
def created_book():
    book_serializer = BookSerializer()
    new_book = book_serializer.load(request.json, partial=True)
    db.session.add(new_book)
    db.session.commit()
    # return Response(json.dumps({'message':'Author Created')}),status=201)
    return book_serializer.jsonify(new_book), 201


@urls.route('/book', methods=GET)
def get_book():
    book_serializer = BookSerializer()
    books = Book.query.all()
    serialized_books = book_serializer.dump(books)
    return jsonify(serialized_books)
