import pytest
from network_as_code.errors import InvalidParameter
from network_as_code.models.device import Device

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+999999991000")
    return device

def test_kyc_age_with_all_params(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/passthrough/kyc-age-verification/v0.1/verify"
    
    mock_response = {
        "ageCheck": "true",
        "verifiedStatus": True,
        "identityMatchScore": 60,
        "contentLock": False,
        "parentalControl": False
        }
            
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "ageThreshold": 18,
            "phoneNumber": "+99999991000",
            "idDocument": "123456",
            "name": "testName",
            "givenName": "givenName",
            "familyName": "familyName",
            "middleNames": "middleName",
            "familyNameAtBirth": "YYYY",
            "birthdate": "2025-9-18",
            "email": "test@example.com",
            "includeContentLock": True,
            "includeParentalControl": True
            })
                
    result = device.verify_age(
            age_threshold=18,
            phone_number="+99999991000",
            id_document="123456",
            name="testName",
            given_name="givenName",
            family_name="familyName",
            family_name_at_birth="YYYY",
            middle_names="middleName",
            birthdate="2025-9-18",
            email="test@example.com",
            include_content_lock=True,
            include_parental_control=True
            )
    
    assert result.age_check == "true"
    assert result.identity_match_score == 60
    assert result.parental_control is False

def test_get_kyc_age_without_optional_params(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/passthrough/kyc-age-verification/v0.1/verify"
    
    mock_response = {
        "ageCheck": "true",
        "verifiedStatus": True,
        "contentLock": None,
        "parentalControl": None
        }
    
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "ageThreshold":18,
            "phoneNumber":"+99999991000"
            })
    
    result = device.verify_age(
            age_threshold=18,
            phone_number="+99999991000"
        )
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

def test_get_kyc_age_with_devices_phone_number(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/passthrough/kyc-age-verification/v0.1/verify"
    
    mock_response = {
        "ageCheck": "true",
        "verifiedStatus": True,
        "contentLock": None,
        "parentalControl": None
        }
    
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "ageThreshold":18,
            "phoneNumber":"+999999991000"
            })
    
    result = device.verify_age(
            age_threshold=18
        )
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

def test_get_kyc_age_unknown_status(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/passthrough/kyc-age-verification/v0.1/verify"
    
    mock_response = {
        "ageCheck": "not_available",
        "verifiedStatus": 'unknown',
        "contentLock": None,
        "parentalControl": None
        }
    
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "ageThreshold":18,
            "phoneNumber":"+999999991000"
            })
    
    result = device.verify_age(
            age_threshold=18
        )
    assert isinstance(result.verified_status, str)