
import pytest

import network_as_code as nac

def test_client_connection(httpx_mock):
    httpx_mock.add_response(json={"service": "up"})

    client = nac.NetworkAsCodeClient(token="not_a_real_token")

    assert client.connected() == True
