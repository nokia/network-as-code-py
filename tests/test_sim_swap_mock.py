from datetime import datetime
import pytest
from network_as_code.errors import APIError, InvalidParameter
from network_as_code.models.device import Device

import pytest


@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="3637123456")
    return device

def test_get_sim_swap_date(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/retrieve-date"

    mock_response = {
        "latestSimChange": "2024-06-19T10:36:59.976Z",
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "3637123456"
        }
    )

    latest_sim_swap_date = device.get_sim_swap_date()
    
    assert latest_sim_swap_date == datetime.fromisoformat("2024-06-19T10:36:59.976+00:00")

def test_get_sim_swap_date_no_response(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/retrieve-date"

    mock_response = {}

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "3637123456"
        }
    )

    latest_sim_swap_date = device.get_sim_swap_date()
    
    assert latest_sim_swap_date == None

def test_get_sim_swap_date_with_no_phone_number(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.get_sim_swap_date()
    
def test_verify_sim_swap_with_no_phone_number(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.verify_sim_swap()

def test_verify_sim_swap_without_max_age(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "3637123456"
        }
    )

    assert device.verify_sim_swap(max_age=None) == True

def test_verify_sim_swap_with_max_age(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "3637123456",
            "maxAge": 120
        }
    )

    assert device.verify_sim_swap(max_age=120) == True

# This test actually tests the error handler class by taking simswap as use-case
def test_error_trace_info(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/check"
    httpx_mock.add_response(
        url=url,
        match_json={
            "phoneNumber": "3637123456",
            "maxAge": 120
        },
        method="POST",
        status_code=422,
        json= {'detail': [{'msg': 'Input should be less than or equal to 2400'}]}  
    )

    
    with pytest.raises(APIError) as exc_info:
        device.verify_sim_swap(max_age=120)
        
    assert str(exc_info.value) == "Status Code: 422, Response Body: {'detail': [{'msg': 'Input should be less than or equal to 2400'}]}"
        
