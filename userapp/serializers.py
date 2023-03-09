from rest_framework.serializers import ModelSerializer
from .models import Users
from rest_framework import serializers
from django.contrib.auth.models import User


# This module returns object (serialized data)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email')


class UserModelSerializerWithFullName(ModelSerializer):
    class Meta:
        model = Users
        # fields = '__all__'
        fields = ('username', 'email', 'first_name', 'last_name')
