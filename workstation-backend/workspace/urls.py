from django.urls import re_path

from .views import BackgroundView, WorkspaceView

urlpatterns = [
    re_path(
        r"^background/(?P<workspace_id>\d+)?$",
        BackgroundView.as_view(),
        name="workspace-background",
    ),
    re_path(
        r"^workspace/(?P<workspace_id>\d+)?$",
        WorkspaceView.as_view(),
        name="workspace",
    ),
]
