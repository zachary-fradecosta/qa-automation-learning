import requests
import pytest


@pytest.mark.regression
@pytest.mark.api
def test_create_post_returns_created(api_base_url, valid_post_payload):
    url = f"{api_base_url}/posts"

    response = requests.post(url, json=valid_post_payload, timeout=10)
    assert response.status_code == 201

    data = response.json()
    assert isinstance(data, dict)
    assert data["title"] == valid_post_payload["title"]
    assert data["body"] == valid_post_payload["body"]
    assert data["userId"] == valid_post_payload["userId"]
    assert isinstance(data["id"], int)


@pytest.mark.regression
@pytest.mark.api
def test_replace_post_returns_updated_post(api_base_url):
    url = f"{api_base_url}/posts/1"
    payload = {
        "id": 1,
        "title": "My first API post",
        "body": "Created during QA Automation learning",
        "userId": 1,
    }

    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.api
def test_update_post_title_returns_partial_update(api_base_url):
    url = f"{api_base_url}/posts/1"
    payload = {
        "title": "My first API post"
    }

    response = requests.patch(url, json=payload, timeout=10)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert "body" in data


@pytest.mark.regression
@pytest.mark.api
def test_delete_post_returns_success(api_base_url):
    url = f"{api_base_url}/posts/1"

    response = requests.delete(url, timeout=10)
    assert response.status_code == 200, "Expected HTTP 200 after deleting the post"

    data = response.json()
    assert isinstance(data, dict)
    assert data == {}, "Expected an empty JSON object after deleting the post"
