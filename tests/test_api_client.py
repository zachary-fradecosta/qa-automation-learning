import pytest
from utils.api_client import get_user_by_id

@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    mock_user = {"id": 1, "name": "Test User"}
    requests_mock.get(
        url, 
        json=mock_user, 
        status_code=200)
    response = get_user_by_id(api_session, api_base_url, 1)
    assert response.status_code == 200
    assert response.json() == mock_user
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Test User"

@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_not_found(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/999"
    requests_mock.get(
        url,  
        status_code=404)
    response = get_user_by_id(api_session, api_base_url, 999)
    assert response.status_code == 404, "Expected HTTP 404 for an unknown user"


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_server_error(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    requests_mock.get(
            url,  
            status_code=500)
    response = get_user_by_id(api_session, api_base_url, 1)
    assert response.status_code == 500, "Expected HTTP 500 for a server error, not a valid user response" 
