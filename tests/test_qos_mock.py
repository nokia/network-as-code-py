from datetime import datetime, timedelta
import pytest

import os
import json
from network_as_code.models.device import DeviceIpv4Addr, PortsSpec
from network_as_code.errors import NotFound, AuthenticationException
from network_as_code.models.session import PortRange

def test_getting_a_device(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    assert device.network_access_identifier == "testuser@open5glab.net"


def test_creating_a_session_mock(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number = "9382948473")
    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "phoneNumber": "9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")
    assert session.status == mock_response["qosStatus"]
    
    httpx_mock.add_response(
        json={}
    )
    session.delete()

def test_creating_a_minimal_session(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "phoneNumber": "9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L")

def test_creating_a_session_with_ipv6(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), ipv6_address = "2266:25::12:0:ad12", phone_number = "9382948473")
    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "phoneNumber": "9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                },
                "ipv6Address": "2266:25::12:0:ad12",
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
                "ipv6Address": "2266:25::12:0:ad12"
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ipv6="2266:25::12:0:ad12", profile="QOS_L")
    assert type(session.started_at) == datetime
    assert type(session.expires_at) == datetime
    assert type(session.duration()) == timedelta
    assert session.status == mock_response["qosStatus"]
    
    httpx_mock.add_response(
        json={}
    )
    session.delete()

def test_creating_qod_session_with_device_ports(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8"
            },
            "devicePorts": {
                "ports": [80, 443]
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", device_ports=PortsSpec(ports=[80, 443]))

def test_creating_qod_session_with_device_port_range(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8"
            },
            "devicePorts": {
                "ranges": [{"from": 1024, "to": 3000}]
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", device_ports=PortsSpec(ranges=[PortRange(start=1024, end=3000)]))

def test_creating_qod_session_with_service_ports(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8"
            },
            "applicationServerPorts": {
                "ports": [80, 443]
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", service_ports=PortsSpec(ports=[80, 443]))

def test_creating_qod_session_with_service_port_range(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8"
            },
            "applicationServerPorts": {
                "ranges": [{"from": 1024, "to": 3000}]
            },
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", service_ports=PortsSpec(ranges=[PortRange(start=1024, end=3000)]))

def test_creating_a_qod_session_with_duration(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "phoneNumber": "9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
            "duration": 3600
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

def test_creating_a_qod_session_with_notification_url_and_auth_token(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "phoneNumber": "9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
            "notificationUrl": "https://example.com",
            "notificationAuthToken": "Bearer my-auth-token"
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", notification_url="https://example.com", notification_auth_token="my-auth-token")

def test_getting_one_session(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    mock_response = {
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }
    
    httpx_mock.add_response(
        method = 'GET',
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions/1234",
        json=mock_response
    )
    session = client.sessions.get("1234")
    assert session.id == mock_response['sessionId']


def test_getting_all_sessions(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    mock_response = [{
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }]

    httpx_mock.add_response(
        method='GET',
        url='https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions?networkAccessIdentifier=testuser@open5glab.net',
        json=mock_response
    )

    session = device.sessions()

    assert session[0].id == "1234"

def test_getting_all_sessions_phone_number(httpx_mock, client):
    device = client.devices.get(phone_number="1234567890", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    mock_response = [{
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }]

    httpx_mock.add_response(
        method='GET',
        url='https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions?phoneNumber=1234567890',
        json=mock_response
    )

    session = device.sessions()

    assert session[0].id == "1234"

@pytest.mark.skip(reason="We are currently working around an API issue with this, so we have to return empty list instead")    
def test_getting_sessions_for_nonexistent_device(httpx_mock, client):
    device = client.devices.get("nonexistent-user@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port="80"))

    httpx_mock.add_response(
        method="GET",
        url='https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions?device-id=nonexistent-user@open5glab.net',
        status_code=404,
        json={
            "detail": "QoS subscription not found"
        }
    )

    with pytest.raises(NotFound):
        device.sessions()

def test_getting_sessions_as_unauthenticated_user(httpx_mock, client):
    device = client.devices.get("not-my-device@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port="80"))

    httpx_mock.add_response(
        method="GET",
        url='https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions?networkAccessIdentifier=not-my-device@open5glab.net',
        status_code=403,
        json={
            "message":"Invalid API key."
        }
    )

    with pytest.raises(AuthenticationException):
        device.sessions()

def test_create_qod_session_requires_ip(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="9382948473")
    
    with pytest.raises(ValueError) as excinfo:
        session = device.create_qod_session(profile="QOS_L")

    assert "At least one of IP parameters must be provided" in str(excinfo.value)
