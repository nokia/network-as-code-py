
from network_as_code.models.device import DeviceIpv4Addr

def test_serializing_device_with_network_id(client):
    device = client.devices.get("test_device_id")

    assert device.model_dump(mode='json', by_alias=True, exclude_none=True) == { "networkAccessIdentifier": "test_device_id" }

def test_serializing_device_with_ipv4_public_address_and_private_address(client):
    device = client.devices.get("test_device_id", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2"))

    assert device.model_dump(mode='json', by_alias=True, exclude_none=True) == {
        "networkAccessIdentifier": "test_device_id",
        "ipv4Address": {
            "publicAddress": "1.1.1.2",
            "privateAddress": "1.1.1.2"
        }
    }

def test_serializing_device_with_ipv6(client):
    device = client.devices.get("test_device_id", ipv6_address="2345:0425:2CA1:0000:0000:0567:5673:23b5")

    assert device.model_dump(mode='json', by_alias=True, exclude_none=True) == {
        "networkAccessIdentifier": "test_device_id",
        "ipv6Address": "2345:0425:2CA1:0000:0000:0567:5673:23b5"
    }

def test_serializing_device_with_phone_number(client):
    device = client.devices.get("test_device_id", phone_number="+1 206 555 0100")

    assert device.model_dump(mode='json', by_alias=True, exclude_none=True) == {
        "networkAccessIdentifier": "test_device_id",
        "phoneNumber": "+1 206 555 0100"
    }
