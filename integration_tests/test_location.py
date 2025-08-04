
from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number = "+367199991001")
    return device

@pytest.fixture
def device_for_false(client) -> Device:
    device = client.devices.get(phone_number = "+367199991000")
    return device

def test_getting_a_device_location_sends_out_request(device):
    location = device.location(max_age=10_000)
    
    assert location.longitude
    assert location.latitude

def test_verifying_a_device_location_sends_out_request(device):
    assert device.verify_location(longitude=19.07915612501993, latitude=47.48627616952785, radius=10_000).result_type == "TRUE"

def test_verifying_a_device_location_too_returns_false(device_for_false):
    assert device_for_false.verify_location(longitude=24.07915612501993, latitude=47.48627616952785, radius=10_000).result_type == "FALSE"
