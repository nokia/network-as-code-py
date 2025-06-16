# Copyright 2023 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations
from typing import Union, List, Optional, TYPE_CHECKING
from datetime import datetime

from pydantic import ConfigDict, BaseModel, PrivateAttr
from network_as_code.api.client import APIClient
if TYPE_CHECKING:
    from network_as_code.models.device import Device

ALIASES = {"start": "from", "end": "to"}


def alias_generator(name: str) -> str:
    return ALIASES.get(name, name)


class PortRange(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=alias_generator)
    """
    A class representing the `PortRange` model.

    #### Public Attributes:
            start (int): the `start` of a port object.
            end (int): the `end` of a port object.
    """

    start: int
    end: int


class PortsSpec(BaseModel):
    """
    A class representing the `PortsSpec` model.

    #### Public Attributes:
            ranges (List[PortRange]): the `ranges` of a ports spec object.
            ports (Optional[str]): the `ports` of a ports spec object.
    """

    ranges: Optional[List[PortRange]] = None
    ports: Optional[List[int]] = None


class QoDSession(BaseModel, arbitrary_types_allowed=True):
    """
    A class representing the `Session` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (str): Session identifier.
        service_ipv4 (str): IPv4 address of the service.
        service_ipv6 (str): IPv6 address of the service.
        service_ports (Union[PortsSpec, None]): List of ports for a service.
        profile (str): Name of the requested QoS profile.
        status(str): Status of the requested QoS.
        duration(int): Session duration in seconds.
        started_at (Union[datetime, None]): Starting time of the session.
        expires_at (Union[datetime, None]): Expiry time of the session.
        device (Device): Session belongs to device.
        device_ports (Union[PortsSpec, None]): List of ports for a device.
    #### Public Methods:
        delete (None): Deletes a given session.
        extend (None): Extends the duration of a given session.
    #### Static Methods:
        convert_session_model (Session): Returns A `Session` instance.
    """

    _api: APIClient = PrivateAttr()
    id: str
    profile: str
    status: str
    duration: Union[int, None] = None
    started_at: Union[datetime, None] = None
    expires_at: Union[datetime, None] = None
    device: Device # ForwardRef value is used here
    service_ipv4: Union[str, None] = None
    service_ipv6: Union[str, None] = None
    device_ports: Union[PortsSpec, None] = None
    service_ports: Union[PortsSpec, None] = None


    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self):
        """
        Deletes a given session
        ."""
        self._api.sessions.delete_session(self.id)

    def extend(self, additional_duration: int):
        """Extends the duration of a given session.
            #### Args:
                additional_duration (int): Additional session duration in seconds.
        """
        res = self._api.sessions.extend_session(self.id, additional_duration)
        self.duration = res.json()['duration']

    @staticmethod
    def convert_session_model(api, device, session):
        """Returns a `Session` instance.

        Assigns the startedAt and expiresAt attributes None if their value not found.
        #### Args:
            device (Device): A `Device` object.
            session (any): A `Session` object created by the low-level API.
        """
        started_at = (
            # I really hate having to carry this hack around
            datetime.fromisoformat(session["startedAt"].replace("Z", "+00:00"))
            if session.get("startedAt", False)
            else None
        )
        expires_at = (
            # I might just bump minimum Python version over this
            datetime.fromisoformat(session["expiresAt"].replace("Z", "+00:00"))
            if session.get("expiresAt", False)
            else None
        )
        service = session.get("applicationServer")
        device_ports = session.get('devicePorts')
        service_ports = session.get('applicationServerPorts')
        return QoDSession(
            api=api,
            id=session["sessionId"],
            device=device,
            device_ports=PortsSpec(**device_ports) if device_ports else None,
            service_ipv4=service.get("ipv4Address") if service else None,
            service_ipv6=service.get("ipv6Address") if service else None,
            service_ports=PortsSpec(**service_ports) if service_ports else None,
            profile=session["qosProfile"],
            status=session["qosStatus"],
            duration=session.get('duration'),
            started_at=started_at,
            expires_at=expires_at,
        )
    