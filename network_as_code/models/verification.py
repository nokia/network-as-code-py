from pydantic import BaseModel
from ..api.utils import tokenizer

class Credentials(BaseModel):
    """
    A class representing the `Credentials` model.

    #### Public Attributes:
            client_id (str): Refers to the client which will make the token request.
            client_secret (str): Used for fetching Access Token. Must be kept confidential.
    """
    client_id: str
    client_secret: str

class Endpoints(BaseModel):
    """
    A class representing the `Endpoints` model.

    #### Public Attributes:
            authorization_endpoint (str): The Authorization Server endpoint. Used to build login URL.
            token_endpoint (str): The Authorization Server endpoint. Used for fetching Access Token.
    """
    authorization_endpoint: str
    token_endpoint: str

class AccessToken(BaseModel):
    """
    A class representing the `AccessToken` model.

    #### Public Attributes:
            access_token (str): String representation of the access token.
            token_type (str): Authentication scheme.
            expires_in (str): The lifetime of access token
    """
    access_token: str
    token_type: str
    expires_in: int

    @staticmethod
    def create(api, code: str) -> "AccessToken":
        """Get Access Token for number verification API

        #### Args:
             code (str): Changes the code for Access Token from Authorization Servers token_endpoint
        #### Returns
             AccessToken object containing access token, token type and expiration time
        """
        grant_type = "authorization_code"
        credentials = api.credentials.fetch_credentials()
        token_endpoint = api.authorization.fetch_endpoints().get(
            "token_endpoint"
        )
        data = {
            "client_id": credentials['client_id'],
            "client_secret": credentials['client_secret'],
            "grant_type": grant_type,
            "code": code,
        }
        response = tokenizer(token_endpoint, data=data)
        body = response.json()
        access_token = body["access_token"]
        token_type = body["token_type"]
        expires_in = body["expires_in"]

        return AccessToken(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in
        )