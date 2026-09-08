import pytest
from utils.json_loader import load_users

import truststore
truststore.inject_into_ssl()

import requests


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


@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def valid_post_payload():
    return {
        "title": "My first API post",
        "body": "Created during QA Automation learning",
        "userId": 1,
    }

@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()
