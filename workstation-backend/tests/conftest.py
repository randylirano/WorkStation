import pytest

from django.contrib.auth.models import User

from workspace.models import Background, Workspace


@pytest.fixture
def user_1():
    return User.objects.create(username="test_user1")


@pytest.fixture
def workspace_1(user_1):
    return Workspace.objects.create(
        user=user_1,
        name="Sample Workspace #1",
    )


@pytest.fixture
def background_1(workspace_1):
    return Background.objects.create(
        workspace=workspace_1, image_url="http://sample_url.com"
    )
