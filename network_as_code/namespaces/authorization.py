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

from urllib.parse import urlencode
from . import Namespace
from ..models.authorization import Credentials, Endpoints

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
        fast_flow_csp_auth_endpoint = body["fast_flow_csp_auth_endpoint"]

        authorization_endpoints = Endpoints(
            authorization_endpoint=authorization_endpoint,
            token_endpoint=token_endpoint,
            fast_flow_csp_auth_endpoint=fast_flow_csp_auth_endpoint
        )
        return authorization_endpoints

    def create_authorization_link(self,
                            redirect_uri: str,
                            scope: str,
                            login_hint: str,
                            state: str,
                            )-> str:
        """Create authorization link for user

        #### Args:
             redirect_uri (str): Redirection URI where the auth code and state is to be sent.
             scope (str): Service the application is requesting access to.
             login_hint (str): Hint about the login identifier to the authorization endpoint.
             state (str): Value used to store request-specific data and maintain state between request and callback.
        #### Returns:
             authorization URL"""

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
        auth_url = f'{auth_endpoint.fast_flow_csp_auth_endpoint}?{urlencode(params)}'
        return auth_url