from os import access
from urllib.error import HTTPError
from pydantic import BaseModel, EmailStr, PrivateAttr, Field, ValidationError
from typing import List, Union, Optional
from enum import Enum

from slice_client.model.throughput import Throughput
from slice_client.model.slice_data import SliceData
from slice_client.model.network_identifier import NetworkIdentifier
from slice_client.model.slice_info import SliceInfo
from slice_client.model.area_of_service import AreaOfService
from slice_client.model.point import Point

from ..api import APIClient
from ..models.session import Session
from ..models.location import CivicAddress, Location
from ..models.device import Device
from ..errors import NotFound, InvalidParameter, NotFound, AuthenticationException, ServiceError, error_handler


class Slice(BaseModel, arbitrary_types_allowed=True):
    """
    A class representing the `Slice` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.

    #### Public Attributes:
        name (optional): Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".
        networkIdentifier (NetworkIdentifier): Name of the network
        sliceInfo (SliceInfo): Purpose of this slice
        areaOfService (AreaOfService): Location of the slice
        maxDataConnections (optional): Optional maximum number of data connection sessions in the slice.
        maxDevices (optional): Optional maximum number of devices using the slice.
        sliceDownlinkThroughput (optional): 
        sliceUplinkThroughput (optional):
        deviceDownlinkThroughput (optional):
        deviceUplinkThroughput: (optional):


    #### Public Methods:
        get (SliceData | None): Get network slice data.
        activate (None): Activate a network slice.
        attach (): Attach a network slice to a device.
        deactivate (None): Deactivate a network slice. The slice state must be active to be able to perform this operation.
        delete (None): Delete network slice. The slice state must not be active to perform this operation.

    #### Callback Functions:
        on_creation ():
        on_event ():

    """

    _api: APIClient = PrivateAttr()
    _sessions: List[Session] = PrivateAttr()
    id: Optional[str]
    state: str
    name: Optional[str] = Field(None, description='Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".',
                                min_length=8, max_length=64, regex="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$")
    network_identifier: NetworkIdentifier
    slice_info: SliceInfo
    area_of_service: AreaOfService
    max_data_connections: Optional[int] = Field(None, description="Maximum number of data connection sessions in the slice.", ge=0)
    max_devices: Optional[int] = Field(None, description="Maximum number of devices using the slice.", ge=0)
    slice_downlink_throughput: Optional[Throughput]
    slice_uplink_throughput: Optional[Throughput]
    device_downlink_throughput: Optional[Throughput]
    device_uplink_throughput: Optional[Throughput]


    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []

    def activate(self) -> None:
        """Activate network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            slice_data.slice.activate(id)
            ```
        """
        self._api.slice.activate_slice(self.id)
    
    def deactivate(self) -> None:
        """Deactivate network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            slice_data.slice.deactivate(id)
            ```
        """
        self._api.slice.deactivate_slice(self.id)
    
    def delete(self) -> None:
        """Delete network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            slice_data.slice.delete(id)
            ```
        """
        self._api.slice.delete_slice(self.id)

    def refresh(self) -> None:
        try:
            slice_data = self._api.slice.get_slice(self.id)

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
