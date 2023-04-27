
from network_as_code.models.location import CivicAddress


def test_getting_a_device_location_sends_out_request(client):
    device = client.devices.get("testuser@testcsp.net", ip = "1.1.1.2")

    location = device.location()

    assert location.longitude
    assert location.latitude
    assert location.civic_address

def test_verifying_a_device_location_sends_out_request(client):
    device = client.devices.get("testuser@testcsp.net", ip = "1.1.1.2")

    device.verify_location(longitude=19.07915612501993, latitude=47.48627616952785, accuracy="10km")
