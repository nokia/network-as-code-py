from network_as_code.errors import InvalidParameter

import pytest

def test_get_kyc_match(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/kyc-match/v0.3/match"
    
    mock_response = {
            "idDocumentMatch": True,
            "nameMatch": True,
            "givenNameMatch": None,
            "familyNameMatch": None,
            "nameKanaHankakuMatch": True,
            "nameKanaZenkakuMatch": False,
            "middleNamesMatch": True,
            "familyNameAtBirthMatch": False,
            "familyNameAtBirthMatchScore": 90,
            "addressMatch": True,
            "streetNameMatch": True,
            "streetNumberMatch": True,
            "postalCodeMatch": True,
            "regionMatch": True,
            "localityMatch": None,
            "countryMatch": True,
            "houseNumberExtensionMatch": None,
            "birthdateMatch": False,
            "emailMatch": False,
            "emailMatchScore": 87,
            "genderMatch": False
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
    assert result.name_match and result.name_match is True
    assert result.birthdate_match is False
    if not result.email_match:
        assert result.email_match_score

def test_get_kyc_without_all_fields(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-match/kyc-match/v0.3/match"
    
    mock_response = {
            "idDocumentMatch": True,
            "nameMatch": True,
            "familyNameMatch": False,
            "familyNameMatchScore": 87,
            "addressMatch": True,
            "streetNameMatch": True,
            "streetNumberMatch": True,
            "postalCodeMatch": True,
            "regionMatch": True,
            "emailMatch": True,
            "genderMatch": True
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
    assert result.family_name_match is False
    assert result.family_name_match_score == 87

        
