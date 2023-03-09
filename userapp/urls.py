from django.contrib import admin
from django.urls import path, include

from userapp.views import UserListAPIView

app_name = 'userapp'

urlpattern = []

urlpatterns = [
    path('', UserListAPIView.as_view()),
]
