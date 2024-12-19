
import pytest

from datetime import datetime, timezone, timedelta
from network_as_code.models.congestion import Congestion
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

def test_can_subscribe_for_congestion_info(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1)
    )

    assert subscription.id

    subscription.delete()


def test_can_subscribe_for_congestion_info(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1)
    )

    assert subscription.id

    subscription.delete()


def test_can_subscribe_for_congestion_info_with_auth_token(client, nef_device: Device):
    subscription = client.insights.subscribe_to_congestion_info(
        nef_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        notification_auth_token="my-auth-token"
    )

    assert subscription.id

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


def test_can_query_congestion_level_from_camara_device(client, nef_device):
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


def test_can_query_congestion_level_from_nef_device(client, nef_device):
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
