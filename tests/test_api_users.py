import pytest


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id(api_base_url, api_session):
    url = f"{api_base_url}/users/1"
    response = api_session.get(url, timeout=10)
    
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1

    required_fields = {"id", "name", "username", "email"} 
    assert required_fields.issubset(data)
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)


@pytest.mark.regression
@pytest.mark.api
def test_get_unknown_user_returns_not_found(api_base_url, api_session):
    url = f"{api_base_url}/users/999"
    response = api_session.get(url, timeout=10)

    assert response.status_code == 404

@pytest.mark.regression
@pytest.mark.api
def test_get_all_users_returns_valid_user_list(api_base_url, api_session):
    url = f"{api_base_url}/users"
    response = api_session.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    required_fields = {"id", "name", "email"}
    assert all(required_fields.issubset(user) for user in data)

    
     
