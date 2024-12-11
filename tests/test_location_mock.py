import httpx
from pytest_httpx import httpx_mock
from network_as_code.errors import AuthenticationException, ServiceError
from network_as_code.models.location import CivicAddress, Location
from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest
import json

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("test_device_id", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device


def test_get_location(httpx_mock: httpx_mock, device):
    url = "https://location-retrieval.p-eu.rapidapi.com/retrieve"

    mock_response = {
        "lastLocationTime": "2023-09-12T11:41:28+03:00",
        "area": {
            "areaType": "CIRCLE",
            "center": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "radius": 10000
        },
        "civicAddress": {
            "country": "Finland",
            "A1": "",
            "A2": "",
            "A3": "",
            "A4": "",
            "A5": "",
            "A6": ""
        }
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "maxAge": 60
        }).encode("utf-8")
    )

    location = device.location()
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert location.civic_address
    assert location.radius == 10000

def test_get_location_without_maxage(httpx_mock: httpx_mock, device):
    url = "https://location-retrieval.p-eu.rapidapi.com/retrieve"

    mock_response = {
        "lastLocationTime": "2023-09-12T11:41:28+03:00",
        "area": {
            "areaType": "CIRCLE",
            "center": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "radius": 10000
        },
        "civicAddress": {
            "country": "Finland",
            "A1": "",
            "A2": "",
            "A3": "",
            "A4": "",
            "A5": "",
            "A6": ""
        }
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "maxAge": 60
        }).encode("utf-8")
    )

    location = device.location()
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert location.civic_address
    assert location.radius == 10000

def test_get_location_without_civic_address(httpx_mock: httpx_mock, device):
    url = "https://location-retrieval.p-eu.rapidapi.com/retrieve"

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
        match_content=json.dumps({
            "device": {
                "networkAccessIdentifier": "test_device_id",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            },
            "maxAge": 60
        }).encode("utf-8")
    )

    location = device.location()
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert not location.civic_address
    assert location.radius == 10000

def test_verify_location(httpx_mock: httpx_mock, device):
    url = f"https://location-verification.p-eu.rapidapi.com/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_content=json.dumps({
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
        }).encode(),
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "TRUE"
        }
    )
    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000)
    assert location_verification.result_type == "TRUE"

def test_verify_location_with_max_age(httpx_mock: httpx_mock, device):
    url = f"https://location-verification.p-eu.rapidapi.com/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_content=json.dumps({
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
        }).encode(),
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "TRUE"
        }
    )
    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000, max_age=70)
    assert location_verification.result_type == "TRUE"
    assert location_verification.lastLocationTime == "2023-09-11T18:34:01+03:00"

def test_verify_partial_location(httpx_mock: httpx_mock, device):
    url = f"https://location-verification.p-eu.rapidapi.com/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_content=json.dumps({
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
        }).encode(),
        json={
            "lastLocationTime": "2023-09-11T18:34:01+03:00",
            "verificationResult": "PARTIAL"
            "matchRate": 74
        }
    )

    location_verification = device.verify_location(longitude=19, latitude=47, radius=10_000)
    assert location_verification.result_type == "PARTIAL"
    assert location_verification.matchRate == 74

def test_verify_location_raises_exception_if_unauthenticated(httpx_mock: httpx_mock, device):
    url = f"https://location-verification.p-eu.rapidapi.com/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_content=json.dumps({
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
        }).encode(),
        status_code=403,
        json={
            "message": "You are not authorized!"
        }
    )

    with pytest.raises(AuthenticationException):
        device.verify_location(longitude=19, latitude=47, radius=10_000)

def test_verify_location_raises_exception_if_server_fails(httpx_mock: httpx_mock, device):
    url = f"https://location-verification.p-eu.rapidapi.com/verify"

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        match_content=json.dumps({
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
        }).encode(),
        status_code=500,
        json={
            "message": "Internal server error"
        }
    )

    with pytest.raises(ServiceError):
        device.verify_location(longitude=19, latitude=47, radius=10_000)
