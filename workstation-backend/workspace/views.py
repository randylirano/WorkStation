from django.db.utils import IntegrityError
from rest_framework import generics, mixins, serializers

from .models import Background, Workspace
from .serializers import WorkspaceSerializer, BackgroundSerializer


class WorkspaceView(mixins.CreateModelMixin, generics.GenericAPIView):
    lookup_field = "user"
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BackgroundView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    lookup_field = "workspace_id"
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except IntegrityError:
            raise serializers.ValidationError({"workspace_id": "Existing background."})
