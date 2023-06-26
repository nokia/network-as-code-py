
from pydantic import BaseModel, PrivateAttr, Field

from typing import Union, List

from network_as_code.api.client import APIClient

from ..errors import error_handler

ALIASES = {
    "start": "from",
    "end": "to"
}

def alias_generator(name: str) -> str:
    return ALIASES.get(name, name)

class PortRange(BaseModel, allow_population_by_field_name = True, alias_generator=alias_generator):
    start: int
    end: int

class PortsSpec(BaseModel):
    ranges: List[PortRange] = []
    ports: List[int] = []

class Session(BaseModel, arbitrary_types_allowed = True):
    """
    A class representing the `Session` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (str): Session identifier.
        device_ip (str): IP address of the device.
        device_ports (Union[PortsSpec, None]): List of ports for a device.
        service_ip (str): IP address of a service.
        service_ports (Union[PortsSpec, None]): List of ports for a service.
        profile (str): Name of the requested QoS profile.
        status(str): Status of the requested QoS.
        started_at (Union[int, None]): Starting time of the session.
        expires_at (Union[int, None]): Expiry time of the session.
        notification_url (Union[int, None]): Notification URL for session-related events.
    #### Public Methods:
        delete (None): Deletes a given session.
        duration (int | None): Returns the duration of a given session.
    #### Static Methods:
        convert_session_model (Session): Returns A `Session` instance.
    """

    _api: APIClient = PrivateAttr()
    id: str
    device_ip: str
    device_ports: Union[PortsSpec, None]
    service_ip: str
    service_ports: Union[PortsSpec, None] 
    profile: str
    status: str
    started_at: Union[int, None]
    expires_at: Union[int, None]
    notification_url: Union[str, None]

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self):
        """Deletes a given session."""
        error_handler(func=self._api.sessions.delete_session, arg={'sessionId': self.id})

    def duration(self):
        """Returns the duration of a given session."""
        if self.started_at and self.expires_at:
            return self.expires_at - self.started_at
        else:
            return None

    @staticmethod
    def convert_session_model(api, ip, session):
        """Returns a `Session` instance.

        Assigns the startedAt and expiresAt attributes None if their value not found.
        #### Args:
            ip (any): IP address of the service.
            session (any): A `Session` object created by the low-level API.
        """
        started_at = int(session["startedAt"]) if session["startedAt"] else None
        expires_at = int(session["expiresAt"]) if session["expiresAt"] else None
        return Session(api=api, id=session["id"], device_ip=ip, device_ports=None, service_ip="", service_ports=None, profile=session["qosProfile"], status=session["qosStatus"], started_at=started_at, expires_at=expires_at) 


