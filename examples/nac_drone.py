import network_as_code as nac
from functools import partial

def main(camera):
    # Initialize a Device object for 5G network management
    drone = nac.Device(
        id="drone123@dronecompany.site",
        sdk_token="KbyUmhTLMpYj7CD2di7JKP1P3qmLlkPt",
    )

    # Create a private network slice for this device
    network_profile = nac.NetworkProfile("uav_lowpowermode")

    drone.apply(network_profile)

    # Setup functions that will be used to respond to movement and cleanup afterwards.
    setup = partial(anomaly_response, camera, drone, network_slice)
    teardown = partial(anomaly_response_teardown, camera, drone, network_slice)
    camera.monitor(event="movement", setup=setup, teardown=teardown)

def anomaly_response(camera, drone, network_slice):
    """Changes that are required for responding to a detected anomaly."""
    drone.apply(nac.NetworkProfile("uav_streaming"))
    drone.follow_target(target="human")

def anomaly_response_teardown(camera, drone, network_slice):
    """Changes that need to be done after carrying out a response to an anomaly."""
    drone.apply(nac.NetworkProfile("uav_lowpowermode"))
    drone.return_to_normal()
