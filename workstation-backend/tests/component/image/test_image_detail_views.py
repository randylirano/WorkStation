import json
import pytest

from decimal import Decimal
from uuid import uuid4

from django.urls import reverse
from rest_framework import status

from component.models import Image


class BaseTestImage:
    # Base test to check if the response from the tested endpoint match the expected result.
    def _assert_result(self, result, expected_image):
        assert result["id"] == str(expected_image.id)
        assert result["workspace_id"] == str(expected_image.workspace.id)
        assert Decimal(result["x"]) == Decimal(expected_image.x)
        assert Decimal(result["y"]) == Decimal(expected_image.y)
        assert Decimal(result["height"]) == Decimal(expected_image.height)
        assert Decimal(result["width"]) == Decimal(expected_image.width)
        assert result["url"] == expected_image.url


@pytest.mark.django_db
class TestImageDetail(BaseTestImage):
    def test_get_not_found(self, client, workspace_1, image_1):
        url = reverse(
            "image-detail",
            kwargs={
                "id": uuid4(),
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = reverse("image-detail", kwargs={"id": workspace_1.id})

        reponse = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get(self, client, image_1):
        url = reverse(
            "image-detail",
            kwargs={
                "id": image_1.id,
            },
        )

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()
        self._assert_result(result, image_1)

    def test_update(self, client, image_1):
        url = reverse(
            "image-detail",
            kwargs={
                "id": image_1.id,
            },
        )

        response = client.patch(
            url,
            data=json.dumps(
                {
                    "url": "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing",
                    "y": "100.0",
                }
            ),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_200_OK

        image_1.refresh_from_db()
        result = response.json()

        self._assert_result(result, image_1)
        assert (
            image_1.url
            == "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing"
        )
        assert image_1.y == Decimal("100.0")

    def test_delete(self, client, image_1):
        image_1_id = image_1.id
        assert Image.objects.count() == 1

        url = reverse(
            "image-detail",
            kwargs={
                "id": image_1_id,
            },
        )

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not Image.objects.filter(id=image_1_id).exists()
        assert Image.objects.count() == 0
