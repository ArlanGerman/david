from rest_framework import generics
from django.contrib.auth.models import User

from authentication.serializers import UserModelSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def perform_create(self, serializer: UserModelSerializer):
        User.objects.create_user(**serializer.validated_data)