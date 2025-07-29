
import os

import pytest

from dotenv import load_dotenv

import network_as_code as nac
from network_as_code import NetworkAsCodeClient

@pytest.fixture(scope="module")
def client() -> NetworkAsCodeClient:
    load_dotenv()
    nac_env = os.environ.get("NAC_ENV")

    token = os.environ["NAC_TOKEN"]

    if nac_env == "staging":
        token = os.environ["NAC_TOKEN_STAGE"]
    elif nac_env == "prod":
        token = os.environ["NAC_TOKEN_PROD"]

    print(nac_env, token)

    return NetworkAsCodeClient(token=token, env_mode=nac_env if nac_env else "dev")

@pytest.fixture(scope="module")
def notification_base_url() -> str:
    notification_url = f"{os.environ['SDK_NOTIFICATION_SERVER_URL']}python"
    return notification_url
