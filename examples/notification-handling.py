# Notification handling for multiple NaC functionalities:

import time

from fastapi import FastAPI, Header

from pydantic import BaseModel

from typing_extensions import Annotated
from typing import Union

# Our web server for receiving QoD notifications

app = FastAPI()

class EventDetail(BaseModel):
    sessionId: str
    qosStatus: str
    statusInfo: str

class Event(BaseModel):
    eventType: str
    eventTime: str
    eventDetail: EventDetail

class QoDNotification(BaseModel):
    event: Event

@app.post("/qod")
def receive_notification(
    notification: QoDNotification,
    authorization: Annotated[Union[str, None], Header]
):
    if authorization == "Bearer my-token":
        # We can now react to the notifications
        # based on the Notification object
        print(notification)

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

# Our web server for receiving Device Status notifications

# Get roaming-status notifications

# status_handler.py for ROAMING_STATUS

# run with: uvicorn status_handler:app

from fastapi import FastAPI, Header
from pydantic import BaseModel

from typing_extensions import Annotated
from typing import Union


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

# Get connectivity notifications

# status_handler.py for CONNECTIVITY

# run with: uvicorn status_handler:app

from fastapi import FastAPI, Header
from pydantic import BaseModel

from typing_extensions import Annotated
from typing import Union


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
