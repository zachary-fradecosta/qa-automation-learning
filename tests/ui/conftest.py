import pytest
from playwright.sync_api import Page
from urllib.parse import urlparse


ALLOWED_UI_HOSTS = {"demo.playwright.dev"}

@pytest.fixture
def todo_page(page: Page):
    page.goto("/todomvc/")
    return page

@pytest.fixture(scope="session", autouse=True)
def validate_ui_environment(base_url):
    parsed_url = urlparse(base_url)
    if parsed_url.hostname not in ALLOWED_UI_HOSTS:
        pytest.fail(f"Unsafe UI environment: {parsed_url.hostname} is not allowed")