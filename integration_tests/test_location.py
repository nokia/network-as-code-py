
import pdb
from network_as_code.models.location import CivicAddress

from network_as_code.models.device import Device, DeviceIpv4Addr

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("device@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_getting_a_device_location_sends_out_request(client, device):
    location = device.location(max_age=10_000)

    assert location.longitude
    assert location.latitude

def test_verifying_a_device_location_sends_out_request(client, device):
    assert device.verify_location(longitude=19.07915612501993, latitude=47.48627616952785, radius=10_000)

def test_verifying_a_device_location_too_returns_false(client, device):
    assert not device.verify_location(longitude=24.07915612501993, latitude=47.48627616952785, radius=10_000)
