import os

import network_as_code as nac
import datetime

SDK_TOKEN = os.environ['NAC_TOKEN']
UE_ID = os.environ['UE_ID']

# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN,
    base_url="http://localhost:5050/nwac/v4",
    testmode=True # We execute API calls against simulated network
)

device = client.subscriptions.get(UE_ID)

"""
NaC-py and Network as Code also provide access to location information exposed by
the mobile network infrastructure. This allows determining the rough coordinates
of a device connected to the network based on the base station the device is
connected to at a given moment.

This data is more accurate in areas with a dense concentration of base stations
and less accurate in more sparse areas.
"""

# Getting the device location is quite simple
location = device.get_location()

# The location object contains fields for longitude, latitude and also elevation

longitude = location["lat"]
latitude = location["long"]
elevation = location["elev"]

print(longitude)
print(latitude)
print(elevation)

# The location data does not update automatically, to get an up-to-date device location, we need to fetch it again
location = device.get_location()
