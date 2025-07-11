from datetime import datetime
import pytest

from network_as_code.models.device import DeviceIpv4Addr, PortsSpec
from network_as_code.errors import AuthenticationException
from network_as_code.models.session import PortRange

def test_creating_a_session_mock(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number = "+9382948473")
    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
            "ipv4Address": {
                "publicAddress": "1.1.1.2",
                "privateAddress": "1.1.1.2",
                "publicPort": 80
            },
            "phoneNumber": "+9382948473"
        },
        "applicationServer": {
            "ipv4Address": "5.6.7.8",
        },
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
            "qosProfile": "QOS_L",
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "phoneNumber": "+9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
            "duration": 3600
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
    assert session.status == mock_response["qosStatus"]
    assert session.device.network_access_identifier == device.network_access_identifier
    assert session.service_ipv4 == "5.6.7.8"
    

    httpx_mock.add_response(
        json={}
    )
    session.delete()

def test_creating_a_minimal_session(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "+9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "device": {
            "ipv4Address": {
                "publicAddress": "1.1.1.2",
                "publicPort": 80
            },
            "phoneNumber": "+9382948473"
        },
        "applicationServer": {
            "ipv4Address": "5.6.7.8",
        },
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
            "qosProfile": "QOS_L",
            "device": {
                "phoneNumber": "+9382948473",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
            "applicationServer": {
                "ipv4Address": "5.6.7.8",
            },
            "duration": 3600
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)
    assert session.device.phone_number == device.phone_number
    assert session.service_ipv4 == "5.6.7.8"

def test_creating_a_session_with_ipv6(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), ipv6_address = "2266:25::12:0:ad12", phone_number = "9382948473")
    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
            "phoneNumber": "9382948473",
            "ipv4Address": {
                "publicAddress": "1.1.1.2",
                "privateAddress": "1.1.1.2",
                "publicPort": 80
            }
        },
        "applicationServer": {
            "ipv4Address": "5.6.7.8",
            "ipv6Address": "2266:25::12:0:ad12"
        },
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", service_ipv6="2266:25::12:0:ad12", profile="QOS_L", duration=3600)
    
    assert type(session.started_at) == datetime
    assert type(session.expires_at) == datetime
    assert type(session.duration) == int
    assert session.status == mock_response["qosStatus"]
    assert session.service_ipv4 == "5.6.7.8"
    assert session.service_ipv6 == "2266:25::12:0:ad12"

    httpx_mock.add_response(
        json={}
    )
    session.delete()

