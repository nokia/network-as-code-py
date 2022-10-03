import os
import time
import httpx
import random
import pytest
from asyncio import sleep
from network_as_code import NetworkAsCodeClient

from network_as_code.models.notification import Notification
from network_as_code.models.subscription import Subscription

os.environ["TESTMODE"] = "1"
SDK_TOKEN = os.getenv("NAC_TOKEN", "test12345")
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

    yield await client.subscriptions.create(subscriber, imsi, msisdn)
    await client.subscriptions.delete(subscriber)


async def test_creation_of_nac_subscriber(client: NetworkAsCodeClient):
    assert await client.connected()


async def test_getting_network_profile(device: Subscription):
    network_profile = await device.get_bandwidth()
    assert network_profile == "uav_lowpowermode"


async def test_setting_network_profile(device: Subscription):
    await device.set_bandwidth("uav_streaming")
    network_profile = await device.get_bandwidth()
    assert network_profile == "uav_streaming"


async def test_setting_custom_network_profile(device: Subscription):
    await device.set_custom_bandwidth(5000, 20000)
    await sleep(2)
    network_profile = await device.get_bandwidth()
    assert network_profile == "custom"


async def test_getting_device_location(device: Subscription):
    location = await device.get_location()
    assert float(location["long"]) == 90.0
    assert float(location["lat"]) == 90.0
    assert float(location["elev"]) == 123.0


@pytest.fixture
async def channel(client: NetworkAsCodeClient):
    channel = await client.notifications.create()
    yield channel
    await client.notifications.delete(channel.uuid)


def test_can_create_valid_channel(channel: Notification):
    assert channel.uuid is not None and channel.uuid != ""


async def test_can_poll_messages_from_channel(
    client: NetworkAsCodeClient, channel: Notification
):
    await client._api.post(
        f"{BASE_URL}/notifier/callback-handler/{channel.uuid}",
        json={"msg": "hello, world"},
    )
    msgs = await channel.poll()
    assert len(msgs) == 1


async def test_can_read_messages_via_websocket(
    client: NetworkAsCodeClient, channel: Notification
):
    await client._api.post(
        f"{BASE_URL}/notifier/callback-handler/{channel.uuid}",
        json={"msg": "hello, world"},
    )
    sock = await channel.get_websocket_channel()
    msg = await sock.recv()
    assert msg == '{"msg": "hello, world"}'
    await sock.close()
