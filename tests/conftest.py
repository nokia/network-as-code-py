
import os

import pytest

from dotenv import load_dotenv

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    load_dotenv()
    token = os.environ["NAC_TOKEN"]
    return NetworkAsCodeClient(token=token)
