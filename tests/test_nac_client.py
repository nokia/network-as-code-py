
import pytest

import network_as_code as nac
from network_as_code.client import NetworkAsCodeClient

@pytest.fixture
def client() -> NetworkAsCodeClient:
    return NetworkAsCodeClient(token="not_a_real_token")

def test_client_connection(httpx_mock, client):
    httpx_mock.add_response(json={"service": "up"})

    assert client.connected() == True

def test_getting_a_device(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    assert device.sid == "sami.lahtinen@nokia.com"

def test_creating_a_qos_flow(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    device.create_qos_flow(service_ip="8.8.8.8", service_tier="QOS_L")

    assert len(device.qos_flows()) == 1

def test_clearing_qos_flows(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    device.create_qos_flow(service_ip="8.8.8.8", service_tier="QOS_L")

    device.clear_qos_flows()

    assert len(device.qos_flows()) == 0
