import requests
import pytest

@pytest.mark.regression
@pytest.mark.api
def test_create_post_returns_created():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My first API post",
        "body": "Created during QA Automation learning",
        "userId": 1,
    }

    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 201

    data = response.json()
    assert isinstance(data, dict)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert isinstance(data["id"], int)

@pytest.mark.regression
@pytest.mark.api
def test_replace_post_returns_updated_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
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
def test_update_post_title_returns_partial_update():
    url = "https://jsonplaceholder.typicode.com/posts/1"
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
