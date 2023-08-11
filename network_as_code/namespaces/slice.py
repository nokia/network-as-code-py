import json
from typing import List, Optional, Union
import math

from httpx import Response

from . import Namespace
from ..models import Slice
from ..errors import NotFound, AuthenticationException, ServiceError, InvalidParameter
from urllib.error import HTTPError
from pydantic import ValidationError
from slice_client.model.throughput import Throughput
from slice_client.model.slice_data import SliceData
from slice_client.model.network_identifier import NetworkIdentifier
from slice_client.model.slice_info import SliceInfo
from slice_client.model.area_of_service import AreaOfService
from slice_client.model.point import Point


class Slices(Namespace):
    """Representation of a 5G network slice.

    Through this class many of the parameters of a
    network slice can be configured and managed.
    """

    def create(self,
               network_id: NetworkIdentifier, 
               slice_info: SliceInfo, 
               area_of_service: AreaOfService, 
               notification_url: str,
               name: Optional[str] = None,
               notification_auth_token: Optional[str] = None,
               slice_downlink_throughput: Optional[Throughput] = Throughput(guaranteed=0, maximum=0), 
               slice_uplink_throughput: Optional[Throughput] = Throughput(guaranteed=0, maximum=0),
               device_downlink_throughput: Optional[Throughput] = Throughput(guaranteed=0, maximum=0),
               device_uplink_throughput: Optional[Throughput] = Throughput(guaranteed=0, maximum=0),
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
            maxDataConnections = max_data_connections,
            maxDevices = max_devices,
            sliceDownlinkThroughput = slice_downlink_throughput, 
            slice_uplink_throughput = slice_uplink_throughput,
            device_downlink_throughput = device_downlink_throughput,
            device_uplink_throughput = device_uplink_throughput
        )

        # Error Case: Creating Slice
        try:
            body = {
                "networkIdentifier": dict(network_id),
                "sliceInfo": self.convert_slice_info_obj(slice_info),
                "areaOfService": self.convert_area_of_service_obj(area_of_service),
                "notificationUrl": notification_url,
            }

            if name:
                body["name"] = name

            if notification_auth_token:
                body["notificationAuthToken"] = notification_auth_token

            if max_data_connections:
                body["maxDataConnections"] = max_data_connections 

            if max_devices:
                body["maxDevices"] = max_devices

            if slice_downlink_throughput:
                body["sliceDownlinkThroughput"] = self.convert_throughput_obj(slice_downlink_throughput)

            if slice_uplink_throughput:
                body["sliceUplinkThroughput"] = self.convert_throughput_obj(slice_uplink_throughput)

            if device_uplink_throughput:
                body["deviceUplinkThroughput"] = self.convert_throughput_obj(device_uplink_throughput)

            if device_downlink_throughput:
                body["deviceDownlinkThroughput"] = self.convert_throughput_obj(device_downlink_throughput)
            
            slice_data = self.api.slice_new.create(json.dumps(body))
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
        slice_data = self.api.slice_new.get(id).json()
        slice = Slice(
            api=self.api,
            sid=slice_data['csi_id'],
            state = slice_data['state'],
            name = slice_data['slice']['name'], 
            network_identifier = Slice.network_identifier(slice_data['slice']['networkIdentifier']),
            slice_info = Slice.slice_info(slice_data['slice']['sliceInfo']), 
            area_of_service = Slice.area_of_service(slice_data['slice']['areaOfService']), 
            maxDataConnections = slice_data['slice']['maxDataConnections'],
            maxDevices = slice_data['slice']['maxDevices'], 
            sliceDownlinkThroughput = Slice.throughput(slice_data['slice']['sliceDownlinkThroughput']), 
            slice_uplink_throughput = Slice.throughput(slice_data['slice']['sliceUplinkThroughput']),
            device_downlink_throughput = Slice.throughput(slice_data['slice']['deviceDownlinkThroughput']),
            device_uplink_throughput = Slice.throughput(slice_data['slice']['deviceUplinkThroughput'])
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
        slice_data = self.api.slice_new.getAll()

        slices = [Slice(
            api=self.api,
            sid=slice['csi_id'],
            state = slice['state'],
            name = slice['slice']['name'], 
            network_identifier = Slice.network_identifier(slice['slice']['networkIdentifier']),
            slice_info = Slice.slice_info(slice['slice']['sliceInfo']), 
            area_of_service = Slice.area_of_service(slice['slice']['areaOfService']), 
            maxDataConnections = slice['slice']['maxDataConnections'],
            maxDevices = slice['slice']['maxDevices'],
            sliceDownlinkThroughput = Slice.throughput(slice['slice']['sliceDownlinkThroughput']), 
            slice_uplink_throughput = Slice.throughput(slice['slice']['sliceUplinkThroughput']),
            device_downlink_throughput = Slice.throughput(slice['slice']['deviceDownlinkThroughput']),
            device_uplink_throughput = Slice.throughput(slice['slice']['deviceUplinkThroughput'])
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

        return self.api.slice_new.activate(slice_id=slice_id)
    
    def deactivate(self, slice_id: str) -> Response:
        """Activate a slice by id.

        #### Args:
            slice_id

        #### Example:
            ```python
            nac_client.slices.deactivate(slice_id=1)
            ```
        """

        return self.api.slice_new.deactivate(slice_id=slice_id)
    
    def delete(self, slice_id: str) -> Response:
        """Activate a slice by id.

        #### Args:
            slice_id

        #### Example:
            ```python
            nac_client.slices.activate(slice_id=1)
            ```
        """

        return self.api.slice_new.delete(slice_id=slice_id)
    

    def convert_area_of_service_obj(self, areaOfService: AreaOfService):
        return {aosK:list({k: float(v) for k, v in dict(x).items()} for x in aosV) for aosK, aosV in dict(areaOfService).items()}
    
    def convert_slice_info_obj(self, sliceInfo: SliceInfo):
        return {k: str(v) for k, v in dict(sliceInfo).items()}
    
    def convert_throughput_obj(self, throughput: Throughput):
        return {k: float(v) for k, v in throughput.items()}