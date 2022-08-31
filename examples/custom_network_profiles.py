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

client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN,
    base_url="http://localhost:5050/nwac/v4",
    testmode=True
)

# Give the device the UE identifier and SDK token
device = client.subscriptions.get(UE_ID)

# Let's create a 20/5 megabit Custom Network Profile
device.set_custom_bandwidth(5 * 1000 * 1000, 20 * 1000 * 1000)

# If we now query the device's network profile, we will be told that we are using a custom profile
assert device.get_custom_bandwidth() == (5 * 1000 * 1000, 20 * 1000 * 1000)
