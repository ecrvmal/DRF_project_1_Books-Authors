# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from rest_framework.viewsets import ViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from authors.models import Author, Biography, Book
# from authors.filters import BookFilter
from authors.serializers import BookModelSerializer
# from rest_framework.viewsets import GenericViewSet

# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


# from rest_framework.mixins import ListModelMixin, DestroyModelMixin


# from rest_framework.decorators import api_view
# from rest_framework.decorators import renderer_classes


# class BookAPIView(APIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def get(self, request, format=None):
#         book = Book.objects.all()
#         serializer = BookModelSerializer(book, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         pass

# ----------------------------------------------------------------
# @api_view(['GET', 'POST'])  # 'POST'
# @renderer_classes([JSONRenderer, BrowsableAPIRenderer])
# def get(request):
#     if request.method == 'GET':
#         # book = Book.objects.all()
#         # serializer = BookModelSerializer(book, many=True)
#         # return Response(serializer.data)
#         return Response({'test': 1})  # l+дополнительный пример
#     elif request.method == 'POST':
#         pass

# set here un urls.py   path('api/book', get),

# ------------------------------------------------------------------------
# level 3  Generic views
#
# class BookCreateAPIView(CreateAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# class BookListAPIView(ListAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# class BookRetrieveAPIView(RetrieveAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# class BookDestroyAPIView(DestroyAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# class BookUpdateAPIView(UpdateAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer

# ------------------------------------------------------
# Level 3 ViewSets
# class BookViewSet(ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def list(self, request):  # список
#         book = Book.objects.all()
#         serializer_class = BookModelSerializer(book, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):  # детализация
#         book = get_object_or_404(Book, pk=pk)
#         serializer_class = BookModelSerializer(book)
#         return Response(serializer_class.data)
#
#     @action(detail=True, methods=['get'])
#     def only(self, request, pk=None):  # pk=1
#         book = Book.objects.get(id=pk)
#         serializer_class = BookModelSerializer(book)
#         return Response({'book': book.name, 'id': book.id})
#
#     # с функциями ниже становятся доступны соответствуюзие функции в web интерфейсе
#     # create, update, delete, read...
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def create(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass
#

# -----------------------------------------------------
# # Level 4
# # Работает без url  routing
# # полный доступ к объекту
# class BookViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrokenPipeError]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer


# ListModelMixin,CretaApiView,DestroyModelMixin,RetrieveApiView,UpdateAPIView,GenericAPIViewSet
# class BookCustomViewSet(ListModelMixin, CreateAPIView, DestroyModelMixin, RetrieveAPIView, UpdateAPIView,
#                         GenericViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#

# Filter Example 1
# class BookQuerysetFilterViewSet(ModelViewSet):
#     serializer_class = BookModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#
#     def get_queryset(self):
#         return Book.objects.filter(name__contains="Captain")  # содержит


# Filter Example2
# class BookListAPIView(ListAPIView):
#     serializer_class = BookModelSerializer
#
#     def get_queryset(self):
#         name = self.kwargs['name']
#         return Book.objects.filter(name__contains=name)


# Filter Example 3


# Example DJANGO-FILTER 1

class BookDjangoFilterViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filterset_fields = ['id', 'name']
    # filterset_class = BookFilter


# PAGINATION Example 1
class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class BookLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    # pagination_class = BookLimitOffsetPaginationViewSet
