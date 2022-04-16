from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import PostIt
from .serializers import PostItSerializer


class PostItListView(generics.ListCreateAPIView):
    serializer_class = PostItSerializer

    def get_queryset(self):
        workspace_id = self.request.query_params.get("workspace_id")
        if workspace_id is not None:
            return PostIt.objects.filter(workspace_id=workspace_id)
        else:
            return PostIt.objects.all()


class PostItDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer
