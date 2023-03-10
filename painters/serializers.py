from rest_framework.serializers import ModelSerializer
from .models import Painters
from rest_framework import serializers


# This module returns object (serialized data)


class PaintersSerializerBase(ModelSerializer):
    class Meta:
        model = Painters
        # fields = '__all__'
        fields = ('username',)


class PaintersSerializer(ModelSerializer):
    class Meta:
        model = Painters
        # fields = '__all__'
        fields = ('username', 'email', 'first_name')


class PaintersModelSerializerWithFullName(ModelSerializer):
    class Meta:
        model = Painters
        # fields = '__all__'
        fields = ('username', 'email', 'first_name', 'last_name')
