import os
from network_as_code import NetworkAsCodeClient
from network_as_code.models.device import DeviceIpv4Addr, Device
import pytest
from dotenv import load_dotenv

load_dotenv()
token = os.environ["NAC_TOKEN"]

@pytest.fixture
def device() -> Device:
    client = NetworkAsCodeClient(token=token, env_mode="dev")
    device = client.devices.get(phone_number="+367199991001", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_getting_a_device_location_sends_out_request(device):
    location = device.location(max_age=10_000)

    assert location.longitude
    assert location.latitude
