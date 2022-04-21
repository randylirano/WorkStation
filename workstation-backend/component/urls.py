from django.urls import re_path

from .views import PostItDetailView, PostItListView, ChecklistListView, ChecklistDetailView, ChecklistItemListView, ChecklistItemDetailView, ImageListView, ImageDetailView

urlpatterns = [
    re_path(
        r"^post-it/$",
        PostItListView.as_view(),
        name="post-it-list",
    ),
    re_path(
        r"^post-it/(?P<id>[0-9a-f\-]+)?/$",
        PostItDetailView.as_view(),
        name="post-it-detail",
    ),
    re_path(
        r"^checklist/$",
        ChecklistListView.as_view(),
        name="checklist-list",
    ),
    re_path(
        r"^checklist/(?P<id>[0-9a-f\-]+)?/$",
        ChecklistDetailView.as_view(),
        name="checklist-detail",
    ),
    re_path(
        r"^checklist/item/(?P<checklist_id>[0-9a-f\-]+)?$",
        ChecklistItemListView.as_view(),
        name="checklist-item-list"
    ),
    re_path(
        r"^checklist/item/(?P<id>[0-9a-f\-]+)?$",
        ChecklistItemDetailView.as_view(),
        name="checklist-item-detail"
    ),
    re_path(
        r"image/$",
        ImageListView.as_view(),
        name="image-list"
    ),
    re_path(
        r"image/(?P<id>[0-9a-f\-]+)?/$",
        ImageDetailView.as_view(),
        name="image-detail"
    )
]
