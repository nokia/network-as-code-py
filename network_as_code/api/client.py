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

from network_as_code.api.qod_api import QodAPI
from ..api.slice_api import AttachAPI, SliceAPI
from .location_api import LocationVerifyAPI, LocationRetrievalAPI
from .device_status_api import DeviceStatusAPI
from .congestion_api import CongestionAPI
from .sim_swap_api import SimSwapAPI
from .geofencing_api import GeofencingAPI
from .credentials_api import CredentialsAPI
from .authorization_api import AuthorizationAPI
from. number_verification_api import NumberVerificationAPI

QOS_BASE_URL_PROD = "https://quality-of-service-on-demand.p-eu.rapidapi.com"
QOS_RAPID_HOST_PROD = "quality-of-service-on-demand.nokia.rapidapi.com"
QOS_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/qod/v0"

LOCATION_VERIFY_BASE_URL_PROD = "https://location-verification.p-eu.rapidapi.com/v1"
LOCATION_VERIFY_RAPID_HOST_PROD = "location-verification.nokia.rapidapi.com"
LOCATION_VERIFY_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/location-verification/v1"

LOCATION_RETRIEVE_BASE_URL_PROD = "https://location-retrieval.p-eu.rapidapi.com"
LOCATION_RETRIEVE_RAPID_HOST_PROD = "location-retrieval.nokia.rapidapi.com"
LOCATION_RETRIEVE_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/location-retrieval/v0"

SLICE_BASE_URL_PROD = "https://network-slicing.p-eu.rapidapi.com"
SLICE_RAPID_HOST_PROD = "network-slicing.nokia.rapidapi.com"
SLICE_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/slice/v1"

SLICE_ATTACH_BASE_URL_PROD = "https://network-slice-device-attachment.p-eu.rapidapi.com"
SLICE_ATTACH_RAPID_HOST_PROD = "network-slice-device-attachment.nokia.rapidapi.com"
SLICE_ATTACH_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/device-attach/v0"

DEVICE_STATUS_BASE_URL_PROD = "https://device-status.p-eu.rapidapi.com"
DEVICE_STATUS_RAPID_HOST_PROD = "device-status.nokia.rapidapi.com"
DEVICE_STATUS_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/device-status/v0"

CONGESTION_BASE_URL_PROD = "https://congestion-insights.p-eu.rapidapi.com"
CONGESTION_RAPID_HOST_PROD = "congestion-insights.nokia.rapidapi.com"
CONGESTION_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/congestion-insights/v0"

SIM_SWAP_BASE_URL_PROD = "https://sim-swap.p-eu.rapidapi.com/sim-swap/sim-swap/v0"
SIM_SWAP_RAPID_HOST_PROD = "sim-swap.nokia.rapidapi.com"
SIM_SWAP_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0"

GEOFENCING_BASE_URL_PROD = "https://geofencing-subscriptions.p-eu.rapidapi.com/v0.3"
GEOFENCING_RAPID_HOST_PROD = "geofencing-subscription.nokia.rapidapi.com"
GEOFENCING_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/geofencing-subscriptions/v0.3"

CREDENTIALS_BASE_URL_PROD = "https://nac-authorization-server.p-eu.rapidapi.com"
CREDENTIALS_RAPID_HOST_PROD = "nac-authorization-server.nokia.rapidapi.com"
CREDENTIALS_BASE_URL_DEV = "https://nac-authorization-server.p-eu.rapidapi.com"

AUTHORIZATION_BASE_URL_PROD = "https://well-known-metadata.p-eu.rapidapi.com"
AUTHORIZATION_RAPID_HOST_PROD = "well-known-metadata.nokia.rapidapi.com"
AUTHORIZATION_BASE_URL_DEV = "https://well-known-metadata.p-eu.rapidapi.com"

NUMBER_VERIFICATION_BASE_URL_PROD = "https://number-verification.p-eu.rapidapi.com"
NUMBER_VERIFICATION_RAPID_HOST_PROD = "number-verification.nokia.rapidapi.com"
NUMBER_VERIFICATION_BASE_URL_DEV = "https://network-as-code1.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0"

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
        sim_swap_base_url: str = SIM_SWAP_BASE_URL_PROD,
        geofencing_base_url: str = GEOFENCING_BASE_URL_PROD,
        credentials_base_url: str = CREDENTIALS_BASE_URL_PROD,
        authorization_base_url: str = AUTHORIZATION_BASE_URL_PROD,
        number_verification_base_url: str = NUMBER_VERIFICATION_BASE_URL_PROD,
        dev_mode: bool = False,
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

        if dev_mode and sim_swap_base_url == SIM_SWAP_BASE_URL_PROD:
            sim_swap_base_url = SIM_SWAP_BASE_URL_DEV

        if dev_mode and geofencing_base_url == GEOFENCING_BASE_URL_PROD:
            geofencing_base_url = GEOFENCING_BASE_URL_DEV

        if dev_mode and credentials_base_url == CREDENTIALS_BASE_URL_PROD:
            credentials_base_url = CREDENTIALS_BASE_URL_DEV

        if dev_mode and authorization_base_url == AUTHORIZATION_BASE_URL_PROD:
            authorization_base_url = AUTHORIZATION_BASE_URL_DEV

        if dev_mode and number_verification_base_url == NUMBER_VERIFICATION_BASE_URL_PROD:
            number_verification_base_url = NUMBER_VERIFICATION_BASE_URL_DEV

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
                else device_status_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.location_verify = LocationVerifyAPI(
            base_url=location_verify_base_url,
            rapid_key=token,
            rapid_host=(
                location_verify_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else location_verify_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )
        self.location_retrieve = LocationRetrievalAPI(
            base_url=location_retrieve_base_url,
            rapid_key=token,
            rapid_host=(
                location_retrieve_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else location_retrieve_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
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
                else slice_attach_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.congestion = CongestionAPI(
            base_url=congestion_base_url,
            rapid_key=token,
            rapid_host=(
                congestion_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else congestion_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.sim_swap = SimSwapAPI(
            base_url=sim_swap_base_url,
            rapid_key=token,
            rapid_host=(
                sim_swap_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else sim_swap_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.geofencing = GeofencingAPI(
            base_url=geofencing_base_url,
            rapid_key=token,
            rapid_host=(
                geofencing_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else geofencing_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            )
        )

        self.credentials = CredentialsAPI(
            base_url = credentials_base_url,
            rapid_key = token,
            rapid_host=(
                credentials_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else credentials_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.authorization = AuthorizationAPI(
            base_url = authorization_base_url,
            rapid_key = token,
            rapid_host=(
                authorization_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else authorization_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )

        self.number_verification = NumberVerificationAPI(
            base_url = number_verification_base_url,
            rapid_key = token,
            rapid_host=(
                number_verification_base_url.replace("https://", "").replace("p-eu", "nokia")
                if not dev_mode
                else number_verification_base_url.replace("https://", "").replace("p-eu", "nokia-dev")
            ),
        )
