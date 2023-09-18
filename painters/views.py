from rest_framework import generics, viewsets

from .models import Painters
from .serializers import PaintersSerializer, PaintersModelSerializerWithFullName, PaintersSerializerBase


class PaintersListAPIView(generics.ListAPIView):
    queryset = Painters.objects.all()
    serializer_class = PaintersSerializer

    # UrlPathVersioning   and NamespaceVersioning
    # select serializer depending on condition
    # if the method not defined, then use method   serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.request.version == '0.2':
            return PaintersModelSerializerWithFullName
        return PaintersSerializer

    # Указание версии в  параметре URL - адреса
    # select serializer depending on condition
    # if the method not defined, then use method   serializer_class = UserSerializer


class PaintersViewSet(viewsets.ModelViewSet):
    queryset = Painters.objects.all()
    serializer_class = PaintersSerializer

    def get_serializer_class(self):
        """
        The get_serializer_class function is a helper function that allows you to dynamically return the correct serializer class based on the request.
        In this case, we are checking if the version in our Accept header is 2.0 and returning PaintersSerializer if it is.

        :param self: Represent the instance of the class
        :return: The serializer class to use
        :doc-author: Trelent
        """
        print(self.request.headers)
        version = self.request.headers['Accept']
        print(version)
        # if self.request.version == '2.0':
        if version == "application/json; version=2.0":
            print('goes to Serializer')
            return PaintersSerializer
        print('goes to SerializerBase')
        return PaintersSerializerBase
