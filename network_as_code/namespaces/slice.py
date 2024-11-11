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

from typing import List, Optional, Union

from . import Namespace
from ..models.slice import (
    Slice,
    NetworkIdentifier,
    SliceInfo,
    Throughput,
    AreaOfService,
)
from ..api import Throughput as ApiThroughput


class Slices(Namespace):
    """Representation of a 5G network slice.

    Through this class many of the parameters of a
    network slice can be configured and managed.
    """

    def _to_api_throughput(self, throughput: Optional[Throughput]) -> Optional[ApiThroughput]:
        if throughput is None:
            return None
        return ApiThroughput(guaranteed=throughput.guaranteed, maximum=throughput.maximum)

    def create(
        self,
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
        max_devices: Optional[int] = None,
    ) -> Slice:
        """Create a slice with its network identifier, slice info, area of service, and notification url.

        #### Args:
            network_id (NetworkIdentifier): Name of the network
            slice_info (SliceInfo): Purpose of this slice
            notification_url (str): Destination URL of notifications
            area_of_service (AreaOfService): Location of the slice
            slice_downlink_throughput (optional): Optional throughput object
            slice_uplink_throughput (optional): Optional throughput object
            device_downlink_throughput (optional): Optional throughput object
            device_uplink_throughput: (optional): Optional throughput object
            notification_auth_token: (optional): Authorization token for notification sending.
            name (optional): Optional short name for the slice. 
            Must be ASCII characters, digits and dash. 
            Like name of an event, such as "Concert-2029-Big-Arena".
            max_data_connections (optional): Optional maximum number of data connection sessions in the slice.
            max_devices (optional): Optional maximum number of devices using the slice.

        #### Example:
        ```python
        from network_as_code.models.slice import NetworkIdentifier, SliceInfo, AreaOfService, Point

        network_id = NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE")
        slice_info = SliceInfo(service_type="eMBB", differentiator="44eab5")
        area_of_service = AreaOfService(poligon=[Point(lat=47.344, lon=104.349), 
        Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)])
        notification_url = "https://notify.me/here"

        new_slice = nac_client.slices.create(
            network_id = network_id,
            slice_info = slice_info,
            area_of_service = area_of_service,
            notification_url = notification_url
        )
        ```

        """

        new_slice = Slice(
            api=self.api,
            sid=None,
            state="NOT_SUBMITTED",
            name=name,
            network_identifier=network_id,
            slice_info=slice_info,
            notification_url=notification_url,
            notification_auth_token=notification_auth_token,
            area_of_service=area_of_service,
            max_data_connections=max_data_connections,
            max_devices=max_devices,
            slice_downlink_throughput=slice_downlink_throughput,
            slice_uplink_throughput=slice_uplink_throughput,
            device_downlink_throughput=device_downlink_throughput,
            device_uplink_throughput=device_uplink_throughput,
        )

        slice_data = self.api.slicing.create(
            network_id=network_id,
            slice_info=slice_info,
            notification_url=notification_url,
            area_of_service=area_of_service,
            name=name,
            notification_auth_token=notification_auth_token,
            slice_downlink_throughput=self._to_api_throughput(slice_downlink_throughput),
            slice_uplink_throughput=self._to_api_throughput(slice_uplink_throughput),
            device_downlink_throughput=self._to_api_throughput(device_downlink_throughput),
            device_uplink_throughput=self._to_api_throughput(device_uplink_throughput),
            max_data_connections=max_data_connections,
            max_devices=max_devices,
        )
        new_slice.sid = slice_data.json().get("csi_id")
        new_slice.state = slice_data.json()["state"]

        return new_slice

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
        existing_slice = Slice(
            api=self.api,
            sid=slice_data.get("csi_id"),
            state=slice_data["state"],
            name=slice_data["slice"]["name"],
            network_identifier=Slice.network_identifier_from_dict(
                slice_data["slice"]["networkIdentifier"]
            ),
            notification_url=slice_data["slice"]["notificationUrl"],
            slice_info=Slice.slice_info_from_dict(slice_data["slice"]["sliceInfo"]),
            area_of_service=Slice.area_of_service_from_dict(
                slice_data["slice"].get("areaOfService")
            ),
            max_data_connections=slice_data["slice"].get("maxDataConnections"),
            max_devices=slice_data["slice"].get("maxDevices"),
            slice_downlink_throughput=Slice.throughput(
                slice_data["slice"].get("sliceDownlinkThroughput")
            ),
            slice_uplink_throughput=Slice.throughput(
                slice_data["slice"].get("sliceUplinkThroughput")
            ),
            device_downlink_throughput=Slice.throughput(
                slice_data["slice"].get("deviceDownlinkThroughput")
            ),
            device_uplink_throughput=Slice.throughput(
                slice_data["slice"].get("deviceUplinkThroughput")
            ),
        )

        attachments = self.api.slice_attach.get_attachments().json()

        slice_attachments = [
            attachment
            for attachment in attachments
            if attachment["resource"]["sliceId"] == existing_slice.name
        ]

        existing_slice.set_attachments(slice_attachments)

        return existing_slice

    def get_all(self) -> List[Slice]:
        """Get All slices by id.

        #### Args:
            None

        #### Example:
            ```python
            fetched_slices = nac_client.slices.get_all()
            ```
        """
        slice_data = self.api.slicing.get_all()

        slices = [self._convert_to_slice_model(slice_json) for slice_json in slice_data.json()]

        return slices

    def get_attachment(self, id: str) -> None:
        """Get Application Attachment Instance

        #### Args:
            id (str): Application Attachment Id

        #### Example:
            ```python
            attachment = nac_client.slices.get_attachment(id)
            ```
        """
        return self.api.slice_attach.get(id).json()

    def get_all_attachments(self) -> None:
        """Get All Application Attachments

        #### Args:
            None

        #### Example:
            ```python
            nac_client.slices.get_all_attachments()
            ```
        """
        return self.api.slice_attach.get_attachments().json()

    def _convert_to_slice_model(self, slice_json):
        slice_instance = Slice(
            api=self.api,
            state=slice_json["state"],
            name=slice_json["slice"]["name"],
            sid=slice_json.get("csi_id"),
            network_identifier=Slice.network_identifier_from_dict(
                slice_json["slice"]["networkIdentifier"]
            ),
            slice_info=Slice.slice_info_from_dict(slice_json["slice"]["sliceInfo"]),
            notification_url=slice_json["slice"]["notificationUrl"],
            area_of_service=Slice.area_of_service_from_dict(
                slice_json["slice"].get("areaOfService")
            ),
            max_data_connections=slice_json["slice"].get("maxDataConnections"),
            max_devices=slice_json["slice"].get("maxDevices"),
            slice_downlink_throughput=Slice.throughput(
                slice_json["slice"].get("sliceDownlinkThroughput")
            ),
            slice_uplink_throughput=Slice.throughput(
                slice_json["slice"].get("sliceUplinkThroughput")
            ),
            device_downlink_throughput=Slice.throughput(
                slice_json["slice"].get("deviceDownlinkThroughput")
            ),
            device_uplink_throughput=Slice.throughput(
                slice_json["slice"].get("deviceUplinkThroughput")
            ),
        )

        attachments = self.api.slice_attach.get_attachments().json()

        slice_attachments = [
            attachment
            for attachment in attachments
            if attachment["resource"]["sliceId"] == slice_instance.name
        ]

        slice_instance.set_attachments(slice_attachments)

        return slice_instance
