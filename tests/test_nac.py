import time
import random
import pytest
from network_as_code import NetworkSlice, Device, DeviceLocation, RequestHandler

API_PATH = "https://sdk-gateway.ext.dynamic.nsn-net.nokia.com:8000/api"


@pytest.fixture
def device():
    return Device("310170845466094", "random_api_token")


def test_device_init():
    test_imsi = "310170845466094"
    test_sdk_token = "random_api_token"
    test_device = Device(test_imsi, test_sdk_token)
    assert test_device.imsi == test_imsi
    assert test_device.sdk_token == test_sdk_token


def test_get_location(requests_mock, device):
    # Generate random data
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    alt = random.randint(0, 1000)
    ts = time.time()

    # Register a mocked response
    requests_mock.get(
        f"{API_PATH}/{device.imsi}",
        json={
            "imsi": device.imsi,
            "location": {
                "latitude": lat,
                "longitude": lon,
                "altitude": alt,
                "timestamp": ts,
            },
        },
    )

    # Get the device location
    device_location = DeviceLocation(device)

    # Assert that the data is received and stored correctly
    assert device_location.latitude == lat
    assert device_location.longitude == lon
    assert device_location.altitude == alt
    assert device_location.timestamp == ts
