from rest_framework import generics, mixins

from .models import Background
from .serializers import BackgroundSerializer


class BackgroundView(generics.GenericAPIView):
    lookup_field="id"
    queryset
    serializer_class = BackgroundSerializer
