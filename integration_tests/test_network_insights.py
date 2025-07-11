
import uuid
import pytest
import time
import httpx

from datetime import datetime, timezone, timedelta
from network_as_code.models.device import Device

@pytest.fixture
def nef_device(client) -> Device:
    """Test device for NEF backend"""
    device = client.devices.get(phone_number="+3670123456")
    return device

@pytest.fixture
def camara_device(client) -> Device:
    """This is a device object for the CAMARA backend"""
    device = client.devices.get(phone_number="+3637123456")
    return device

def test_can_subscribe_for_congestion_info_with_nef(client, nef_device: Device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url=f"{notification_base_url}/notify/{notification_id}",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1)
    )

    assert subscription.id

    # Waiting for the subscription notification to be sent
    time.sleep(10)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/congestion-insights/{notification_id}")
    assert notification.json()[0]['id'] is not None
    notification_info = notification.json()[0]["data"]
    assert notification_info[0]['congestionLevel'] in ["None", "Low", "Medium", "High"]
    notification = httpx.delete(f"{notification_base_url}/congestion-insights/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200]

    subscription.delete()

def test_can_subscribe_for_congestion_info_with_camara(client, camara_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        camara_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1)
    )

    assert subscription.id

    subscription.delete()

def test_can_subscribe_for_congestion_info_with_auth_token(client, nef_device: Device, notification_base_url):
    notification_id = str(uuid.uuid4())
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url=f"{notification_base_url}/notify/{notification_id}",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        notification_auth_token="my-auth-token"
    )

    assert subscription.id

    # Waiting for subscription notification to be sent
    time.sleep(10)

    # Fetching and deleting the subscription notification
    notification = httpx.get(f"{notification_base_url}/congestion-insights/{notification_id}")
    assert notification.json()[0]['id'] is not None    
    notification_info = notification.json()[0]["data"]
    assert notification_info[0]['congestionLevel'] in ["None", "Low", "Medium", "High"]
    notification = httpx.delete(f"{notification_base_url}/congestion-insights/{notification_id}")
    assert notification.json() == [{'message': 'Notification deleted'}, 200]

    subscription.delete()

def test_can_get_subscription_by_id(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        notification_auth_token="my-auth-token"
    )

    same_subscription = client.insights.get_congestion_subscription(subscription.id)

    assert same_subscription == subscription

    subscription.delete()

def test_can_get_subscription_start_and_expiration(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1)
    )

    assert subscription.id
    
    assert subscription.starts_at
    assert subscription.expires_at

    assert isinstance(subscription.starts_at, datetime)

    subscription.delete()

def test_can_get_list_of_subscriptions(client, nef_device: Device):
    for _i in range(5):
        client.insights.subscribe_to_congestion_info(
            nef_device,
            notification_url="https://example.com",
            subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
            notification_auth_token="my-auth-token"
        )

    subscriptions = client.insights.get_congestion_subscriptions()

    assert len(subscriptions) >= 5

    for subscription in subscriptions:
        subscription.delete()

def test_can_query_congestion_level_from_camara_device(client, camara_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        camara_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(minutes=5),
        notification_auth_token="my-auth-token"
    )

    congestion = camara_device.get_congestion()

    assert isinstance(congestion, list)

    assert congestion[0].level in ["None", "Low", "Medium", "High"]

    subscription.delete()

def test_can_query_congestion_level_from_nef_device(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(minutes=5),
        notification_auth_token="my-auth-token"
    )

    congestion = nef_device.get_congestion()

    assert isinstance(congestion, list)

    assert congestion[0].level in ["None", "Low", "Medium", "High"]

    subscription.delete()

def test_can_query_within_time_range(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(minutes=5),
        notification_auth_token="my-auth-token"
    )

    congestion = nef_device.get_congestion(start=datetime.now(timezone.utc), end=datetime.now(timezone.utc) + timedelta(hours=3))

    assert congestion[0].level in ["None", "Low", "Medium", "High"]

    # assert congestion[0].confidence

    subscription.delete()
