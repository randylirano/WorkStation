import json
import pytest

from uuid import uuid4

from django.urls import reverse
from rest_framework import status

from workspace.models import Background


@pytest.mark.django_db
class TestBackground:
    def test_get_not_found(self, client):
        url = reverse("workspace-background", kwargs={"workspace_id": 1})

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get(self, client, background_1):
        url = reverse(
            "workspace-background", kwargs={"workspace_id": background_1.workspace_id}
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": str(background_1.id),
            "workspace_id": str(background_1.workspace_id),
            "image_url": background_1.image_url,
        }

    def test_post_invalid_url(self, client, workspace_1):
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_1.id})

        response = client.post(
            url, data={"workspace_id": workspace_1.id, "image_url": "random-url"}
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "image_url" in response.data
        assert response.data["image_url"][0].title() == "Enter A Valid Url."

    def test_post(self, client, workspace_1):
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_1.id})

        response = client.post(
            url,
            data={
                "workspace_id": workspace_1.id,
                "image_url": "http://helloworld.com/image",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert Background.objects.count() == 1

        background = Background.objects.get()
        assert background.workspace_id == workspace_1.id
        assert background.image_url == "http://helloworld.com/image"

    def test_post_duplicate(self, client, background_1):
        workspace_id = background_1.workspace_id
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_id})

        response = client.post(
            url,
            data={
                "workspace_id": workspace_id,
                "image_url": "http://helloworld.com/image",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {"workspace_id": "Existing background."}

    def test_patch_invalid_url(self, client, background_1):
        workspace_id = background_1.workspace_id
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_id})

        response = client.patch(
            url,
            data=json.dumps({"image_url": "random_url"}),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "image_url" in response.data
        assert response.data["image_url"][0].title() == "Enter A Valid Url."

    def test_patch_workspace(self, client, background_1):
        workspace_id = background_1.workspace_id
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_id})

        new_uuid = uuid4()

        response = client.patch(
            url,
            data=json.dumps(
                {
                    "workspace_id": str(new_uuid),
                }
            ),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_200_OK
        background_1.refresh_from_db()
        assert background_1.workspace_id == workspace_id

    def test_patch(self, client, background_1):
        workspace_id = background_1.workspace_id
        url = reverse("workspace-background", kwargs={"workspace_id": workspace_id})

        response = client.patch(
            url,
            data=json.dumps({"image_url": "http://world.com/image"}),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_200_OK

        background_1.refresh_from_db()
        assert background_1.image_url == "http://world.com/image"
