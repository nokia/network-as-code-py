
from network_as_code import NetworkAsCodeClient

from network_as_code.models.device import DeviceIpv4Addr

def test_getting_a_device(client):
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    assert device.network_access_identifier == "testuser@open5glab.net"

def test_creating_device_with_only_public_address_populates_private_field(client: NetworkAsCodeClient):
    device = client.devices.get("testuser@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2"))

    assert device.ipv4_address.private_address == device.ipv4_address.public_address
