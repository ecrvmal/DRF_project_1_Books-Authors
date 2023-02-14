"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter  # this helps to define entry points
from users.views import UserModelViewSet
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet

router = DefaultRouter()  # initiate the class

# register entry point to model
# entry point = users , that we had imported
router.register('users', UserModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
# router.register('books', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # connect  path = api/    router
]
