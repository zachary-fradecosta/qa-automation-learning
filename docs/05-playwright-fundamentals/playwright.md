# Playwright Fundamentals

## Installation

Install the Playwright Pytest plugin:

```powershell
python -m pip install pytest-playwright
```

Install the Chromium browser:

```powershell
python -m playwright install chromium
```

Check the installed versions:

```powershell
python -m pip show playwright
python -m pip show pytest-playwright
```

## The `page` fixture

The Playwright Pytest plugin provides the `page` fixture automatically:

```python
from playwright.sync_api import Page

def test_example(page: Page):
    page.goto("https://example.com")
```

The fixture opens an isolated browser page for the test.

## Navigation

Navigate to a page with:

```python
page.goto("https://example.com")
```

## Accessible locators

Prefer locators based on the role and accessible name of an element:

```python
heading = page.get_by_role("heading", name="Example Domain")
link = page.get_by_role("link", name="More information")
```

These locators describe how a user or assistive technology identifies the element.

## Web-first assertions

Import Playwright's `expect` function:

```python
from playwright.sync_api import expect
```

Verify that an element is visible:

```python
expect(heading).to_be_visible()
```

Verify that a link is enabled:

```python
expect(link).to_be_enabled()
```

Verify an attribute:

```python
expect(link).to_have_attribute("href", "/documentation")
```

Verify the page URL:

```python
expect(page).to_have_url("https://example.com/documentation")
```

Verify the page title:

```python
expect(page).to_have_title("Example Domain")
```

## Regular expressions

Regular expressions can make assertions less dependent on an exact value:

```python
import re

expect(page).to_have_title(re.compile("Playwright"))
```

They can also be used with locators:

```python
heading = page.get_by_role(
    "heading",
    name=re.compile("Playwright enables reliable web automation"),
)
```

## Automatic waiting

Playwright assertions automatically retry until:

- the expected condition becomes true;
- or the assertion timeout expires.

Avoid fixed waits such as:

```python
time.sleep(5)
```

A fixed wait can be too short on a slow environment or unnecessarily long on a fast environment. It also does not verify that the expected condition has become true.

## Running UI tests

Run every UI test:

```powershell
pytest -m ui -v
```

Run one UI test file:

```powershell
pytest tests/ui/test_playwright_homepage.py -v
```

Run tests with a visible browser:

```powershell
pytest tests/ui/test_playwright_homepage.py --headed -v
```

Run tests on Chromium:

```powershell
pytest tests/ui/test_playwright_homepage.py --browser chromium -v
```

## Key takeaway

A Playwright test reproduces a user interaction in a browser and verifies the resulting UI behavior. Accessible locators and web-first assertions make browser tests clearer and more reliable.