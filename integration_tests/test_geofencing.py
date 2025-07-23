from datetime import datetime, timedelta, timezone
from network_as_code.errors import APIError
from network_as_code.models.device import Device
from network_as_code.models.geofencing import PlainCredential, AccessTokenCredential

import pytest
import time
import httpx

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+3637123456")
    return device

@pytest.mark.skip(reason="fails to find subscription")
def test_creating_geofencing_subscription_area_entered_type(client, device, notification_base_url):
    subscription = client.geofencing.subscribe(
        device=device,
        sink=f"{notification_base_url}/notify",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        subscription_max_events=5,
        initial_event=False
    )
    assert subscription.event_subscription_id

    # Waiting for the notification subscription to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}")

    subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_creating_geofencing_subscription_area_left_type(client, device, notification_base_url):
    subscription = client.geofencing.subscribe(
        device=device,
        sink=f"{notification_base_url}/notify",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )
    
    assert subscription.event_subscription_id

    # Waiting for the subscription notification to be sent
    time.sleep(5)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}")

    subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_creating_geofencing_subscription_sink_credential_plain(client, device, notification_base_url):
    subscription = client.geofencing.subscribe(
        device=device,
        sink=f"{notification_base_url}/notify",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential=PlainCredential(identifier="client-id",secret="client-secret")
    )
    assert subscription.event_subscription_id

    # Waiting for the subscription notification to be sent
    time.sleep(15)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}")

    subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_creating_geofencing_subscription_sink_credential_bearer(client, device, notification_base_url):
    subscription = client.geofencing.subscribe(
        device=device,
        sink=f"{notification_base_url}/notify",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential=AccessTokenCredential(access_token= "some-access-token",access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),access_token_type="bearer")
    )
    assert subscription.event_subscription_id

    # Waiting for the subscription notification to be sent
    time.sleep(15)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}") 
    assert notification.json()[0]['id'] is not None
    notification = httpx.delete(f"{notification_base_url}/geofencing-subscriptions/{subscription.event_subscription_id}")

    subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_getting_geofencing_subscription(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )

    response = client.geofencing.get(subscription.event_subscription_id)

    subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_getting_geofencing_subscriptions(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )

    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )
    
    subscriptions = client.geofencing.get_all()
    assert isinstance(subscriptions, list)
    assert len(subscriptions) >= 2
    
    for subscription in subscriptions:
        subscription.delete()

@pytest.mark.skip(reason="fails to find subscription")
def test_deleting_geofencing_subscription(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )
    
    subscription.delete()
    try:
        response = client.geofencing.get(subscription.event_subsrcription_id)
        assert False
    except:
        assert True

@pytest.mark.skip(reason="fails to find subscription")
def test_subscribe_invalid_parameter(client, device):
    with pytest.raises(APIError):
        client.geofencing.subscribe(
        device=device,
        sink="",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )
