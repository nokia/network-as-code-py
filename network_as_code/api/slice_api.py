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

import pdb
from typing import Union
import json
import os
import httpx

from typing import Optional, Any
from pydantic import BaseModel

from ..errors import error_handler



class Throughput(BaseModel):
    """
    A class representing the `Throughput` API field.

    #### Public Attributes:
            guaranteed (float): the guaranteed throughput in kbps
            maximum (float): the maximum throughput in kbps
    """

    guaranteed: Optional[float]
    maximum: Optional[float]


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
            "sliceInfo": self.convert_slice_info_obj(slice_info),
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
            body["sliceDownlinkThroughput"] = self.convert_throughput_obj(
                slice_downlink_throughput
            )

        if slice_uplink_throughput:
            body["sliceUplinkThroughput"] = self.convert_throughput_obj(
                slice_uplink_throughput
            )

        if device_uplink_throughput:
            body["deviceUplinkThroughput"] = self.convert_throughput_obj(
                device_uplink_throughput
            )

        if device_downlink_throughput:
            body["deviceDownlinkThroughput"] = self.convert_throughput_obj(
                device_downlink_throughput
            )

        if modify:
            if name is None:
                raise ValueError('Name is mandatory for modify')
            response = self.client.put(url=f"/slices/{name}", json=body)
        else:
            response = self.client.post(url="/slices", json=body)

        error_handler(response)

        return response

    def getAll(self):
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

    def convert_area_of_service_obj(self, areaOfService):
        polygons = []

        for point in areaOfService.polygon:
            polygons.append({"lat": point.latitude, "lon": point.longitude})

        return {"polygon": polygons}

    def convert_slice_info_obj(self, slice_info):
        return { "serviceType": slice_info.service_type, "differentiator": slice_info.differentiator}

    def convert_throughput_obj(self, throughput: Throughput):
        return {k: float(v) for k, v in dict(throughput).items()}


def delete_none(_dict):
    """Delete None values recursively from all of the dictionaries"""
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    delete_none(v_i)

    return _dict


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
        traffic_categories: Union[any, None]
    ):
        
        payload = {
                "device": {
                        "phoneNumber": device.phone_number,
                        "networkAccessIdentifier": device.network_access_identifier,
                        "ipv4Address": {
                            "publicAddress": device.ipv4_address.public_address,
                            "privateAddress": device.ipv4_address.private_address,
                            "publicPort": device.ipv4_address.public_port,
                        },
                        "ipv6Address": device.ipv6_address
                    },
                    "sliceID": slice_id,
        }

        if traffic_categories:
            payload['osId'] = traffic_categories.apps.os
            payload['appIds'] = traffic_categories.apps.apps
        
        
        res = self.client.post(
            url=f"/attachments",
            json=delete_none(payload),
        )
        error_handler(res)
        return res
        

    def detach(self, id):
        res = self.client.delete(
            url=f"/attachments/{id}"
        )
        error_handler(res)
