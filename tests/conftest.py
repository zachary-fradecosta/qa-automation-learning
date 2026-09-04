import pytest
from utils.json_loader import load_users

import truststore
truststore.inject_into_ssl()


@pytest.fixture
def users():
    return load_users("data/users.json")


@pytest.fixture
def user_factory():
    def create_user(username, password, role, locked):
        return {
            "username": username,
            "password": password,
            "role": role,
            "locked": locked
        }       

    return create_user

