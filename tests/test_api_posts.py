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
