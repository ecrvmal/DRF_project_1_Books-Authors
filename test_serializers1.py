import io

from rest_framework import serializers

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from test_models import Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birtday_year)
        return instance

    # Validation of single field
    def validate_birthday_year(self,value):
        if value <5:
            rise serializers.ValidationError('Год рождения не может быть отрицательным')
        return value

    # Validation of all fields
    def validate(self, attrs):
        if attrs['name']== 'Толстой' and attrs['birthday_year'] != 1828:
            raise serializers.ValidationError('Нвверный год рождения Толстого ')
        return attrs


def start():  # dict > object
    author = Author('Толстой', 1828)
    serializer = AuthorSerializer(author)


    # object  > bytes
    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)

    # get string > dict
    stream = io.BytesIO(json_bytes)  # get string
    data = JSONParser().parse(stream)

    serializer = AuthorSerializer(data=data)
    serializer.is_valid()
    # Продолжение скрипта#1

    # Создание

    author = serializer.save()
    print(type(author))
    print(author)

    # Обновление всех данных   create : dict > object > save
    data = {'name': 'Пушкин', 'Birthday_year': 1880}  # делаем словарь
    serializer = AuthorSerializer(author, data=data)  # передаем новый словарь data, обновляем объект author ,
    serializer.is_valid()  # обязательно вызываем, нужно его проверить
    author = serializer.save()  # когда вызываем save вызывается функция обновления def update(self, instance, validated_data):
    # возвращается обновленный объект
    print(author)

    # Обновление частичное     updare : dict > object > save
    data = {'birthday_year': 10}
    serializer = AuthorSerializer(author, data=data, partitial=True)
    serializer.is_valid()
    author = serializer.save()
    print(f'({author} {author.birthday_year})')

    # Проверка 1-го поля
    data = {'birthday_year': 1}
    serializer = AuthorSerializer(author, data=data, partial=True)
    if serializer.is_valid():
        author = serializer.save()
        print(f'{author} {author.birthday_year}')
    else:
        print(serializer.errors)

    # Проверка всех полей
    data = {'name': 'Толстой', 'birthday_year': 2000}
    serializer = AuthorSerializer(author, data=data)
    if serializer.is_valid():
        author = serializer.save()
        print(author)
    else:
        print(serializer.errors)




start()
