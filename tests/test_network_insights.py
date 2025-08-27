import pytest

from datetime import datetime
from network_as_code.models.congestion import Congestion, CongestionSubscription

from network_as_code.models.device import Device

@pytest.fixture
def nef_device(client) -> Device:
    device = client.devices.get(phone_number="3670123456")
    return device

@pytest.fixture
def camara_device(client) -> Device:
    device = client.devices.get(phone_number="3637123456")
    return device

def test_can_fetch_current_congestion_info_from_device_model(httpx_mock, camara_device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/query",
        method="POST",
        json=[
            {
                "timeIntervalStart": "2024-08-20T21:00:00+00:00",
                "timeIntervalStop": "2024-08-20T21:05:00+00:00",
                "congestionLevel": "medium",
                "confidenceLevel": 50
            }
        ],
        match_json=
        {
            "device": {
                "phoneNumber": "3637123456"
            }
        }
    )

    congestion = camara_device.get_congestion()

    assert isinstance(congestion, list)

    assert congestion[0]
    assert isinstance(congestion[0], Congestion)
    assert congestion[0].level == "medium"

def test_can_request_congestion_time_range(httpx_mock, camara_device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/query",
        method="POST",
        json=[
            {
                "timeIntervalStart": "2024-08-20T21:00:00+00:00",
                "timeIntervalStop": "2024-08-20T21:05:00+00:00",
                "congestionLevel": "medium",
                "confidenceLevel": 50
            }
        ],
        match_json=
        {
            "device": {
                "phoneNumber": "3637123456"
            },
            "start": "2024-04-15T08:17:16.664106+00:00",
            "end": "2024-04-16T08:18:01.773761+00:00"
        }
    )

    congestion= camara_device.get_congestion(
        start=datetime.fromisoformat("2024-04-15T08:17:16.664106+00:00"),
        end=datetime.fromisoformat("2024-04-16T08:18:01.773761+00:00")
    )

    assert congestion[0].level == "medium"

def test_can_subscribe_to_congestion_reports(httpx_mock, client, camara_device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions",
        method="POST",
        json={
            "subscriptionId": "asd",
            "startsAt": None,
            "expiresAt": None
        },
        match_json={
            "device": {
                "phoneNumber": "3637123456"
            },
            "webhook": {
                "notificationUrl": "https://example.com",
                "notificationAuthToken": "my-auth-token"
            },
            "subscriptionExpireTime": "2024-04-16T08:18:01.773761+00:00"
        }
    )

    subscription = client.insights.subscribe_to_congestion_info(
        camara_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.fromisoformat("2024-04-16T08:18:01.773761+00:00"),
        notification_auth_token="my-auth-token"
    )

    assert subscription.id == "asd"

def test_can_delete_subscription(httpx_mock, client, camara_device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions",
        method="POST",
        json={
            "subscriptionId": "asd",
            "startsAt": None,
            "expiresAt": None
        },
        match_json={
            "device": {
                "phoneNumber": "3637123456"
            },
            "webhook": {
                "notificationUrl": "https://example.com"
            },
            "subscriptionExpireTime": "2024-04-16T08:18:01.773761+00:00"
        }
    )

    subscription = client.insights.subscribe_to_congestion_info(
        camara_device,
        notification_url="https://example.com",
        subscription_expire_time=datetime.fromisoformat("2024-04-16T08:18:01.773761+00:00")
    )

    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions/asd",
        method="DELETE"
    )

    subscription.delete()

def test_get_subscription_by_id(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions/asd",
        method="GET",
        json={
            "subscriptionId": "asd",
            "startsAt": None,
            "expiresAt": None
        }
    )

    subscription = client.insights.get_congestion_subscription("asd")

    assert isinstance(subscription, CongestionSubscription)

    assert subscription.id

def test_subscription_stores_start_and_expiry_as_datetime(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions/asd",
        method="GET",
        json={
            "subscriptionId": "asd",
            "startedAt": "2024-04-18T10:50:43.991418+00:00",
            "expiresAt": "2024-04-18T10:50:43.991418+00:00"
        }
    )

    subscription = client.insights.get_congestion_subscription("asd")

    assert isinstance(subscription.starts_at, datetime)
    assert isinstance(subscription.expires_at, datetime)


def test_get_subscriptions(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0/subscriptions",
        method="GET",
        json=[
            {
                "subscriptionId": "asd",
                "startsAt": None,
                "expiresAt": None
            },
            {
                "subscriptionId": "second",
                "startsAt": None,
                "expiresAt": None
            }
        ]
    )

    subscriptions = client.insights.get_congestion_subscriptions()

    assert isinstance(subscriptions, list)

    for subscription in subscriptions:
        assert subscription.id
