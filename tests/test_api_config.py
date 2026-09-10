import pytest
from utils.api_config import get_api_base_url


@pytest.mark.regression
@pytest.mark.api
def test_get_api_base_url_returns_test_url_when_env_is_missing(monkeypatch):
    monkeypatch.delenv("QA_ENV", raising=False)
    base_url = get_api_base_url()
    assert base_url == "https://jsonplaceholder.typicode.com"

@pytest.mark.regression
@pytest.mark.api
def test_get_api_base_url_returns_error_when_env_is_invalid(monkeypatch):
    monkeypatch.setenv("QA_ENV", "production")
    with pytest.raises(ValueError):
        get_api_base_url()
