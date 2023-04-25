
def test_getting_a_device_location_sends_out_request(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    location = device.location()

def test_verifying_a_device_location_sends_out_request(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    device.verify_location(latitude=3.14, longitude=3.14, accuracy="10km")
