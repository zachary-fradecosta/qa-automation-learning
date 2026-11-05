import pytest
from urllib.parse import urlparse

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_base_url_targets_expected_environment(base_url):
    parsed_url = urlparse(base_url)
    assert parsed_url.scheme == "https"
    assert parsed_url.hostname == "demo.playwright.dev"