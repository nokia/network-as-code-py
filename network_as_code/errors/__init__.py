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

import httpx


class NaCError(Exception):
    """Network as Code base exception."""

    # This class can define common processing functionality
    # for the exceptions of this library.
    # E.g. https://docs.python-requests.org/en/master/_modules/requests/exceptions/


class APIError(NaCError):
    """Error for when the Network as Code API returns an error message."""


class GatewayConnectionError(NaCError):
    """Error for when a connection to the SDK gateway can't be established."""


class NotFound(NaCError):
    """Error for when a resource can't be found from the Network as Code API."""


class APIConnectionError(NaCError):
    """Error for when the Network as Code API cannot be reached."""


class AuthenticationException(NaCError):
    """Error for when the API key is invalid, the user of the key is not subscribed to the API, 
    or the API key was not supplied. (403)"""


class ServiceError(NaCError):
    """Error for when the server returns an error when responding to the request. (5XX)"""


class InvalidParameter(NaCError):
    """Error for when the user input parameters are invalid"""


def parse_response(response):
    if "application/json" in response.headers.get("Content-Type", ""):
        try:
            response_body = response.json()
        except ValueError:
            response_body = "Invalid JSON response"
    else:
        response_body = response.text
    return response_body

def error_handler(response):
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        trace_info = f"Status Code: {e.response.status_code}, Response Body: {parse_response(response)}"

        if e.response.status_code == 404:
            raise NotFound(trace_info) from e
        elif e.response.status_code in (403, 401):
            raise AuthenticationException(trace_info) from e
        elif e.response.status_code >= 400 and e.response.status_code < 500:
            raise APIError(trace_info) from e
        elif e.response.status_code >= 500:
            raise ServiceError(trace_info) from e
