# Specialized Network functionalities

# Slice examples:

import asyncio
import time
from integration_tests.test_slice import Apps, DeviceIpv4Addr, TrafficCategories
import network_as_code as nac

from network_as_code.models.slice import (
    Point,
    AreaOfService,
    NetworkIdentifier,
    SliceInfo,
    Throughput
)

SDK_TOKEN = "<YOUR-API-KEY>"

# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN
)

async def slice_life_cycle():
    # Creation of a slice
    # We use the country code (MCC) and network code (MNC) to identify the network
    # Different types of slices can be requested using service type and differentiator
    # Area of the slice must also be described in geo-coordinates
    my_slice = client.slices.create(
        name="slice-test-xyzzy",
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

    print(f"Slice created: {my_slice}")

    # # We can take advantage of Slice.wait_for() in async functions
    # # This allows us to, e.g., wait for a slice to become available
    await my_slice.wait_for(desired_state="AVAILABLE")

    print("Slice is now operational")

    # # Get a slice by its ID
    my_slice = client.slices.get("slice-test-xyzzy")

    # # Get a slice by using an index
    # # or remove the index '[0]' to get all slices
    # one_slice = client.slices.get_all()[0]

    # # Slices must be activated before devices can be added
    my_slice.activate()
    await my_slice.wait_for(desired_state="OPERATING")

    print("Slice is active and ready for devices")

    # Afterwards we can attach or detach devices
    device = client.devices.get(phone_number="+3670123456", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", public_port=54000))
    my_slice.attach(
        device,
        traffic_categories=TrafficCategories(
            apps=Apps(
                os="97a498e3-fc92-5c94-8986-0333d06e4e47",
                apps=["ENTERPRISE"]
            )
        ),
        notification_url="https://example.com/notifications",
        notification_auth_token="c8974e592c2fa383d4a3960714")

    print("Device attached")

    time.sleep(10)

    my_slice.detach(device)

    print("Device detached")

    # For unallocating a slice, we first deactivate the slice
    my_slice.deactivate()
    await my_slice.wait_for(desired_state="AVAILABLE")

    print("Slice deactivated")

    # A deactivated slice can be freely removed
    my_slice.delete()
    
    print("Slice deleted")

# Since we use the asynchronous Slice.wait_for(), we must execute
# in an async function. We can run such functions with asyncio:
asyncio.run(slice_life_cycle())

# If you cannot run async functions, you can also utilize webhook
# handlers or polling to handle slice state transitions.
# Simple manual polling can be implemented like this:

# while my_slice.state != "AVAILABLE":
#     my_slice.refresh()
#     time.sleep(1)
