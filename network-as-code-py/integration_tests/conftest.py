import os

import pytest
from dotenv import load_dotenv

from network_as_code.client import NetworkAsCodeApi

load_dotenv()


@pytest.fixture(scope="session")
def client() -> NetworkAsCodeApi:
    api_key = os.environ["NAC_TOKEN"]
    return NetworkAsCodeApi(
        api_key=api_key,
        rapidapi_host="network-as-code.nokia.rapidapi.com",
    )
