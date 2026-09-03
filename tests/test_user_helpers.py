import pytest

from utils.user_helpers import count_users, get_active_users, find_user, is_valid_user, get_eligible_users
    

def test_count_users(users):
    count = count_users(users)
    assert count == 4

@pytest.mark.regression
def test_get_active_users(users):
    active_users = get_active_users(users)
    assert len(active_users) == 3

    usernames = [user["username"] for user in active_users]
    assert "locked_user" not in usernames

    assert all(not user["locked"] for user in active_users), "A locked user should never be returned as active"

@pytest.mark.regression
def test_find_existing_user(users):
    user = find_user(users, "admin_user")
    assert user is not None
    assert user["username"] == "admin_user"

@pytest.mark.regression
def test_find_unknown_user(users):
    user = find_user(users, "unknown_user")
    assert user is None

@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("standard_user", "secret_sauce", True),
        ("", "secret_sauce", False),
        ("standard_user", "", False)
    ],
)
def test_is_valid_user(username, password, expected):
    user = {
        "username": username, 
        "password": password
    }

    result = is_valid_user(user)
    assert result is expected

@pytest.mark.smoke
def test_get_eligible_users(users):
    eligible_users = get_eligible_users(users)
    assert len(eligible_users) == 2

    usernames = [user["username"] for user in eligible_users]
    assert "standard_user" in usernames
    assert "problem_user" in usernames

    assert all(user["role"] == "customer" for user in eligible_users), "Only customers should be eligible"
    assert all(is_valid_user(user) for user in eligible_users), "Eligible users must have valid credentials"


@pytest.mark.regression
def test_get_eligible_users_returns_empty_list_when_no_user_is_eligible():
    users = [
        {
            "username": "customer_user", 
            "password": "secret_sauce",
            "role": "customer",
            "locked": True
        },
        {
            "username": "admin_user", 
            "password": "secret_sauce",
            "role": "admin",
            "locked": False
        }
    ]

    eligible_users = get_eligible_users(users)
    assert eligible_users == []

@pytest.mark.regression
def test_find_user_returns_none_for_empty_user_list():
    users = []

    find_users = find_user(users, "test")
    assert find_users is None