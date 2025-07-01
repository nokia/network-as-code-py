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

QOS_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/qod/v0"

LOCATION_VERIFY_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/location-verification/v1"

LOCATION_RETRIEVE_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/location-retrieval/v0"

SLICE_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/slice/v1"

SLICE_ATTACH_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/device-attach/v0"

DEVICE_STATUS_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/device-status/v0"

CONGESTION_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/congestion-insights/v0"

SIM_SWAP_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0"

GEOFENCING_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3"

NUMBER_VERIFICATION_BASE_URL_PROD = (
    "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/number-verification/number-verification/v0"
    )

CREDENTIALS_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/oauth2/v1"

AUTHORIZATION_BASE_URL_PROD = "https://network-as-code.p-eu.rapidapi.com/.well-known"

RAPID_HOST_PROD = "network-as-code.nokia.rapidapi.com"

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
        rapid_host_prod: str = RAPID_HOST_PROD,
        dev_mode: bool = False,
    ):
        if dev_mode and qos_base_url == QOS_BASE_URL_PROD:
            qos_base_url = qos_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and location_verify_base_url == LOCATION_VERIFY_BASE_URL_PROD:
            location_verify_base_url = location_verify_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and location_retrieve_base_url == LOCATION_RETRIEVE_BASE_URL_PROD:
            location_retrieve_base_url = location_retrieve_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and slice_base_url == SLICE_BASE_URL_PROD:
            slice_base_url = slice_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and slice_attach_base_url == SLICE_ATTACH_BASE_URL_PROD:
            slice_attach_base_url = slice_attach_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and device_status_base_url == DEVICE_STATUS_BASE_URL_PROD:
            device_status_base_url = device_status_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and congestion_base_url == CONGESTION_BASE_URL_PROD:
            congestion_base_url = congestion_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and sim_swap_base_url == SIM_SWAP_BASE_URL_PROD:
            sim_swap_base_url = sim_swap_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and geofencing_base_url == GEOFENCING_BASE_URL_PROD:
            geofencing_base_url = geofencing_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and number_verification_base_url == NUMBER_VERIFICATION_BASE_URL_PROD:
            number_verification_base_url = number_verification_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and credentials_base_url == CREDENTIALS_BASE_URL_PROD:
            credentials_base_url = credentials_base_url.replace(".p-eu", "1.p-eu")

        if dev_mode and authorization_base_url == AUTHORIZATION_BASE_URL_PROD:
            authorization_base_url = authorization_base_url.replace(".p-eu", "1.p-eu")

        self.sessions = QodAPI(
            base_url=qos_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.devicestatus = DeviceStatusAPI(
            base_url=device_status_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.location_verify = LocationVerifyAPI(
            base_url=location_verify_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )
        self.location_retrieve = LocationRetrievalAPI(
            base_url=location_retrieve_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.slicing = SliceAPI(
            base_url=slice_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.slice_attach = AttachAPI(
            base_url=slice_attach_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.congestion = CongestionAPI(
            base_url=congestion_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.sim_swap = SimSwapAPI(
            base_url=sim_swap_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.geofencing = GeofencingAPI(
            base_url=geofencing_base_url,
            rapid_key=token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            )
        )

        self.number_verification = NumberVerificationAPI(
            base_url = number_verification_base_url,
            rapid_key = token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.credentials = CredentialsAPI(
            base_url = credentials_base_url,
            rapid_key = token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )

        self.authorization = AuthorizationAPI(
            base_url = authorization_base_url,
            rapid_key = token,
            rapid_host=(
                rapid_host_prod
                if not dev_mode
                else rapid_host_prod.replace(".nokia", "1.nokia-dev")
            ),
        )
