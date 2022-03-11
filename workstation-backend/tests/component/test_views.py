import json
import pytest

from decimal import Decimal
from uuid import uuid4

from django.urls import reverse
from rest_framework import status

from component.models import PostIt


class BaseTestPostIt:
    def _assert_result(self, result, expected_post_it):
        assert result["id"] == str(expected_post_it.id)
        assert result["workspace_id"] == str(expected_post_it.workspace.id)
        assert Decimal(result["x"]) == Decimal(expected_post_it.x)
        assert Decimal(result["y"]) == Decimal(expected_post_it.y)
        assert Decimal(result["height"]) == Decimal(expected_post_it.height)
        assert Decimal(result["width"]) == Decimal(expected_post_it.width)
        assert result["collapsed"] == expected_post_it.collapsed
        assert result["title"] == expected_post_it.title
        assert result["content"] == expected_post_it.content
        assert result["color"] == expected_post_it.color


@pytest.mark.django_db
class TestPostitList(BaseTestPostIt):
    def test_get_not_found(self, client):
        url = reverse("post-it-list", kwargs={"workspace_id": uuid4()})

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_get(self, client, post_it_1, post_it_2):
        url = reverse("post-it-list", kwargs={"workspace_id": post_it_1.workspace.id})

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()
        assert len(result) == 1
        self._assert_result(result[0], post_it_1)

        url = reverse("post-it-list", kwargs={"workspace_id": post_it_2.workspace.id})

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()
        assert len(result) == 1
        self._assert_result(result[0], post_it_2)

    def test_post(self, client, workspace_1):
        url = reverse("post-it-list", kwargs={"workspace_id": workspace_1.id})

        response = client.post(
            url,
            data={
                "title": "New Post",
                "content": "Sample content",
                "x": 0,
                "y": -100,
                "width": 20.25,
                "height": 52.02,
            },
        )

        assert response.status_code == status.HTTP_201_CREATED

        post_it = PostIt.objects.get()
        assert post_it.title == "New Post"
        assert post_it.content == "Sample content"
        assert post_it.x == Decimal("0")
        assert post_it.y == Decimal("-100")
        assert post_it.width == Decimal("20.25")
        assert post_it.height == Decimal("52.02")
        assert not post_it.collapsed
        assert post_it.color == "#baaf13"
        assert post_it.workspace == workspace_1

    def test_post_invalid_workspace(self, client, workspace_1):
        url = reverse("post-it-list", kwargs={"workspace_id": uuid4()})

        response = client.post(
            url,
            data={
                "title": "New Post",
                "content": "Sample content",
                "x": 0,
                "y": -100,
                "width": 20.25,
                "height": 52.02,
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"workspace_id": "Workspace doesn't exist"}


@pytest.mark.django_db
class TestPostitDetail(BaseTestPostIt):
    def test_get_not_found(self, client, workspace_1, post_it_2):
        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": workspace_1.id,
                "id": uuid4(),
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": workspace_1.id,
                "id": post_it_2.id,
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get(self, client, post_it_1):
        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": post_it_1.workspace_id,
                "id": post_it_1.id,
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()
        self._assert_result(result, post_it_1)

    def test_update(self, client, post_it_1):
        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": post_it_1.workspace_id,
                "id": post_it_1.id,
            },
        )

        response = client.patch(
            url,
            data=json.dumps(
                {
                    "title": "This is a new title",
                    "color": "#bbbbbb",
                    "y": "0.01",
                }
            ),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_200_OK

        post_it_1.refresh_from_db()
        result = response.json()

        self._assert_result(result, post_it_1)
        assert post_it_1.title == "This is a new title"
        assert post_it_1.color == "#bbbbbb"
        assert post_it_1.y == Decimal("0.01")

    def test_update_workspace_id(self, client, post_it_1, workspace_1, workspace_2):
        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": post_it_1.workspace_id,
                "id": post_it_1.id,
            },
        )

        response = client.patch(
            url,
            data=json.dumps(
                {
                    "workspace_id": str(workspace_2.id),
                }
            ),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_200_OK

        post_it_1.refresh_from_db()
        result = response.json()

        self._assert_result(result, post_it_1)
        # Workspace should not change
        assert post_it_1.workspace == workspace_1

    def test_delete(self, client, post_it_1):
        post_id = post_it_1.id
        assert PostIt.objects.count() == 1

        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": post_it_1.workspace_id,
                "id": post_id,
            },
        )

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not PostIt.objects.filter(id=post_id).exists()
        assert PostIt.objects.count() == 0

    def test_delete_mismatch_id(self, client, post_it_1, workspace_2):
        post_id = post_it_1.id
        assert PostIt.objects.count() == 1

        url = reverse(
            "post-it-detail",
            kwargs={
                "workspace_id": workspace_2.id,
                "id": post_id,
            },
        )

        response = client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert PostIt.objects.count() == 1
