from network_as_code.models.device_status import ConnectivitySubscription
from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.errors import error_handler
from your_module_path import AuthenticationException, NotFound, ServiceError, APIError



import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("device@bestcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
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

    assert hasattr(subscription, 'ID'), "Subscription does not have an ID"
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

def test_subscribe_authentication_exception(client, device):
    with pytest.raises(AuthenticationException):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/",  
            notification_auth_token="INVALID_TOKEN",  # Supply an invalid token here to trigger a 403
        )

def test_subscribe_device_not_found(client, device):
    with pytest.raises(DeviceNotFound):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device="INVALID_DEVICE_ID",  # Supply an invalid device ID to trigger a 404
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/", 
            notification_auth_token="c8974e592c2fa383d4a3960714",
        )

def test_subscribe_service_error(client, device):
    with pytest.raises(ServiceError):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY_TRIGGER_500_ERROR",  # Make sure this event type triggers a 500 error from your server
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/", 
            notification_auth_token="c8974e592c2fa383d4a3960714",
        )

def test_subscribe_invalid_parameter(client, device):
    with pytest.raises(InvalidParameter):
        client.connectivity.subscribe(
            event_type="",  # An empty event type might trigger a validation error.
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://192.0.2.0:8080/", 
            notification_auth_token="c8974e592c2fa383d4a3960714",
        )