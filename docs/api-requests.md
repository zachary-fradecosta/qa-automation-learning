# API Requests Guide


## Install API dependencies

```powershell
pip install requests
pip install truststore
```


## HTTPS certificate issue

If Python raises `SSLCertVerificationError`, use the Windows certificate store before importing `requests`:

```python
import truststore

truststore.inject_into_ssl()

import requests
```

Do not use `verify=False` in professional test code because it disables HTTPS certificate verification.


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


## Run API demonstration scripts

```powershell
python scripts/api_demo.py
python scripts/api_post_demo.py
python scripts/api_put_demo.py
python scripts/api_delete_demo.py
```


## GET request

```python
response = requests.get(url, timeout=10)

assert response.status_code == 200

data = response.json()
assert "name" in data
```


## POST request

```python
payload = {
    "title": "My first API post",
    "body": "Created during QA Automation learning",
    "userId": 1,
}

response = requests.post(url, json=payload, timeout=10)

assert response.status_code == 201
```

Use `json=payload` to send a Python dictionary as JSON.


## PUT request

Use `PUT` when replacing a complete resource.

```python
response = requests.put(url, json=payload, timeout=10)

assert response.status_code == 200
```


## PATCH request

Use `PATCH` when updating only selected fields.

```python
payload = {
    "title": "Updated API post",
}

response = requests.patch(url, json=payload, timeout=10)

assert response.status_code == 200
```


## DELETE request

```python
response = requests.delete(url, timeout=10)

assert response.status_code == 200
```

A successful DELETE response depends on the API contract. Some APIs return `200 OK` with a body; others return `204 No Content` with no body. JSONPlaceholder simulates write operations and returns `200` with an empty JSON object for this endpoint.



## Configurable request timeouts

Always define a timeout for external API requests. A client function can provide a safe default while allowing the caller to choose a different value.

```python
def get_user_by_id(api_session, api_base_url, user_id, timeout=10):
    url = f"{api_base_url}/users/{user_id}"

    response = api_session.get(url, timeout=timeout)
    response.raise_for_status()

    return response.json()
```

```text
HTTPError       → the server returned a 4xx or 5xx response
Timeout         → the client waited too long for the connection or data
ConnectionError → the connection could not be established
```

A Requests timeout is not necessarily a strict limit for the complete operation. It controls how long the client waits during connection and response activity.



## Query parameters and filtering

Query parameters filter or modify a collection request.

```text
/users/1         → retrieve one specific user
/posts           → retrieve the posts collection
/posts?userId=1  → retrieve posts belonging to user 1
```

Use the Requests `params` argument instead of building the query string manually.

```python
def get_posts_by_user_id(
    api_session,
    api_base_url,
    user_id,
    timeout=10,
):
    url = f"{api_base_url}/posts"
    params = {
        "userId": user_id,
    }

    response = api_session.get(
        url,
        params=params,
        timeout=timeout,
    )
    response.raise_for_status()

    return response.json()
```

Requests converts the dictionary into the query string `?userId=1` and handles value encoding.



## Pagination Query Parameters

Pagination limits the number of resources returned by one API request. The client can send the requested page and page size through the `params` argument:

```python
params = {
    "_page": page,
    "_per_page": per_page,
}

response = api_session.get(
    f"{api_base_url}/posts",
    params=params,
    timeout=timeout,
)
```

Requests builds a URL such as:

```text
/posts?_page=2&_per_page=10
```

Pagination parameter names depend on the API contract. Common alternatives include `page`, `page_size`, `limit`, `offset`, `_page`, and `_per_page`.



## Bearer Token Authentication

Protected API endpoints commonly expect an access token in the `Authorization` request header:

```text
Authorization: Bearer <token>
```

The client can send this header with Requests:

```python
headers = {
    "Authorization": f"Bearer {token}"
}

response = api_session.get(
    url,
    headers=headers,
    timeout=timeout,
)
```

Tests can inspect the request intercepted by `requests-mock`:

```python
request_headers = requests_mock.last_request.headers

assert request_headers.get("Authorization") == f"Bearer {token}"
```

Only fictional tokens should be committed to the repository. Real API tokens must be supplied through protected environment variables or CI secrets and must never appear in source code, documentation, test reports, or logs.