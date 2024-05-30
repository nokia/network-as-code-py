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

from pydantic import ConfigDict, BaseModel, PrivateAttr, Field

from typing import Union, List

from network_as_code.api.client import APIClient

from ..errors import error_handler

from datetime import datetime

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

    ranges: List[PortRange] = []
    ports: List[int] = []


class QoDSession(BaseModel, arbitrary_types_allowed=True):
    """
    A class representing the `Session` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (str): Session identifier.
        service_ip (str): IP address of a service.
        service_ports (Union[PortsSpec, None]): List of ports for a service.
        profile (str): Name of the requested QoS profile.
        status(str): Status of the requested QoS.
        started_at (Union[datetime, None]): Starting time of the session.
        expires_at (Union[datetime, None]): Expiry time of the session.
    #### Public Methods:
        delete (None): Deletes a given session.
        duration (timedelta | None): Returns the duration of a given session.
    #### Static Methods:
        convert_session_model (Session): Returns A `Session` instance.
    """

    _api: APIClient = PrivateAttr()
    id: str
    profile: str
    status: str
    started_at: Union[datetime, None] = None
    expires_at: Union[datetime, None] = None

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self):
        """
        Deletes a given session
        ."""
        self._api.sessions.delete_session(self.id)

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
        started_at = (
            datetime.fromtimestamp(session["startedAt"])
            if session.get("startedAt", False)
            else None
        )
        expires_at = (
            datetime.fromtimestamp(session["expiresAt"])
            if session.get("expiresAt", False)
            else None
        )
        return QoDSession(
            api=api,
            id=session["sessionId"],
            device_ip=ip,
            device_ports=None,
            service_ip="",
            service_ports=None,
            profile=session["qosProfile"],
            status=session["qosStatus"],
            started_at=started_at,
            expires_at=expires_at,
        )
