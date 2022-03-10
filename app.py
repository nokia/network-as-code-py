import os

import network_as_code as nac

SDK_TOKEN = os.environ['NAC_TOKEN']

UE_ID = os.environ['UE_ID']

device = nac.Device(UE_ID, SDK_TOKEN)

print("API connection established: ", device.check_api_connection())

network_profile = device.get_network_profile()

print("Network profile in use: " + network_profile.bandwidth_profile)

# network_profile.bandwidth_profile = "bronze"

# device.apply(network_profile)

# print("Network profile in use: " + device.get_network_profile().bandwidth_profile)

# drone_location = nac.DeviceLocation(drone)
# drone_location.refresh()
# drone_location.latitude
# drone_location.longitude
# drone_location.altitude

# network_slice = nac.NetworkSlice(
#     drone,
#     index=0,
#     qos="best-effort",
#     bandwidth="300 Mbps",
#     default=True,
# )

# network_slice.destroy()
