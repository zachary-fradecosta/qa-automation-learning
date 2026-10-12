import pytest
import requests
import requests_mock
from tests.conftest import api_base_url, api_session
from utils.api_client import get_user_by_id, get_posts_by_user_id, get_posts_page, get_private_profile

@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    mock_user = {
        "id": 1, 
        "name": "Test User"
    }

    requests_mock.get(
        url, 
        json=mock_user, 
        status_code=200
    )
    user_data = get_user_by_id(api_session, api_base_url, 1)
    
    assert user_data["id"] == mock_user["id"]
    assert user_data["name"] == mock_user["name"]


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_not_found(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/999"
    requests_mock.get(
        url,  
        status_code=404
    )
    with pytest.raises(requests.exceptions.HTTPError):
        get_user_by_id(api_session, api_base_url, 999)


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_server_error(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    requests_mock.get(
        url,  
        status_code=500
    )

    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        get_user_by_id(api_session, api_base_url, 1)
    assert exc_info.value.response.status_code == 500, "Expected HTTP 500 for a server error, not a valid user response"


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_uses_default_timeout(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    mock_user = {
        "id": 1, 
        "name": "Test User"
    }

    requests_mock.get(
        url, 
        json=mock_user, 
        status_code=200
    )

    get_user_by_id(api_session, api_base_url, 1)
    assert requests_mock.last_request.timeout == 10


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_with_custom_timeout(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    mock_user = {
        "id": 1, 
        "name": "Test User"
    }

    requests_mock.get(
        url, 
        json=mock_user, 
        status_code=200
    )

    get_user_by_id(api_session, api_base_url, 1, timeout=3)
    assert requests_mock.last_request.timeout == 3


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_raises_timeout_when_request_times_out(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    requests_mock.get(
        url, 
        exc=requests.exceptions.Timeout,
    )

    with pytest.raises(requests.exceptions.Timeout):
        get_user_by_id(api_session, api_base_url, 1)


@pytest.mark.regression
@pytest.mark.api
def test_get_user_by_id_raises_connection_error_when_connection_fails(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/users/1"
    requests_mock.get(
        url, 
        exc=requests.exceptions.ConnectionError,
    )

    with pytest.raises(requests.exceptions.ConnectionError):
        get_user_by_id(api_session, api_base_url, 1)


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_by_user_id(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/posts"
    user_id = 1
    mock_posts = [
        {"userId": user_id},
        {"userId": user_id}
    ]
    requests_mock.get(
        url,
        json=mock_posts,
        status_code=200
    )

    posts = get_posts_by_user_id(api_session, api_base_url, user_id=1)
    assert posts == mock_posts, "Expected the returned posts to match the mock posts"
    assert len(posts) == 2, "Expected 2 posts for userId 1"
    assert all(post["userId"] == user_id for post in posts), "Expected all posts to have userId 1"


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_by_user_id_query_params(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/posts"
    user_id = 1
    mock_posts = [
        {"userId": user_id, "id": 1},
        {"userId": user_id, "id": 2}
    ]
    requests_mock.get(
        url,
        json=mock_posts,
        status_code=200
    )

    get_posts_by_user_id(api_session, api_base_url, user_id=user_id)
    query_params = requests_mock.last_request.qs
    assert query_params.get("userid") == [str(user_id)], "Expected the query parameter userId to match the requested user_id"


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_by_user_id_empty(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/posts"
    user_id = 999
    mock_posts = []
    requests_mock.get(
        url,
        json=mock_posts,
        status_code=200
    )

    posts = get_posts_by_user_id(api_session, api_base_url, user_id=user_id)
    assert isinstance(posts, list), "Expected the returned posts to be a list"
    assert posts == mock_posts, "Expected the returned posts to be an empty list"


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_page_returns_requested_page(api_session, api_base_url, requests_mock):
    url = f"{api_base_url}/posts"
    
    mock_response = {
        "prev": 1,
        "next": 3,
        "pages": 2,
        "items": 5,
        "data": [
            {
                "id": 3,
                "userId": 1,
                "title": "Third post"
            },
            {
                "id": 4,
                "userId": 1,
                "title": "Fourth post"
            }
        ]
    }

    requests_mock.get(
        url,
        json=mock_response,
        status_code=200
    )

    page = 2
    per_page = 2
    posts_page = get_posts_page(api_session, api_base_url, page=page, per_page=per_page)
    assert isinstance(posts_page, dict), "Expected the returned posts page to be a dictionary"
    assert isinstance(posts_page.get("data"), list), "Expected the 'data' field to be a list"
    
    assert len(posts_page.get("data")) == 2, "Expected 2 posts in the 'data' field"
    post_ids = [post["id"] for post in posts_page.get("data")]
    assert post_ids == [3, 4], "Expected the post IDs in the 'data' field to be [3, 4]"
    assert posts_page.get("items") == 5, "Expected the 'items' field to be 5"


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_page_sends_pagination_query_params(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/posts"
    page = 2
    per_page = 2

    requests_mock.get(
        url,
        json={"data": []},
        status_code=200
    )

    get_posts_page(api_session, api_base_url, page=page, per_page=per_page)
    query_params = requests_mock.last_request.qs
    assert query_params.get("_page") == [str(page)], "Expected the query parameter page to match the requested page"
    assert query_params.get("_per_page") == [str(per_page)], "Expected the query parameter per_page to match the requested per_page"


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_page_returns_partial_last_page(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/posts"
    
    mock_response = {
        "prev": 2,
        "next": None,
        "last": 3,
        "pages": 3,
        "items": 5,
        "data": [
            {
                "id": 5,
                "userId": 1,
                "title": "Fifth post"
            }
        ]
    }

    requests_mock.get(
        url,
        json=mock_response,
        status_code=200
    )

    page = 3
    per_page = 2
    posts_page = get_posts_page(api_session, api_base_url, page=page, per_page=per_page)
    assert posts_page.get("last") == 3, "Expected the 'last' field to be 3"
    assert posts_page.get("next") is None, "Expected the 'next' field to be None"
    assert len(posts_page.get("data")) == 1, "Expected the 'data' field to contain 1 post"
    post_ids = [post["id"] for post in posts_page.get("data")]
    assert post_ids == [5], "Expected the post IDs in the 'data' field to be [5]"
    assert len(posts_page.get("data")) <= per_page, "Expected the 'data' field to contain at most 'per_page' posts"


@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize(
    "page, per_page",
    [
        (0, 2),
        (-3, 2),
        (None, 26),
        (1, None),
        (2, -2),
        (3, 0),
        (4, 1000),
    ],
)
def test_get_posts_page_rejects_invalid_pagination(
    api_session,
    api_base_url,
    requests_mock,
    page,
    per_page,
):
    with pytest.raises(ValueError):
        get_posts_page(
            api_session,
            api_base_url,
            page=page,
            per_page=per_page,  
        )

    assert requests_mock.called is False


@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize(
    "page, per_page",
    [
        (1, 1),
        (1, 7),
        (1, 100),
    ],
)
def test_get_posts_page_accepts_valid_boundaries(
    api_session,
    api_base_url,
    requests_mock,
    page,
    per_page,
):
    url = f"{api_base_url}/posts"
    mock_response = {
        "data": []
    }

    requests_mock.get(
        url,
        json=mock_response,
        status_code=200
    )

    posts_page = get_posts_page(api_session, api_base_url, page=page, per_page=per_page)
    assert posts_page == mock_response, "Expected the posts page to match the mock response"
    assert requests_mock.called is True, "Expected the requests_mock to have been called"


@pytest.mark.regression
@pytest.mark.api
def test_get_private_profile_returns_profile_for_valid_token(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/profile"
    token = "test-token-123"
    mock_response = {
        "id": 1,
        "username": "standard_user",
        "role": "customer",
    }

    requests_mock.get(
        url,
        json=mock_response,
        status_code=200
    )
    profile = get_private_profile(api_session, api_base_url, token=token)
    assert profile == mock_response, "Expected the profile to match the mock response"
    assert profile["id"] == mock_response["id"], "Expected the profile ID to match the mock response"
    assert profile["username"] == mock_response["username"], "Expected the profile username to match the mock response"


@pytest.mark.regression
@pytest.mark.api
def test_get_private_profile_sends_bearer_token(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/profile"
    token = "test-token-123"

    requests_mock.get(
        url,
        json={},
        status_code=200
    )

    get_private_profile(api_session, api_base_url, token=token)
    request_headers = requests_mock.last_request.headers
    assert request_headers.get("Authorization") == f"Bearer {token}", "Expected the Authorization header to contain the Bearer token"

@pytest.mark.regression
@pytest.mark.api
def test_get_private_profile_raises_http_error_for_invalid_token(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/profile"
    token = "invalid-token-123"

    requests_mock.get(
        url,
        json={"detail": "Invalid token."},
        status_code=401
    )

    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        get_private_profile(api_session, api_base_url, token=token) 

    assert exc_info.value.response.status_code == 401, "Expected a 401 Unauthorized status code for an invalid token"


@pytest.mark.regression
@pytest.mark.api
def test_get_private_profile_raises_http_error_when_access_is_forbidden(
    api_session,
    api_base_url,
    requests_mock,
):
    url = f"{api_base_url}/profile"
    token = "forbidden-token-123"

    requests_mock.get(
        url,
        json={"detail": "Access forbidden."},
        status_code=403
    )

    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        get_private_profile(api_session, api_base_url, token=token)

    assert exc_info.value.response.status_code == 403, "Expected a 403 Forbidden status code when access is forbidden"