def test_creating_qod_session_with_device_ports(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
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
        "duration": 3600,
        "devicePorts": {
                "ports": [80, 443]
            },
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600,
            "devicePorts": {
                "ports": [80, 443]
            }
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", device_ports=PortsSpec(ports=[80, 443]), duration=3600)
    assert session.device_ports.ports == [80, 443]

def test_creating_qod_session_with_device_port_range(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
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
        "duration": 3600,
        "devicePorts": {
            "ranges": [{"from": 1024, "to": 3000}]
        },
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600,
            "devicePorts": {
                "ranges": [{"from": 1024, "to": 3000}]
            }
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", device_ports=PortsSpec(ranges=[PortRange(start=1024, end=3000)]), duration=3600)
    assert session.device_ports.ranges[0].start == 1024
    assert session.device_ports.ranges[0].end == 3000

def test_creating_qod_session_with_service_ports(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
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
        "duration": 3600,
        "applicationServerPorts": {
                "ports": [80, 443]
        },
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600,
            "applicationServerPorts": {
                "ports": [80, 443]
            }
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", service_ports=PortsSpec(ports=[80, 443]), duration=3600)
    assert session.service_ports.ports == [80, 443]

def test_creating_qod_session_with_service_port_range(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
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
        "duration": 3600,
        "applicationServerPorts": {
            "ranges": [{"from": 1024, "to": 3000}]
        },
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600,
            "applicationServerPorts": {
                "ranges": [{"from": 1024, "to": 3000}]
            }
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", service_ports=PortsSpec(ranges=[PortRange(start=1024, end=3000)]), duration=3600)
    assert session.service_ports.ranges[0].start == 1024
    assert session.service_ports.ranges[0].end == 3000

def test_creating_a_qod_session_with_duration(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
        "qosProfile": "QOS_L",
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", duration=3600)

def test_creating_a_qod_session_with_notification_url_and_auth_token(httpx_mock, client):
    device = client.devices.get(ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), phone_number = "9382948473")

    mock_response = {
        "sessionId": "08305343-7ed2-43b7-8eda-4c5ae9805bd0",
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
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions",
        match_json={
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
            "duration": 3600,
            "webhook" : {
                "notificationUrl": "https://example.com",
                "notificationAuthToken": "Bearer my-auth-token"
            }
        },
        json=mock_response)

    session = device.create_qod_session(service_ipv4="5.6.7.8", profile="QOS_L", notification_url="https://example.com", notification_auth_token="my-auth-token", duration=3600)

def test_getting_one_session(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    mock_response = {
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
            "ipv4Address": {
                "publicAddress": "1.1.1.2",
                "privateAddress": "1.1.1.2",
                "publicPort": 80
            },
        },
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }
    
    httpx_mock.add_response(
        method = 'GET',
        url = "https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions/1234",
        json=mock_response
    )
    session = client.sessions.get("1234")
    assert session.id == mock_response['sessionId']

    

def test_getting_all_sessions(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    mock_response = [{
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
            "ipv4Address": {
                "publicAddress": "1.1.1.2",
                "privateAddress": "1.1.1.2",
                "publicPort": 80
            },
        },
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }]

    httpx_mock.add_response(
        method='POST',
        url='https://network-as-code.p-eu.rapidapi.com/qod/v0/retrieve-sessions',
        match_json={
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
        },
        json=mock_response
    )

    session = device.sessions()

    assert session[0].id == "1234"

def test_clearing_device_sessions(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net")

    mock_response = [{
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }, {
        "sessionId": "12345",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }]

    httpx_mock.add_response(
        method='POST',
        url='https://network-as-code.p-eu.rapidapi.com/qod/v0/retrieve-sessions',
        match_json={
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
            },
        },
        json=mock_response
    )

    sessions = device.sessions()
    assert len(sessions) == 2
    assert len(httpx_mock.get_requests()) == 1

    httpx_mock.add_response(
        method='DELETE',
        url=f"https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions/{mock_response[0]['sessionId']}",
        json=mock_response
    )

    httpx_mock.add_response(
        method='DELETE',
        url=f"https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions/{mock_response[1]['sessionId']}",
        json=mock_response
    )

    mock_response = [{
        "sessionId": "1234",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }, {
        "sessionId": "12345",
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "qosStatus": "BLA",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }]

    httpx_mock.add_response(
        method='POST',
        url='https://network-as-code.p-eu.rapidapi.com/qod/v0/retrieve-sessions',
        match_json={
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
            },
        },
        json=mock_response
    )

    device.clear_sessions()
    requests = httpx_mock.get_requests()
    assert requests[-2].method == 'DELETE'
    assert requests[-1].method == 'DELETE'

# @pytest.mark.skip(reason="We are currently working around an API issue with this, so we have to return empty list instead")    
def test_getting_sessions_for_nonexistent_device(httpx_mock, client):
    device = client.devices.get("nonexistent-user@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))

    httpx_mock.add_response(
        method="POST",
        url='https://network-as-code.p-eu.rapidapi.com/qod/v0/retrieve-sessions',
        status_code=404,
        json={
            "detail": "QoS subscription not found"
        }
    )

    sessions = device.sessions()
    assert len(sessions) == 0
    

def test_getting_sessions_as_unauthenticated_user(httpx_mock, client):
    device = client.devices.get("not-my-device@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))

    httpx_mock.add_response(
        method="POST",
        url='https://network-as-code.p-eu.rapidapi.com/qod/v0/retrieve-sessions',
        status_code=403,
        match_json={
            "device": {
                "networkAccessIdentifier": "not-my-device@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "publicPort": 80
                },
            },
        },
        json={
            "message":"Invalid API key."
        }
    )

    with pytest.raises(AuthenticationException):
        device.sessions()

def test_create_qod_session_requires_ip(httpx_mock, client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="9382948473")
    
    with pytest.raises(ValueError) as excinfo:
        session = device.create_qod_session(profile="QOS_L", duration=3600)

    assert "At least one of IP parameters must be provided" in str(excinfo.value)



def test_extending_a_qod_session_duration(httpx_mock, client):
    session_id = "08305343-7ed2-43b7-8eda-4c5ae9805bd0"

    mock_response_fetch = {
        "sessionId": session_id,
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "duration": 3600,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    mock_response = {
        "sessionId": session_id,
        "qosProfile": "QOS_L",
        "device": {
            "networkAccessIdentifier": "testuser@open5glab.net",
        },
        "duration": 3840,
        "qosStatus": "REQUESTED",
        "startedAt": "2024-06-18T08:48:12.300312Z",
        "expiresAt": "2024-06-18T08:48:12.300312Z"
    }

    httpx_mock.add_response(
        method="POST",
        url = f"https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions/{session_id}/extend",
        match_json={
            "requestedAdditionalDuration": 240
        },
        json=mock_response)
    
    httpx_mock.add_response(
        method = 'GET',
        url = f"https://network-as-code.p-eu.rapidapi.com/qod/v0/sessions/{session_id}",
        json=mock_response_fetch
    )

    session = client.sessions.get(session_id)
    session.extend(additional_duration=240)
    assert session.duration == 3840
