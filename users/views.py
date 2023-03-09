from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import Users
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer
