from datetime import datetime, timedelta, timezone
from network_as_code.errors import error_handler
from network_as_code.errors import APIError
from network_as_code.models.device import Device, DeviceIpv4Addr
from network_as_code.models.geofencing import PlainCredential, AccessTokenCredential

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+3637123456")
    return device


def test_creating_geofencing_subscription_area_entered_type(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        subscription_max_events=1,
        initial_event=False
    )

    subscription.delete()

def test_creating_geofencing_subscription_area_left_type(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001
    )
    
    subscription.delete()

def test_creating_geofencing_subscription_sink_credential_plain(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential=PlainCredential(identifier="client-id",secret="client-secret"),
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        subscription_max_events=1,
        initial_event=False
    )

    subscription.delete()

def test_creating_geofencing_subscription_sink_credential_bearer(client, device):
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential=AccessTokenCredential(access_token= "some-access-token",access_token_expires_utc= "2025-07-01T14:15:16.789Z",access_token_type="bearer"),
        subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
        subscription_max_events=1,
        initial_event=False
    )

    subscription.delete()

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

    for subscription in subscriptions:
        subscription.delete()

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
