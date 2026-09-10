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
