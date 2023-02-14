import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from test_models import Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()


def start():
    # Преобразования
    author = Author('Грин', 1880)
    serializer = AuthorSerializer(author)
    print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}
    print(type(serializer.data))  # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

    print(50 * '*')
    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)
    print(json_bytes)  # b'{"name":"\xd0\x93\xd1\x80\xd0\xb8\xd0\xbd","birthday_year":1880}'
    print(type(json_bytes))  # <class 'bytes'>

    # Обратное преобразование
    print(50 * '*')
    from rest_framework.parsers import JSONParser
    stream = io.BytesIO(json_bytes)  # JSON > bytes
    data = JSONParser().parse(stream)  # Bytes > dict
    print(data)  # {'name': 'Грин', 'birthday_year': 1880}
    print(type(data))  # <class 'dict'>
    #
    # Восстановить объект
    serializer = AuthorSerializer(data=data)  # compare AutorSerializer.data  = data
    print(serializer.is_valid())  # True   - MANDATORY LINE
    print(serializer.validated_data)  # OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])
    print(type(serializer.validated_data))  # <class 'collections.OrderedDict'>


start()
