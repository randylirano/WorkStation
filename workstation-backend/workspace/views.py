from django.db.utils import IntegrityError
from rest_framework import generics, mixins, serializers

from .models import Background, Workspace
from .serializers import WorkspaceSerializer, BackgroundSerializer


class WorkspaceListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WorkspaceDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    lookup_field = "id"
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BackgroundView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    lookup_field = "workspace_id"
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except IntegrityError:
            raise serializers.ValidationError({"workspace_id": "Existing background."})
