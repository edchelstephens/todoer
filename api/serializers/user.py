from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers, viewsets


User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "username",
        ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

