
import os

from network_as_code.models.session import PortsSpec, PortRange

def test_getting_a_device(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    assert device.sid == "testuser@open5glab.net"

def test_creating_a_qos_flow(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", profile="QOS_L")

    session.delete()

def test_getting_a_created_qos_session_by_id(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", profile="QOS_L")

    assert client.sessions.get(session.id).id == session.id

    session.delete()

    try:
        client.sessions.get(session.id)
        assert False # Should fail
    except:
        assert True

def test_creating_a_qos_flow_with_port_info(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L")

    session.delete()

def test_creating_a_qos_flow_with_service_port_and_device_port(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ports=[80]), profile="QOS_L", device_ports=PortsSpec(ports=[20000]))

    session.delete()

def test_port_range_field_aliasing():
    port_range = PortRange(start=80, end=499)

    assert "from" in port_range.dict(by_alias=True).keys()
    assert "to" in port_range.dict(by_alias=True).keys()

def test_creating_a_qos_flow_with_service_port_range(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", service_ports=PortsSpec(ranges=[PortRange(start=80, end=443)]), profile="QOS_L")

    session.delete()

def test_clearing_qos_flows(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    device.create_session(service_ip="5.6.7.8", profile="QOS_L")

    device.clear_sessions()

    assert len(device.sessions()) == 0
