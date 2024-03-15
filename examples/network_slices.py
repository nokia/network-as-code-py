import time

from fastapi import FastAPI, Header

from pydantic import BaseModel

from typing_extensions import Annotated
from typing import Union

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

device = client.devices.get(DEVICE_ID)

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

# Delete a slice by its name
my_slice.delete()


# Our web server for receiving slice notifications

app = FastAPI()

class Notification(BaseModel):
    resource: str
    action: str
    state: str

# We'll keep track of when we are retiring the slice between the notifications
retiring = False

@app.post("/notifications")
def receive_notification(
    notification: Notification,
    authorization: Annotated[Union[str, None], Header]
):
    if authorization == "Bearer my-token":
        # We can now react to the notifications
        # based on the Notification object
        print(notification)
