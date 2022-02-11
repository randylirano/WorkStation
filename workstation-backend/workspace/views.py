from django.db.utils import IntegrityError
from rest_framework import generics, mixins, serializers

from .models import Background
from .serializers import BackgroundSerializer


class BackgroundView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    lookup_field = "workspace_id"
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except IntegrityError:
            raise serializers.ValidationError({"workspace_id": "Existing background."})
