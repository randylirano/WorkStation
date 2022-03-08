from django.urls import re_path

from .views import BackgroundView, WorkspaceListView, WorkspaceDetailView

urlpatterns = [
    re_path(
        r"^workspace/",
        WorkspaceListView.as_view(),
        name="workspace-list",
    ),
    re_path(
        r"^workspace/(?P<workspace_id>\d+)?$",
        WorkspaceDetailView.as_view(),
        name="workspace-detail",
    ),
    re_path(
        r"^background/(?P<workspace_id>\d+)?$",
        BackgroundView.as_view(),
        name="workspace-background",
    ),
]
