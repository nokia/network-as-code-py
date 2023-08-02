from fastapi import FastAPI
from pydantic import BaseModel

import network_as_code as nac

client = nac.NetworkAsCodeClient(
    token="<MY_TOKEN>"
)

device = client.devices.get("testuser@open5glab.net", ip="1.1.1.2")

subscription = client.connectivity.subscribe(
    event_type="CONNECTIVITY",
    device=device, 
    max_num_of_reports=5, 
    notification_url="https://example.com/notifications", 
)

subscription.delete()

app = FastAPI()

class Notification(BaseModel):
    id: str
    status: str

@app.post("/notifications")
def receive_notification(notification: Notification):
    print(notification.status)
