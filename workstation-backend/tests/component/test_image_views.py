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
class TestImageList(BaseTestImage):
    url = reverse("image-list")

    def test_get_invalid_workspace_id(self, client):
        # workspace id not provided
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

        # workspace id does not exist in DB
        response = client.get(self.url, {"workspace_id":uuid4()})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []


    def test_get_valid_workspace_id(self, client, workspace_1, workspace_2, image_1, image_2, image_3, image_4):
        response_1 = client.get(self.url, {"workspace_id":workspace_1.id})
        assert response_1.status_code == status.HTTP_200_OK
        result_1 = response_1.json()
        assert len(result_1) == 2
        self._assert_result(result_1[0], image_1)
        self._assert_result(result_1[1], image_2)

        response_2 = client.get(self.url, {"workspace_id":workspace_2.id})
        assert response_2.status_code == status.HTTP_200_OK
        result_2 = response_2.json()
        assert len(result_2) == 2
        self._assert_result(result_2[0], image_3)
        self._assert_result(result_2[1], image_4)
