
from datetime import datetime
from pydantic import BaseModel, PrivateAttr
from typing import Optional
from network_as_code.api.client import APIClient

from network_as_code.models.device import Device

class CongestionSubscription(BaseModel):
    id: Optional[str]
    _api: APIClient = PrivateAttr()
    starts_at: Optional[datetime]
    expires_at: Optional[datetime]

    def __init__(self, api: APIClient, **data):
        super().__init__(**data)
        self._api = api

    def delete(self):
        self._api.congestion.delete_subscription(self.id)
