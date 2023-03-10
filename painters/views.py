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
        print(self.request.headers)
        version = self.request.headers['Accept']
        print(version)
        # if self.request.version == '2.0':
        if version == "application/json; version=2.0":
            print('goes to Serializer')
            return PaintersSerializer
        print('goes to SerializerBase')
        return PaintersSerializerBase
