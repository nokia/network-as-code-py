
import time

from pydantic import BaseModel

import network_as_code as nac

from network_as_code.models.slice import Point, AreaOfService

client = nac.NetworkAsCodeClient(
    token="<MY_TOKEN>"
)

device = client.devices.get("testuser@open5glab.net", ip="1.1.1.2")

# Creation of a slice
# We use the country code (MCC) and network code (MNC) to identify the network
# Different types of slices can be requested using service type and differentiator
# Area of the slice must also be described in geo-coordinates
slice = client.slices.create(
    network_id = NetworkIdentifier(mcc="664", mnc="22"),
    slice_info = SliceInfo(service_type="eMBB", differentiator="42A5de"),
    area_of_service=AreaOfService(poligon=[Point(lat=42.0, lon=42.0), Point(lat=41.0, lon=42.0), Point(lat=42.0, lon=41.0)])
)

while slice.state != "CREATED":
    slice.refresh()
    time.sleep(1)

# Activating a slice
slice.activate()
while slice.state != "AVAILABLE":
    slice.refresh()
    time.sleep(1)

# We can attach a device to an active slice
slice.attach(device)

# We can also then detach devices
slice.detach(device)

# Deactivating a slice
slice.deactivate()
while slice.state != "CREATED":
    slice.refresh()

# Only deactivated slices may be deleted
slice.delete()
