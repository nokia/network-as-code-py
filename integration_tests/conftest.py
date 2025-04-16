
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

@pytest.fixture(score="module")
def notification_base_url() -> str:
    # To be fetched from os.environ
    notification_url = "http://notification-testing-alb-948081273.us-east-1.elb.amazonaws.com:3000/python"
    return notification_url