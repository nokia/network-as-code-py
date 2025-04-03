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

from typing import Optional, Union
from urllib.parse import urlencode

from . import Namespace
from ..models.number_verification import Credentials, Endpoints

class Authorization(Namespace):
    """Gain essential components for authentication methods"""

    def credentials(self) -> Credentials:
        """Get client credentials

        #### Returns:
             Credentials object"""
        response = self.api.credentials.fetch_credentials()
        body = response
        client_id = body["client_id"]
        client_secret = body["client_secret"]

        credentials = Credentials(
            client_id=client_id,
            client_secret=client_secret
        )
        return credentials

    def auth_endpoints(self) -> Endpoints:
        """Get authorization endpoints

        #### Returns:
             Endpoints object"""
        response = self.api.authorization.fetch_endpoints()
        body = response
        authorization_endpoint = body["authorization_endpoint"]
        token_endpoint = body["token_endpoint"]

        authorization_endpoints = Endpoints(
            authorization_endpoint=authorization_endpoint,
            token_endpoint=token_endpoint
        )
        return authorization_endpoints

    def create_authentication_link(self,
                            redirect_uri: str,
                            scope: str,
                            login_hint: Union[str, None],
                            state: Optional[str] = None,
                            )-> str:
        """Create authentication link for user

        #### Args:
             redirect_uri (str):  redirection URI where the auth code is to be sent
             scope (str): service the application is requesting access to
             login_hint (str): hint about the login identifier to the authorization endpoint
             state (Optional[str]): value used to maintain state between request and callback
        #### Returns:
             authentication URL"""

        credentials = self.credentials()
        auth_endpoint = self.auth_endpoints()
        response_type = "code"
        params = {
            "scope": scope,
            "state": state,
            "response_type": response_type,
            "client_id": credentials.client_id,
            "redirect_uri": redirect_uri,
            "login_hint": login_hint
        }
        params = {k: v for k, v in params.items() if v is not None}
        auth_url = f'{auth_endpoint.authorization_endpoint}?{urlencode(params)}'
        return auth_url