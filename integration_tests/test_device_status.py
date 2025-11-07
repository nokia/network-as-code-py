from datetime import datetime, timedelta, timezone
from network_as_code.models.device import Device, DeviceIpv4Addr
from network_as_code.models.device_status import EventType, AccessTokenCredential

from network_as_code.errors import NotFound, APIError

import uuid
import pytest
import time
import httpx

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+99999991000", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_creating_reachability_subscription_with_notification(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        device=device, 
        max_num_of_reports=5, 
        sink=f"{notification_base_url}/notify/{notification_id}",
        initial_event=True
    )
    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)
    
    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 


    subscription.delete()

def test_creating_reachability_subscription_with_notification_and_type_string_constant(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType["REACHABILITY_SMS"]],
        device=device, 
        max_num_of_reports=5, 
        sink=f"{notification_base_url}/notify/{notification_id}", 
        initial_event=True
    )
    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)
    
    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 


    subscription.delete()

def test_creating_roaming_subscription(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType.ROAMING_STATUS],
        device=device, 
        max_num_of_reports=5, 
        sink=f"{notification_base_url}/notify/{notification_id}", 
        initial_event=True

    )

    assert subscription.id is not None
    assert subscription.max_num_of_reports == 5, f"Expected max_num_of_reports to be 5 but got {subscription.max_num_of_reports}"

    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_creating_reachability_subscription_with_sink_and_credential(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        device=device, 
        max_num_of_reports=5, 
        sink=f"{notification_base_url}/notify/{notification_id}", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True
    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_creating_roaming_subscription_with_sink_and_credential(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType.ROAMING_CHANGE_COUNTRY],
        device=device, 
        max_num_of_reports=5, 
        sink=f"{notification_base_url}/notify/{notification_id}", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True

    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_creating_reachability_subscription_with_expiration(client, device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_SMS],
        device=device, 
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        sink=f"{notification_base_url}/notify/{notification_id}", 
        initial_event=True

    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/device-status/{notification_id}") 
    assert notification.json() == [{'message': 'Notification deleted'}, 200] 

    subscription.delete()

def test_getting_reachability_subscription(client, device):
    reachability_subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        device=device, 
        max_num_of_reports=5, 
        sink="https://example.com/notify", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True
    )

    response = client.device_status.get_reachability_subscription(reachability_subscription.id)

    assert response.id

    reachability_subscription.delete()

def test_delete_reachability(client, device):
    reachability_subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        device=device, 
        max_num_of_reports=5, 
        sink="https://thisisexample.com/notify", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True
    )

    reachability_subscription.delete()

    try:
        response = client.device_status.get_reachability_subscription(reachability_subscription.id)
        assert False
    except:
        # We expect 404
        assert True

def test_getting_roaming_subscription(client, device):
    roaming_subscription = client.device_status.subscribe(
        event_type=[EventType.ROAMING_STATUS],
        device=device, 
        max_num_of_reports=5, 
        sink="https://thisisexample.com/notify", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True
    )

    response = client.device_status.get_roaming_subscription(roaming_subscription.id)

    assert response.id

    roaming_subscription.delete()

def test_delete_roaming(client, device):
    roaming_subscription = client.device_status.subscribe(
        event_type=[EventType.ROAMING_STATUS],
        device=device, 
        max_num_of_reports=5, 
        sink="https://example.com/notify", 
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
            access_token_type="bearer"
        ),
        initial_event=True
    )

    roaming_subscription.delete()

    try:
        response = client.device_status.get_roaming_subscription(roaming_subscription.id)
        assert False
    except:
        # We expect 404
        assert True
        
@pytest.mark.skip
def test_get_subscriptions(client, device):
    subscriptions = client.device_status.get_subscriptions()

    assert isinstance(subscriptions, list)

def test_get_reachability_status_sms(client):
    device = client.devices.get(phone_number="+99999991000")

    status = device.get_reachability()

    assert status.connectivity == ["SMS"]

def test_get_reachability_status_connected(client):
    device = client.devices.get(phone_number="+99999991001")

    status = device.get_reachability()
    
    assert status.reachable
    assert status.connectivity == ["DATA"]

def test_get_connectivity_status_not_connected(client):
    device = client.devices.get(phone_number="+99999991003")

    status = device.get_reachability()

    assert not status.reachable

def test_get_roaming_status_true(client):
    device = client.devices.get(phone_number="+99999991000")

    status = device.get_roaming()

    assert status.roaming

def test_get_roaming_status_false(client):
    device = client.devices.get(phone_number="+99999991001")

    status = device.get_roaming()

    assert not status.roaming

def test_subscribe_device_not_found(client):
    device = client.devices.get(phone_number="+99999990404")

    with pytest.raises(NotFound):
        client.device_status.subscribe(
            event_type=[EventType.REACHABILITY_SMS],
            device=device,
            max_num_of_reports=5, 
            sink="https://example.com/notify",
        )

def test_subscribe_invalid_parameter(client, device):
    with pytest.raises(APIError):
        client.device_status.subscribe(
            event_type=[""],
            device=device, 
            max_num_of_reports=5, 
            sink="https://example.com/notify",
 
        )
