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
import datetime
from typing import Dict, List, Union, Optional
from pydantic import BaseModel, PrivateAttr, Field

from ..api import APIClient
from ..models.session import QoDSession
from ..models.device import Device
from ..errors import NotFound


class Customer(BaseModel):
    """
    A class representing the `Customer` model.

    #### Public Attributes:
            name (str): The name of the Customer.
            description (Optional[str]): The description of the Slice.
            address (Optional[str]): Address of the customer ordering slice creation.
            contact (Optional[str]): Contact of the customer ordering slice creation.
    """

    name: str = Field(serialization_alias="name")
    description: Optional[str] = Field(None, serialization_alias="description")
    address: Optional[str] = Field(None, serialization_alias="address")
    contact: Optional[str] = Field(None, serialization_alias="contact")


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

    service_type: str = Field(serialization_alias="serviceType")
    differentiator: Optional[str] = None


class Throughput(BaseModel):
    """
    A class representing the `Throughput` model.

    #### Public Attributes:
            guaranteed (float): the guaranteed throughput in kbps
            maximum (float): the maximum throughput in kbps
    """

    guaranteed: Optional[float] = None
    maximum: Optional[float] = None


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
    """
    A class representing the `Apps` model.

    #### Public Attributes:
            apps (List[str]): The enterprise app name (ID).
            os (str): The OSId identifier according to the OS you use (Android, iOS, etc.).
    """
    os: str
    apps: List[str]


class TrafficCategories(BaseModel):
    apps: Apps


class DeviceAttachment(BaseModel):
    device_phone_number: str
    attachment_id: str


def fetch_and_remove(slice_attachments: List[DeviceAttachment], device: Device):
    for i, attachment in enumerate(slice_attachments):
        if attachment.device_phone_number == device.phone_number:
            attachment_id = attachment.attachment_id
            del slice_attachments[i]
            return attachment_id
    return None


