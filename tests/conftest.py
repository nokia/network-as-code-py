
import os

import pytest

from dotenv import load_dotenv

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    load_dotenv()
    token = os.environ["NAC_TOKEN"]
    assert token == "ec4dae30fdmsh5e4983f533494e3p14b972jsn6c66126ba2b1"
    return NetworkAsCodeClient(token=token)
