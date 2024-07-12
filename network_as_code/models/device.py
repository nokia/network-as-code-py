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

from typing import List, Union, Optional
from datetime import datetime
from pydantic import BaseModel, Field, PrivateAttr, model_validator


from ..api import APIClient
from ..models.session import QoDSession, PortsSpec
from ..models.location import CivicAddress, Location
from ..models.congestion import Congestion
from ..errors import NotFound


class RoamingStatus(BaseModel):
    roaming: bool
    country_code: Optional[int] = None
    country_name: Optional[List[str]] = None


class Event(BaseModel):
    """
    A class representing the `Event` model.

    #### Public Attributes:
            target (float): the `target` of an event object.
            atUnix (float): the `atUnix` of an event object.
    """

    target: str
    atUnix: int


class DeviceIpv4Addr(BaseModel):
    """
    A class representing the `DeviceIpv4Addr` model.

    #### Public Attributes:
            public_address (float): the `public_address` of a device IPv4 address object.
            private_address (float): the `private_address` of a device IPv4 address object.
            public_port (Optional[CivicAddress]): the `public_port` of a device IPv4 address object.
    """

    public_address: Optional[str] = Field(None, serialization_alias="publicAddress")
    private_address: Optional[str] = Field(None, serialization_alias="privateAddress")
    public_port: Optional[int] = Field(None, serialization_alias="publicPort")


    @model_validator(mode='before')
    @classmethod
    def check_addresses_and_port(cls, values):
        public_address = values.get('public_address')
        private_address = values.get('private_address')
        public_port = values.get('public_port')
        if public_address:
            if not (private_address or public_port):
                raise ValueError('Either private_address or public_port must be provided when public_address is set.')
        return values


