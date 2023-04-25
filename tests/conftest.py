
import os

import pytest

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    # token = os.environ["NAC_TOKEN"]
    token = "not_a_real_token"
    return NetworkAsCodeClient(token=token, qos_base_url="http://localhost:8000", location_base_url="http://localhost:8001")
