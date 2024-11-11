
import os

import pytest

from dotenv import load_dotenv

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    load_dotenv()
    using_prod = "PRODTEST" in os.environ

    token = os.environ["NAC_TOKEN"] if not using_prod else os.environ["NAC_TOKEN_PROD"]
    return NetworkAsCodeClient(token=token, dev_mode=not using_prod)
