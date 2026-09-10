import pytest
from utils.json_loader import load_users
from utils.api_config import get_api_base_url

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
    return get_api_base_url()


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
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()
