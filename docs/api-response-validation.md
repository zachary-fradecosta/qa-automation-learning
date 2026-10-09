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



## Validating filtered collections

A filtered collection test should verify the collection type, its expected size, and the business rule applied to every item.

```python
assert isinstance(posts, list)
assert len(posts) == 2
assert all(post["userId"] == user_id for post in posts)
```

A valid collection request with no matching resources can return `200 OK` and an empty list.

```python
assert isinstance(posts, list)
assert posts == []
```

This differs from requesting an individual resource that does not exist, which can return `404 Not Found`.



## Validating Paginated Responses

A paginated response can contain both page data and pagination metadata:

```python
{
    "prev": 1,
    "next": 3,
    "last": 3,
    "pages": 3,
    "items": 5,
    "data": [...]
}
```

The number of items in `data` represents the current page, while `items` represents the complete collection. A page size is normally a maximum rather than a mandatory result count. The final page can therefore contain fewer items:

```python
assert len(response_data["data"]) <= per_page
assert response_data["next"] is None
```

Tests should validate page content, total collection metadata, navigation metadata, and partial final pages according to the API contract.