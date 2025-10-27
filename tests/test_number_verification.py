import pytest
from unittest.mock import patch
from network_as_code.errors import AuthenticationException, APIError, InvalidParameter
from network_as_code.models.device import Device

import pytest


@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="3637123456")
    return device

def test_verify_number(httpx_mock, device):
    mock_response={
        "devicePhoneNumberVerified": True
    }

    httpx_mock.add_response(
        url= "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0/verify?code=your-code&state=foobar",
        method= 'POST',
        match_json={
            "phoneNumber": "3637123456"
        },
        json=mock_response,
    )

    assert device.verify_number(code='your-code', state='foobar') == True

def test_get_device_phone_number(httpx_mock, device):
    mock_response={
        "devicePhoneNumber": "+123456789"
    }

    httpx_mock.add_response(
        url= "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0/device-phone-number?code=your-code&state=foobar",
        method= 'GET',
        json= mock_response,
    )

    assert device.get_phone_number(code='your-code', state="foobar") == "+123456789"

def test_verify_number_unauthenticated(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0/verify?code=invalid-code&state=your-state"

    mock_response = {
        "message": "Request not authenticated due to missing, invalid, or expired credentials"
    }

    httpx_mock.add_response(
        url=url,
        method="POST",
        match_json={
            "phoneNumber": "3637123456"
        },
        status_code=401,
        json= mock_response 
    )

    with pytest.raises(AuthenticationException):
        device.verify_number(code='invalid-code', state='your-state')

def test_number_verification_api_error(httpx_mock, device):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0/verify?code=your-code&state=your-state"
    httpx_mock.add_response(
        url=url,
        method="POST",
        status_code=400
    )
    
    with pytest.raises(APIError):
        device.verify_number(code='your-code', state='your-state')

def test_verify_number_with_no_phone_number(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.verify_number(code='your-code', state='your-state')
                            

