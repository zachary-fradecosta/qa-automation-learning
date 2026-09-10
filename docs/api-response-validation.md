# API Response Validation Guide

## Validate a JSON object

After checking the HTTP status, convert the response body to Python data and validate its contract.

```python
data = response.json()

assert isinstance(data, dict)

required_fields = {"id", "name", "email"}
assert required_fields.issubset(data)

assert isinstance(data["id"], int)
assert isinstance(data["name"], str)
assert isinstance(data["email"], str)
```

## Validate a JSON list

```python
data = response.json()

assert isinstance(data, list)
assert len(data) > 0

required_fields = {"id", "name", "email"}
assert all(required_fields.issubset(user) for user in data)
```

`all(...)` verifies that every item in the list satisfies the condition.

## Validate a created resource

```python
data = response.json()

assert isinstance(data, dict)
assert data["title"] == payload["title"]
assert data["body"] == payload["body"]
assert data["userId"] == payload["userId"]
assert isinstance(data["id"], int)
```

## Request and response headers

Headers provide information about the format of an HTTP request and response.

```text
Accept        → format requested by the client
Content-Type  → format sent by the client or returned by the server
```

Verify that the request asked for JSON:

```python
assert response.request.headers.get("Accept") == "application/json", (
    "The API request should declare an Accept header for JSON responses"
)
```

Verify that the API response declares JSON:

```python
assert response.headers["Content-Type"].startswith("application/json"), (
    "The API response should declare JSON content type in the headers"
)
```

Use `startswith("application/json")` rather than an exact equality check because valid responses can include an encoding such as `application/json; charset=utf-8`.

## Useful assertion messages

An assertion message should explain the expected API contract:

```python
assert response.status_code == 201, "Expected HTTP 201 after creating a post"
```

Messages make a failed test easier to diagnose in local execution and CI logs.
