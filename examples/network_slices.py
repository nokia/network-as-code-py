# Specialized Network functionalities

# Slice examples:

import asyncio
import time
import network_as_code as nac

from network_as_code.models.slice import (
    Point,
    AreaOfService,
    NetworkIdentifier,
    Slice,
    SliceInfo,
    Throughput
)

SDK_TOKEN = "<replace-me>"
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
    name="slice-name",
    network_id=NetworkIdentifier(mcc="664", mnc="22"),
    slice_info=SliceInfo(service_type="eMBB", differentiator="123456"),
    area_of_service=AreaOfService(
        polygon=[
            Point(latitude=42.0, longitude=42.0),
            Point(latitude=41.0, longitude=42.0),
            Point(latitude=42.0, longitude=41.0),
            Point(latitude=42.0, longitude=42.0)
        ]
    ),
    notification_url="https://notify.me/here",
    # Use HTTPS to send notifications
    notification_auth_token="replace-with-your-auth-token"
)

# Get a slice by its ID
slice = client.slices.get(my_slice.name)

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