class Slice(BaseModel, arbitrary_types_allowed=True):
    """
    A class representing the `Slice` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.
        _attachments(List[DeviceAttachment]): List of device attachments

    #### Public Attributes:
        sid (optional): String ID of the slice
        state (str): State of the slice (ie. NOT_SUBMITTED)
        name (optional): Optional short name for the slice.
        Must be ASCII characters, digits and dash.
        Like name of an event, such as "Concert-2029-Big-Arena".
        network_identifier (NetworkIdentifier): Name of the network
        slice_info (SliceInfo): Purpose of this slice
        notification_url: Destination URL of notifications
        notification_auth_token: Authorization token for notifications
        area_of_service (AreaOfService): Location of the slice
        max_data_connections (optional): Optional maximum number of data
        connection sessions in the slice.
        max_devices (optional): Optional maximum number of devices using the slice.
        slice_downlink_throughput (optional): Optional throughput object
        slice_uplink_throughput (optional): Optional throughput object
        device_downlink_throughput (optional): Optional throughput object
        device_uplink_throughput: (optional): Optional throughput object


    #### Public Methods:
        activate (None): Activate a network slice.
        attach (): Attach a network slice to a device.
        deactivate (None): Deactivate a network slice.
        The slice state must be active to be able to perform this operation.
        delete (None): Delete network slice.
        The slice state must not be active to perform this operation.
        refresh (None): Refresh the state of the network slice.
        wait_for (str): Wait until a slice is no longer PENDING or until specified state is reached, returns state

    #### Callback Functions:
        on_creation ():
        on_event ():
    """

    _api: APIClient = PrivateAttr()
    _sessions: List[QoDSession] = PrivateAttr()
    sid: Optional[str] = None
    state: str
    name: str = Field(
        default = '',
        description="""Optional short name for the slice.
        Must be ASCII characters, digits and dash. 
        Like name of an event, such as "Concert-2029-Big-Arena".""",
        min_length=4,
        max_length=64,
        pattern="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$",
    )
    network_identifier: NetworkIdentifier
    slice_info: SliceInfo
    notification_url: str
    notification_auth_token: Optional[str] = None
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
        self._api.slicing.activate(self.name)

    def deactivate(self) -> None:
        """Deactivate network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.deactivate()
            ```
        """
        self._api.slicing.deactivate(self.name)

    def delete(self) -> None:
        """Delete network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.delete()
            ```
        """
        self._api.slicing.delete(self.name)

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

    async def wait_for(
            self,
            desired_state: Optional[str] = None,
            timeout: datetime.timedelta = datetime.timedelta(seconds=3600),
            poll_backoff: datetime.timedelta = datetime.timedelta(seconds=10)
    ) -> str:
        """Wait for an ongoing order to complete.
           I.e. not being in "PENDING" state.
           Returns new state.

        #### Args:
            desired_state (str): if not provided, the AVAILABLE state will be returned.
            timeout (datetime.timedelta): Timeout of waiting. Default is 1h.
            poll_backoff (datetime.timedelta): Backoff time between polling.

        #### Example:
            ```python
            new_state = slice.wait_for()
            ```
        """
        if not desired_state:
            desired_state = "AVAILABLE"

        poll_backoff_seconds = float(poll_backoff.total_seconds())
        end = datetime.datetime.now() + timeout
        while self.state != desired_state and datetime.datetime.now() < end:
            await asyncio.sleep(poll_backoff_seconds)
            self.refresh()
        return self.state

    def set_attachments(self, attachments):
        if len(attachments) > 0:
            self._attachments = [
                DeviceAttachment(
                    device_phone_number=attachment["resource"]["device"]["phoneNumber"],
                    attachment_id=attachment["nac_resource_id"],
                )
                for attachment in attachments
            ]

    def attach(
        self,
        device: Device,
        customer: Union[Customer, None] = None,
        traffic_categories: Union[TrafficCategories, None] = None,
        notification_url: Union[str, None] = None,
        notification_auth_token: Union[str, None] = None,
    ) -> None:
        """Attach network slice.

        #### Args:
            device (Device): Device object that the slice is being attached to
            customer (Customer): Customer who orders the device attach operations
            traffic_categories (TrafficCategories): It should contain the OSId, according to the OS and the OsAppId
            notification_url (str): Notification URL for attachment-related events.
            notification_auth_token (str): Authorization token for notification sending.

        #### Example:
            ```python
            device = client.devices.get("testuser@open5glab.net", 
            ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", 
            private_address="1.1.1.2", public_port=80), imsi=1223334444)
            slice.attach(device, customer = Customer(name="Joe Doe", description="B2B_5G_eMBB_Slice",
            address="123 Main Street, Anytown, USA 12345", contact="(555) 123-4567"),
            traffic_categories = TrafficCategories(
                apps=Apps(
                    os="97a498e3-fc92-5c94-8986-0333d06e4e47",
                    apps=["ENTERPRISE", "ENTERPRISE2"]
                )
            )
        )
            ```
        """

        new_attachment = self._api.slice_attach.attach(
            device,
            customer,
            self.name,
            traffic_categories,
            notification_url,
            notification_auth_token,
        ).json()

        assert isinstance(device.phone_number, str)

        self._attachments.append(
            DeviceAttachment(
                attachment_id=new_attachment["nac_resource_id"],
                device_phone_number=device.phone_number,
            )
        )

        return new_attachment

    def detach(
        self,
        device: Device,
    ) -> None:
        """Detach network slice.

        #### Args:
            device (Device): Device object that the slice is being attached to

        #### Example:
            ```python
            device = client.devices.get("testuser@open5glab.net", 
            ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", 
            private_address="1.1.1.2", public_port=80))
            slice.attach(device)
            slice.detach(device)
            ```
        """
        attachment_id = fetch_and_remove(self._attachments, device)

        if attachment_id:
            self._api.slice_attach.detach(attachment_id)
        else:
            raise NotFound("Attachment not found")

    @staticmethod
    def network_identifier_from_dict(network_identifier_dict: Optional[Dict[str, str]]):
        """Returns a `NetworkIdentifier` instance.

        Assigns the `mcc` and `mnc`.
        #### Args:
            network_identifier_dict (Dict[str, str]): A Network Identifier object with `mcc` and `mnc` values.
        """
        if network_identifier_dict:
            return NetworkIdentifier(
                mcc=network_identifier_dict["mcc"], mnc=network_identifier_dict["mnc"]
            )

    @staticmethod
    def slice_info_from_dict(slice_info_dict: Optional[Dict[str, str]]):
        """Returns a `SliceInfo` instance.

        Assigns the `service_type` and `differentiator`.
        #### Args:
            slice_info_dict (Dict[str, str]): A Slice Info object with `service_type` and `differentiator` values.
        """
        if slice_info_dict:
            return SliceInfo(
                service_type=str(slice_info_dict["serviceType"]),
                differentiator=slice_info_dict.get("differentiator"),
            )

    @staticmethod
    def area_of_service_from_dict(
        area_of_service_dict: Optional[Dict[str, List[Dict[str, float]]]]
    ) -> Optional[AreaOfService]:
        """Returns a `AreaOfService` instance.

        Assigns the `polygon`.
        #### Args:
            area_of_service_dict (Dict[str, List[Dict[str, float]]]): An Area Of Service object with polygon list value.
        """
        if area_of_service_dict:
            polygon = area_of_service_dict["polygon"]
            return AreaOfService(
                polygon=[
                    Point(latitude=polygon[0]["lat"], longitude=polygon[0]["lon"]),
                    Point(latitude=polygon[1]["lat"], longitude=polygon[1]["lon"]),
                    Point(latitude=polygon[2]["lat"], longitude=polygon[2]["lon"]),
                    Point(latitude=polygon[3]["lat"], longitude=polygon[3]["lon"]),
                ]
            )
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
