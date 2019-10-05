from .models import Author, Book
from .plugins import ma


class BookSerializer(ma.ModelSchema):

    author = ma.Nested('SimpleAuthorSerializer')
    publication_date = ma.DateTime(format='%Y-%m-%d')

    class Meta:
        model = Book
        fields = ('_id', 'name', 'publication_date', 'author')


class SimpleBookSerializer(ma.ModelSchema):

    publication_date = ma.DateTime(format='%Y-%m-%d')

    class Meta:
        model = Book
        fields = ('_id', 'name', 'publication_date')


class AuthorSerializer(ma.ModelSchema):

    books = ma.Nested('SimpleBookSerializer', many=True)
    birth_date = ma.DateTime(format='%Y-%m-%d')

    class Meta:
        model = Author
        fields = ('_id', 'name', 'dni', 'birth_date', 'books')


class SimpleAuthorSerializer(ma.ModelSchema):

    birth_date = ma.DateTime(format='%Y-%m-%d')

    class Meta:
        model = Author
        fields = ('name', 'dni', 'birth_date')
