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

# Give the device the UE identifier and SDK token
device = nac.Device(UE_ID, SDK_TOKEN)

# Fetch the network profile of a device
network_profile = device.network_profile()

# Determine the type of network profile in use
if network_profile.bandwidth_profile == "uav_lowpowermode":
    # We can switch to a new profile with Device.apply()
    # This function takes a configuration object (such as a NetworkProfile) as its parameter
    device.apply(nac.NetworkProfile("uav_streaming"))
