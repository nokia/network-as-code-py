import os
import json
from network_as_code.models.device import DeviceIpv4Addr

def test_getting_a_device(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    assert device.sid == "testuser@open5glab.net"


def test_creating_a_session_mock(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    mock_response = {
        "id": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "qosStatus": "REQUESTED",
        "startedAt": 1691671102,
        "expiresAt": 1691757502
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions",
        match_content = json.dumps({
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2"
                }
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8"
            },
            "devicePorts": None,
            "applicationServerPorts": None
        }).encode('utf-8'),
        json=mock_response)

    session = device.create_session(service_ip="5.6.7.8", profile="QOS_L")
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
        url = "https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions/1234",
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
        url='https://quality-of-service-on-demand.p-eu.rapidapi.com/sessions?device-id=testuser@open5glab.net',
        json=mock_response
    )

    session = device.sessions()

    assert session[0].id == "testuser@open5Glab.ne"
