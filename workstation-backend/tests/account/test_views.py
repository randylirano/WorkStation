import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_register(client):
    url = reverse("account-register")
    response = client.post(
        url,
        data={
            "username": "test_user",
            "email": "test@test.com",
            "password": "testpassword",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "test_user",
        "message": ("User Created Successfully. Perform Login to get your token."),
    }
