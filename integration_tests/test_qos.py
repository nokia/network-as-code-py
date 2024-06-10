
import pytest

from network_as_code.models.session import PortsSpec, PortRange
from network_as_code.models.device import Device, DeviceIpv4Addr
import random

@pytest.fixture()
def device(client) -> Device:
    device = client.devices.get(f"test-device{random.randint(1, 1000)}@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def setup_and_cleanup_session_data(device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")

    yield session

    session.delete()

def test_getting_a_device(client, device):
    assert device.ipv4_address.public_address == "1.1.1.2"

def test_creating_a_qos_flow(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")

    session.delete()

def test_creating_a_qos_flow_medium_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_M")

    session.delete()

def test_creating_a_qos_flow_small_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_S")

    session.delete()

def test_creating_a_qos_flow_low_latency_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_E")

    session.delete()

def test_getting_a_created_qos_session_by_id(client, device, setup_and_cleanup_session_data):
    session = setup_and_cleanup_session_data
    assert client.sessions.get(session.id).id == session.id

    try:
        client.sessions.get(session.id)
        assert False # Should fail
    except:
        assert True

def test_creating_a_qos_flow_with_port_info(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L")

    session.delete()

def test_creating_a_qos_flow_with_service_port_and_device_port(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]))

    session.delete()

def test_port_range_field_aliasing():
    port_range = PortRange(start=80, end=499)
    
    assert "from" in port_range.model_dump(by_alias=True).keys()
    assert "to" in port_range.model_dump(by_alias=True).keys()

def test_creating_a_qos_flow_with_service_port_range(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ranges=[PortRange(start=80, end=443)]), profile="QOS_L")

    session.delete()

def test_creating_a_qos_flow_with_duration(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=60)

    assert session.started_at
    assert session.expires_at

    assert session.duration().seconds == 60

def test_creating_a_qos_flow_with_notification_url(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", notification_url="https://example.com/notifications", notification_auth_token="c8974e592c2fa383d4a3960714")

    session.delete()

def test_clearing_qos_flows(client, device):
    ids = []

    for i in range(5):
        created_session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")
        ids.append(created_session.id)

    device.clear_sessions()

    for session in device.sessions():
        assert not session.id in ids

def test_creating_session_with_just_public_ipv4(client):
    device = client.devices.get("test-device@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2"))

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")

    session.delete()
