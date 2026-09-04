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