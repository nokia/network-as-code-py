import os

import network_as_code as nac

SDK_TOKEN = os.environ['NAC_TOKEN']
UE_ID = os.environ['UE_ID']

"""
This example shows how NaC-py can be used to create Custom Network Profiles.

Sometimes a developer might want more control over the exact bandwidth values
for upload and download speed than the pre-made Network Profiles allow. For
this purpose we can use Custom Network Profiles, which apply specific bandwidth
values for a device.

NaC-py allows these values to be specified as bit-per-second, kilobit-per-second
or megabit-per-second using a Unit enum.
"""

# Give the device the UE identifier and SDK token
device = nac.Device(UE_ID, SDK_TOKEN)

# Let's create a 20/5 megabit Custom Network Profile

network_profile = nac.CustomNetworkProfile(download=20, upload=5, unit=nac.Unit.MBIT)

# We then apply this configuration change similarly to a Network Profile using Device.apply()
device.apply(network_profile)

# If we now query the device's network profile, we will be told that we are using a custom profile

assert device.network_profile().bandwidth_profile == "custom"

# We can also use Kbps or bps as our units if we want to
network_profile = nac.CustomNetworkProfile(download=20000, upload=5000, unit=nac.Unit.KBIT)
network_profile = nac.CustomNetworkProfile(download=20000000, upload=5000000, unit=nac.Unit.BIT)
