import os
from network_as_code import NetworkAsCodeClient
from network_as_code.models.device import DeviceIpv4Addr, Device
import pytest
from dotenv import load_dotenv

load_dotenv()
token = os.environ["NAC_TOKEN"]

@pytest.fixture
def device() -> Device:
    client = NetworkAsCodeClient(token=token, dev_mode=True)
    device = client.devices.get("device@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_getting_a_device_location_sends_out_request(device):
    location = device.location(max_age=10_000)

    assert location.longitude
    assert location.latitude

def test_verifying_a_device_location_sends_out_request(device):
    assert device.verify_location(longitude=19.07915612501993, latitude=47.48627616952785, radius=10_000)

def test_verifying_a_device_location_too_returns_false(device):
    assert not device.verify_location(longitude=24.07915612501993, latitude=47.48627616952785, radius=10_000)