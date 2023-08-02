from typing import List, Optional
import math
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
            # network_identifier = NetworkIdentifier(mcc=network_id["mcc"], mnc=network_id["mnc"]),
            # slice_info = SliceInfo(service_type=slice_info["service_type"], differentiator=slice_info["differentiator"]), 
            # area_of_service = AreaOfService(poligon=area_of_service["poligon"]), 
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
                "networkIdentifier": network_id,
                "sliceInfo": slice_info,
                "areaOfService": area_of_service,
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
                body["sliceDownlinkThroughput"] = slice_downlink_throughput

            if slice_uplink_throughput:
                body["sliceUplinkThroughput"] = slice_uplink_throughput

            if device_uplink_throughput:
                body["deviceUplinkThroughput"] = device_uplink_throughput

            if device_downlink_throughput:
                body["deviceDownlinkThroughput"] = device_downlink_throughput

            slice_data = self.api.slice.create_slice(body)
            # slice_data = self.api.slice.create_slice({"notificationUrl": "", "networkIdentifier": {"mcc": "000aaFFF", "mnc": "000eeGGG"}, "areaOfService": {"poligon": [{"lat": 0, "lon": 0},{"lat": 0, "lon": 0},{"lat": 0, "lon": 0},{"lat": 0, "lon": 0}]}, "sliceInfo": {"service_type": "eMBB","differentiator": "44eab5"} })
            slice.sid = slice_data.csi_id
            slice.state = slice_data.state
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

    def get(self, id: str) -> Slice | None:
        """Get network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            fetched_slice = nac_client.slices.get(id)
            ```
        """
        slice_data = self.api.slice.get_slice(id)

        slice = Slice(
            api=self.api, 
            sid = slice_data.csi_id,
            state = slice_data.state,
            name = slice_data.slice.name, 
            networkIdentifier = slice_data.slice.network_id,
            sliceInfo = slice_data.slice.slice_info, 
            areaOfService = slice_data.slice.area_of_service, 
            maxDataConnections = slice_data.slice.max_data_connections,
            maxDevices = slice_data.slice.max_devices,
            sliceDownlinkThroughput = slice_data.slice.slice_downlink_throughput, 
            slice_uplink_throughput = slice_data.slice.slice_uplink_throughput,
            device_downlink_throughput = slice_data.slice.device_downlink_throughput,
            device_uplink_throughput = slice_data.slice.device_uplink_throughput
        )

        return slice

