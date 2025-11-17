import pytest
from network_as_code.errors import AuthenticationException

def test_kyc_tenure_returns_true(client):
    result = client.kyc.check_tenure(
        phone_number = "+99999991000",
        tenure_date = "2023-07-03"
    )
    assert result.tenure_date_check == True
    assert isinstance(result.contract_type, str)

def test_kyc_tenure_returns_false(client):
    result = client.kyc.check_tenure(
        phone_number = "+99999991005",
        tenure_date = "2023-07-13"
    )
    assert result.tenure_date_check == False

def test_kyc_tenure_contract_type(client):
    result = client.kyc.check_tenure(
        phone_number = "+99999991000",
        tenure_date = "2023-07-13"
    )
    if result.contract_type:
        assert result.contract_type in ["PAYG", "PAYM", "Business"]

def test_AuthenticationExeption(client):
    with pytest.raises(AuthenticationException):
        client.kyc.check_tenure(
            phone_number = "+123456",
            tenure_date = "2023-07-13"
        )
