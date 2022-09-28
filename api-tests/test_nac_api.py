from network_as_code.models.subscription import Subscription

import pytest
import os
import time
import random

import httpx

import network_as_code as nac

os.environ["TESTMODE"] = "1"
SDK_TOKEN = os.getenv("NAC_TOKEN", "test12345")

BASE_URL = "http://nwac.atg.dynamic.nsn-net.net/nwac/v4"

def create_random_imsi():
    imsi = "69"
    for i in range(13):
        imsi += str(random.randint(1, 9))

    return imsi


def create_random_msisdn():
    imsi = "69"
    for i in range(8):
        imsi += str(random.randint(1, 9))

    return imsi


client = nac.NetworkAsCodeClient(
    token="testing",
    base_url=BASE_URL,
    testmode=True
)


@pytest.fixture
def device():
    subscriber = f"sdk.test{random.randint(0, 99)}@nokia.com"
    imsi = create_random_imsi()
    msisdn = create_random_msisdn()

    yield client.subscriptions.create(subscriber, imsi, msisdn)
    client.subscriptions.delete(subscriber)


def test_creation_of_nac_subscriber(device):
    assert client.connected()


def test_getting_network_profile(device: Subscription):
    network_profile = device.get_bandwidth()
    assert network_profile == "uav_lowpowermode"


def test_setting_network_profile(device: Subscription):
    device.set_bandwidth("uav_streaming")
    network_profile = device.get_bandwidth()
    assert network_profile == "uav_streaming"


def test_setting_custom_network_profile(device: Subscription):
    device.set_custom_bandwidth(5000, 20000)
    time.sleep(2)
    network_profile = device.get_bandwidth()
    assert network_profile == "custom"


def test_getting_device_location(device: Subscription):
    location = device.get_location()
    assert float(location["long"]) == 90.0
    assert float(location["lat"]) == 90.0
    assert float(location["elev"]) == 123.0

@pytest.fixture
def channel():
    chan = client.notifications.create()
    yield chan
    client.notifications.delete(chan.uuid)

def test_can_create_valid_channel(channel):
    assert channel.uuid is not None


def test_can_poll_messages_from_channel(channel):
    http_client = httpx.Client()

    http_client.post(f"{BASE_URL}/notifier/callback-handler/{channel.uuid}", json={"msg": "hello, world"})

    msgs = channel.poll()

    assert len(msgs) == 1

@pytest.mark.asyncio
async def test_can_read_messages_via_websocket(channel):
    http_client = httpx.Client()

    http_client.post(f"{BASE_URL}/notifier/callback-handler/{channel.uuid}", json={"msg": "hello, world"})

    sock = await channel.get_websocket_channel()
    msg = await sock.recv()

    assert msg == '{"msg": "hello, world"}'

    await sock.close()
