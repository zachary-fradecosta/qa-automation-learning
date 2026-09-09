# API Testing Guide

## Install API dependencies

```powershell
pip install requests
pip install truststore
```

## Run the API demonstration script

```powershell
python scripts/api_demo.py
```

## Run API tests

```powershell
pytest tests/test_api_users.py -v
```

## Run one API test

```powershell
pytest tests/test_api_users.py::test_get_user_by_id -v
```

## API testing flow

```text
Request
↓
Response status code
↓
JSON response body
↓
Assertions
```

## Important HTTP status codes

```text
200 → successful request
201 → resource created
400 → invalid request
401 → authentication required
403 → access forbidden
404 → resource not found
500 → server error
```

## Basic Requests example

```python
import requests

response = requests.get(url, timeout=10)

assert response.status_code == 200

data = response.json()
assert "name" in data
```

## HTTPS certificate issue

If Python raises:

```text
SSLCertVerificationError
```

use `truststore` before importing `requests`:

```python
import truststore

truststore.inject_into_ssl()

import requests
```

Do not use `verify=False` in professional test code because it disables HTTPS certificate verification.


## Response payload validation

```python
data = response.json()

assert isinstance(data, dict)

required_fields = {"id", "name", "email"}
assert required_fields.issubset(data)

assert isinstance(data["id"], int)
assert isinstance(data["name"], str)
```

For a list response:

```python
assert isinstance(data, list)
assert len(data) > 0

required_fields = {"id", "name", "email"}
assert all(required_fields.issubset(user) for user in data)
```

## POST request example

Run the demonstration script:

```powershell
python scripts/api_post_demo.py
```

Create a post:

```python
payload = {
    "title": "My first API post",
    "body": "Created during QA Automation learning",
    "userId": 1,
}

response = requests.post(url, json=payload, timeout=10)

assert response.status_code == 201

data = response.json()
assert data["title"] == payload["title"]
assert data["body"] == payload["body"]
assert data["userId"] == payload["userId"]
assert isinstance(data["id"], int)
```

## PUT request example

```powershell
python scripts/api_put_demo.py
```

```python
response = requests.put(url, json=payload, timeout=10)

assert response.status_code == 200
```

## PATCH request example

```python
payload = {
    "title": "Updated API post",
}

response = requests.patch(url, json=payload, timeout=10)

assert response.status_code == 200

data = response.json()
assert data["title"] == payload["title"]
assert data["id"] == 1
```

## DELETE request example

Run the demonstration script:

```powershell
python scripts/api_delete_demo.py
```

```python
response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10,
)

assert response.status_code == 200, "Expected HTTP 200 after deleting the post"

data = response.json()
assert data == {}, "Expected an empty JSON object after deleting the post"
```

## Reusable API configuration with Pytest fixtures

Store shared API configuration and reusable test data in `tests/conftest.py`.

```python
@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def valid_post_payload():
    return {
        "title": "My first API post",
        "body": "Created during QA Automation learning",
        "userId": 1,
    }
```

Pytest injects these fixtures automatically into tests. Build endpoint URLs from the shared base URL and reuse the payload where required.

```python
def test_create_post_returns_created(api_base_url, valid_post_payload):
    url = f"{api_base_url}/posts"

    response = requests.post(
        url,
        json=valid_post_payload,
        timeout=10,
    )

    assert response.status_code == 201
```

Centralizing the base URL prevents duplicated configuration, makes environment changes safer, and reduces the risk of sending write requests to the wrong environment.


## Reusable HTTP sessions

Use a Pytest fixture to create a reusable HTTP session for API tests. `yield` provides the session to the test, and the code after `yield` cleans up the resource once the test is finished.

```python
import requests
import pytest


@pytest.fixture
def api_session():
    session = requests.Session()

    yield session

    session.close()
```

Inject the fixture into a test and use session methods instead of direct `requests` calls.

```python
def test_get_user_by_id(api_base_url, api_session):
    url = f"{api_base_url}/users/1"

    response = api_session.get(url, timeout=10)

    assert response.status_code == 200
```

The same session object can send all HTTP methods:

```python
api_session.get(url, timeout=10)
api_session.post(url, json=payload, timeout=10)
api_session.put(url, json=payload, timeout=10)
api_session.patch(url, json=payload, timeout=10)
api_session.delete(url, timeout=10)
```

A session manages HTTP communication. The `api_base_url` fixture remains responsible for identifying the target environment.


## HTTP headers and JSON response contracts

HTTP headers provide information about the request and response format. The `Accept` request header tells the API that the client expects JSON. The `Content-Type` response header tells the client which format the API actually returned.

Configure the shared session in `tests/conftest.py`:

```python
@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})

    yield session

    session.close()
```

Test the session configuration:

```python
@pytest.mark.regression
@pytest.mark.api
def test_api_session_headers(api_session):
    assert "Accept" in api_session.headers
    assert api_session.headers["Accept"] == "application/json"
```

Validate that an API response declares JSON without making an overly strict comparison:

```python
assert response.headers["Content-Type"].startswith(
    "application/json"
), "The API response should declare JSON content type in the headers"
```

Use `response.request.headers` to inspect headers sent by the test, and `response.headers` to inspect headers received from the API.

```python
assert response.request.headers.get("Accept") == "application/json", (
    "The API request should declare an Accept header for JSON responses"
)
```