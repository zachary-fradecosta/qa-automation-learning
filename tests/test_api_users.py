import requests
import pytest
import truststore

@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "name" in data

@pytest.mark.regression
@pytest.mark.api
def test_get_unknown_user_returns_not_found():
    url = "https://jsonplaceholder.typicode.com/users/999"
    response = requests.get(url, timeout=10)

    assert response.status_code == 404
