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