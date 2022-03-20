from django.urls import re_path

from .views import PostItDetailView, PostItListView

urlpatterns = [
    re_path(
        r"^post-it/(?P<workspace_id>[0-9a-f\-]+)?$",
        PostItListView.as_view(),
        name="post-it-list",
    ),
    re_path(
        r"^post-it/(?P<workspace_id>[0-9a-f\-]+)?/(?P<id>[0-9a-f\-]+)?$",
        PostItDetailView.as_view(),
        name="post-it-detail",
    ),
]