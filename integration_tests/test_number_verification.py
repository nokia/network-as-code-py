import pytest
import httpx
from network_as_code.models.device import Device
from urllib.parse import urlparse, parse_qs

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+3637123456")
    return device

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
    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='number-verification:verify', login_hint="+3637123456")
    
    response = httpx.get(url= auth_link)

    assert response.status_code == 302

def test_number_verification(client, device):
    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='number-verification:verify', login_hint="+3637123456")
    
    response = httpx.get(url= auth_link)

    redirect_url = response.headers["location"]
    response = httpx.get(url= redirect_url)
    
    redirect_url = response.headers["location"]
    response = httpx.get(url= redirect_url)

    parsed_url = urlparse(response.headers.get('location'))
    code = parse_qs(parsed_url.query)['code'][0]

    assert device.verify_number(code= code)

def test_get_device_phone_number(client, device):

    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='number-verification:device-phone-number:read', login_hint="+3637123456")

    response = httpx.get(url= auth_link)

    redirect_url = response.headers["location"]
    response = httpx.get(url= redirect_url)
    
    redirect_url = response.headers["location"]
    response = httpx.get(url= redirect_url)

    parsed_url = urlparse(response.headers.get('location'))
    code = parse_qs(parsed_url.query)['code'][0]

    assert device.get_phone_number(code=code)