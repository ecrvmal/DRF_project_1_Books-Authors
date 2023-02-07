from rest_framework.serializers import ModelSerializer

from .models import Users


# This module returns object (serialized data)

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ('first_name',)
