import pytest
import requests
from configuration import SERVICE_URL_USERS


@pytest.fixture
def get_response():
    res = requests.get(SERVICE_URL_USERS)
    return res
