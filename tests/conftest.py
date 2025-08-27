import pytest

from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    token = "TEST_TOKEN"
    return NetworkAsCodeClient(token=token)
