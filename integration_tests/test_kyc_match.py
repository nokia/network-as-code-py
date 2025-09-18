import pytest
import httpx
import time
from network_as_code.models.device import Device
from network_as_code.errors import APIError, AuthenticationException


def test_get_client_credentials(client):
    credentials = client.authorization.credentials()

    assert credentials.client_id
    assert credentials.client_secret
    assert type(credentials.client_id) is str

def test_get_auth_endpoints(client):
    auth_endpoints = client.authorization.auth_endpoints()

    assert auth_endpoints.authorization_endpoint
    assert auth_endpoints.token_endpoint
    assert type(auth_endpoints.authorization_endpoint) is str

def test_authentication_link(client):
    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='dpv:FraudPreventionAndDetection kyc-match:match', login_hint="+3637123456")
    
    response = httpx.get(url= auth_link)
    
    assert response.status_code == 302

def test_kyc_match_with_phone_number(client):
    result = client.kyc_match.match_customer(
            phone_number="+99999991000",
            id_document="66666666q",
            name="TestName",
            family_name="TestFamilyName",
            address="TestAddress",
            postal_code="TestPostalCode",
            email="test@email.com"
            email="test@email.com"
    )
    print(result)

def test_kyc_match_with_token(client, notification_base_url):
    auth_link = client.authorization.create_authentication_link(redirect_uri=f'https://example.com/kyc', scope='dpv:FraudPreventionAndDetection kyc-match:match', login_hint="+99999991000")

    print(auth_link)
    #with httpx.Client(follow_redirects=True) as client:
    #    response = client.get(auth_link)
#
    #time.sleep(2)
    #response = httpx.get(f'{notification_base_url}/kyc-get-code')
#
    #code = response.json().get('code')
#
    #result = client.kyc_match.match_customer(
    #        code=code,
    #        id_document="123456",
    #        given_name="TestGivenName",
    #        name_kana_hankaku="TestNameKanaHankaku",
    #        family_name_at_birth="TestFamilyNameAtBirth",
    #        street_name="TestStreetName",
    #        street_number="TestStreetNumber",
    #        region="TestRegion",
    #        country="TestCountry",
    #        gender="OTHER"
    #)
    #assert result something

def test_APIError(client):
    with pytest.raises(APIError):
        client.kyc_match.match_customer(
                code="wrong-code",
                id_document="TestIdDocument",
                given_name="TestGivenName",
                name_kana_hankaku="TestKanaHankakuName",
                middle_names="TestNames"
        )

def test_AuthenticationExeption(device):
    with pytest.raises(AuthenticationException):
        device.match_customer(
                phone_number="+12345678",
                id_document="TestIdDocument",
                given_name="TestGivenName",
                name_kana_hankaku="TestKanaHankakuName",
                middle_names="TestNames"
        )