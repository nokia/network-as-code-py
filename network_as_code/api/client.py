# Copyright 2025 Nokia
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

from typing import Optional

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
from .call_forwarding_api import CallForwardingAPI

QOS_URL = "/qod/v0"

LOCATION_VERIFY_URL = "/location-verification/v1"

LOCATION_RETRIEVE_URL = "/location-retrieval/v0"

SLICE_URL= "/slice/v1"

SLICE_ATTACH_URL = "/device-attach/v0"

DEVICE_STATUS_URL = "/device-status/v0"

CONGESTION_URL = "/congestion-insights/v0"

SIM_SWAP_URL = "/passthrough/camara/v1/sim-swap/sim-swap/v0"

GEOFENCING_URL = "/geofencing-subscriptions/v0.3"

NUMBER_VERIFICATION_URL = "/passthrough/camara/v1/number-verification/number-verification/v0"

CREDENTIALS_URL = "/oauth2/v1"

AUTHORIZATION_URL = "/.well-known"

CALL_FORWARDING_URL = "/passthrough/camara/v1/call-forwarding-signal/call-forwarding-signal/v0.3"

# RAPID_HOST_PROD = "network-as-code.nokia.rapidapi.com"

def environment_hostname(env_mode):
    """Select the right hostname based on given environment"""
    if env_mode == "dev":
        return "network-as-code1.nokia-dev.rapidapi.com"

    if env_mode == "staging":
        return "network-as-code.nokia-stage.rapidapi.com"

    return "network-as-code.nokia.rapidapi.com"

def environment_base_url(env_mode):
    """Select the right API base URL based on given environment"""
    if env_mode == "dev":
        return "https://network-as-code1.p-eu.rapidapi.com"

    if env_mode == "staging":
        return "https://network-as-code.p-eu.rapidapi.com"

    return "https://network-as-code.p-eu.rapidapi.com"


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
        qos_base_url: Optional[str] = None,
        location_verify_base_url: Optional[str] = None,
        location_retrieve_base_url: Optional[str] = None,
        slice_base_url: Optional[str] = None,
        slice_attach_base_url: Optional[str] = None,
        device_status_base_url: Optional[str] = None,
        congestion_base_url: Optional[str] = None,
        sim_swap_base_url: Optional[str] = None,
        geofencing_base_url: Optional[str] = None,
        credentials_base_url: Optional[str] = None,
        authorization_base_url: Optional[str] = None,
        number_verification_base_url: Optional[str] = None,
        call_forwarding_base_url: Optional[str] = None,
        env_mode: Optional[str] = None,
    ):
        base_url = environment_base_url(env_mode)

        hostname = environment_hostname(env_mode)

        if not qos_base_url:
            qos_base_url = f"{base_url}{QOS_URL}"

        if not location_verify_base_url:
            location_verify_base_url = f"{base_url}{LOCATION_VERIFY_URL}"

        if not location_retrieve_base_url:
            location_retrieve_base_url = f"{base_url}{LOCATION_RETRIEVE_URL}"

        if not slice_base_url:
            slice_base_url = f"{base_url}{SLICE_URL}"

        if not slice_attach_base_url:
            slice_attach_base_url = f"{base_url}{SLICE_ATTACH_URL}"

        if not device_status_base_url:
            device_status_base_url = f"{base_url}{DEVICE_STATUS_URL}"

        if not congestion_base_url:
            congestion_base_url = f"{base_url}{CONGESTION_URL}"

        if not sim_swap_base_url:
            sim_swap_base_url = f"{base_url}{SIM_SWAP_URL}"

        if not geofencing_base_url:
            geofencing_base_url = f"{base_url}{GEOFENCING_URL}"

        if not number_verification_base_url:
            number_verification_base_url = f"{base_url}{NUMBER_VERIFICATION_URL}"

        if not credentials_base_url:
            credentials_base_url = f"{base_url}{CREDENTIALS_URL}"

        if not authorization_base_url:
            authorization_base_url = f"{base_url}{AUTHORIZATION_URL}"

        if not call_forwarding_base_url:
            call_forwarding_base_url = f"{base_url}{CALL_FORWARDING_URL}"

        self.sessions = QodAPI(
            base_url=qos_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.devicestatus = DeviceStatusAPI(
            base_url=device_status_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.location_verify = LocationVerifyAPI(
            base_url=location_verify_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )
        self.location_retrieve = LocationRetrievalAPI(
            base_url=location_retrieve_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.slicing = SliceAPI(
            base_url=slice_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.slice_attach = AttachAPI(
            base_url=slice_attach_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.congestion = CongestionAPI(
            base_url=congestion_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.sim_swap = SimSwapAPI(
            base_url=sim_swap_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.geofencing = GeofencingAPI(
            base_url=geofencing_base_url,
            rapid_key=token,
            rapid_host=hostname,
        )

        self.number_verification = NumberVerificationAPI(
            base_url = number_verification_base_url,
            rapid_key = token,
            rapid_host=hostname,
        )

        self.credentials = CredentialsAPI(
            base_url = credentials_base_url,
            rapid_key = token,
            rapid_host=hostname,
        )

        self.authorization = AuthorizationAPI(
            base_url = authorization_base_url,
            rapid_key = token,
            rapid_host=hostname,
        )

        self.call_forwarding = CallForwardingAPI(
            base_url = call_forwarding_base_url,
            rapid_key = token,
            rapid_host=hostname,
        )
