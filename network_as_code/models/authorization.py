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
            fast_flow_csp_auth_endpoint (str): Faster authorization flow server endpoint. Used to build login URL.
    """
    authorization_endpoint: str
    token_endpoint: str
    fast_flow_csp_auth_endpoint: str