import json
import httpx
from datetime import datetime
from pytest_httpx import httpx_mock
from network_as_code.errors import InvalidParameter
from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest


@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="3637123456")
    return device

def test_get_sim_swap_date(httpx_mock: httpx_mock, device):
    url = "https://sim-swap.p-eu.rapidapi.com/sim-swap/sim-swap/v0/retrieve-date"

    mock_response = {
        "latestSimChange": "2024-06-19T10:36:59.976Z",
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "phoneNumber": "3637123456"
        }).encode("utf-8")
    )

    latest_sim_swap_date = device.get_sim_swap_date()
    
    assert latest_sim_swap_date == datetime.fromisoformat("2024-06-19T10:36:59.976+00:00")

def test_get_sim_swap_date_no_response(httpx_mock: httpx_mock, device):
    url = "https://sim-swap.p-eu.rapidapi.com/sim-swap/sim-swap/v0/retrieve-date"

    mock_response = {}

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "phoneNumber": "3637123456"
        }).encode("utf-8")
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

def test_verify_sim_swap_without_max_age(httpx_mock: httpx_mock, device):
    url = "https://sim-swap.p-eu.rapidapi.com/sim-swap/sim-swap/v0/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "phoneNumber": "3637123456"
        }).encode("utf-8")
    )

    assert device.verify_sim_swap(max_age=None) == True

def test_verify_sim_swap_with_max_age(httpx_mock: httpx_mock, device):
    url = "https://sim-swap.p-eu.rapidapi.com/sim-swap/sim-swap/v0/check"

    mock_response = {
        "swapped": True,
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_content=json.dumps({
            "phoneNumber": "3637123456",
            "maxAge": 120
        }).encode("utf-8")
    )

    assert device.verify_sim_swap(max_age=120) == True

