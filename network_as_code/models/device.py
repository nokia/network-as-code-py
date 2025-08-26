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
from pydantic import BaseModel, Field, PrivateAttr

from ..api import APIClient
from ..models.session import QoDSession, PortsSpec
from ..models.location import Location, VerificationResult
from ..models.congestion import Congestion
from ..models.number_verification import AccessToken
from ..api.utils import tokenizer
from ..errors import InvalidParameter, NotFound

class RoamingStatus(BaseModel):
    roaming: bool
    country_code: Optional[int] = None
    country_name: Optional[List[str]] = None

class DeviceIpv4Addr(BaseModel):
    """
    A class representing the `DeviceIpv4Addr` model.

    #### Public Attributes:
            public_address Optional[str]: the `public_address` of a device IPv4 address object.
            private_address Optional[str]: the `private_address` of a device IPv4 address object.
            public_port (Optional[int]): the `public_port` of a device IPv4 address object.
    """

    public_address: Optional[str] = Field(None, serialization_alias="publicAddress")
    private_address: Optional[str] = Field(default=None, serialization_alias="privateAddress")
    public_port: Optional[int] = Field(default=None, serialization_alias="publicPort")

class Device(BaseModel):
    """
    A class representing the `Device` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.


    #### Public Attributes:
        network_access_identifier(EmailStr): Device Identifier email string.
        phone_number(str): Phone Number string
        ipv4_address (DeviceIpv4Addr): Ipv4 address of the device.
        ipv6_address (str): Ipv6 address of the device.
        imsi (Optional[int]): International Mobile Subscriber Identity (IMSI) of the device.

    #### Public Methods:
        create_session (Session): Creates a session for the device.
        sessions (List[Session]): Returns all the sessions created by the device network_access_id.
        clear_sessions (): Deletes all the sessions created by the device network_access_id.
        location (Location): Gets the location of the device and returns a Location client object.
        verify_location (bool): Verifies if a device is located in a given location point.
        get_connectivity (ConnectivityData): Retrieve device connectivity status data
        update_connectivity (ConnectivityData): Update device connectivity status data
        delete_connectivity (): Delete device connectivity status
        get_sim_swap_date (): Retrieve the latest sim swap date
        verify_sim_swap (): Verify if there was sim swap
    """
    _api: APIClient = PrivateAttr()
    _sessions: List[QoDSession] = PrivateAttr()
    network_access_identifier: Union[str, None] = Field(
        None, serialization_alias="networkAccessIdentifier"
    )
    phone_number: Optional[str] = Field(None, serialization_alias="phoneNumber")
    ipv4_address: Union[DeviceIpv4Addr, None] = Field(
        None, serialization_alias="ipv4Address"
    )
    ipv6_address: Union[str, None] = Field(None, serialization_alias="ipv6Address")
    imsi: Optional[int] = Field(None, serialization_alias="imsi")

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
        duration,
        service_ipv4=None,
        service_ipv6=None,
        device_ports: Union[None, PortsSpec] = None,
        service_ports: Union[None, PortsSpec] = None,
        notification_url=None,
        notification_auth_token=None,
    ) -> QoDSession:
        """Creates a session for the device.

        #### Args:
            profile (any): Name of the requested QoS profile.
            duration(int): The length of the QoD session in seconds.
            service_ipv4 (any): IPv4 address of the service.
            service_ipv6 (optional): IPv6 address of the service.
            device_ports (optional): List of the device ports.
            service_ports (optional): List of the application server ports.
            notification_url (optional): Notification URL for session-related events.
            notification_token (optional): Security bearer token to authenticate registration of session.

        #### Example:
            ```python
            session = device.create_session(profile="QOS_L", duration=3600,
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
            duration,
            service_ipv4,
            service_ipv6,
            device_ports,
            service_ports,
            notification_url,
            notification_auth_token,
        )
        return QoDSession.convert_session_model(self._api, self, session.json())

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
                     sessions
                ))
        except NotFound:
            # API will return 404 for a device which has had all of its sessions deleted
            # Because this is not an error, we will simply return an empty list here
            return []

    def clear_sessions(self):
        """Clears sessions of the device."""
        for session in self.sessions():
            session.delete()

    def __convert_session_model(self, session) -> QoDSession:
        return QoDSession.convert_session_model(self._api, self, session)

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
        radius = body["area"]["radius"]

        return Location(
            longitude=longitude,
            latitude=latitude,
            radius=radius,
        )

    def verify_location(
        self, longitude: float, latitude: float, radius: float, max_age: int = 60
    ) -> VerificationResult:
        """Verifies the location of the device (Returns VerificationResult object).

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
        response = self._api.location_verify.verify_location(latitude, longitude, self, radius, max_age)
        body = response
        result_type = body["verificationResult"]
        match_rate = body["matchRate"] if "matchRate" in body.keys() else None
        last_location_time = datetime.fromisoformat(
            body["lastLocationTime"]
        ) if "lastLocationTime" in body.keys() else None

        return VerificationResult(
            result_type = result_type,
            match_rate = match_rate,
            last_location_time = last_location_time
        )

    def get_connectivity(self):
        """Get the connectivity status for the device as a string"""
        status = self._api.devicestatus.get_connectivity(
            self.model_dump(mode="json", by_alias=True, exclude_none=True)
        )["connectivityStatus"]

        return status

    def get_roaming(self) -> RoamingStatus:
        """Get the roaming status for the device

        #### Returns
        Object of RoamingStatus class, which contains the roaming status, country code and country name
        """
        status = self._api.devicestatus.get_roaming(
            self.model_dump(mode="json", by_alias=True, exclude_none=True)
        )

        return RoamingStatus(
            roaming=status["roaming"],
            country_code=status.get("countryCode"),
            country_name=status.get("countryName"),
        )

    # TODO:                                                              # pylint: disable=fixme
    #       In the future this won't be possible without first creating a CongestionSubscription
    #       Either this needs to be migrated to CongestionSubscription, needs to take a valid
    #       CongestionSubscription as a parameter or needs to be documented as having that requirement
    def get_congestion(
        self,
        start: Union[datetime, str, None] = None,
        end: Union[datetime, str, None] = None,
    ) -> List[Congestion]:
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

        assert isinstance(json, list)

        return [Congestion.from_json(congestion_json) for congestion_json in json]

    def get_sim_swap_date(self) -> Union[datetime, None]:
        """Get the latest SIM swap date.

        #### Returns
             datetime object containing the date of last SIM swap OR the activation date OR None
             if date is not available
        """
        if self.phone_number is None:
            raise InvalidParameter("Device phone number is required.")

        response = self._api.sim_swap.fetch_sim_swap_date(self.phone_number).get(
            "latestSimChange"
        )

        if response:
            return datetime.fromisoformat(response)

        return None

    def verify_sim_swap(self, max_age: Optional[int] = None) -> bool:
        """Verify if there was sim swap.

        #### Args:
             max_age (Optional[int]): Max acceptable age for sim swap verification info in hours
        #### Returns
             True/False
        """
        if self.phone_number is None:
            raise InvalidParameter("Device phone number is required.")
        return self._api.sim_swap.verify_sim_swap(self.phone_number, max_age)

    def _get_single_use_access_token(self, code: str) -> AccessToken:
        """Get Access Token for number verification API

        #### Args:
             code (str): Changes the code for Access Token from Authorization Servers token_endpoint
        #### Returns
             AccessToken object containing access token, token type and expiration time
        """
        grant_type = "authorization_code"
        credentials = self._api.credentials.fetch_credentials()
        token_endpoint = self._api.authorization.fetch_endpoints().get(
            "token_endpoint"
        )
        data = {
            "client_id": credentials['client_id'],
            "client_secret": credentials['client_secret'],
            "grant_type": grant_type,
            "code": code,
        }
        response = tokenizer(token_endpoint, data=data)
        body = response.json()
        access_token = body["access_token"]
        token_type = body["token_type"]
        expires_in = body["expires_in"]

        single_use_token = AccessToken(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in
        )
        return single_use_token

    def verify_number(self, code: str) -> bool:
        """Verifies users phone number.

        #### Args:
             code (str): Changes the code for Access Token through  _get_single_use_access_token
        #### Returns
             True/False
        """
        if self.phone_number is None:
            raise InvalidParameter("Device phone number is required.")
        authenticator = self._get_single_use_access_token(code=code)
        payload = {
            "phoneNumber": self.phone_number,
        }
        headers = {'Authorization': f'{authenticator.token_type} {authenticator.access_token}'}

        return self._api.number_verification.verify_number(payload=payload, headers=headers)

    def get_phone_number(self, code: str) -> str:
        """Gets the users phone number.

        #### Args:
             code (str): Changes the code for Access Token through  _get_single_use_access_token
        #### Returns:
             String 
        """

        authenticator = self._get_single_use_access_token(code=code)
        headers = {'Authorization': f'{authenticator.token_type} {authenticator.access_token}'}

        return self._api.number_verification.get_phone_number(headers=headers)

    def get_call_forwarding(self) -> List:
        """Gets information about Call Forwarding Services active for the given device.

        #### Returns
             List of string descriptions about active Call Forwarding Services for the given device.
        """
        if self.phone_number is None:
            raise InvalidParameter("Device phone number is required.")

        return self._api.call_forwarding.retrieve_call_forwarding(self.phone_number)

    def verify_unconditional_forwarding(self) -> bool:
        """Verify if device has unconditional call forwarding active.

        #### Returns
             True/False
        """
        if self.phone_number is None:
            raise InvalidParameter("Device phone number is required.")

        return self._api.call_forwarding.verify_unconditional_forwarding(self.phone_number)

    @staticmethod
    def convert_to_device_model(api, device_json):
        device = Device(api=api)
        device.network_access_identifier = device_json.get("networkAccessIdentifier")
        device.phone_number = device_json.get("phoneNumber")
        device.ipv6_address = device_json.get("ipv6Address")
        device.imsi = device_json.get("imsi")
        if "ipv4Address" in device_json:
            device.ipv4_address = DeviceIpv4Addr(
                public_address=device_json["ipv4Address"].get("publicAddress"),
                private_address=device_json["ipv4Address"].get("privateAddress"),
                public_port=device_json["ipv4Address"].get("publicPort"),
            )
        return device
