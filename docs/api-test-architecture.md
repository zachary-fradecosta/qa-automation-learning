# API Test Architecture Guide

## Shared API base URL

Keep the API base URL in a Pytest fixture instead of repeating it in every test.

```python
@pytest.fixture
def api_base_url():
    return get_api_base_url()
```

Build endpoint URLs with f-strings:

```python
url = f"{api_base_url}/users/1"
```

## Reusable request data

Fixtures can provide reusable request payloads.

```python
@pytest.fixture
def valid_post_payload():
    return {
        "title": "My first API post",
        "body": "Created during QA Automation learning",
        "userId": 1,
    }
```

Use the fixture directly in a test:

```python
def test_create_post_returns_created(api_base_url, valid_post_payload):
    url = f"{api_base_url}/posts"
    response = requests.post(url, json=valid_post_payload, timeout=10)

    assert response.status_code == 201
```

## Reusable HTTP sessions

Use a session fixture to centralize HTTP configuration and close the session after each test.

```python
@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})

    yield session

    session.close()
```

The session can send every HTTP method:

```python
api_session.get(url, timeout=10)
api_session.post(url, json=payload, timeout=10)
api_session.put(url, json=payload, timeout=10)
api_session.patch(url, json=payload, timeout=10)
api_session.delete(url, timeout=10)
```

## Safe environment configuration

Keep environment selection in `utils/api_config.py`. Only approved environments should be allowed.

```python
import os


API_ENVIRONMENTS = {
    "test": "https://jsonplaceholder.typicode.com",
}


def get_api_base_url():
    env = os.getenv("QA_ENV", "test")

    if env not in API_ENVIRONMENTS:
        raise ValueError(f"Invalid API environment: {env}")

    return API_ENVIRONMENTS[env]
```

The default environment is `test`. An unknown value causes an explicit error instead of allowing an arbitrary URL.

## Test configuration without network calls

Use Pytest's `monkeypatch` fixture to change environment variables temporarily.

```python
def test_get_api_base_url_returns_test_url_when_env_is_missing(monkeypatch):
    monkeypatch.delenv("QA_ENV", raising=False)

    assert get_api_base_url() == "https://jsonplaceholder.typicode.com"


def test_get_api_base_url_returns_error_when_env_is_invalid(monkeypatch):
    monkeypatch.setenv("QA_ENV", "production")

    with pytest.raises(ValueError):
        get_api_base_url()
```

This protects the test suite from accidentally targeting an environment that has not been explicitly approved.
