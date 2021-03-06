from django.urls import re_path

from .views import BackgroundView, WorkspaceListView, WorkspaceDetailView

urlpatterns = [
    re_path(
        r"^$",
        WorkspaceListView.as_view(),
        name="workspace-list",
    ),
    re_path(
        r"^(?P<workspace_id>[0-9a-f\-]+)?$",
        WorkspaceDetailView.as_view(),
        name="workspace-detail",
    ),
    re_path(
        r"^background/(?P<workspace_id>[0-9a-f\-]+)?$",
        BackgroundView.as_view(),
        name="workspace-background",
    ),
]
