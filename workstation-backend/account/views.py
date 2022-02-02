from django.contrib.auth.models import User

from rest_framework import generics, permissions, mixins
from rest_framework.response import Response

from .serializers import UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "username": user.username,
                "message": (
                    "User Created Successfully. Perform Login to get your token."
                ),
            }
        )
