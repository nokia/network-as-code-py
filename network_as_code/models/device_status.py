from os import access
from pydantic import BaseModel, EmailStr, PrivateAttr, ValidationError
from typing import List, Union

from ..api import APIClient
from ..models.device import Device
from typing import Optional


class EventSubscription(BaseModel):
    """
    A class representing the `ConnectivitySubscription` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        max_num_of_reports (str): Number of notifications until the subscription is available
        notification_url (str): Notification URL for session-related events.
        notification_auth_token (optional): Authorization token for notification sending.
        device (Device): Identifier of the device
    """

    id: Optional[str]
    _api: APIClient = PrivateAttr()
    max_num_of_reports: int
    notification_url: str
    notification_auth_token: Optional[str]
    device: Device

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self) -> None:
        """Delete device connectivity status

        #### Args:
            id (str): Resource ID

        #### Example:
            ```python
            device.delete_connectivity(id="hadsghsio")
            ```
        """

        # Error Case: Delete connectivity status
        self._api.devicestatus.delete_subscription(self.id)
