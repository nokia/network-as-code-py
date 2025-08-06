import pytest
from network_as_code.errors import APIError, InvalidParameter
from network_as_code.models.device import Device

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+367199991000")
    return device

def test_verify_unconditional_call_forwarding(httpx_mock, device):
    url="https://call-forwarding-signal.p-eu.rapidapi.com/unconditional-call-forwardings"

    mock_response = {
        "active": True
    }

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+367199991000"
        }
    )
    assert device.verify_unconditional_forwarding() == True

def test_get_call_forwarding(httpx_mock, device):
    url="https://call-forwarding-signal.p-eu.rapidapi.com/call-forwardings"

    mock_response = [
    "unconditional",
    "conditional_no_answer"
    ]

    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+367199991000"
        }
    )
    result = device.get_call_forwarding()
    types = ['inactive', 'unconditional', 'conditional_busy', 'conditional_not_reachable', 'conditional_no_answer']

    assert isinstance(result, list)
    assert all([r in types for r in result])

def test_verify_unconditional_forwarding_without_phone_number(client):
    device = client.devices.get(network_access_identifier="test@device.net")

    with pytest.raises(InvalidParameter):
        device.verify_unconditional_forwarding()

def test_get_call_forwarding_without_phone_number(client):
    device = client.devices.get(network_access_identifier="test@device.net")

    with pytest.raises(InvalidParameter):
        device.get_call_forwarding()
