from network_as_code.models.device_status import ConnectivitySubscription
from network_as_code.models.device import Device, DeviceIpv4Addr

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
