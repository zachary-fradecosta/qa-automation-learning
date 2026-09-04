# Pytest Guide

## Check the installed version

```powershell
pytest --version
```

## Run the complete test suite

```powershell
pytest -v
```

`-v` displays each test name and result.

## Run one test file

```powershell
pytest tests/test_user_helpers.py -v
```

## Run one specific test

```powershell
pytest tests/test_user_helpers.py::test_get_active_users -v
```

## Run API tests

```powershell
pytest tests/test_api_users.py -v
```

## Run one API test

```powershell
pytest tests/test_api_users.py::test_get_user_by_id -v
```

## Run smoke tests

```powershell
pytest -m smoke -v
```

## Run regression tests

```powershell
pytest -m regression -v
```

## Combine markers

```powershell
pytest -m "smoke or regression" -v
```

## Exclude smoke tests

```powershell
pytest -m "not smoke" -v
```

## Test naming convention

```python
def test_expected_behavior():
    ...
```

Pytest automatically discovers files named `test_*.py` and functions named `test_*`.