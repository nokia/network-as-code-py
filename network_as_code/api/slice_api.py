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

from typing import Union, Optional, Any
import httpx

from pydantic import BaseModel

from ..errors import error_handler
from .utils import delete_none


class Throughput(BaseModel):
    """
    A class representing the `Throughput` API field.

    #### Public Attributes:
            guaranteed (float): the guaranteed throughput in kbps
            maximum (float): the maximum throughput in kbps
    """

    guaranteed: Optional[float] = None
    maximum: Optional[float] = None


class SliceAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.client = httpx.Client(
            base_url=base_url,
            headers={
                "content-type": "application/json",
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": rapid_host,
            },
        )

    def create(
        self,
        network_id,
        slice_info,
        notification_url,
        modify: bool = False,
        name: Optional[str] = None,
        notification_auth_token: Optional[str] = None,
        area_of_service: Optional[Any] = None,
        slice_downlink_throughput: Optional[Throughput] = None,
        slice_uplink_throughput: Optional[Throughput] = None,
        device_downlink_throughput: Optional[Throughput] = None,
        device_uplink_throughput: Optional[Throughput] = None,
        max_data_connections: Optional[int] = None,
        max_devices: Optional[int] = None,
    ):
        body = {
            "networkIdentifier": dict(network_id),
            "sliceInfo": slice_info.model_dump(mode='json', by_alias=True, exclude_none=True),
            "notificationUrl": notification_url,
        }

        if name:
            body["name"] = name

        if area_of_service:
            body["areaOfService"] = self.convert_area_of_service_obj(area_of_service)

        if notification_auth_token:
            body["notificationAuthToken"] = notification_auth_token

        if max_data_connections:
            body["maxDataConnections"] = max_data_connections

        if max_devices:
            body["maxDevices"] = max_devices

        if slice_downlink_throughput:
            body["sliceDownlinkThroughput"] = slice_downlink_throughput.model_dump(mode='json')

        if slice_uplink_throughput:
            body["sliceUplinkThroughput"] = slice_uplink_throughput.model_dump(mode='json')

        if device_uplink_throughput:
            body["deviceUplinkThroughput"] = device_uplink_throughput.model_dump(mode='json')

        if device_downlink_throughput:
            body["deviceDownlinkThroughput"] = device_downlink_throughput.model_dump(mode='json')

        if modify:
            if name is None:
                raise ValueError("Name is mandatory for modify")
            response = self.client.put(url=f"/slices/{name}", json=body)
        else:
            response = self.client.post(url="/slices", json=body)

        error_handler(response)

        return response

    def get_all(self):
        res = self.client.get(
            url="/slices",
        )

        error_handler(res)

        return res

    def get(self, slice_id: str):
        res = self.client.get(
            url=f"/slices/{slice_id}",
        )

        error_handler(res)

        return res

    def activate(self, slice_id: str):
        res = self.client.post(
            url=f"/slices/{slice_id}/activate",
        )

        error_handler(res)

        return res

    def deactivate(self, slice_id: str):
        return self.client.post(
            url=f"/slices/{slice_id}/deactivate",
        )

    def delete(self, slice_id: str):
        res = self.client.delete(
            url=f"/slices/{slice_id}",
        )

        error_handler(res)

        return res

    def convert_area_of_service_obj(self, area_of_service):
        polygons = []

        for point in area_of_service.polygon:
            polygons.append({"lat": point.latitude, "lon": point.longitude})

        return {"polygon": polygons}


class AttachAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.client = httpx.Client(
            base_url=base_url,
            headers={"X-RapidAPI-Key": rapid_key, "X-RapidAPI-Host": rapid_host},
        )

    def attach(
        self,
        device,
        slice_id: str,
        traffic_categories: Union[any, None],
        notification_url: Union[str, None],
        notification_auth_token: str,
    ):
        payload = {
            "device": {
                "phoneNumber": device.phone_number,
                "ipv4Address": {
                    "publicAddress": device.ipv4_address.public_address,
                    "privateAddress": device.ipv4_address.private_address,
                    "publicPort": device.ipv4_address.public_port,
                },
                "ipv6Address": device.ipv6_address,
            },
            "sliceId": slice_id,
            "traffic_categories": {"apps": traffic_categories.apps.__dict__},
            "webhook": {
                "notificationUrl": notification_url,
                "notificationAuthToken": notification_auth_token,
            },
        }

        res = self.client.post(
            url="/attachments",
            json=delete_none(payload),
        )

        error_handler(res)
        return res

    def get_attachments(self):
        res = self.client.get(url="/attachments")

        error_handler(res)

        return res

    def get(self, id: str):
        res = self.client.get(
            url=f"/attachments/{id}",
        )

        error_handler(res)

        return res

    def detach(self, id):
        res = self.client.delete(url=f"/attachments/{id}")
        error_handler(res)
