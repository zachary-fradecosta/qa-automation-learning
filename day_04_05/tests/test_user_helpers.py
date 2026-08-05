from unittest import result

from utils.user_helpers import count_users, get_active_users, find_user, is_valid_user
from utils.json_loader import load_users

def test_count_users():
    users = load_users("data/users.json")
    count = count_users(users)
    assert count == 4


def test_get_active_users():
    users = load_users("data/users.json")
    active_users = get_active_users(users)
    assert len(active_users) == 3

    usernames = [user["username"] for user in active_users]
    assert "locked_user" not in usernames


def test_find_existing_user():
    users = load_users("data/users.json")
    user = find_user(users, "admin_user")
    assert user is not None
    assert user["username"] == "admin_user"


def test_find_unknown_user():
    users = load_users("data/users.json")
    user = find_user(users, "unknown_user")
    assert user is None

#Exercice 4: 
def test_is_valid_user():
    user = {
        "username": "standard_user",
        "password": "secret_sauce"
    }
    result = is_valid_user(user)
    assert result is True

def test_user_without_username():
    user = {
        "username": "",
        "password": "secret_sauce"
    }
    result = is_valid_user(user)
    assert result is False

def test_user_without_password():
    user = {
        "username": "standard_user",
        "password": ""
    }
    result = is_valid_user(user)
    assert result is False