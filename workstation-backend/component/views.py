from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import PostIt
from .serializers import PostItSerializer


class PostItListView(generics.ListCreateAPIView):
    serializer_class = PostItSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get("workspace_id")
        return PostIt.objects.filter(workspace_id=workspace_id)


class PostItDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer

    def get_object(self):
        qs = self.get_queryset()

        workspace_id = self.kwargs.get("workspace_id")
        id = self.kwargs.get("id")

        return get_object_or_404(
            qs.filter(
                id=id,
                workspace_id=workspace_id,
            )
        )
