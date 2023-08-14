import httpx
from pytest_httpx import httpx_mock
from network_as_code.api.location_api import LocationAPI
from network_as_code.models.location import CivicAddress, Location
from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("test_device_id", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_get_location(httpx_mock: httpx_mock, device):
    url = "https://device-location.p-eu.rapidapi.com/get?device_id=test_device_id"

    mock_response = {
        "point": {"lon": 0, "lat": 0},
        "civicAddress": {"country": "", "A1": "", "A2": "", "A3": "", "A4": "", "A5": "", "A6": ""}
    }
    httpx_mock.add_response(
        url=url, 
        method='GET', 
        json=mock_response
    )

    location = device.location()
    
    assert location.longitude == 0.0
    assert location.latitude == 0.0
    assert location.civic_address

def test_verify_location(httpx_mock: httpx_mock, device):
   
    params = {
        "longitude":"19",
        "latitude":"47",
        "device_id":"test_device_id",
        "accuracy":"10km"
        }
    url = f"https://device-location.p-eu.rapidapi.com/verify?latitude={params['latitude']}&longitude={params['longitude']}&device_id={params['device_id']}&accuracy={params['accuracy']}"

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        #params=params,  # <-- Added this line to ensure mock matches the request based on query params
        json={"message": "Success"}
    )

    assert device.verify_location(longitude=19, latitude=47, accuracy="10km")
