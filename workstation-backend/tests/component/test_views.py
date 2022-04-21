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
    url = reverse("post-it-list")

    def test_get_not_found(self, client):
        # No post it in the DB, should return empty list
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

        response = client.get(self.url, {"workspace_id": uuid4()})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_get_with_workspace_id(self, client, post_it_1, post_it_2):
        # Get without workspace ID should return both post-its
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert len(result) == 2
        result_ids = set(r["id"] for r in result)
        assert result_ids == set([str(post_it_1.id), str(post_it_2.id)])

        # Get with workspace ID should only return post it in that workspace
        response = client.get(self.url, {"workspace_id": post_it_1.workspace.id})
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert len(result) == 1
        self._assert_result(result[0], post_it_1)

        response = client.get(self.url, {"workspace_id": post_it_2.workspace.id})
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert len(result) == 1
        self._assert_result(result[0], post_it_2)

    def test_post(self, client, workspace_1):
        response = client.post(
            self.url,
            data={
                "title": "New Post",
                "content": "Sample content",
                "x": 0,
                "y": -100,
                "width": 20.25,
                "height": 52.02,
                "workspace_id": workspace_1.id
            },
        )

        print(response.data)
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
        # Try to post without workspace ID
        response = client.post(
            self.url,
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

        # Try to post without invalid workspace ID
        response = client.post(
            self.url,
            data={
                "title": "New Post",
                "content": "Sample content",
                "x": 0,
                "y": -100,
                "width": 20.25,
                "height": 52.02,
                "workspace_id": uuid4()
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
                "id": uuid4(),
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = reverse(
            "post-it-detail",
            kwargs={
                "id": workspace_1.id,
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get(self, client, post_it_1):
        url = reverse(
            "post-it-detail",
            kwargs={
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
        assert post_it_1.workspace == workspace_2

    def test_delete(self, client, post_it_1):
        post_id = post_it_1.id
        assert PostIt.objects.count() == 1

        url = reverse(
            "post-it-detail",
            kwargs={
                "id": post_id,
            },
        )

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not PostIt.objects.filter(id=post_id).exists()
        assert PostIt.objects.count() == 0
