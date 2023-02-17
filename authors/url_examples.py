from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter  # this helps to define entry points

# from users.views import UserModelViewSet

# from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet

# from authors.view_examples import BookAPIView
# from authors.view_examples import get
# from authors.view_examples import BookCreateAPIView, BookRetrieveAPIView, BookListAPIView
# from authors.view_examples import BookDestroyAPIView, BookUpdateAPIView
# from authors.view_examples import BookCustomViewSet
# from authors.view_examples import BookListAPIView
# from authors.view_examples import BookModelViewSet
# from authors.view_examples import BookDjangoFilterViewSet
from authors.view_examples import BookLimitOffsetPaginationViewSet

# from authors.view_examples import BookQuerysetFilterViewSet

# from authors.view_examples import BookViewSet

router = DefaultRouter()  # initiate the class
# router.register('book', BookCustomViewSet)

# router.register('book', BookViewSet, basename='book')
# Добавляем входную точку
# если используем ViewSet, то basename указывать обязательно


# register entry point to model
# entry point = users , that we had imported

# router.register('books', BookModelViewSet)
#  router.register('book-f', BookDjangoFilterViewSet)
router.register('book-p', BookLimitOffsetPaginationViewSet)
# router.register('books', BookModelViewSet)
# router.register('book_filter', BookQuerysetFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # level1
    # path('api/book', BookAPIView.as_view()),             # for 1-st example
    # path('api/book', get),  # for POST example
    #
    # path('api/list/', BookListAPIView.as_view()),
    # path('api/create/', BookCreateAPIView.as_view()),
    # path('api/update/<int:pk>', BookUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>', BookDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>', BookRetrieveAPIView.as_view()),

]
