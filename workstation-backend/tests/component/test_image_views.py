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

    def test_get_not_found(self, client):
        """
        Test get on invalid workspace id.
        No workspace and image fixture provided.
        """

        # no workspace id provided and no image in DB ==> []
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

        # workspace id does not exist in DB ==> []
        response = client.get(self.url, {"workspace_id":uuid4()})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []


    def test_get_found(self, client, workspace_1, workspace_2, workspace_3, image_1, image_2, image_3, image_4):
        """
        Test get on valid workspace id.
        Use pre-defined test fixtures.
        Workspace 1 and 2 has 2 images each, and workspace 3 is empty.
        """
        # workspace id not provided ==> [all current user's images]
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        result_0 = response.json()
        assert len(result_0) == 4

        # get all images from workspace 1
        response_1 = client.get(self.url, {"workspace_id":workspace_1.id})
        assert response_1.status_code == status.HTTP_200_OK
        result_1 = response_1.json()
        assert len(result_1) == 2
        self._assert_result(result_1[0], image_1)
        self._assert_result(result_1[1], image_2)

        # get all images from workspace_2
        response_2 = client.get(self.url, {"workspace_id":workspace_2.id})
        assert response_2.status_code == status.HTTP_200_OK
        result_2 = response_2.json()
        assert len(result_2) == 2
        self._assert_result(result_2[0], image_3)
        self._assert_result(result_2[1], image_4)

        # get all images from workspace 3, currently contain no image
        response_3 = client.get(self.url, {"workspace_id":workspace_3.id})
        assert response_3.status_code == status.HTTP_200_OK
        result_3 = response_3.json()
        assert len(result_3) == 0


    def test_post_invalid_workspace(self, client):
        """
        Test post on invalid workspace.
        No test fixture was provided.
        """
        # post without workspace id ==> no image created, receive a code HTTP_400_BAD_REQUEST
        response_0 = client.post(
            self.url,
            data={
                "x": 0.0,
                "y": -100.0,
                "width": 3.0,
                "height": 3.0,
                "url": "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing"
            },
        )

        assert response_0.status_code == status.HTTP_400_BAD_REQUEST

        # post to invalid workspace id ==> no image created, receive a code HTTP_400_BAD_REQUEST
        response_1 = client.post(
            self.url,
            data={
                "x": 0.0,
                "y": -100.0,
                "width": 3.0,
                "height": 3.0,
                "url": "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing",
                "workspace_id": uuid4()
            },
        )

        assert response_1.status_code == status.HTTP_400_BAD_REQUEST
        assert response_1.data == {"workspace_id": "Workspace doesn't exist"}


    def test_post_valid_workspace(self, client, workspace_1):
        """
        Test on valid workspace id.
        Using pre-defined workspace fixture, workspace_1.
        """

        # several valid and invalid image payloads
        # dog 1 image
        valid_payload_1 = {
            "workspace_id": workspace_1.id,
            "x": 0,
            "y": -100,
            "width": 3.0,
            "height": 3.0,
            "url": "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing",
        }

        # dog 2 image
        valid_payload_2 = {
            "workspace_id": workspace_1.id,
            "x": 0,
            "y": -100,
            "width": 3.0,
            "height": 3.0,
            "url": "https://drive.google.com/file/d/1gBEz1xudWrx9YTWJUH1nldIP8WOP6nAL/view?usp=sharing",
        }

        # payload with missing required data except workspace id
        invalid_payload = {
            "workspace_id": workspace_1.id,
            "y": -100,
            "width": 3.0,
            "height": 3.0,
        }

        # test post valid payload
        response = client.post(
            self.url,
            data=valid_payload_1,
        )

        assert response.status_code == status.HTTP_201_CREATED

        response = client.get(self.url, {"workspace_id":workspace_1.id})
        result = response.json()
        image = result[0]
        # print(image)
        assert image["workspace_id"] == str(workspace_1.id)
        assert Decimal(image["x"]) == Decimal("0")
        assert Decimal(image["y"]) == Decimal("-100.0")
        assert Decimal(image["width"]) == Decimal("3.0")
        assert Decimal(image["height"]) == Decimal("3.0")
        assert image["url"] == "https://drive.google.com/file/d/1isn9sfa0He-YcxeJDzwsJz_6uGklH3ES/view?usp=sharing"

        # test post different valid payload into the same workspace
        response = client.post(
            self.url,
            data=valid_payload_2,
        )
        response = client.get(self.url, {"workspace_id":workspace_1.id})
        result = response.json()
        assert len(result) == 2

        # at this point, image of dog 1 and 2 should be in workspace 1
        # try posting image of dog 1 again to workspace 1, this will create duplicate image url condition
        # this should still allows an input
        response = client.post(
            self.url,
            data=valid_payload_1,
        )
        response = client.get(self.url, {"workspace_id":workspace_1.id})
        result = response.json()
        assert len(result) == 3

        # test post an invalid payload
        response = client.post(
            self.url,
            data=invalid_payload,
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "url" in response.data
        assert "x" in response.data


@pytest.mark.django_db
class TestImageDetail(BaseTestImage):
    url = reverse("image-detail")
