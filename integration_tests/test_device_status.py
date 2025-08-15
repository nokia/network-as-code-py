from datetime import datetime, timedelta, timezone
from network_as_code.models.device import Device, DeviceIpv4Addr
from network_as_code.models.device_status import EventType

from network_as_code.errors import NotFound, APIError

import pytest
import time
import httpx

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("sdk-integration@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_creating_connectivity_subscription_with_notification(client, device, notification_base_url):
    subscription = client.connectivity.subscribe(
        event_type="org.camaraproject.device-status.v0.connectivity-data",
        device=device, 
        max_num_of_reports=5, 
        notification_url=f"{notification_base_url}/notify", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )
    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)
    
    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{subscription.id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 


    subscription.delete()

def test_creating_connectivity_subscription_with_notification_and_type_string_constant(client, device, notification_base_url):
    subscription = client.connectivity.subscribe(
        event_type=EventType["CONNECTIVITY_DATA"],
        device=device, 
        max_num_of_reports=5, 
        notification_url=f"{notification_base_url}/notify", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )
    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)
    
    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{subscription.id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 


    subscription.delete()

def test_creating_connectivity_subscription_roaming(client, device, notification_base_url):
    subscription = client.connectivity.subscribe(
        event_type=EventType.ROAMING_STATUS,
        device=device, 
        max_num_of_reports=5, 
        notification_url=f"{notification_base_url}/notify", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    assert subscription.id is not None
    assert subscription.max_num_of_reports == 5, f"Expected max_num_of_reports to be 5 but got {subscription.max_num_of_reports}"

    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{subscription.id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_creating_connectivity_subscription_with_notification_with_auth_token(client, device, notification_base_url):
    subscription = client.connectivity.subscribe(
        event_type="org.camaraproject.device-status.v0.connectivity-data",
        device=device, 
        max_num_of_reports=5, 
        notification_url=f"{notification_base_url}/notify", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{subscription.id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_creating_connectivity_subscription_with_expiration(client, device, notification_base_url):
    subscription = client.connectivity.subscribe(
        event_type=EventType.CONNECTIVITY_DATA,
        device=device, 
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        notification_url=f"{notification_base_url}/notify", 
        notification_auth_token="c8974e592c2fa383d4a3960714",
    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{subscription.id}") 
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_getting_connectivity(client, device):
    connectivity_subscription = client.connectivity.subscribe(
        event_type="org.camaraproject.device-status.v0.connectivity-data",
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
        event_type="org.camaraproject.device-status.v0.connectivity-data",
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

def test_get_subscriptions(client, device):
    subscriptions = client.connectivity.get_subscriptions()

    assert isinstance(subscriptions, list)

def test_get_connectivity_status_sms(client):
    device = client.devices.get(phone_number="+99999991000")

    status = device.get_connectivity()

    assert status == "CONNECTED_SMS"

def test_get_connectivity_status_connected(client):
    device = client.devices.get(phone_number="+99999991001")

    status = device.get_connectivity()

    assert status == "CONNECTED_DATA"

def test_get_connectivity_status_not_connected(client):
    device = client.devices.get(phone_number="+99999991002")

    status = device.get_connectivity()

    assert status == "NOT_CONNECTED"

def test_get_roaming_status_true(client):
    device = client.devices.get(phone_number="+99999991000")

    status = device.get_roaming()

    assert status.roaming

def test_get_roaming_status_false(client):
    device = client.devices.get(phone_number="+99999991001")

    status = device.get_roaming()

    assert not status.roaming

@pytest.mark.skip(reason="the API currently gives a 400 error for this")
def test_subscribe_device_not_found(client):
    device = client.devices.get(phone_number="+99999990404")

    with pytest.raises(NotFound):
        client.connectivity.subscribe(
            event_type="org.camaraproject.device-status.v0.connectivity-data",
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