class Device(BaseModel):
    """
    A class representing the `Device` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.


    #### Public Attributes:
        sid(EmailStr): Device Identifier email string.
        phone_number(str): Phone Number string
        ipv4_address (DeviceIpv4Addr): DeviceIpv4Addr
        ipv6_address (str): string

    #### Public Methods:
        create_session (Session): Creates a session for the device.
        sessions (List[Session]): Returns all the sessions created by the device network_access_id.
        clear_sessions (): Deletes all the sessions created by the device network_access_id.
        location (Location): Gets the location of the device and returns a Location client object.
        verify_location (bool): Verifies if a device is located in a given location point.
        get_connectivity (ConnectivityData): Retrieve device connectivity status data
        update_connectivity (ConnectivityData): Update device connectivity status data
        delete_connectivity (): Delete device connectivity status
    """

    _api: APIClient = PrivateAttr()
    _sessions: List[QoDSession] = PrivateAttr()
    network_access_identifier: Union[str, None] = Field(None, serialization_alias='networkAccessIdentifier')
    phone_number: Union[str, None] = Field(None, serialization_alias='phoneNumber')
    ipv4_address: Union[DeviceIpv4Addr, None] = Field(None, serialization_alias='ipv4Address')
    ipv6_address: Union[str, None] = Field(None, serialization_alias='ipv6Address')

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []

    @property
    def network_access_id(self) -> Union[str, None]:
        return self.network_access_identifier

    def create_qod_session(
        self,
        profile,
        service_ipv4=None,
        service_ipv6=None,
        device_ports: Union[None, PortsSpec] = None,
        service_ports: Union[None, PortsSpec] = None,
        duration=None,
        notification_url=None,
        notification_auth_token=None,
    ) -> QoDSession:
        """Creates a session for the device.

        #### Args:
            profile (any): Name of the requested QoS profile.
            service_ipv4 (any): IPv4 address of the service.
            service_ipv6 (optional): IPv6 address of the service.
            device_ports (optional): List of the device ports.
            service_ports (optional): List of the application server ports.
            duration (optional): Session duration in seconds.
            notification_url (optional): Notification URL for session-related events.
            notification_token (optional): Security bearer token to authenticate registration of session.

        #### Example:
            ```python
            session = device.create_session(profile="QOS_L", 
            service_ipv4="5.6.7.8", service_ipv6="2041:0000:140F::875B:131B", 
            notification_url="https://example.com/notifications, 
            notification_token="c8974e592c2fa383d4a3960714")
            ```
        """
        # Checks if at least one parameter is set
        if not service_ipv4 and not service_ipv6:
            raise ValueError("At least one of IP parameters must be provided")

        session = self._api.sessions.create_session(
            self,
            profile,
            service_ipv4,
            service_ipv6,
            device_ports,
            service_ports,
            duration,
            notification_url,
            notification_auth_token,
        )

        # Convert response body to an Event model
        # Event(target=session.json().get('id'), atUnix=session.json().get('expiresAt'))
        return QoDSession.convert_session_model(self._api, self.ipv4_address, session.json())

    def sessions(self) -> List[QoDSession]:
        """List sessions of the device. TODO change the name to get_sessions

        #### Example:
            ```python
            sessions = device.sessions()
            ```
        """
        try:
            sessions = self._api.sessions.get_all_sessions(self)
            return list(
                map(
                    self.__convert_session_model,
                    sessions.json(),
                )
            )
        except NotFound:
            # API will return 404 for a device which has had all of its sessions deleted
            # Because this is not an error, we will simply return an empty list here
            return []

    def clear_sessions(self):
        """Clears sessions of the device."""
        for session in self.sessions():
            session.delete()

    def __convert_session_model(self, session) -> QoDSession:
        return QoDSession.convert_session_model(self._api, self.ipv4_address, session)

    def location(self, max_age: int = 60) -> Location:
        """Returns the location of the device.

         #### Args:
            max_age : Max acceptable age for location info in seconds

        #### Example:
            ```python
            location = device.location(max_age=60)
            ```
        """
        response = self._api.location_retrieve.get_location(self, max_age)
        body = response

        longitude = body["area"]["center"]["longitude"]
        latitude = body["area"]["center"]["latitude"]
        civic_address = None

        if "civicAddress" in body.keys():
            civic_address = CivicAddress(
                country=body["civicAddress"]["country"],
                a1=(
                    body["civicAddress"]["A1"]
                    if "A1" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A1"], str)
                    else None
                ),
                a2=(
                    body["civicAddress"]["A2"]
                    if "A2" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A2"], str)
                    else None
                ),
                a3=(
                    body["civicAddress"]["A3"]
                    if "A3" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A3"], str)
                    else None
                ),
                a4=(
                    body["civicAddress"]["A4"]
                    if "A4" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A4"], str)
                    else None
                ),
                a5=(
                    body["civicAddress"]["A5"]
                    if "A5" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A5"], str)
                    else None
                ),
                a6=(
                    body["civicAddress"]["A6"]
                    if "A6" in body["civicAddress"].keys()
                    and isinstance(body["civicAddress"]["A6"], str)
                    else None
                ),
            )

        return Location(longitude=longitude, latitude=latitude, civic_address=civic_address)

    def verify_location(
        self, longitude: float, latitude: float, radius: float, max_age: int = 60
    ) -> bool:
        """Verifies the location of the device (Returns boolean value).

        #### Args:
            longitude (float): longitude of the device.
            latitude (float): longitude of the device.
            radius (float): radius of the area in meters.
            max_age (int | None): Max acceptable age for location info in seconds, Default=60s

        #### Example:
            ```python
            located? = device.verify_location(longitude=24.07915612501993, 
            latitude=47.48627616952785, radius=10_000, max_age=60)
            ```
        """
        return self._api.location_verify.verify_location(latitude, longitude, self, radius, max_age)

    def get_connectivity(self):
        """Get the connectivity status for the device as a string"""
        status = self._api.devicestatus.get_connectivity(
            self.model_dump(mode='json', by_alias=True, exclude_none=True))["connectivityStatus"]

        return status

    def get_roaming(self) -> RoamingStatus:
        """Get the roaming status for the device

        #### Returns
        Object of RoamingStatus class, which contains the roaming status, country code and country name
        """
        status = self._api.devicestatus.get_roaming(self.model_dump(mode='json', by_alias=True, exclude_none=True))

        return RoamingStatus(
            roaming=status["roaming"],
            country_code=status.get("countryCode"),
            country_name=status.get("countryName"),
        )

    def get_congestion(
        self,
        start: Union[datetime, str, None] = None,
        end: Union[datetime, str, None] = None,
    ) -> Congestion:
        """Get the congestion level this device is experiencing

        #### Args:
             start (Union[datetime, str]): Beginning of the time range to access historical or predicted congestion
             end (Union[datetime, str]): End of the time range to access historical or predicted congestion
        #### Returns
             Congestion object containing congestion level ("low", "medium", "high")
        """
        start = start.isoformat() if isinstance(start, datetime) else start
        end = end.isoformat() if isinstance(end, datetime) else end

        json = self._api.congestion.fetch_congestion(self, start=start, end=end)

        return Congestion(level=json["level"])
