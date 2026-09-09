import pytest

@pytest.mark.regression
@pytest.mark.api
def test_api_session_headers(api_session):
    assert "Accept" in api_session.headers
    assert api_session.headers["Accept"] == "application/json"