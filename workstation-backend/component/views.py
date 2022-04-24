from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import PostIt, Checklist, ChecklistItem, Image
from .serializers import (
    PostItSerializer,
    ChecklistSerializer,
    ChecklistItemSerializer,
    ImageSerializer,
)


# Post-it list and detail views
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


# Checklist list and detail views
class ChecklistListView(generics.ListCreateAPIView):
    serializer_class = ChecklistSerializer

    def get_queryset(self):
        workspace_id = self.request.query_params.get("workspace_id")
        if workspace_id is not None:
            return Checklist.objects.filter(workspace_id=workspace_id)
        else:
            return Checklist.objects.all()


class ChecklistDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer


# Checklist Item list and detail views
class ChecklistItemListView(generics.ListCreateAPIView):
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        checklist_id = self.request.query_params.get("checklist_id")
        if checklist_id is not None:
            return ChecklistItem.objects.filter(checklist_id=checklist_id)
        else:
            return ChecklistItem.objects.all()


class ChecklistItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer


# Image list and detail views
class ImageListView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        workspace_id = self.request.query_params.get("workspace_id")
        if workspace_id is not None:
            return Image.objects.filter(workspace_id=workspace_id)
        else:
            return Image.objects.all()


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
