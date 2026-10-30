import pytest
from playwright.sync_api import Page

TODO_APP_URL = "https://demo.playwright.dev/todomvc/"

@pytest.fixture
def todo_page(page: Page):
    page.goto(TODO_APP_URL)
    return page
