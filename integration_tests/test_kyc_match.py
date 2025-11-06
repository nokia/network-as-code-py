import pytest
from network_as_code.errors import AuthenticationException

def test_kyc_match_with_phone_number(client):
    result = client.kyc.match_customer(
            phone_number="+99999991000",
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            family_name_at_birth="MyFamilyName",
            name_kana_hankaku="TestChickenName",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
    )
    assert result.id_document_match is True
    assert result.name_kana_hankaku_match is None
    assert result.name_kana_zenkaku_match is None
    assert result.address_match is False

def test_kyc_match_and_match_score(client):
    result = client.kyc.match_customer(
            phone_number="+99999991000",
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            family_name_at_birth="BirthFamily",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
    )
    assert result.id_document_match is True
    assert result.name_match is False
    if not result.family_name_at_birth_match:
        assert result.family_name_at_birth_match_score >= 0

def test_kyc_match_with_all_params(client):
    result = client.kyc.match_customer(
        phone_number="+99999991000",
        id_document="66666666q",
        name="TestName",
        given_name="TestGiven",
        family_name="TestFamily",
        name_kana_hankaku="TestKana",
        name_kana_zenkaku="TestZenKana",
        middle_names="TestNames",
        family_name_at_birth="TestFamilyNameBirth",
        address="TestAddress",
        street_name="TestStreet",
        street_number="12",
        postal_code="654321",
        region="TestRegion",
        locality="TestLocality",
        country="TestCountry",
        house_number_extension="B",
        birthdate="1212-12-12",
        email="some@email.com",
        gender="OTHER"
    )
    for k, v in vars(result).items():
        if "score" not in k:
            assert v in {True, False, None}

def test_AuthenticationExeption(client):
    with pytest.raises(AuthenticationException):
        client.kyc.match_customer(
                phone_number="+12345678",
                id_document="TestIdDocument",
                given_name="TestGivenName",
                name_kana_hankaku="TestKanaHankakuName",
                middle_names="TestNames"
        )
