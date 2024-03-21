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

import asyncio
from os import access
import datetime
import pdb
from urllib.error import HTTPError
from pydantic import BaseModel, EmailStr, PrivateAttr, Field, ValidationError
from typing import Dict, List, Union, Optional
from enum import Enum

from ..api import APIClient
from ..api.slice_api import Throughput as ApiThroughput
from ..models.session import QoDSession
from ..models.location import CivicAddress, Location
from ..models.device import Device
from ..errors import (
    NotFound,
    InvalidParameter,
    NotFound,
    AuthenticationException,
    ServiceError,
    error_handler,
)


class NetworkIdentifier(BaseModel):
    """
    A class representing the `NetworkIdentifier` model.

    #### Public Attributes:
            mnc (str): the `mnc` of a network identifier object.
            mcc (Optional[str]): the `mcc` of a network identifier object.
    """

    mnc: str
    mcc: str


class SliceInfo(BaseModel):
    """
    A class representing the `SliceInfo` model.

    #### Public Attributes:
            service_type (str): the service type of a slice object, Example: `eMBB`
            differentiator (Optional[str]): the differentiator of a slice object.
    """

    service_type: str
    differentiator: Optional[str]


class Throughput(BaseModel):
    """
    A class representing the `Throughput` model.

    #### Public Attributes:
            guaranteed (float): the guaranteed throughput in kbps
            maximum (float): the maximum throughput in kbps
    """

    guaranteed: Optional[float]
    maximum: Optional[float]


class Point(BaseModel):
    """
    A class representing the `Point` model.

    #### Public Attributes:
            longitude (Union[float, int]): the `longitude` of a point object.
            latitude (Union[float, int]): the `latitude` of a point object.
    """

    longitude: Union[float, int] = Field(serialization_alias="lon")
    latitude: Union[float, int] = Field(serialization_alias="lat")


class AreaOfService(BaseModel):
    """
    A class representing the `AreaOfService` model.

    #### Public Attributes:
            polygon (List[Point]): the `polygon` value of an area of service object.
    """

    polygon: List[Point]


class Apps(BaseModel):
    os: str
    apps: List[str]

class TrafficCategories(BaseModel):
    apps: Apps

class DeviceAttachment(BaseModel):
    id: str
    device_phone_number: str
    _api: APIClient = PrivateAttr()

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        
    
    def delete(self):
        if self.id:
            return self._api.slice_attach.detach(self.id)


