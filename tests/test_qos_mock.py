import os
import json
from network_as_code.models.device import DeviceIpv4Addr
from network_as_code.errors import NotFound, AuthenticationException

def test_getting_a_device(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    assert device.sid == "testuser@open5glab.net"


def test_creating_a_session_mock(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number = "9382948473")
    mock_response = {
        "id": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": 1691671102,
        "expiresAt": 1691757502
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://qos-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                },
                "networkAccessIdentifier": "testuser@open5glab.net",
                "phoneNumber": "9382948473"
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
                "ipv6Address": "2041:0000:140F::875B:131B"
            },
            "devicePorts": None,
            "applicationServerPorts": None
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_session(service_ipv4="5.6.7.8", service_ipv6="2041:0000:140F::875B:131B", profile="QOS_L")
    assert session.status == mock_response["qosStatus"]
    
    httpx_mock.add_response(
        json={}
    )
    session.delete()


def test_getting_one_session(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    mock_response = {
        "id": "1234",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": 1691671102,
        "expiresAt": 1691757502
    }
    
    httpx_mock.add_response(
        method = 'GET',
        url = "https://qos-on-demand.p-eu.rapidapi.com/sessions/1234",
        json=mock_response
    )
    session = client.sessions.get("1234")
    assert session.id == mock_response['id']


def test_getting_all_sessions(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    mock_response = [{
        "id": "testuser@open5Glab.ne",
        "qosProfile": "QOS_L",
        "qosStatus": "BLA",
        "expiresAt": 1641494400,
        "startedAt": 0,
    }]

    httpx_mock.add_response(
        method='GET',
        url='https://qos-on-demand.p-eu.rapidapi.com/sessions?device-id=testuser@open5glab.net',
        json=mock_response
    )

    session = device.sessions()

    assert session[0].id == "testuser@open5Glab.ne"

def test_getting_sessions_for_nonexistent_device(httpx_mock, client):
    device = client.devices.get("nonexistent-user@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port="80"))

    httpx_mock.add_response(
        method="GET",
        url='https://qos-on-demand.p-eu.rapidapi.com/sessions?device-id=nonexistent-user@open5glab.net',
        status_code=404,
        json={
            "detail": "QoS subscription not found"
        }
    )

    try:
        device.sessions()
        assert False
    except NotFound as e:
        assert True


def test_getting_sessions_as_unauthenticated_user(httpx_mock, client):
    device = client.devices.get("not-my-device@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port="80"))

    httpx_mock.add_response(
        method="GET",
        url='https://qos-on-demand.p-eu.rapidapi.com/sessions?device-id=not-my-device@open5glab.net',
        status_code=403,
        json={
            "message":"Invalid API key."
        }
    )

    try:
        device.sessions()
        assert False
    except AuthenticationException as e:
        assert True
