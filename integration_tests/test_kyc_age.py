import pytest
from network_as_code.errors import AuthenticationException

def test_kyc_age_with_all_params(client):
    result = client.kyc.verify_age(
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
    assert result.age_check is True
    assert result.verified_status is True
    assert result.content_lock is not None
    assert result.parental_control is not None

def test_kyc_age_without_optional_params(client):
    result = client.kyc.verify_age(
        age_threshold=20,
        phone_number="+99999991000"
    )
    assert result.age_check is True
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

def test_AuthenticationExeption(client):
    with pytest.raises(AuthenticationException):
        client.kyc.verify_age(
                age_threshold=18,
                phone_number="+12345678",
        )
    
