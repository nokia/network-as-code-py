import pytest
import httpx
import time
from network_as_code.models.device import Device

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
    auth_link = client.authorization.create_authentication_link(redirect_uri='https://example.com/redirect', scope='dpv:FraudPreventionAndDetection number-verification:verify', login_hint="+3637123456")
    
    response = httpx.get(url= auth_link)
    
    assert response.status_code == 302

def test_number_verification(client, device, notification_base_url):
    auth_link = client.authorization.create_authentication_link(redirect_uri=f'{notification_base_url}/nv', scope='dpv:FraudPreventionAndDetection number-verification:verify', login_hint="+3637123456")

    with httpx.Client(follow_redirects=True) as client:
        response = client.get(auth_link)

    time.sleep(2)
    response = httpx.get(f'{notification_base_url}/nv-get-code')

    code = response.json().get('code')

    assert device.verify_number(code= code)

def test_get_device_phone_number(client, device, notification_base_url):

    auth_link = client.authorization.create_authentication_link(redirect_uri=f'{notification_base_url}/nv', scope='number-verification:device-phone-number:read', login_hint="+3637123456")

    with httpx.Client(follow_redirects=True) as client:
        response = client.get(auth_link)

    time.sleep(10)
    response = httpx.get(f'{notification_base_url}/nv-get-code')

    code = response.json().get('code')

    assert device.get_phone_number(code=code)