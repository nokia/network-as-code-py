def test_kyc_fill_in(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-fill-in/kyc-fill-in/v0.4/fill-in"

    mock_response = {
          "phoneNumber": "+99999991000",
          "idDocument": "66666666q",
          "idDocumentType": "passport",
          "idDocumentExpiryDate": "2027-07-12",
          "name": "Federica Sanchez Arjona",
          "givenName": "Federica",
          "familyName": "Sanchez Arjona",
          "nameKanaHankaku": "federica",
          "nameKanaZenkaku": "Ｆｅｄｅｒｉｃａ",
          "middleNames": "Sanchez",
          "familyNameAtBirth": "YYYY",
          "address": "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
          "streetName": "Nicolas Salmeron",
          "streetNumber": "4",
          "postalCode": "1028460",
          "region": "Tokyo",
          "locality": "ZZZZ",
          "country": "JP",
          "houseNumberExtension": "36",
          "birthdate": "1978-08-22",
          "email": "abc@example.com",
          "gender": "MALE",
          "cityOfBirth": "Madrid",
          "countryOfBirth": "ES",
          "nationality": "ES"
}
    httpx_mock.add_response(
        url=url,
        method="POST",
        json=mock_response,
        match_json={
            "phoneNumber":"+99999991000"
        }
    )

    result = client.kyc.request_customer_info(
        phone_number = "+99999991000"
    )
    assert result.city_of_birth == "Madrid"
    assert result.id_document_type == "passport"
    assert result.country_of_birth == "ES"
    

def test_kyc_fill_in_returns_none_values(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-fill-in/kyc-fill-in/v0.4/fill-in"

    mock_response = {
          "phoneNumber": None,
          "idDocument": "66666666q",
          "idDocumentType": None,
          "idDocumentExpiryDate": None,
          "name": "Federica Sanchez Arjona",
          "givenName": "Federica",
          "familyName": "Sanchez Arjona",
          "nameKanaHankaku": "federica",
          "nameKanaZenkaku": "Ｆｅｄｅｒｉｃａ",
          "middleNames": "Sanchez",
          "familyNameAtBirth": "YYYY",
          "address": "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
          "streetName": "Nicolas Salmeron",
          "streetNumber": "4",
          "postalCode": "1028460",
          "region": "Tokyo",
          "locality": "ZZZZ",
          "country": "JP",
          "houseNumberExtension": "36",
          "birthdate": "1978-08-22",
          "email": "abc@example.com",
          "gender": "MALE",
          "cityOfBirth": None,
          "countryOfBirth": "ES",
          "nationality": "ES"
    }
    httpx_mock.add_response(
        url=url,
        method="POST",
        json=mock_response,
        match_json={
            "phoneNumber":"+99999991000"
        }
    )

    result = client.kyc.request_customer_info(
        phone_number = "+99999991000"
    )
    assert not result.phone_number
    assert not result.city_of_birth
    assert not result.id_document_type
    assert not result.id_document_expiry_date


def test_kyc_fill_in_returns_strings(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-fill-in/kyc-fill-in/v0.4/fill-in"

    mock_response = {
          "phoneNumber": "+99999991000",
          "idDocument": "66666666q",
          "idDocumentType": None,
          "idDocumentExpiryDate": None,
          "name": "Federica Sanchez Arjona",
          "givenName": "Federica",
          "familyName": "Sanchez Arjona",
          "nameKanaHankaku": "federica",
          "nameKanaZenkaku": "Ｆｅｄｅｒｉｃａ",
          "middleNames": "Sanchez",
          "familyNameAtBirth": "YYYY",
          "address": "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
          "streetName": "Nicolas Salmeron",
          "streetNumber": "4",
          "postalCode": "1028460",
          "region": "Tokyo",
          "locality": "ZZZZ",
          "country": "JP",
          "houseNumberExtension": "36",
          "birthdate": "1978-08-22",
          "email": "abc@example.com",
          "gender": "MALE",
          "cityOfBirth": None,
          "countryOfBirth": "ES",
          "nationality": "ES"
    }
    httpx_mock.add_response(
        url=url,
        method="POST",
        json=mock_response,
        match_json={
            "phoneNumber":"+99999991000"
        }
    )

    result = client.kyc.request_customer_info(
        phone_number = "+99999991000"
    )
    for fill_value in vars(result).values():
        if fill_value:
            assert isinstance(fill_value, str)
