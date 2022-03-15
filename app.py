import os

import network_as_code as nac

SDK_TOKEN = os.environ['NAC_TOKEN']
UE_ID = os.environ['UE_ID']

# Give the device the UE identifier and SDK token
device = nac.Device(UE_ID, SDK_TOKEN)

# Checking for an API connection
print("API connection established: ", device.check_api_connection())

# Get the network profile for the device
old_network_profile = device.network_profile()
print("Network profile in use: " + old_network_profile.bandwidth_profile)

# Change the network profile
device.apply(nac.NetworkProfile("bronze"))

# Get the changed profile
new_network_profile = device.network_profile()
print("Network profile in use: " + new_network_profile.bandwidth_profile)

# Reset the device back to previous profile
device.apply(old_network_profile)
print("Reset the network profile")

# Get the device location
location = device.location()
print("Device at location: ", location.longitude, location.latitude, location.elevation)
