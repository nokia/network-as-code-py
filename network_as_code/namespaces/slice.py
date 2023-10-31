import json
from typing import List, Optional, Union
import math

from httpx import Response

from . import Namespace
from ..models.slice import Slice, NetworkIdentifier, SliceInfo, Throughput, AreaOfService
from ..errors import NotFound, AuthenticationException, ServiceError, InvalidParameter
from urllib.error import HTTPError
from pydantic import ValidationError

class Slices(Namespace):
    """Representation of a 5G network slice.

    Through this class many of the parameters of a
    network slice can be configured and managed.
    """

    def create(self,
               network_id: NetworkIdentifier, 
               slice_info: SliceInfo, 
               notification_url: str,
               area_of_service: Optional[AreaOfService] = None, 
               name: Optional[str] = None,
               notification_auth_token: Optional[str] = None,
               slice_downlink_throughput: Optional[Throughput] = None, 
               slice_uplink_throughput: Optional[Throughput] = None,
               device_downlink_throughput: Optional[Throughput] = None,
               device_uplink_throughput: Optional[Throughput] = None,
               max_data_connections: Optional[int] = None,
               max_devices: Optional[int] = None
               ) -> Slice:
        """Create a slice with its network identifier, slice info, area of service, and notification url.

        #### Args:
            network_id (NetworkIdentifier): Name of the network
            slice_info (SliceInfo): Purpose of this slice
            area_of_service (AreaOfService): Location of the slice
            slice_downlink_throughput (optional): Optional throughput object
            slice_uplink_throughput (optional): Optional throughput object
            device_downlink_throughput (optional): Optional throughput object
            device_uplink_throughput: (optional): Optional throughput object
            name (optional): Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".
            max_data_connections (optional): Optional maximum number of data connection sessions in the slice.
            max_devices (optional): Optional maximum number of devices using the slice.

        #### Example:
        ```python
        from network_as_code.models.slice import NetworkIdentifier, SliceInfo, AreaOfService, Point
        
        network_id = NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE")
        slice_info = SliceInfo(service_type="eMBB", differentiator="44eab5")
        area_of_service = AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)])
        notification_url = "https://notify.me/here"

        new_slice = nac_client.slices.create(
            network_id = network_id,
            slice_info = slice_info,
            area_of_service = area_of_service,
            notification_url = notification_url
        )
        ```

        """

        slice = Slice(
            api=self.api, 
            sid = None,
            state = "NOT_SUBMITTED",
            name = name, 
            network_identifier = network_id,
            slice_info = slice_info,
            area_of_service = area_of_service,
            max_data_connections = max_data_connections,
            max_devices = max_devices,
            slice_downlink_throughput = slice_downlink_throughput, 
            slice_uplink_throughput = slice_uplink_throughput,
            device_downlink_throughput = device_downlink_throughput,
            device_uplink_throughput = device_uplink_throughput
        )

        # Error Case: Creating Slice
        try:
            slice_data = self.api.slicing.create(
                network_id=network_id,
                slice_info=slice_info,
                notification_url=notification_url,
                area_of_service=area_of_service,
                name=name,
                notification_auth_token=notification_auth_token,
                slice_downlink_throughput=slice_downlink_throughput,
                slice_uplink_throughput=slice_uplink_throughput,
                device_downlink_throughput=device_downlink_throughput,
                device_uplink_throughput=device_uplink_throughput,
                max_data_connections=max_data_connections,
                max_devices=max_devices
            )
            slice.sid = slice_data.json()['csi_id']
            slice.state = slice_data.json()['state']
        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise NotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)
        
        return slice

    def get(self, id: str) -> Union[Slice, None]:
        """Get network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            fetched_slice = nac_client.slices.get(id)
            ```
        """
        slice_data = self.api.slicing.get(id).json()
        slice = Slice(
            api=self.api,
            sid=slice_data['csi_id'],
            state = slice_data['state'],
            name = slice_data['slice']['name'], 
            network_identifier = Slice.network_identifier(slice_data['slice']['networkIdentifier']),
            slice_info = Slice.slice_info(slice_data['slice']['sliceInfo']), 
            area_of_service = Slice.area_of_service(slice_data['slice'].get('areaOfService')), 
            max_data_connections = slice_data['slice'].get('maxDataConnections'),
            max_devices = slice_data['slice'].get('maxDevices'), 
            slice_downlink_throughput = Slice.throughput(slice_data['slice'].get('sliceDownlinkThroughput')), 
            slice_uplink_throughput = Slice.throughput(slice_data['slice'].get('sliceUplinkThroughput')),
            device_downlink_throughput = Slice.throughput(slice_data['slice'].get('deviceDownlinkThroughput')),
            device_uplink_throughput = Slice.throughput(slice_data['slice'].get('deviceUplinkThroughput'))
        )

        return slice

    def getAll(self) -> List[Slice]:
        """Get All slices by id.

        #### Args:
            None

        #### Example:
            ```python
            fetched_slices = nac_client.slices.getAll()
            ```
        """
        slice_data = self.api.slicing.getAll()

        slices = [Slice(
            api=self.api,
            state = slice['state'],
            name = slice['slice']['name'], 
            network_identifier = Slice.network_identifier(slice['slice']['networkIdentifier']),
            slice_info = Slice.slice_info(slice['slice']['sliceInfo']), 
            area_of_service = Slice.area_of_service(slice['slice'].get('areaOfService')), 
            max_data_connections = slice['slice'].get('maxDataConnections'),
            max_devices = slice['slice'].get('maxDevices'),
            slice_downlink_throughput = Slice.throughput(slice['slice'].get('sliceDownlinkThroughput')), 
            slice_uplink_throughput = Slice.throughput(slice['slice'].get('sliceUplinkThroughput')),
            device_downlink_throughput = Slice.throughput(slice['slice'].get('deviceDownlinkThroughput')),
            device_uplink_throughput = Slice.throughput(slice['slice'].get('deviceUplinkThroughput'))
        ) for slice in slice_data.json()]
        
        return slices
    
    def activate(self, slice_id: str) -> Response:
        """Activate a slice by id.

        #### Args:
            slice_id

        #### Example:
            ```python
            nac_client.slices.activate(slice_id=1)
            ```
        """

        return self.api.slicing.activate(slice_id=slice_id)
    
    def deactivate(self, slice_id: str) -> Response:
        """Activate a slice by id.

        #### Args:
            slice_id

        #### Example:
            ```python
            nac_client.slices.deactivate(slice_id=1)
            ```
        """

        return self.api.slicing.deactivate(slice_id=slice_id)
    
    def delete(self, slice_id: str) -> Response:
        """Activate a slice by id.

        #### Args:
            slice_id

        #### Example:
            ```python
            nac_client.slices.activate(slice_id=1)
            ```
        """

        return self.api.slicing.delete(slice_id=slice_id)
