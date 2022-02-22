import os

import network_as_code as nac

SDK_TOKEN = os.environ['NAC_TOKEN']

drone = nac.Device("imsi", SDK_TOKEN)

print("API connection established: ", drone.check_api_connection())

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
