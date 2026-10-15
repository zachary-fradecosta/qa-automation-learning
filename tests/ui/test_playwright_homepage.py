import re

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.smoke
def test_playwright_homepage_has_expected_title(page: Page):
    page.goto("https://playwright.dev/python/")
    expect(page).to_have_title(re.compile("Playwright"))

@pytest.mark.ui
@pytest.mark.smoke
def test_playwright_homepage_displays_main_heading(page: Page):
    page.goto("https://playwright.dev/python/")
    main_heading = page.get_by_role("heading", name=re.compile("Playwright enables reliable web automation"))
    expect(main_heading).to_be_visible()


@pytest.mark.ui
@pytest.mark.smoke
def test_playwright_homepage_displays_get_started_link(page: Page):
    page.goto("https://playwright.dev/python/")
    get_started_link = page.get_by_role("link", name="Get started")
    
    expect(get_started_link).to_be_visible()
    expect(get_started_link).to_be_enabled()
    expect(get_started_link).to_have_attribute("href", re.compile("/python/docs/intro"))


@pytest.mark.ui
@pytest.mark.smoke
def test_get_started_link_opens_installation_documentation(page: Page):
    page.goto("https://playwright.dev/python/")
    get_started_link = page.get_by_role("link", name="Get started")

    expect(get_started_link).to_be_visible()
    expect(get_started_link).to_be_enabled()
    get_started_link.click()
    
    expect(page).to_have_url(re.compile("/python/docs/intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()