
import os

from binding_generation.qos_client.qos_client.model.ports_spec import PortsSpecRangesInner
import pytest

import network_as_code as nac
from network_as_code import NetworkAsCodeClient
from network_as_code.models.session import PortsSpec

@pytest.fixture
def client() -> NetworkAsCodeClient:
    token = os.environ["NAC_TOKEN"]
    return NetworkAsCodeClient(token=token)

def test_getting_a_device(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    assert device.sid == "testuser@open5glab.net"

def test_list_of_sessions_should_be_empty_at_start(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    assert len(device.sessions()) == 0

def test_creating_a_qos_flow(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", profile="QOS_L")

    assert len(device.sessions()) == 1

    session.delete()

def test_creating_a_qos_flow_with_port_info(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L")

    assert len(device.sessions()) == 1

    session.delete()

def test_creating_a_qos_flow_with_service_port_and_device_port(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]))

    assert len(device.sessions()) == 1

    session.delete()

# TODO: Port ranges don't seem to generate working models due to the "from" keyword
# def test_creating_a_qos_flow_with_service_port_range(client):
#     device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

#     session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ranges=[PortsSpecRangesInner(_from=80, to=443)]), profile="QOS_L")

#     assert len(device.sessions()) == 1

#     session.delete()

def test_clearing_qos_flows(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    device.create_session(service_ip="5.6.7.8", profile="QOS_L")

    device.clear_sessions()

    assert len(device.sessions()) == 0

