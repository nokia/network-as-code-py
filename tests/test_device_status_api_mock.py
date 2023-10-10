from pytest_httpx import httpx_mock
import pytest
import json

from network_as_code.models.device import Device, DeviceIpv4Addr

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def to_bytes(json_content: dict) -> bytes:
    return json.dumps(json_content).encode()

def test_device_status_creation_minimal_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "eventSubscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "eventType": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe("CONNECTIVITY", 1, "https://localhost:9090/notify", "my_auth_token", device)

def test_device_status_creation_with_optional_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        json={
            "eventSubscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "eventType": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "subscriptionExpireTime": "2023-08-31",
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )
    
    subscription = client.connectivity.subscribe("CONNECTIVITY", 1, "https://localhost:9090/notify", "my_auth_token", device, subscription_expire_time="2023-08-31")

def test_device_status_creation_with_roaming_status(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "eventSubscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "eventType": "ROAMING_STATUS"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe("ROAMING_STATUS", 1, "https://localhost:9090/notify", "my_auth_token", device)

def test_getting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        json={
            "eventSubscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2"
                    },
                },
                "eventType": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")


def test_deleting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        json={
            "eventSubscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2"
                    },
                },
                "eventType": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")

    httpx_mock.add_response(
        method="DELETE",
    )

    subscription.delete()
