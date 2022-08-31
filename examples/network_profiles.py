import os

import network_as_code as nac

SDK_TOKEN = os.environ['NAC_TOKEN']
UE_ID = os.environ['UE_ID']

"""
This example shows how NaC-py can be used to get and set Network Profiles.

A Network Profile represents a pre-made network configuration, which determines
things like download and upload speed and in the future also the quality-of-service.

Currently two pre-made Network Profiles exist:
- "uav_lowpowermode" - a low-bandwidth configuration intended for devices that need little bandwidth
- "uav_streaming" - an unlimited bandwidth configuration when a device needs to send or receive as much data as possible

A device will have one Network Profile active at a time, but can be easily switched between Network Profiles.
"""

# We begin by creating a client for Network as Code
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN,
    base_url="http://localhost:5050/nwac/v4",
    testmode=True # We execute our API calls against a simulated network
)

# We get the device by querying subscriptions with the UE's external identifer
device = client.subscriptions.get(UE_ID)

print(device)

# Fetch the network profile of a device
network_profile = device.get_bandwidth()

print(network_profile)

# Determine the type of network profile in use
if network_profile == "uav_lowpowermode":
    # We can switch to a new profile with Device.apply()
    # This function takes a configuration object (such as a NetworkProfile) as its parameter
    device.set_bandwidth("uav_streaming")
