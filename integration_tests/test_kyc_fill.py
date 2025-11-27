import pytest
from network_as_code.errors import AuthenticationException

@pytest.mark.skip
def test_kyc_fill_in(client):
    result = client.kyc.request_customer_info(
        phone_number = "+99999991000"
    )
    assert result.city_of_birth == "Budapest"
    assert result.country_of_birth == "HU"
    assert result.nationality == "HU"
    assert result.id_document == "66666666q"
    assert result.given_name == "Federica"
@pytest.mark.skip
def test_kyc_fill_in_returns_none_values(client):
    result = client.kyc.request_customer_info(
        phone_number = "+99999991001"
    )
    assert not result.city_of_birth
    assert not result.country_of_birth
    assert not result.nationality
    assert not result.id_document_type
@pytest.mark.skip
def test_kyc_fill_returns_strings(client):
    result = client.kyc.request_customer_info(
        phone_number = "+99999991000"
    )
    for fill_value in vars(result).values():
        if fill_value:
            assert isinstance(fill_value, str)
@pytest.mark.skip
def test_AuthenticationExeption(client):
    with pytest.raises(AuthenticationException):
        client.kyc.request_customer_info(
                phone_number = "+12345678",
        )

