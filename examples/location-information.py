
import network_as_code as nac

SDK_TOKEN = "<replace-me>" 
DEVICE_ID = "testuser@testcsp.net"

# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN
)

device = client.devices.get(DEVICE_ID)

"""
NaC-py and Network as Code also provide access to location information exposed by
the mobile network infrastructure. This allows determining the rough coordinates
of a device connected to the network based on the base station the device is
connected to at a given moment.

This data is more accurate in areas with a dense concentration of base stations
and less accurate in more sparse areas.
"""

# Getting the device location is quite simple
location = device.location()

# The location object contains fields for longitude, latitude and also elevation

print(location.longitude)
print(location.latitude)
print(location.civic_address)

import network_as_code as nac
 
from network_as_code.models.location import CivicAddress, Location
 
from network_as_code.models.device import Device, DeviceIpv4Addr
 
# Give the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>",
)
 
device = client.devices.get("device@testcsp.net",
                            ipv4_address = DeviceIpv4Addr(public_address="233.252.0.2",
                                                          private_address="192.0.2.25",
                                                          public_port=80)
)
 
# The default value for max_age parameter is 60
# The location object contains fields for longitude and latitude
location = device.location()
 
longitude = location.longitude
latitude = location.latitude
 
 
print(longitude)
print(latitude)
print(location.civic_address)
