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

import sys
from ..api.slice_api import AttachAPI, SliceAPI
from network_as_code.api.qod_api import QodAPI
from .location_api import LocationVerifyAPI, LocationRetrievalAPI
from .device_status_api import DeviceStatusAPI
from .congestion_api import CongestionAPI

QOS_BASE_URL_PROD = "https://quality-of-service-on-demand.p-eu.rapidapi.com"
QOS_RAPID_HOST_PROD = "quality-of-service-on-demand.nokia.rapidapi.com"
QOS_BASE_URL_DEV = "https://qos-on-demand2.p-eu.rapidapi.com"

LOCATION_VERIFY_BASE_URL_PROD = "https://location-verification.p-eu.rapidapi.com"
LOCATION_VERIFY_RAPID_HOST_PROD = "location-verification.nokia.rapidapi.com"
LOCATION_VERIFY_BASE_URL_DEV = "https://location-verification5.p-eu.rapidapi.com"

LOCATION_RETRIEVE_BASE_URL_PROD = "https://location-retrieval.p-eu.rapidapi.com"
LOCATION_RETRIEVE_RAPID_HOST_PROD = "location-retrieval.nokia.rapidapi.com"
LOCATION_RETRIEVE_BASE_URL_DEV = "https://location-retrieval3.p-eu.rapidapi.com"

SLICE_BASE_URL_PROD = "https://network-slicing.p-eu.rapidapi.com"
SLICE_RAPID_HOST_PROD = "network-slicing.nokia.rapidapi.com"
SLICE_BASE_URL_DEV = "https://network-slicing2.p-eu.rapidapi.com"

SLICE_ATTACH_BASE_URL_PROD = "https://device-application-attach.p-eu.rapidapi.com"
SLICE_ATTACH_RAPID_HOST_PROD = "device-application-attach.nokia.rapidapi.com"
SLICE_ATTACH_BASE_URL_DEV = "https://device-application-attach.p-eu.rapidapi.com"

DEVICE_STATUS_BASE_URL_PROD = "https://device-status.p-eu.rapidapi.com"
DEVICE_STATUS_RAPID_HOST_PROD = "device-status.nokia.rapidapi.com"
DEVICE_STATUS_BASE_URL_DEV = "https://device-status1.p-eu.rapidapi.com"

CONGESTION_BASE_URL_PROD = "https://congestion-insights.p-eu.rapidapi.com"
CONGESTION_RAPID_HOST_PROD = "congestion-insights.nokia.rapidapi.com"
CONGESTION_BASE_URL_DEV = "https://congestion-insights.p-eu.rapidapi.com"


class APIClient:
    """A client for communicating with Network as Code APIs.

    ### Args:
        token (str): Authentication token for the Network as Code API.
        base_url (str): Base URL for the Network as Code API.
        testmode (bool): Whether to use simulated or real resources.
    """

    def __init__(
        self,
        token: str,
        qos_base_url: str = QOS_BASE_URL_PROD,
        location_verify_base_url: str = LOCATION_VERIFY_BASE_URL_PROD,
        location_retrieve_base_url: str = LOCATION_RETRIEVE_BASE_URL_PROD,
        slice_base_url: str = SLICE_BASE_URL_PROD,
        slice_attach_base_url: str = SLICE_ATTACH_BASE_URL_PROD,
        device_status_base_url: str = DEVICE_STATUS_BASE_URL_PROD,
        congestion_base_url: str = CONGESTION_BASE_URL_PROD,
        dev_mode: bool = False,
        **kwargs,
    ):
        if dev_mode and qos_base_url == QOS_BASE_URL_PROD:
            qos_base_url = QOS_BASE_URL_DEV

        if dev_mode and location_verify_base_url == LOCATION_VERIFY_BASE_URL_PROD:
            location_verify_base_url = LOCATION_VERIFY_BASE_URL_DEV

        if dev_mode and location_retrieve_base_url == LOCATION_RETRIEVE_BASE_URL_PROD:
            location_retrieve_base_url = LOCATION_RETRIEVE_BASE_URL_DEV

        if dev_mode and slice_base_url == SLICE_BASE_URL_PROD:
            slice_base_url = SLICE_BASE_URL_DEV

        if dev_mode and slice_attach_base_url == SLICE_ATTACH_BASE_URL_PROD:
            slice_attach_base_url = SLICE_ATTACH_BASE_URL_DEV

        if dev_mode and device_status_base_url == DEVICE_STATUS_BASE_URL_PROD:
            device_status_base_url = DEVICE_STATUS_BASE_URL_DEV

        if dev_mode and congestion_base_url == CONGESTION_BASE_URL_PROD:
            congestion_base_url = CONGESTION_BASE_URL_DEV

        self.sessions = QodAPI(
            base_url=qos_base_url,
            rapid_key=token,
            rapid_host=(
                qos_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else qos_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.devicestatus = DeviceStatusAPI(
            base_url=device_status_base_url,
            rapid_key=token,
            rapid_host=(
                device_status_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else device_status_base_url.replace("https://", "").replace(
                    "p-eu", "nokia-dev"
                )
            ),
        )

        self.location_verify = LocationVerifyAPI(
            base_url=location_verify_base_url,
            rapid_key=token,
            rapid_host=(
                location_verify_base_url.replace("https://", "").replace(
                    "p-eu", "nokia"
                )
                if not dev_mode
                else location_verify_base_url.replace("https://", "").replace(
                    "p-eu", "nokia-dev"
                )
            ),
        )
        self.location_retrieve = LocationRetrievalAPI(
            base_url=location_retrieve_base_url,
            rapid_key=token,
            rapid_host=(
                location_retrieve_base_url.replace("https://", "").replace(
                    "p-eu", "nokia"
                )
                if not dev_mode
                else location_retrieve_base_url.replace("https://", "").replace(
                    "p-eu", "nokia-dev"
                )
            ),
        )

        self.slicing = SliceAPI(
            base_url=slice_base_url,
            rapid_key=token,
            rapid_host=(
                slice_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else slice_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.slice_attach = AttachAPI(
            base_url=slice_attach_base_url,
            rapid_key=token,
            rapid_host=(
                slice_attach_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else slice_attach_base_url.replace("https://", "").replace(
                    "p-eu", "nokia-dev"
                )
            ),
        )

        self.congestion = CongestionAPI(
            base_url=congestion_base_url,
            rapid_key=token,
            rapid_host=(
                congestion_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else congestion_base_url.replace("https://", "").replace(
                    "p-eu", "nokia-dev"
                )
            ),
        )
