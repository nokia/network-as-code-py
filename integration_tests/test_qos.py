
import pdb
import pytest
import httpx
import time

from network_as_code.models.session import PortsSpec, PortRange
from network_as_code.models.device import Device, DeviceIpv4Addr
import random

@pytest.fixture()
def device(client) -> Device:
    device = client.devices.get(f"test-device{random.randint(1, 1000)}@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def setup_and_cleanup_session_data(device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

    yield session

    session.delete()

def test_getting_a_device(client, device):
    assert device.ipv4_address.public_address == "1.1.1.2"

def test_creating_a_qos_flow(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
    
    assert session.service_ipv4 == "5.6.7.8"
    assert session.duration == 3600
    assert session.device.network_access_identifier == device.network_access_identifier
    session.delete()

def test_creating_a_qos_flow_for_device_with_only_phone_number(client, device):
    device = client.devices.get(phone_number=f"+3670{random.randint(123456, 999999)}", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

    assert session.device.phone_number == device.phone_number
    assert session.duration == 3600
    session.delete()

def test_creating_a_qos_flow_medium_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_M", duration=3600)

    session.delete()

def test_creating_a_qos_flow_small_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_S", duration=3600)

    session.delete()

def test_creating_a_qos_flow_low_latency_profile(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_E", duration=3600)

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
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L", duration=3600)

    assert session.service_ports.ports == [80]
    session.delete()

def test_creating_a_qos_flow_with_service_port_and_device_port(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]), duration=3600)
    
    assert session.service_ports.ports == [80]
    assert session.device_ports.ports == [20000]

    session.delete()

def test_creating_a_qos_flow_with_service_ipv6(client, device):
    session = device.create_qod_session(service_ipv6="2001:db8:1234:5678:9abc:def0:fedc:ba98", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]), duration=3600)
    
    assert session.service_ipv6 == "2001:db8:1234:5678:9abc:def0:fedc:ba98"
    session.delete()

def test_creating_a_qos_flow_with_device_ipv6(client):
    device_ipv6 = client.devices.get(f"test-device{random.randint(1, 1000)}@testcsp.net", ipv6_address = "2001:db8:1234:5678:9abc:def0:fedc:ba98")
    session = device_ipv6.create_qod_session(service_ipv6="2001:db8:1234:5678:9abc:def0:fedc:ba98", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]), duration=3600)
    assert session.service_ipv6 == "2001:db8:1234:5678:9abc:def0:fedc:ba98"
    assert session.device.ipv6_address == device_ipv6.ipv6_address
    session.delete()

def test_port_range_field_aliasing():
    port_range = PortRange(start=80, end=499)
    
    assert "from" in port_range.model_dump(by_alias=True).keys()
    assert "to" in port_range.model_dump(by_alias=True).keys()

def test_creating_a_qos_flow_with_service_port_range(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ports=PortsSpec(ranges=[PortRange(start=80, end=443)]), profile="QOS_L", duration=3600)

    assert session.service_ports.ranges[0].start == 80
    assert session.service_ports.ranges[0].end == 443
    session.delete()

def test_creating_a_qos_flow_with_device_port_range(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", device_ports=PortsSpec(ranges=[PortRange(start=80, end=443)]), profile="QOS_L", duration=3600)

    assert session.device_ports.ranges[0].start == 80
    assert session.device_ports.ranges[0].end == 443
    session.delete()

def test_creating_a_qos_flow_with_duration(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=60)

    assert session.started_at
    assert session.expires_at

    assert session.duration == 60

def test_creating_a_qos_flow_with_notification_url(client, device, notification_base_url):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", notification_url=f"{notification_base_url}/notify", duration=3600)
    assert session.id
    time.sleep(5)
    notification = httpx.get(f"{notification_base_url}/qod/{session.id}")
    assert notification.json()['id'] is not None

    notification_data = notification.json()[0]["data"]

    status_data_keys = ["sessionId", "qosStatus"]
    for key in status_data_keys:
        assert key in notification_data

    session.delete()
    time.sleep(5)

    notification = httpx.delete(f"{notification_base_url}/qod/{session.id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200]

def test_qos_session_info_changes_from_deletion(client, device, notification_base_url):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", notification_url=f"{notification_base_url}/notify", duration=3600)
    assert session.id
    time.sleep(5)

    session.delete()
    time.sleep(5)
    
    notification = httpx.get(f"{notification_base_url}/qod/{session.id}")
    notification_data = notification.json()[1]["data"]

    assert notification_data['statusInfo'] == "DELETE_REQUESTED"

    notification = httpx.delete(f"{notification_base_url}/qod/{session.id}")

def test_getting_all_sessions(client, device):
    device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
    sessions = device.sessions()

    assert len(sessions) >= 0
    device.clear_sessions()

def test_clearing_qos_flows(client, device):
    ids = []

    for i in range(5):
        created_session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
        ids.append(created_session.id)

    device.clear_sessions()

    for session in device.sessions():
        assert not session.id in ids

def test_creating_session_with_public_and_private_ipv4(client):
    device = client.devices.get("test-device@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2"))

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

    assert session.device.ipv4_address.public_address == device.ipv4_address.public_address
    assert session.device.ipv4_address.private_address == device.ipv4_address.private_address
    session.delete()

def test_creating_session_with_public_ipv4_and_public_port(client):
    device = client.devices.get("test-device@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

    assert session.device.ipv4_address.public_address == device.ipv4_address.public_address
    assert session.device.ipv4_address.public_port == device.ipv4_address.public_port
    session.delete()

def test_extending_a_qod_session_duration(client, device):
    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
    assert session.duration == 3600
    session.extend(300)
    assert session.duration == 3900