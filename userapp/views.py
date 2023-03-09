from rest_framework import generics

from .models import Users
from .serializers import UserSerializer, UserModelSerializerWithFullName


class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # select serializer depending on condition
    # if the method not defined, then use method   serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerWithFullName
        return UserSerializer
