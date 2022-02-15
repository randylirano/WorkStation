from django.urls import re_path

from .views import BackgroundView

urlpatterns = [
    re_path(
        r"^background/(?P<workspace_id>\d+)?$",
        BackgroundView.as_view(),
        name="workspace-background",
    ),
]
