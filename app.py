import network_as_code as nac

drone = nac.Device("imsi", "sdk_token")

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
