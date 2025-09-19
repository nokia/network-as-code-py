import pytest
import httpx
import time
from network_as_code.models.device import Device
from network_as_code.errors import APIError, AuthenticationException

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+99999991000")
    return device

def test_kyc_age_with_all_params(device):
    result = device.verify_age(
            age_threshold=18,
            phone_number="+99999991000",
            id_document="66666666q",
            name="Federica Sanchez Arjona",
            given_name="Federica",
            family_name="Sanchez Arjona",
            family_name_at_birth="YYYY",
            middle_names="Sanchez",
            birthdate="1978-08-22",
            email="federicaSanchez.Arjona@example.com",
            include_content_lock=True,
            include_parental_control=True
    )
    assert result.age_check == "true"
    assert result.verified_status is True
    assert result.content_lock is not None
    assert result.parental_control is not None

def test_kyc_age_without_optional_params(device):
    result = device.verify_age(
        age_threshold=20,
        phone_number="+99999991000"
    )
    assert result.age_check == "true"
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

def test_kyc_age_with_devices_phone_number(device):
    result = device.verify_age(
        age_threshold=20
    )
    assert result.age_check == "true"
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

def test_AuthenticationExeption(device):
    with pytest.raises(AuthenticationException):
        device.verify_age(
                age_threshold=18,
                phone_number="+12345678",
        )
    