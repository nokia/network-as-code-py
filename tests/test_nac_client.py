
import pytest

import network_as_code as nac
from network_as_code.client import NetworkAsCodeClient

@pytest.fixture
def client() -> NetworkAsCodeClient:
    return NetworkAsCodeClient(token="not_a_real_token", base_url="http://localhost:8000")

def test_getting_a_device(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    assert device.sid == "sami.lahtinen@nokia.com"

def test_creating_a_qos_flow(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    device.create_session(service_ip="8.8.8.8", service_tier="QOS_L")

    assert len(device.sessions()) == 1

def test_clearing_qos_flows(client):
    device = client.devices.get("sami.lahtinen@nokia.com", ip = "127.0.0.1")

    device.create_session(service_ip="8.8.8.8", service_tier="QOS_L")

    device.clear_sessions()

    assert len(device.sessions()) == 0
