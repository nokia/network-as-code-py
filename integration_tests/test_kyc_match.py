import pytest
import httpx
import time
from network_as_code.models.device import Device
from network_as_code.errors import APIError, AuthenticationException

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+99999991000")
    return device

def test_kyc_match_with_phone_number(device):
    result = device.match_customer(
            phone_number="+99999991000",
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
    )
    
    assert result.id_document_match == "true"
    assert result.name_match
    assert result.address_match == "false"

def test_kyc_match_and_match_score(device):
    result = device.match_customer(
            phone_number="+99999991000",
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            family_name_at_birth="BirthFamily",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
    )
    
    assert result.id_document_match
    assert result.name_match
    if result.family_name_at_birth_match == "false":
        assert result.family_name_at_birth_match_score >= 0

def test_kyc_match_with_devices_phone_number(device):
    result = device.match_customer(
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            family_name_at_birth="BirthFamily",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
    )

    assert result.id_document_match
    assert result.name_match

def test_AuthenticationExeption(device):
    with pytest.raises(AuthenticationException):
        device.match_customer(
                phone_number="+12345678",
                id_document="TestIdDocument",
                given_name="TestGivenName",
                name_kana_hankaku="TestKanaHankakuName",
                middle_names="TestNames"
        )