import pytest
from network_as_code.errors import AuthenticationException, ServiceError
from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest

from datetime import datetime

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("test_device_id", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device


def test_get_location(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/location-retrieval/v0/retrieve"

    mock_response = {
        "lastLocationTime": "2023-09-12T11:41:28+03:00",
        "area": {
            "areaType": "CIRCLE",
            "center": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "radius": 10000
        }
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "maxAge": 3600
        }
    )

    location = device.location(max_age=3600)
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert location.radius == 10000

def test_get_location_without_max_age(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/location-retrieval/v0/retrieve"

    mock_response = {
        "lastLocationTime": "2023-09-12T11:41:28+03:00",
        "area": {
            "areaType": "CIRCLE",
            "center": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "radius": 10000
        }
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "maxAge": 60
        }
    )

    location = device.location()
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert location.radius == 10000

def test_verify_location(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "area": {
                "areaType": "CIRCLE",
                "center": {
                    "latitude": 47,
                    "longitude": 19
                },
                "radius": 10_000
            },
            "maxAge": 60
        },
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "TRUE"
        }
    )
    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000)
    assert location_verification.result_type == "TRUE"

def test_verify_location_with_max_age(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "area": {
                "areaType": "CIRCLE",
                "center": {
                    "latitude": 47,
                    "longitude": 19
                },
                "radius": 10_000
            },
            "maxAge": 70
        },
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "TRUE"
        }
    )
    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000, max_age=70)
    assert location_verification.result_type == "TRUE"
    assert location_verification.last_location_time == datetime.fromisoformat("2023-09-11T18:34:01+03:00")

def test_verify_partial_location(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "area": {
                "areaType": "CIRCLE",
                "center": {
                    "latitude": 47,
                    "longitude": 19
                },
                "radius": 10_000
            },
            "maxAge": 60
        },
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "PARTIAL",
            "matchRate": 74
        }
    )

    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000)
    assert location_verification.result_type == "PARTIAL"
    assert location_verification.match_rate == 74

def test_verify_location_raises_exception_if_unauthenticated(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "area": {
                "areaType": "CIRCLE",
                "center": {
                    "latitude": 47,
                    "longitude": 19
                },
                "radius": 10_000
            },
            "maxAge": 60
        },
        status_code=403,
        json={
            "message": "You are not authorized!"
        }
    )

    with pytest.raises(AuthenticationException):
        device.verify_location(longitude=19, latitude=47, radius=10_000)

def test_verify_location_raises_exception_if_server_fails(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_json={
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "area": {
                "areaType": "CIRCLE",
                "center": {
                    "latitude": 47,
                    "longitude": 19
                },
                "radius": 10_000
            },
            "maxAge": 60
        },
        status_code=500,
        json={
            "message": "Internal server error"
        }
    )

    with pytest.raises(ServiceError):
        device.verify_location(longitude=19, latitude=47, radius=10_000)
