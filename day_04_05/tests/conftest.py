import pytest

from utils.json_loader import load_users


@pytest.fixture
def users():
    return load_users("day_04_05/data/users.json")
