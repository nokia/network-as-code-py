# Specialized Network functionalities

# Slice examples:

import asyncio
import time
import network_as_code as nac

from network_as_code.models.slice import (
    Point,
    AreaOfService,
    NetworkIdentifier,
    SliceInfo,
    Throughput
)

SDK_TOKEN = "<your-application-key-here>"
DEVICE_ID = "device@testcsp.net"


# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN
)

# Creation of a slice
# We use the country code (MCC) and network code (MNC) to identify the network
# Different types of slices can be requested using service type and differentiator
# Area of the slice must also be described in geo-coordinates
my_slice = client.slices.create(
    name="slice-test-2",
    network_id = NetworkIdentifier(mcc="236", mnc="30"),
    slice_info = SliceInfo(service_type="eMBB", differentiator="444444"),
    area_of_service = AreaOfService(polygon=[
        Point(latitude=47.344, longitude=104.349),
        Point(latitude=35.344, longitude=76.619),
        Point(latitude=12.344, longitude=142.541),
        Point(latitude=19.43, longitude=103.53)
    ]),
    slice_downlink_throughput = Throughput(guaranteed=3415, maximum=1234324),
    slice_uplink_throughput = Throughput(guaranteed=3415, maximum=1234324),
    device_downlink_throughput = Throughput(guaranteed=3415, maximum=1234324),
    device_uplink_throughput = Throughput(guaranteed=3415, maximum=1234324),
    max_data_connections=10,
    max_devices=6,
     # Use HTTPS to send notifications
    notification_url="https://snippets.requestcatcher.com/test",
)

# Get a slice by its ID
slice = client.slices.get(my_slice.name)

# Get a slice by using an index
# or remove the index '[0]' to get all slices
one_slice = client.slices.get_all()[0]

# Modify the slice
my_slice.modify(
    max_data_connections = 12,
    max_devices = 3,
    slice_downlink_throughput=Throughput(guaranteed=10, maximum=10),
    slice_uplink_throughput=Throughput(guaranteed=10, maximum=10),
    device_downlink_throughput=Throughput(guaranteed=10, maximum=10),
    device_uplink_throughput=Throughput(guaranteed=10, maximum=10)
)

async def slice_attachments():
    # We can take advantage of Slice.wait_for() in async functions
    # This allows us to, e.g., wait for a slice to become available
    await my_slice.wait_for(desired_state="AVAILABLE")

    # Slices must be activated before devices can be added
    my_slice.activate()
    await my_slice.wait_for(desired_state="OPERATING")

    # Afterwards we can attach or detach devices
    device = client.devices.get(DEVICE_ID)
    my_slice.attach(device)
    my_slice.detach(device)

    # For unallocating a slice, we first deactivate the slice
    my_slice.deactivate()
    await my_slice.wait_for(desired_state="AVAILABLE")

    # A deactivated slice can be freely removed
    my_slice.delete()

# Since we use the asynchronous Slice.wait_for(), we must execute
# in an async function. We can run such functions with asyncio:
asyncio.run(slice_attachments())

# If you cannot run async functions, you can also utilize webhook
# handlers or polling to handle slice state transitions.
# Simple manual polling can be implemented like this:
while my_slice.state != "AVAILABLE":
    my_slice.refresh()
    time.sleep(1)