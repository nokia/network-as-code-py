import pytest
from network_as_code.models.device import Device

import pytest

<<<<<<< HEAD
@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+999999991000")
    return device

def test_get_kyc_match(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/kyc-match/v0.3/match"
    
    mock_response = {
            "idDocumentMatch": "true",
            "nameMatch": "true",
            "givenNameMatch": "not_available",
            "familyNameMatch": "not_available",
            "nameKanaHankakuMatch": "true",
            "nameKanaZenkakuMatch": "false",
            "middleNamesMatch": "true",
            "familyNameAtBirthMatch": "false",
            "familyNameAtBirthMatchScore": 90,
            "addressMatch": "true",
            "streetNameMatch": "true",
            "streetNumberMatch": "true",
            "postalCodeMatch": "true",
            "regionMatch": "true",
            "localityMatch": "not_available",
            "countryMatch": "true",
            "houseNumberExtensionMatch": "not_available",
            "birthdateMatch": "false",
            "emailMatch": "false",
            "emailMatchScore": 87,
            "genderMatch": "false"
            }
    
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber":"+999999991000",
            "idDocument":"66666666q",
            "name":"Federica Sanchez Arjona",
            "givenName":"Federica",
            "familyName":"Sanchez Arjona",
            "nameKanaHankaku":"federica",
            "nameKanaZenkaku":"Ｆｅｄｅｒｉｃａ",
            "middleNames":"Sanchez",
            "familyNameAtBirth":"YYYY",
            "address":"Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            "streetName":"Nicolas Salmeron",
            "streetNumber":"4",
            "postalCode":"1028460",
            "region":"Tokyo",
            "locality":"ZZZZ",
            "country":"JP",
            "houseNumberExtension":"VVVV",
            "birthdate":"1978-08-22",
            "email":"abc@example.com",
            "gender":"MALE"
            })
    
    result = client.kyc.match_customer(
            phone_number="+999999991000",
            id_document = "66666666q",
            name = "Federica Sanchez Arjona",
            given_name ="Federica",
            family_name = "Sanchez Arjona",
            name_kana_hankaku = "federica",
            name_kana_zenkaku = "Ｆｅｄｅｒｉｃａ",
            middle_names = "Sanchez",
            family_name_at_birth = "YYYY",
            address = "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            street_name = "Nicolas Salmeron",
            street_number = "4",
            postal_code = "1028460",
            region = "Tokyo",
            locality = "ZZZZ",
            country = "JP",
            house_number_extension = "VVVV",
            birthdate = "1978-08-22",
            email = "abc@example.com",
            gender = "MALE"
            )
    assert result.name_match and result.name_match == "true"
    assert result.birthdate_match == "false"
    if result.email_match == "false":
        assert result.email_match_score

<<<<<<< HEAD
def test_get_kyc_match_without_all_fields(httpx_mock, device):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/kyc-match/v0.3/match"
    
    mock_response = {
            "idDocumentMatch": "true",
            "nameMatch": "true",
            "familyNameMatch": "false",
            "familyNameMatchScore": 87,
            "addressMatch": "true",
            "streetNameMatch": "true",
            "streetNumberMatch": "true",
            "postalCodeMatch": "true",
            "regionMatch": "true",
            "emailMatch": "true",
            "genderMatch": "true"
            }
    
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber":"+999999991000",
            "idDocument":"TestIdDocument",
            "name":"TestName",
            "familyName":"TestFamilyName",
            "address":"TestAddress",
            "streetName":"TestStreetName",
            "streetNumber":"1",
            "postalCode":"11111",
            "region":"TestRegion",
            "email":"abc@example.com",
            "gender":"OTHER"
            })
    
    result = client.kyc.match_customer(
            phone_number="+999999991000",
            id_document="TestIdDocument",
            name="TestName",
            family_name="TestFamilyName",
            address="TestAddress",
            street_name="TestStreetName",
            street_number="1",
            postal_code="11111",
            region="TestRegion",
            email="abc@example.com",
            gender="OTHER"
    )
    assert not result.house_number_extension_match
    assert result.family_name_match == "false"
    assert result.family_name_match_score == 87

<<<<<<< HEAD

def test_kyc_match_without_added_phone_number(httpx_mock, device):

    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/kyc-match/v0.3/match"
    
    mock_response = {
=======
def test_kyc_match_with_auth_token(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/v0.3/match"

    with patch.object(AccessToken, 'create', return_value= AccessToken(api=fake_instance, access_token='my-token', token_type='Bearer', expires_in=12345)):
        mock_response = {
            "idDocumentMatch": "true",
            "nameMatch": "true",
            "familyNameMatch": "false",
            "familyNameMatchScore": 87,
            "addressMatch": "true",
            "streetNameMatch": "true",
            "streetNumberMatch": "true",
            "postalCodeMatch": "true",
            "regionMatch": "true",
            "emailMatch": "true",
            "genderMatch": "true"
            }
    
        httpx_mock.add_response(
                url=url, 
                method='POST', 
                json=mock_response,
                match_json={
                "idDocument":"TestIdDocument",
                "name":"TestName",
                "familyName":"TestFamilyName",
                "address":"TestAddress",
                "streetName":"TestStreetName",
                "streetNumber":"1",
                "postalCode":"11111",
                "region":"TestRegion",
                "email":"abc@example.com",
                "gender":"OTHER"
                })
        
        result = client.kyc.match_customer(
                code="my-code",
                id_document="TestIdDocument",
                name="TestName",
                family_name="TestFamilyName",
                address="TestAddress",
                street_name="TestStreetName",
                street_number="1",
                postal_code="11111",
                region="TestRegion",
                email="abc@example.com",
                gender="OTHER"
        )
        assert result.id_document_match
        assert result.address_match == "true"
        assert not result.name_kana_zenkaku_match

def test_kyc_without_any_authorization(client):
    with pytest.raises(InvalidParameter):
        client.kyc.match_customer(
                id_document="TestIdDocument",
                given_name="TestGivenName",
                name_kana_hankaku="TestKanaHankakuName",
                middle_names="TestNames",
                street_name="TestStreetName",
                street_number="1",
                postal_code="11111",
                region="TestRegion",
                locality="SomeLocality",
                country="SomeCountry"
        )

        
