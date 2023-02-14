from rest_framework import serializers
from test_models import Author, Book, Biography


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)  # text
    birthday_year = serializers.IntegerField()  # int


class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)  # text
    author = AuthorSerializer()  # object


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)  # text
    author = AuthorSerializer(many=True)  # object


author1 = Author('Грин', 1880)
serializer = AuthorSerializer(author1)
print(serializer.data)

biography = Biography('Текст Биографии 1', author1)
serializer = BiographySerializer(biography)
print(serializer.data)

author2 = Author('Пушкин', 1799)
book = Book('Некоторая книга', [author1, author2])

serializer = BookSerializer(book)
print(serializer.data)
