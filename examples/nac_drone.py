import network_as_code as nac
from functools import partial

def main(camera):
    # Initialize the NWaC client
    client = nac.NetworkAsCodeClient(
        token="testing", # Our API access token
        base_url="http://localhost:5050/nwac/v4",
        testmode=True # We are executing against a simulated network
    )

    # Initialize a Device object for 5G network management
    drone = client.subscriptions.get("drone123@dronecompany.site")

    # Modify the drone's bandwidth
    drone.set_bandwidth("uav_lowpowermode")

    # Setup functions that will be used to respond to movement and cleanup afterwards.
    setup = partial(anomaly_response, camera, drone)
    teardown = partial(anomaly_response_teardown, camera, drone)
    camera.monitor(event="movement", setup=setup, teardown=teardown)

def anomaly_response(camera, drone):
    """Changes that are required for responding to a detected anomaly."""
    drone.set_bandwidth("uav_streaming")
    drone.follow_target(target="human")

def anomaly_response_teardown(camera, drone):
    """Changes that need to be done after carrying out a response to an anomaly."""
    drone.set_bandwidth("uav_lowpowermode")
    drone.return_to_normal()
