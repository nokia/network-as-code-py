from network_as_code.models.subscription import Subscription
import pytest
import os
import time
import random

import network_as_code as nac

os.environ["TESTMODE"] = "1"
SDK_TOKEN = os.environ["NAC_TOKEN"]


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
    token="testing", base_url="http://localhost:5050/nwac/v4", testmode=True
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
