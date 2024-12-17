# location-information.py

"""
NaC-py and Network as Code also provide access to location information exposed by
the mobile network infrastructure. This allows determining the rough coordinates
of a device connected to the network based on the base station the device is
connected to at a given moment.

This data is more accurate in areas with a dense concentration of base stations
and less accurate in more sparse areas.
"""

import network_as_code as nac

from network_as_code.models.location import CivicAddress, Location

from network_as_code.models.device import Device, DeviceIpv4Addr

SDK_TOKEN = "<your-application-key-here>"
DEVICE_ID = "device@testcsp.net"

# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN
)

device = client.devices.get(DEVICE_ID)

# Getting the device location is quite simple
# The default value for max_age parameter is 60
location = device.location(max_age=60)

# The location object contains fields for longitude, latitude and also elevation
longitude = location.longitude
latitude = location.latitude

print(location.longitude)
print(location.latitude)
print(location.civic_address)

# Or for estimations, use the is_there object
# followed by the `verify_location()` method
# with the geo-coordinates and maximum age in seconds:
is_there = device.verify_location(
    longitude=19,
    latitude=47,
    radius=10_000,
    max_age=3600
).result_type
