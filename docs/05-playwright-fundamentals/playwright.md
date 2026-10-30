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


## Form interactions

Fill an input field:

```python
todo_input.fill("Learn Playwright")
```

Send a keyboard key:

```python
todo_input.press("Enter")
```

Verify the current value:

```python
expect(todo_input).to_have_value("Learn Playwright")
```

Verify that the field was cleared:

```python
expect(todo_input).to_have_value("")
```

## Locator collections

A locator can represent multiple matching elements:

```python
todo_items = page.get_by_test_id("todo-item")
```

Verify the number of matching elements:

```python
expect(todo_items).to_have_count(2)
```

## Filtering a locator collection

Filter a collection by its displayed text:

```python
todo_item = todo_items.filter(has_text="Write UI tests")
```

This first identifies all Todo items and then selects the one containing the expected text.

## Locating an element inside another element

Once the correct Todo item has been found, locate its checkbox:

```python
todo_checkbox = todo_item.get_by_role("checkbox")
```

This is more robust and expressive than searching for every checkbox on the page.

## Checkbox interactions

Check a checkbox:

```python
todo_checkbox.check()
```

Verify its state:

```python
expect(todo_checkbox).to_be_checked()
```

## Exact text matching

By default, a text locator may match a longer string containing the expected text.

Use `exact=True` when the complete text must match:

```python
todo_item = page.get_by_text("Learn Playwright", exact=True)
```

## Locator strictness

Playwright generally expects an action locator to resolve to one element.

If a locator matches several elements, Playwright fails instead of silently interacting with an arbitrary element. A collection should therefore be filtered before performing an action on one specific element.

## Key takeaway

A robust UI test first identifies a meaningful element or collection, narrows the locator when necessary, performs a user action, and validates the resulting behavior with a web-first assertion.

## Playwright Pytest fixtures

The Playwright Pytest plugin provides several fixtures:

- `browser`: the browser process used by the tests;
- `context`: an isolated browser profile;
- `page`: a browser tab belonging to an isolated context.

The `page` and `context` fixtures are created for each test. This prevents cookies, sessions, and local storage from leaking between tests.

## Custom UI fixtures

A custom fixture can depend on Playwright's `page` fixture:

```python
import pytest
from playwright.sync_api import Page


TODO_APP_URL = "https://demo.playwright.dev/todomvc/"


@pytest.fixture
def todo_page(page: Page):
    page.goto(TODO_APP_URL)
    return page
```

A test requests the fixture by using its name as a parameter:

```python
def test_todo_page(todo_page: Page):
    pass
```

Fixtures declared in `conftest.py` must not be imported manually. Pytest discovers and injects them automatically.

## Local fixture scope

A fixture placed in:

```text
tests/ui/conftest.py
```

is available to tests located under `tests/ui/`.

This keeps UI-specific fixtures separate from API and unit-test fixtures.

## Technical setup and business actions

Fixtures should centralize stable technical preparation such as:

- opening the application;
- configuring the browser context;
- preparing an environment.

Business actions should normally remain visible inside the test, such as:

- creating a Todo item;
- completing a task;
- submitting a form.

This keeps the tested behavior easy to understand.

## Browser isolation

Each Playwright test receives an isolated browser context:

```text
Browser
├── Context for test A
│   └── Page
└── Context for test B
    └── Page
```

Data created in one test should not affect another test.

## Reloading a page

Reload the current page with:

```python
page.reload()
```

A reload keeps the same browser context. Cookies and local storage therefore remain available during the same test.

After a reload, rebuild the locators used for the final assertions:

```python
page.reload()

todo_items = page.get_by_test_id("todo-item")
todo_item = todo_items.filter(has_text="Persistent UI task")
todo_checkbox = todo_item.get_by_role("checkbox")

expect(todo_checkbox).to_be_checked()
```

## Hash-based routing

Some single-page applications use a URL fragment:

```text
https://example.com/application/#/
```

The fragment is used by client-side routing. A regular expression can accept the application URL with or without that fragment:

```python
expect(page).to_have_url(
    re.compile(r".*/todomvc/(?:#/)?$")
)
```

## Key takeaway

A custom UI fixture removes duplicated technical preparation while Playwright's isolated browser contexts keep tests independent. Reloading a page preserves state inside the current test but that state must not leak into another test.