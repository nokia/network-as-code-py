import pytest

import os
import random

import requests

from network_as_code import (
    NetworkProfile,
    Device,
    DeviceLocation,
    GeoZone,
    CustomNetworkProfile,
    Unit,
)

os.environ["TESTMODE"] = "1"

SDK_TOKEN = os.environ['NAC_TOKEN']

def create_random_imsi():
    imsi = "69"

    for i in range(13):
        imsi += str(random.randint(0, 9))

    return imsi


def create_nac_subscriber(subscriber, imsi, msisdn):
  requestUrl = "https://apigee-api-test.nokia-solution.com/nac/v2/subscriber/testuser"
  requestBody = {
    "id": f"{subscriber}",
    "imsi": f"{imsi}",
    "msisdn": f"{msisdn}"
  }
  requestHeaders = {
    "x-testmode": "true",
    "x-apikey": f"{SDK_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  request = requests.put(requestUrl, headers=requestHeaders, json=requestBody)

  print(f"Created test NaC subscriber {subscriber}")

def delete_nac_subscriber(subscriber):
  requestUrl = "https://apigee-api-test.nokia-solution.com/nac/v2/subscriber/testuser"
  requestBody = {
    "id": f"{subscriber}"
  }
  requestHeaders = {
    "x-apikey": f"{SDK_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  request = requests.delete(requestUrl, headers=requestHeaders, json=requestBody)

  print(f"Deleted test NaC subscriber {subscriber}")

@pytest.fixture
def device():
    subscriber = f"sdk.test{random.randint(0, 99)}@nokia.com"
    imsi = create_random_imsi()

    create_nac_subscriber(subscriber, imsi, imsi) # Should IMSI and MISDN be different? Mayhaps

    yield Device(subscriber, SDK_TOKEN)

    delete_nac_subscriber(subscriber)


def test_creation_of_nac_subscriber(device):
    assert device.check_api_connection()

def test_getting_network_profile(device):
    network_profile = device.network_profile()

    assert network_profile.bandwidth_profile == "uav_lowpowermode"

def test_setting_network_profile(device):
    device.apply(NetworkProfile("uav_streaming"))

    network_profile = device.network_profile()

    assert network_profile.bandwidth_profile == "uav_streaming"

def test_setting_custom_network_profile(device):
    device.apply(CustomNetworkProfile(20, 2, Unit.MBIT))

    network_profile = device.network_profile()

    assert network_profile.bandwidth_profile == "custom"

def test_getting_device_location(device):
    location = device.location()

    assert location.longitude == 90.000000000001
    assert location.latitude == 0.000000000001
    assert location.elevation == 456
