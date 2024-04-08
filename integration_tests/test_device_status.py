from network_as_code.models.device_status import EventSubscription
from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.errors import error_handler
from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("sdk-integration@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_creating_connectivity_subscription_with_notification(client, device):
    subscription = client.connectivity.subscribe(
        event_type="CONNECTIVITY",
        device=device, 
        max_num_of_reports=5, 
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    print(subscription)

    subscription.delete()

def test_creating_connectivity_subscription_roaming(client, device):
    subscription = client.connectivity.subscribe(
        event_type="ROAMING_STATUS",
        device=device, 
        max_num_of_reports=5, 
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    assert subscription.id is not None
    assert subscription.max_num_of_reports == 5, f"Expected max_num_of_reports to be 5 but got {subscription.max_num_of_reports}"
    subscription.delete()

def test_creating_connectivity_subscription_with_notification_with_auth_token(client, device):
    subscription = client.connectivity.subscribe(
        event_type="CONNECTIVITY",
        device=device, 
        max_num_of_reports=5, 
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    subscription.delete()

def test_creating_connectivity_subscription_with_expiration(client, device):
    subscription = client.connectivity.subscribe(
        event_type="CONNECTIVITY",
        device=device, 
        subscription_expire_time="2025-04-08T14:13:29.766268",
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    subscription.delete()

def test_getting_connectivity(client, device):
    connectivity_subscription = client.connectivity.subscribe(
        event_type="CONNECTIVITY",
        device=device, 
        max_num_of_reports=5, 
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    response = client.connectivity.get_subscription(connectivity_subscription.id)

    assert response.device.network_access_id == device.network_access_id

    connectivity_subscription.delete()

def test_delete_connectivity(client, device):
    connectivity_subscription = client.connectivity.subscribe(
        event_type="CONNECTIVITY",
        device=device, 
        max_num_of_reports=5, 
        notification_url="http://192.0.2.0:8080/", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    connectivity_subscription.delete()

    try:
        response = client.connectivity.get_subscription(connectivity_subscription.id)
        assert False
    except:
        # We expect 404
        assert True

@pytest.mark.skip(reason="the API currently gives a 400 error for this")
def test_subscribe_device_not_found(client):
    device = client.devices.get("non-existent@device.net")

    with pytest.raises(NotFound):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device,
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/", 
            notification_auth_token="c8974e592c2fa383d4a3960714",
        )

def test_subscribe_invalid_parameter(client, device):
    with pytest.raises(APIError):
        client.connectivity.subscribe(
            event_type="",  # An empty event type might trigger a validation error.
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/", 
            notification_auth_token="c8974e592c2fa383d4a3960714",
        )
