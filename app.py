import network_as_code as nac

drone = nac.Device("imsi", "sdk_token")

drone_location = nac.DeviceLocation(drone)
drone_location.refresh()
drone_location.latitude
drone_location.longitude
drone_location.altitude
