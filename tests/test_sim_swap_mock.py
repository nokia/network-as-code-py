import json
import httpx
from pytest_httpx import httpx_mock
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
    
    assert latest_sim_swap_date == "2024-06-19T10:36:59.976Z"

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

