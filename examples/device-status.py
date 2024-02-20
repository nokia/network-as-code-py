
# device-status.py

import network_as_code as nac

client = nac.NetworkAsCodeClient(
    token="<MY_TOKEN>"
)

device = client.devices.get("device@bestcsp.net", ip="1.1.1.2")

subscription = client.connectivity.subscribe(
    event_type="CONNECTIVITY",
    device=device, 
    max_num_of_reports=5, 
    notification_url="https://example.com/notifications", 
    notification_auth_token="my_token"
)

# !!! CUT SNIPPET HERE !!!

# status_handler.py for ROAMING_STATUS

# run with: uvicorn status_handler:app

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RoamingEventDetail(BaseModel):
    roaming: bool | None
    countryCode: int | None
    countryName: List[String] | None

class Event(BaseModel):
    eventType: str
    eventTime: str
    eventDetail: RoamingEventDetail

class Notification(BaseModel):
    eventSubscriptionId: str
    event: Event

@app.post("/notifications")
def receive_notification(notification: Notification):
    if notification.event.eventDetail.roaming:
        print("Device is roaming")
    else:
        print("Device is not roaming")


# !!! CUT SNIPPET HERE !!!

# status_handler.py for CONNECTIVITY

# run with: uvicorn status_handler:app

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ConnectivityEventDetail(BaseModel):
    deviceStatus: str

class Event(BaseModel):
    eventType: str
    eventTime: str
    eventDetail: ConnectivityEventDetail

class Notification(BaseModel):
    eventSubscriptionId: str
    event: Event

@app.post("/notifications")
def receive_notification(notification: Notification):
    if notification.event.eventDetail.deviceStatus == "REACHABLE":
        print("Device is available")
    elif notification.event.eventDetail.deviceStatus == "UNREACHABLE":
        print("Device is not available")
