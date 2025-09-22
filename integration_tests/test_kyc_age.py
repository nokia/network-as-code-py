import pytest
import httpx
import time
from network_as_code.models.device import Device
from network_as_code.errors import APIError, AuthenticationException

@pytest.mark.skip
def test_get_client_credentials(client):
    credentials = client.authorization.credentials()

    assert credentials.client_id
    assert credentials.client_secret
    assert type(credentials.client_id) is str

@pytest.mark.skip
def test_get_auth_endpoints(client):
    auth_endpoints = client.authorization.auth_endpoints()

    assert auth_endpoints.authorization_endpoint
    assert auth_endpoints.token_endpoint
    assert type(auth_endpoints.authorization_endpoint) is str

@pytest.mark.skip
def test_authentication_link(client):
    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='kyc-age:verify', login_hint="+3637123456")
    
    response = httpx.get(url= auth_link)
    
    assert response.status_code == 302

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
    assert result.age_check == "true"
    assert result.verified_status is True
    assert result.content_lock is not None
    assert result.parental_control is not None

def test_kyc_age_without_optional_params(client):
    result = client.kyc.verify_age(
        age_threshold=20,
        phone_number="+99999991000"
    )
    assert result.age_check == "true"
    assert result.verified_status is True
    assert result.content_lock is None
    assert result.parental_control is None

@pytest.mark.skip # Implementation not working yet
def test_kyc_match_with_token(client, notification_base_url):
    auth_link = client.authorization.create_authentication_link(redirect_uri=f'{notification_base_url}/kyc', scope='kyc-age:verify', login_hint="+99999991000")
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(auth_link)

    time.sleep(2)
    response = httpx.get(f'{notification_base_url}/kyc-get-code')

    code = response.json().get('code')

    result = client.kyc.verify_age(
            code=code,
            age_threshold=18
    )
    #assert result something

def test_APIError(client):
    with pytest.raises(APIError):
        client.kyc.verify_age(
                code="wrong-code",
                age_threshold=18,
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

def test_AuthenticationExeption(client):
    with pytest.raises(AuthenticationException):
        client.kyc.verify_age(
                age_threshold=18,
                phone_number="+12345678",
        )
    