class Slice(BaseModel, arbitrary_types_allowed=True):
    """
    A class representing the `Slice` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.

    #### Public Attributes:
        sid (optional): String ID of the slice
        state (str): State of the slice (ie. NOT_SUBMITTED)
        name (optional): Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".
        networkIdentifier (NetworkIdentifier): Name of the network
        sliceInfo (SliceInfo): Purpose of this slice
        notification_url: Destination URL of notifications
        notification_auth_token: Authorization token for notifications
        areaOfService (AreaOfService): Location of the slice
        maxDataConnections (optional): Optional maximum number of data connection sessions in the slice.
        maxDevices (optional): Optional maximum number of devices using the slice.
        sliceDownlinkThroughput (optional): Optional throughput object
        sliceUplinkThroughput (optional): Optional throughput object
        deviceDownlinkThroughput (optional): Optional throughput object
        deviceUplinkThroughput: (optional): Optional throughput object


    #### Public Methods:
        activate (None): Activate a network slice.
        attach (): Attach a network slice to a device.
        deactivate (None): Deactivate a network slice. The slice state must be active to be able to perform this operation.
        delete (None): Delete network slice. The slice state must not be active to perform this operation.
        refresh (None): Refresh the state of the network slice.
        wait_done (str): Wait till state of the network slice is not "PENDING", anymore. Returns new state.

    #### Callback Functions:
        on_creation ():
        on_event ():

    """

    _api: APIClient = PrivateAttr()
    _sessions: List[QoDSession] = PrivateAttr()
    sid: Optional[str]
    state: str
    name: Optional[str] = Field(
        None,
        description='Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".',
        min_length=4,
        max_length=64,
        regex="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$",
    )
    network_identifier: NetworkIdentifier
    slice_info: SliceInfo
    notification_url: str
    notification_auth_token: Optional[str]
    area_of_service: Optional[AreaOfService] = Field(
        None, description="Area which the network slice is intended to serve"
    )
    max_data_connections: Optional[int] = Field(
        None,
        description="Maximum number of data connection sessions in the slice.",
        ge=0,
    )
    max_devices: Optional[int] = Field(
        None, description="Maximum number of devices using the slice.", ge=0
    )
    slice_downlink_throughput: Optional[Throughput] = None
    slice_uplink_throughput: Optional[Throughput] = None
    device_downlink_throughput: Optional[Throughput] = None
    device_uplink_throughput: Optional[Throughput] = None
    _attachments: List[DeviceAttachment] = PrivateAttr()

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []
        self._attachments = []

    def activate(self) -> None:
        """Activate network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.activate()
            ```
        """
        if self.name:
            return self._api.slicing.activate(self.name)
    
    def deactivate(self) -> None:
        """Deactivate network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.deactivate()
            ```
        """
        if self.name:
            return self._api.slicing.deactivate(self.name)
    
    def _to_api_throughput(self, throughput: Optional[Throughput] = None) -> Optional[ApiThroughput]:
        if throughput is not None:
            return ApiThroughput(guaranteed=throughput.guaranteed, maximum=throughput.maximum)
        return None

    def modify(
            self,
            slice_downlink_throughput: Optional[Throughput] = None,
            slice_uplink_throughput: Optional[Throughput] = None,
            device_downlink_throughput: Optional[Throughput] = None,
            device_uplink_throughput: Optional[Throughput] = None,
            max_data_connections: Optional[int] = None,
            max_devices: Optional[int] = None,
    ):
        self._api.slicing.create(
            modify = True,
            network_id=self.network_identifier,
            slice_info=self.slice_info,
            notification_url=self.notification_url,
            notification_auth_token=self.notification_auth_token,
            name=self.name,
            area_of_service=self.area_of_service,
            slice_downlink_throughput=self._to_api_throughput(slice_downlink_throughput),
            slice_uplink_throughput=self._to_api_throughput(slice_uplink_throughput),
            device_downlink_throughput=self._to_api_throughput(device_downlink_throughput),
            device_uplink_throughput=self._to_api_throughput(device_uplink_throughput),
            max_data_connections = max_data_connections,
            max_devices=max_devices
        )

        # Update model (if no exception on modify)
        self.slice_downlink_throughput = slice_downlink_throughput
        self.slice_uplink_throughput = slice_uplink_throughput
        self.device_downlink_throughput = device_downlink_throughput
        self.device_uplink_throughput = device_uplink_throughput
        self.max_data_connections = max_data_connections
        self.max_devices = max_devices


    def delete(self) -> None:
        """Delete network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.delete()
            ```
        """
        if self.name:
            return self._api.slicing.delete(self.name)

    def refresh(self) -> None:
        """Refresh state of the network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.refresh()
            ```
        """
        slice_data = self._api.slicing.get(self.name)
        self.state = slice_data.json()["state"]

    async def wait_done(self, timeout: datetime.timedelta = datetime.timedelta(seconds=3600), poll_backoff: datetime.timedelta = datetime.timedelta(seconds=10)) -> str:
        """Wait for an ongoing order to complete.
           I.e. not being in "PENDING" state.
           Returns new state.

        #### Args:
            timeout (datetime.timedelta): Timeout of waiting. Default is 1h.
            poll_backoff (datetime.timedelta): Backoff time between polling.

        #### Example:
            ```python
            new_state = slice.wait_done()
            ```
        """
        poll_backoff_seconds = float(poll_backoff.total_seconds())
        end = datetime.datetime.now() + timeout
        while self.state == "PENDING" and datetime.datetime.now() < end:
            await asyncio.sleep(poll_backoff_seconds)
            self.refresh()
        return self.state

    def attach(
        self,
        device: Device,
        traffic_categories: Union[TrafficCategories, None],
        notificationUrl: Union[str, None],
        notificationAuthToken: str
    ) -> None:
        """Attach network slice.

        #### Args:
            device (Device): Device object that the slice is being attached to

        #### Example:
            ```python
            device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
            slice.attach(device, traffic_categories = TrafficCategories(
                apps=Apps(
                    os="97a498e3-fc92-5c94-8986-0333d06e4e47",
                    apps=["ENTERPRISE", "ENTERPRISE2"]
                )
            )
        )
            ```
        """
        new_attachment = self._api.slice_attach.attach(
            device, self.name, traffic_categories, notificationUrl, notificationAuthToken
        ).json()

        
        self._attachments.append(
            DeviceAttachment(self._api, id=new_attachment['nac_resource_id'], device_phone_number=device.phone_number)
        )

        return new_attachment


    def detach(
        self,
        device: Device,
    ) -> None:
        """Detach network slice.

        #### Args:
            None

        #### Example:
            ```python
            device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
            slice.attach(device)
            slice.detach()
            ```
        """
        attachment = [attachment for attachment in self._attachments if attachment.device_phone_number == device.phone_number]
        if len(attachment) > 0:
            attachment[0].delete()
        else:
            raise NotFound("Attachment not found")


    @staticmethod
    def network_identifier_from_dict(networkIdentifierDict: Optional[Dict[str, str]]):
        """Returns a `NetworkIdentifier` instance.

        Assigns the `mcc` and `mnc`.
        #### Args:
            networkIdentifierDict (Dict[str, str]): A Network Identifier object with `mcc` and `mnc` values.
        """
        if networkIdentifierDict:
            return NetworkIdentifier(
                mcc=networkIdentifierDict["mcc"], mnc=networkIdentifierDict["mnc"]
            )
        else:
            return None

    @staticmethod
    def slice_info_from_dict(sliceInfoDict: Optional[Dict[str, str]]):
        """Returns a `SliceInfo` instance.

        Assigns the `service_type` and `differentiator`.
        #### Args:
            sliceInfoDict (Dict[str, str]): A Slice Info object with `service_type` and `differentiator` values.
        """
        if sliceInfoDict:
            return SliceInfo(
                service_type=sliceInfoDict["serviceType"],
                differentiator=sliceInfoDict["differentiator"],
            )
        else:
            return None

    @staticmethod
    def area_of_service_from_dict(areaOfServiceDict: Optional[Dict[str, List[Dict[str, float]]]]) -> Optional[AreaOfService]:
        """Returns a `AreaOfService` instance.

        Assigns the `polygon`.
        #### Args:
            areaOfServiceDict (Dict[str, List[Dict[str, float]]]): An Area Of Service object with polygon list value.
        """
        if areaOfServiceDict:
            polygon = areaOfServiceDict["polygon"]
            return AreaOfService(
                    polygon=[
                        Point(latitude=polygon[0]["lat"], longitude=polygon[0]["lon"]),
                        Point(latitude=polygon[1]["lat"], longitude=polygon[1]["lon"]),
                        Point(latitude=polygon[2]["lat"], longitude=polygon[2]["lon"]),
                        Point(latitude=polygon[3]["lat"], longitude=polygon[3]["lon"]),
                    ]
            )
        else:
            return None

    @staticmethod
    def throughput(throughputdict: Optional[Dict[str, float]]):
        """Returns a `Throughput` instance.

        Assigns the `guaranteed` and `maximum`.
        #### Args:
            throughputDict (Dict[str, float]): A Throughput object with `guaranteed` and `maximum` values.
        """
        if throughputdict:
            return Throughput(
                guaranteed=throughputdict.get("guaranteed"),
                maximum=throughputdict.get("maximum"),
            )
        else:
            return None
