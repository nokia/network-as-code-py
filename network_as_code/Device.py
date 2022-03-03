from .RequestHandler import RequestHandler


class Device:
    """Representation of a mobile device uniquely identified by an external id.

    This class is used to store information needed for making Network as Code API requests,
    as well as provide basic functionalities, such as device location queries.

    #### Example usage:
    ```python
    device = Device(
        ext_id="string@registered.domain",
        sdk_token="eee0a4d0-2b54-4a7a-a61f-40ce753f44c6"
    )
    ```
    """

    def __init__(self, ext_id: str, sdk_token: str) -> None:
        """Initializes a new Device.

        Args:
            ext_id: External ID that identifies a mobile device. See https://cns-apigee-test-6559-nacpoc.apigee.io/docs/nac/1/types/ExternalId for more details.
            sdk_token: Authentication token for the Network as Code API.
        """
        self.ext_id = ext_id
        self.sdk_token = sdk_token

    def check_api_connection(self) -> bool:
        """
        Checks whether the configured Network as Code API is accessible and is able to process requests.

        Returns:
            `True` when the Network as Code API is accessible and responds, otherwise returns `False`.
        """
        status = RequestHandler.instance.check_api_connection(self)
        return status == 200

    def location(self) -> dict:
        """
        Gets the location of the device from the Network as Code API.

        Returns:
            Dictionary containing keys: `latitude`, `longitude`, `altitude` of the device and `timestamp` of the request.
        """
        res = RequestHandler.instance.get_location(self)
        if res.status_code == 200:
            # location = res.json()
            # return location["longitude"], location["latitude"]
            return res.json()
        return {}
