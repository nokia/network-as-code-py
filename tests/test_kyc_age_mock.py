import pytest
from network_as_code.errors import InvalidParameter
from network_as_code.models.device import Device
from unittest.mock import patch
from network_as_code.models.number_verification import AccessToken

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
        "identityMatchScore": 60,
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

def test_kyc_age_with_auth_token(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/passthrough/kyc-age-verification/v0.1/verify"

    with patch.object(Device, '_get_single_use_access_token', return_value= AccessToken(access_token='my-token', token_type='Bearer', expires_in=12345)):
        mock_response = {
        "ageCheck": "true",
        "verifiedStatus": True,
        "identityMatchScore": 60,
        "contentLock": True,
        "parentalControl": False
        }
        
        httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "ageThreshold": 18,
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
                code="my-code",
                age_threshold=18,
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

        assert result.verified_status
        assert result.content_lock is True

def test_kyc_match_without_any_authorization(client):
    device = client.devices.get(network_access_identifier="testuser@open5glab.net")

    with pytest.raises(InvalidParameter):
        device.verify_age(
                age_threshold=18,
                id_document="123456",
                name="testName",
                given_name="givenName",
                family_name="familyName",
                middle_names="middleName",
                birthdate="2025-9-18",
                email="test@example.com",
                include_content_lock=True,
                include_parental_control=True
        )