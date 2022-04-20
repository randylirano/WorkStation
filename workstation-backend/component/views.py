from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import PostIt, Checklist, ChecklistItem, Image
from .serializers import PostItSerializer, ChecklistSerializer, ChecklistItemSerializer, ImageSerializer


# Post-it list and detail views
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


# Checklist list and detail views
class ChecklistListView(generics.ListCreateAPIView):
    serializer_class = ChecklistSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get("workspace_id")
        return Checklist.objects.filter(workspace_id=workspace_id)


class ChecklistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

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


# Checklist Item list and detail views
class ChecklistItemListView(generics.ListCreateAPIView):
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        checklist_id = self.kwargs.get("checklist_id")
        return ChecklistItem.objects.filter(checklist_id=checklist_id)


class ChecklistItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer

    def get_object(self):
        qs = self.get_queryset

        checklist_id = self.kwargs.get("checklist_id")
        id = self.kwargs.get("id")

        return get_object_or_404(
            qs.filter(
                id=id,
                checklist_id=checklist_id,
            )
        )


# Image list and detail views
class ImageListView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get("workspace_id")
        return Image.objects.filter(workspace_id=workspace_id)


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

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
