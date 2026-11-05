import pytest
from playwright.sync_api import Page, expect
from urllib.parse import urlparse



@pytest.mark.ui
@pytest.mark.smoke
def test_todo_app_displays_main_elements(todo_page: Page):    

    todo_title = todo_page.get_by_role("heading", name="todos")
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    
    expect(todo_title).to_be_visible()
    expect(todo_input).to_be_visible()
    expect(todo_input).to_be_enabled()


@pytest.mark.ui
@pytest.mark.regression
def test_todo_input_accepts_text(todo_page: Page):

    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    test_text = "Learn Playwright"

    todo_input.fill(test_text)
    expect(todo_input).to_have_value(test_text)


@pytest.mark.ui
@pytest.mark.regression
def test_user_can_create_todo(todo_page: Page):

    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    test_text = "Learn Playwright"

    todo_input.fill(test_text)
    todo_input.press("Enter")

    todo_item = todo_page.get_by_text(test_text, exact=True)
    expect(todo_item).to_be_visible()
    expect(todo_input).to_have_value("")


@pytest.mark.ui
@pytest.mark.regression
def test_user_can_create_multiple_todos(todo_page: Page):

    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = ["Learn Playwright", "Write UI Tests"]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    for todo in todos:
        todo_item = todo_page.get_by_text(todo, exact=True)
        expect(todo_item).to_be_visible()

    todo_items = todo_page.get_by_test_id("todo-item")
    expect(todo_items).to_have_count(2)


@pytest.mark.ui
@pytest.mark.regression
def test_user_can_complete_todo(todo_page: Page):

    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    test_text = "Write UI tests"

    todo_input.fill(test_text)
    todo_input.press("Enter")

    todo_items = todo_page.get_by_test_id("todo-item")
    todo_item = todo_items.filter(has_text=test_text)
    expect(todo_item).to_have_text(test_text)    
        
    todo_checkbox = todo_item.get_by_role("checkbox")
    todo_checkbox.check()
    expect(todo_checkbox).to_be_checked()


@pytest.mark.ui
@pytest.mark.regression
def test_todo_page_starts_with_empty_list(base_url, todo_page: Page):
    configured_url = urlparse(base_url)
    current_url = urlparse(todo_page.url)
    
    assert current_url.path == "/todomvc/"
    assert configured_url.scheme == current_url.scheme
    assert configured_url.hostname == current_url.hostname

    todo_items = todo_page.get_by_test_id("todo-item")
    expect(todo_items).to_have_count(0)


@pytest.mark.ui
@pytest.mark.regression
def test_completed_todo_remains_completed_after_reload(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    test_text = "Persistent UI task"

    todo_input.fill(test_text)
    todo_input.press("Enter")

    todo_items = todo_page.get_by_test_id("todo-item")
    todo_item = todo_items.filter(has_text=test_text)
    todo_checkbox = todo_item.get_by_role("checkbox")
    todo_checkbox.check()
    expect(todo_checkbox).to_be_checked()

    todo_page.reload()

    todo_items = todo_page.get_by_test_id("todo-item")
    todo_item = todo_items.filter(has_text=test_text)
    todo_checkbox = todo_item.get_by_role("checkbox")
    expect(todo_checkbox).to_be_checked()  