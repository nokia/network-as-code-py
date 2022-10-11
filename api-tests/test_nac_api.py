import os
import random
import pytest
from asyncio import sleep
from network_as_code import NetworkAsCodeClient
from network_as_code.models import Subscription, NotificationChannel, CustomBandwidth

os.environ["TESTMODE"] = "1"
SDK_TOKEN = os.getenv("NAC_TOKEN", "test12345")
# BASE_URL = "http://nwac.atg.dynamic.nsn-net.net/nwac/v4"
BASE_URL = "http://nwac.atg.dynamic.nsn-net.net/nwac/v4"


def create_random_imsi():
    imsi = "69"
    for _ in range(13):
        imsi += str(random.randint(1, 9))

    return imsi


def create_random_msisdn():
    imsi = "69"
    for _ in range(8):
        imsi += str(random.randint(1, 9))

    return imsi


@pytest.fixture
async def client():
    client = NetworkAsCodeClient(
        token="testing",
        base_url=BASE_URL,
        testmode=True,
    )
    yield client
    await client.close()


@pytest.fixture
async def device(client: NetworkAsCodeClient):
    subscriber = f"sdk.test{random.randint(0, 99)}@nokia.com"
    imsi = create_random_imsi()
    msisdn = create_random_msisdn()

    subscription = await client.subscriptions.create(subscriber, imsi, msisdn)
    yield subscription
    await subscription.delete()


async def test_client_creation_and_context_manager_and_connection():
    async with NetworkAsCodeClient(
        token="testing", base_url=BASE_URL, testmode=True
    ) as client:
        assert await client.connected()

    assert client._api.is_closed


async def test_getting_subscription(client: NetworkAsCodeClient, device: Subscription):
    subscriber = await client.subscriptions.get(device.id)
    assert subscriber == device


async def test_getting_network_profile(device: Subscription):
    network_profile = await device.get_bandwidth()
    assert network_profile.service_tier == "uav_lowpowermode"


async def test_setting_network_profile(device: Subscription):
    await device.set_bandwidth(name="uav_streaming")
    network_profile = await device.get_bandwidth()
    assert network_profile.service_tier == "uav_streaming"


async def test_setting_custom_network_profile(device: Subscription):
    await device.set_bandwidth(up=5000, down=20000)
    await sleep(2)
    network_profile = await device.get_bandwidth()
    assert isinstance(network_profile, CustomBandwidth)
    assert network_profile.upload == 5000
    assert network_profile.download == 20000
    assert network_profile.service_tier == "custom"


async def test_getting_device_location(device: Subscription):
    location = await device.location()
    assert float(location.longitude) == 90.0
    assert float(location.latitude) == 90.0
    assert float(location.elevation) == 123.0


@pytest.fixture
async def channel(client: NetworkAsCodeClient):
    channel = await client.notifications.new_channel()
    yield channel
    await client.notifications.delete(channel.uuid)


def test_can_create_valid_channel(channel: NotificationChannel):
    assert channel.uuid is not None and channel.uuid != ""


async def test_can_get_channel(
    client: NetworkAsCodeClient, channel: NotificationChannel
):
    _channel = await client.notifications.get_channel(channel.uuid)
    assert _channel == channel


async def test_can_poll_messages_from_channel(
    client: NetworkAsCodeClient, channel: NotificationChannel
):
    await client._api.post(
        f"{BASE_URL}/notifier/callback-handler/{channel.uuid}",
        json={"msg": "hello, world"},
    )
    msgs = await channel.poll()
    assert len(msgs) == 1


async def test_can_read_messages_via_websocket(
    client: NetworkAsCodeClient, channel: NotificationChannel
):
    await client._api.post(
        f"{BASE_URL}/notifier/callback-handler/{channel.uuid}",
        json={"msg": "hello, world"},
    )
    async with channel.websocket as sock:
        msg = await sock.recv()
        assert msg == '{"msg": "hello, world"}'
