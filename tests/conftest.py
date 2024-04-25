
import os
import json

import pytest

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    token = "TEST_TOKEN"
    return NetworkAsCodeClient(token=token)

def to_bytes(json_content: dict) -> bytes:
    return json.dumps(json_content).encode()
