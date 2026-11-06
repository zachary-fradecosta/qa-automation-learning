import re

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.regression
def test_todo_counter_tracks_active_items(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = [
        "First active task",
        "Second active task",
    ]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    todo_items = todo_page.get_by_test_id("todo-item")
    expect(todo_items).to_have_count(2)
    
    todo_count = todo_page.get_by_test_id("todo-count")
    expect(todo_count).to_have_text("2 items left")

@pytest.mark.ui
@pytest.mark.regression
def test_completing_todo_updates_active_counter(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = [
        "Active task",
        "Task to complete",
    ]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    # Identify the active and completed todos
    todo_items = todo_page.get_by_test_id("todo-item")
    active_todo = todo_items.filter(has_text="Active task")
    todo_to_complete = todo_items.filter(has_text="Task to complete")

    # Get the checkboxes for the active and completed todos
    active_checkbox = active_todo.get_by_role("checkbox")
    checkbox_to_complete = todo_to_complete.get_by_role("checkbox")

    # Complete the todo that should be marked as done
    checkbox_to_complete.check()
    expect(active_checkbox).not_to_be_checked()
    expect(checkbox_to_complete).to_be_checked()

    # Verify that the active counter is updated correctly
    todo_count = todo_page.get_by_test_id("todo-count")
    expect(todo_count).to_have_text("1 item left")

@pytest.mark.ui
@pytest.mark.regression
def test_active_filter_displays_only_active_todos(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = [
        "Active task",
        "Completed task",
    ]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    # Complete one of the todos
    todo_items = todo_page.get_by_test_id("todo-item")
    todo_to_complete = todo_items.filter(has_text="Completed task")
    checkbox_to_complete = todo_to_complete.get_by_role("checkbox")
    checkbox_to_complete.check()
    expect(checkbox_to_complete).to_be_checked()

    # Click the "Active" filter
    active_filter = todo_page.get_by_role(
        "link",
        name="Active",
        exact=True,
    )
    active_filter.click()
    expect(todo_page).to_have_url(
        re.compile(r".*#/active$")
    )

    # Verify that only the active todo is displayed
    expect(todo_items).to_have_count(1)
    
    active_todo_after_filter = todo_page.get_by_test_id("todo-item").filter(has_text="Active task")
    completed_todo_after_filter = todo_page.get_by_test_id("todo-item").filter(has_text="Completed task")
    
    expect(active_todo_after_filter).to_be_visible()
    expect(completed_todo_after_filter).to_have_count(0)
    

@pytest.mark.ui
@pytest.mark.regression
def test_completed_filter_displays_only_completed_todos(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = [
        "Active task",
        "Completed task",
    ]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    # Complete one of the todos
    todo_items = todo_page.get_by_test_id("todo-item")
    todo_to_complete = todo_items.filter(has_text="Completed task")
    checkbox_to_complete = todo_to_complete.get_by_role("checkbox")
    checkbox_to_complete.check()
    expect(checkbox_to_complete).to_be_checked()

    # Click the "Completed" filter
    completed_filter = todo_page.get_by_role(
        "link",
        name="Completed",
        exact=True,
    )
    completed_filter.click()

    # Verify that only the completed todo is displayed
    expect(todo_page).to_have_url(
        re.compile(r".*#/completed$")
    )
    expect(todo_items).to_have_count(1)

    completed_todo_after_filter = todo_items.filter(has_text="Completed task")
    completed_checkbox_after_filter = (completed_todo_after_filter.get_by_role("checkbox"))
    active_todo_after_filter = todo_items.filter(has_text="Active task")

    expect(completed_todo_after_filter).to_be_visible()
    expect(completed_checkbox_after_filter).to_be_checked()
    expect(active_todo_after_filter).to_have_count(0)


@pytest.mark.ui
@pytest.mark.regression
def test_clear_completed_removes_only_completed_todos(todo_page: Page):
    todo_input = todo_page.get_by_placeholder("What needs to be done?")
    todos = [
        "Task to keep",
        "Task to remove",
    ]

    for todo in todos:
        todo_input.fill(todo)
        todo_input.press("Enter")

    # Complete one of the todos
    todo_items = todo_page.get_by_test_id("todo-item")
    todo_to_complete = todo_items.filter(has_text="Task to remove")
    checkbox_to_complete = todo_to_complete.get_by_role("checkbox")
    checkbox_to_complete.check()
    expect(checkbox_to_complete).to_be_checked()

    # Click the "Clear completed" button
    clear_completed_button = todo_page.get_by_role(
        "button",
        name="Clear completed",
        exact=True,
    )
    expect(clear_completed_button).to_be_visible()
    clear_completed_button.click()

    # Verify that only the active todo remains
    expect(todo_items).to_have_count(1)
    active_todo_after_clear = todo_items.filter(has_text="Task to keep")
    completed_todo_after_clear = todo_items.filter(has_text="Task to remove")
    expect(active_todo_after_clear).to_be_visible()
    expect(completed_todo_after_clear).to_have_count(0)

    # Verify the todo count reflects the remaining active todo
    todo_count = todo_page.get_by_test_id("todo-count")
    expect(todo_count).to_have_text("1 item left")