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
    SliceInfo,
)

client = nac.NetworkAsCodeClient(token="<MY_TOKEN>")

device = client.devices.get("testuser@open5glab.net", ipv4_address="1.1.1.2")

# Creation of a slice
# We use the country code (MCC) and network code (MNC) to identify the network
# Different types of slices can be requested using service type and differentiator
# Area of the slice must also be described in geo-coordinates
slice = client.slices.create(
    network_id=NetworkIdentifier(mcc="664", mnc="22"),
    slice_info=SliceInfo(service_type="eMBB", differentiator="42A5de"),
    area_of_service=AreaOfService(
        polygon=[
            Point(latitude=42.0, longitude=42.0),
            Point(latitude=41.0, longitude=42.0),
            Point(latitude=42.0, longitude=41.0),
        ]
    ),
    notification_url="http://notify.me/here",
    notification_auth_token="my-token",
)

# Our web server for receiving notifications

app = FastAPI()


class Notification(BaseModel):
    resource: str
    action: str
    state: str


# We'll keep track of when we are retiring the slice between the notifications
retiring = False


@app.post("/notifications")
def receive_notification(
    notification: Notification, authorization: Annotated[Union[str, None], Header]
):
    if authorization == "Bearer my-token":
        slice = client.slices.get(notification.resource)

        # Handler for when the slice has been built
        if notification.state == "AVAILABLE":
            # If we are deactivating the slice, we will receive notification here too
            if retiring:
                # Deactivated slices can be deleted
                slice.delete()
            else:
                slice.activate()

        # Handler for when the slice has been activated
        elif notification.state == "OPERATING":
            print("Slice is active")

            # Activated slices can be deactivated
            slice.deactivate()

            global retiring
            retiring = True
