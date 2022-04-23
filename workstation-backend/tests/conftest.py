import pytest

from decimal import Decimal

from django.contrib.auth.models import User

from component.models import PostIt, Image
from workspace.models import Background, Workspace


@pytest.fixture
def user_1():
    return User.objects.create(
        username="test_user1",
        email="test",
        password="test_password",
    )


@pytest.fixture
def workspace_1(user_1):
    return Workspace.objects.create(
        user=user_1,
        name="Sample Workspace #1",
    )


@pytest.fixture
def workspace_2(user_1):
    return Workspace.objects.create(
        user=user_1,
        name="Sample Workspace #2",
    )


@pytest.fixture
def background_1(workspace_1):
    return Background.objects.create(
        workspace=workspace_1, image_url="http://sample_url.com"
    )


@pytest.fixture
def post_it_1(workspace_1):
    return PostIt.objects.create(
        workspace=workspace_1,
        x=Decimal("1.23"),
        y=Decimal("4"),
        width=Decimal("56"),
        height=Decimal("7"),
        collapsed=False,
        title="Hello world",
        content=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
            "eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ),
        color="#baaf10",
    )


@pytest.fixture
def post_it_2(workspace_2):
    return PostIt.objects.create(
        workspace=workspace_2,
        x=Decimal("3.21"),
        y=Decimal("4"),
        width=Decimal("65"),
        height=Decimal("7"),
        collapsed=True,
        title="World Hello",
        content="incididunt ut labore et dolore magna aliqua.",
        color="#aaaf10",
    )


@pytest.fixture
def image_1(workspace_1):
    return Image.objects.create(
        workspace=workspace_1,
        x=Decimal("1.5"),
        y=Decimal("4.0"),
        width=Decimal("3.0"),
        height=Decimal("3.0"),
        url="https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing"
    )


@pytest.fixture
def image_2(workspace_2):
    return Image.objects.create(
        workspace=workspace_2,
        x=Decimal("1.5"),
        y=Decimal("4.0"),
        width=Decimal("3.0"),
        height=Decimal("3.0"),
        url="https://drive.google.com/file/d/1gBEz1xudWrx9YTWJUH1nldIP8WOP6nAL/view?usp=sharing"
    )
