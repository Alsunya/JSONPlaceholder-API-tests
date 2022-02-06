import pytest
from http_client import HttpClient
from random import choice


@pytest.fixture(scope="session")
def post():
    request = f"/posts"
    response = HttpClient().get(path=request)
    yield choice(response.json())
