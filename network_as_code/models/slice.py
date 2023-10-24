from os import access
from urllib.error import HTTPError
from pydantic import BaseModel, EmailStr, PrivateAttr, Field, ValidationError
from typing import Dict, List, Union, Optional
from enum import Enum

from ..api import APIClient
from ..models.session import Session
from ..models.location import CivicAddress, Location
from ..models.device import Device
from ..errors import NotFound, InvalidParameter, NotFound, AuthenticationException, ServiceError, error_handler

class NetworkIdentifier(BaseModel):
    mnc: str
    mcc: str

class SliceInfo(BaseModel):
    service_type: str
    differentiator: Optional[str]

class Throughput(BaseModel):
    guaranteed: int
    maximum: int

class Point(BaseModel):
    longitude: Union[float, int] = Field(serialization_alias="lon")
    latitude: Union[float, int] = Field(serialization_alias="lat")

class AreaOfService(BaseModel):
    poligon: List[Point]


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
        
    #### Callback Functions:
        on_creation ():
        on_event ():

    """

    _api: APIClient = PrivateAttr()
    _sessions: List[Session] = PrivateAttr()
    sid: Optional[str]
    state: str
    name: Optional[str] = Field(None, description='Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".')
    network_identifier: NetworkIdentifier
    slice_info: SliceInfo
    area_of_service: AreaOfService
    max_data_connections: Optional[int] = Field(None, description="Maximum number of data connection sessions in the slice.", ge=0)
    max_devices: Optional[int] = Field(None, description="Maximum number of devices using the slice.", ge=0)
    slice_downlink_throughput: Optional[Throughput] = None
    slice_uplink_throughput: Optional[Throughput] = None
    device_downlink_throughput: Optional[Throughput] = None
    device_uplink_throughput: Optional[Throughput] = None


    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []

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
            self._api.slice.activate(self.name)
    
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
            self._api.slice.deactivate(self.name)
    
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
            self._api.slice.delete(self.name)

    def refresh(self) -> None:
        """Refresh state of the network slice.

        #### Args:
            None

        #### Example:
            ```python
            slice.refresh()
            ```
        """
        try:
            if self.name:
                slice_data = self._api.slice.get(self.name)
                self.state = slice_data.state
        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise NotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)
    
    def attach(self, device: Device, notification_url: str, notification_auth_token: Optional[str] = None) -> None:
        """Attach network slice.

        #### Args:
            device (Device): Device object that the slice is being attached to

        #### Example:
            ```python
            device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
            slice.attach(device)
            ```
        """
        # TMO Customization: Omitted attach_slice() API call to simulate attaching a slice with a no-op
        # self._api.slice_attach.attach(device, self.name, notification_url, notification_auth_token)

    def detach(self, device: Device, notification_url: str, notification_auth_token: Optional[str] = None) -> None:
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
        self._api.slice_attach.detach(device, self.name, notification_url, notification_auth_token)


    @staticmethod
    def network_identifier(networkIdentifierDict: Dict[str, str]):
        return NetworkIdentifier(mcc=networkIdentifierDict['mcc'], mnc=networkIdentifierDict['mnc'])
    
    @staticmethod
    def slice_info(sliceInfoDict: Dict[str, str]):
        return SliceInfo(service_type=sliceInfoDict['service_type'], differentiator=sliceInfoDict['differentiator'])
    
    @staticmethod
    def area_of_service(areaOfServiceDict: Dict[str, List[Dict[str, int]]]):
        poligon = areaOfServiceDict['poligon']
        return AreaOfService(poligon=[Point(latitude=poligon[0]['lat'], longitude=poligon[0]['lon']), Point(latitude=poligon[1]['lat'], longitude=poligon[1]['lon']), Point(latitude=poligon[2]['lat'], longitude=poligon[2]['lon']), Point(latitude=poligon[3]['lat'], longitude=poligon[3]['lon'])]), 

    @staticmethod
    def throughput(throughputdict: Optional[Dict[int, int]]):
        if throughputdict:
            return Throughput(guaranteed=throughputdict['guaranteed'], maximum=throughputdict['maximum'])
        else:
            return None
