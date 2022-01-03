from network_as_code import (
    __version__,
    NetworkSlice,
    Device,
    DeviceLocation,
    RequestHandler,
)


def test_version():
    assert __version__ == "0.1.0"


def test_device_init():
    test_imsi = "310170845466094"
    test_sdk_token = "random_api_token"
    test_device = Device(test_imsi, test_sdk_token)
    assert test_device.imsi == test_imsi
    assert test_device.sdk_token == test_sdk_token
