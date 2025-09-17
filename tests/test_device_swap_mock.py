from datetime import datetime
import pytest
from network_as_code.errors import APIError, InvalidParameter
from network_as_code.models.device import Device

import pytest


@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+3637123456")
    return device

def test_get_device_swap_date(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/retrieve-date"

    mock_response = {
        "latestDeviceChange": "2024-06-19T10:36:59.976Z",
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+3637123456"
        }
    )

    latest_device_swap_date = device.get_device_swap_date()
    
    assert latest_device_swap_date == datetime.fromisoformat("2024-06-19T10:36:59.976+00:00")

def test_get_device_swap_date_no_response(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/retrieve-date"

    mock_response = {}

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+3637123456"
        }
    )

    latest_device_swap_date = device.get_device_swap_date()
    
    assert latest_device_swap_date == None

def test_get_device_swap_date_with_no_phone_number(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.get_device_swap_date()
    
def test_verify_device_swap_with_no_phone_number(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.verify_device_swap()

def test_verify_device_swap_without_max_age(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+3637123456"
        }
    )

    assert device.verify_device_swap() == True

def test_verify_device_swap_with_max_age(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+3637123456",
            "maxAge": 240
        }
    )

    assert device.verify_device_swap(max_age=240) == True

# This test actually tests the error handler class by taking deviceswap as use-case
def test_error_trace_info(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/check"
    httpx_mock.add_response(
        url=url,
        match_json={
            "phoneNumber": "+3637123456",
            "maxAge": 2401
        },
        method="POST",
        status_code=422,
        json= {'detail': [{'msg': 'Input should be less than or equal to 2400'}]}  
    )

    
    with pytest.raises(APIError) as exc_info:
        device.verify_device_swap(max_age=2401)
        
    assert str(exc_info.value) == "Status Code: 422, Response Body: {'detail': [{'msg': 'Input should be less than or equal to 2400'}]}"