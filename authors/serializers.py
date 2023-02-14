from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import Author, Biography, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ()
        # fields = ('first_name', 'last_name')


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'
        # exclude = ()
        # fields = ('first_name', 'last_name')


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ()
        # fields = ('first_name', 'last_name')
