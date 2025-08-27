from network_as_code.errors import ServiceError, APIError
from network_as_code.models.number_verification import Credentials, Endpoints
from network_as_code.namespaces.authorization import Authorization
import pytest
from unittest.mock import patch

def test_get_credentials(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/oauth2/v1/auth/clientcredentials"

    mock_response = {    
        "client_id": "my-client-id",
        "client_secret": "my-client-secret"
    }

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        json=mock_response,
    )

    credentials = client.authorization.credentials()

    assert credentials.client_id == "my-client-id"
    assert credentials.client_secret == "my-client-secret"

def test_get_credentials_raises_exception_if_server_fails(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/oauth2/v1/auth/clientcredentials"

    mock_response = {
        "message": "Internal server error" 
    }

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        status_code=500,
        json=mock_response
    )

    with pytest.raises(ServiceError):
        client.authorization.credentials()

def test_get_credentials_api_error(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/oauth2/v1/auth/clientcredentials"

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        status_code=400,
    )

    with pytest.raises(APIError):
        client.authorization.credentials()

def test_get_auth_endpoints(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/.well-known/openid-configuration"

    mock_response = {
        "authorization_endpoint": "authorization-endpoint",
        "token_endpoint": "token-endpoint"
    }

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        json=mock_response,
    )

    endpoints = client.authorization.auth_endpoints()

    assert endpoints.authorization_endpoint == "authorization-endpoint"
    assert endpoints.token_endpoint == "token-endpoint"

def test_get_auth_endpoints_raises_exception_if_server_fails(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/.well-known/openid-configuration"

    mock_response = {
        "message": "Internal server error" 
    }

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        status_code=500,
        json=mock_response
    )

    with pytest.raises(ServiceError):
        client.authorization.auth_endpoints()

def test_get_auth_endpoints_api_error(httpx_mock, client):
    url = "https://network-as-code.p-eu.rapidapi.com/.well-known/openid-configuration"

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        status_code=400,
    )

    with pytest.raises(APIError):
        client.authorization.auth_endpoints()


def test_create_authentication_link_with_login_hint(client):
    url = "https://some-auth-server.example.com/oauth2/v1/authorize"
    with patch.object(Authorization, 'credentials', return_value= Credentials(client_id= "my-client-id", client_secret= "my-client-secret")):
        with patch.object(Authorization, 'auth_endpoints', return_value= Endpoints(authorization_endpoint= url, token_endpoint= "token-endpoint")):

            authentication_link = client.authorization.create_authentication_link(
            redirect_uri= "https://example.com/redirect",
            login_hint= "+3637123456",
            scope= "number-verification:verify",
            state= "foobar"
            )

            assert authentication_link == "https://some-auth-server.example.com/oauth2/v1/authorize?scope=number-verification%3Averify&state=foobar&response_type=code&client_id=my-client-id&redirect_uri=https%3A%2F%2Fexample.com%2Fredirect&login_hint=%2B3637123456"

def test_create_authentication_link_without_login_hint(client):
    url = "https://some-auth-server.example.com/oauth2/v1/authorize"
    with patch.object(Authorization, 'credentials', return_value= Credentials(client_id= "my-client-id", client_secret= "my-client-secret")):
        with patch.object(Authorization, 'auth_endpoints', return_value= Endpoints(authorization_endpoint= url, token_endpoint= "token-endpoint")):

            authentication_link = client.authorization.create_authentication_link(
            redirect_uri= "https://example.com/redirect",
            login_hint= None,
            scope= "number-verification:device-phone-number:read",
            state= "foobar"
            )

            assert authentication_link == "https://some-auth-server.example.com/oauth2/v1/authorize?scope=number-verification%3Adevice-phone-number%3Aread&state=foobar&response_type=code&client_id=my-client-id&redirect_uri=https%3A%2F%2Fexample.com%2Fredirect"

def test_create_authentication_link_without_optionals(client):
    url = "https://some-auth-server.example.com/oauth2/v1/authorize"
    with patch.object(Authorization, 'credentials', return_value= Credentials(client_id= "my-client-id", client_secret= "my-client-secret")):
        with patch.object(Authorization, 'auth_endpoints', return_value= Endpoints(authorization_endpoint= url, token_endpoint= "token-endpoint")):

            authentication_link = client.authorization.create_authentication_link(
            redirect_uri= "https://example.com/redirect",
            scope= "number-verification:verify",
            login_hint="+3637123456"
            )

            assert authentication_link == "https://some-auth-server.example.com/oauth2/v1/authorize?scope=number-verification%3Averify&response_type=code&client_id=my-client-id&redirect_uri=https%3A%2F%2Fexample.com%2Fredirect&login_hint=%2B3637123456"
