from pydantic import BaseModel

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