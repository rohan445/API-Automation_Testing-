import pytest
from api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    yield client
    client.close()