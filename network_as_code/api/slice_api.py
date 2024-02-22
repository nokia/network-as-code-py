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

import json
import os
import pdb
import httpx

from typing import Optional

from ..errors import error_handler


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
        name: Optional[str] = None,
        notification_auth_token: Optional[str] = None,
        area_of_service: Optional[any] = None,
        slice_downlink_throughput: Optional[any] = None,
        slice_uplink_throughput: Optional[any] = None,
        device_downlink_throughput: Optional[any] = None,
        device_uplink_throughput: Optional[any] = None,
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

    def convert_slice_info_obj(self, sliceInfo):
        return {k: str(v) for k, v in dict(sliceInfo).items()}

    def convert_throughput_obj(self, throughput):
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
        notification_url: str,
        notification_auth_token: Optional[str] = None,
    ):
        res = self.client.post(
            url=f"/slice/{slice_id}/attach",
            json=delete_none(
                {
                    "phoneNumber": device.phone_number,
                    "notificationUrl": notification_url,
                    "notificationAuthToken": notification_auth_token,
                }
            ),
        )

        error_handler(res)

    def detach(
        self,
        device,
        slice_id: str,
        notification_url: str,
        notification_auth_token: Optional[str] = None,
    ):
        res = self.client.post(
            url=f"/slice/{slice_id}/detach",
            json=delete_none(
                {
                    "phoneNumber": device.phone_number,
                    "notificationUrl": notification_url,
                    "notificationAuthToken": notification_auth_token,
                }
            ),
        )

        error_handler(res)
