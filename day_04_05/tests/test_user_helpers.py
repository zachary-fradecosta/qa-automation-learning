import pytest

from utils.user_helpers import count_users, get_active_users, find_user, is_valid_user
    

def test_count_users(users):
    count = count_users(users)
    assert count == 4


def test_get_active_users(users):
    active_users = get_active_users(users)
    assert len(active_users) == 3

    usernames = [user["username"] for user in active_users]
    assert "locked_user" not in usernames


def test_find_existing_user(users):
    user = find_user(users, "admin_user")
    assert user is not None
    assert user["username"] == "admin_user"


def test_find_unknown_user(users):
    user = find_user(users, "unknown_user")
    assert user is None


@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("standard_user", "secret_sauce", True),
        ("", "secret_sauce", False),
        ("standard_user", "", False)
    ],
)
def test_is_valid_user(username, password, expected):
    assert is_valid_user({"username": username, "password": password}) is expected
