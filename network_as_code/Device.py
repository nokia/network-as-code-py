from dateutil.parser import parse
from .RequestHandler import RequestHandler
from .NetworkProfile import NetworkProfile
from .DeviceLocation import DeviceLocation


class Device:
    """Representation of a mobile device uniquely identified by an external id.

    This class is used to store information needed for making Network as Code API requests,
    as well as provide basic functionalities, such as device location queries.

    #### Example usage:
    ```python
    device = Device(
        id="string@registered.domain",
        sdk_token="eee0a4d0-2b54-4a7a-a61f-40ce753f44c6"
    )
    ```

    ###
    """

    def __init__(self, id: str, sdk_token: str) -> None:
        """Initializes a new Device.

        Args:
            id: ID that identifies a subscriber (device). See the [API docs](https://cns-apigee-test-6559-nacpoc.apigee.io/docs/nac/1/types/ExternalId) for more details.
            sdk_token: Authentication token for the Network as Code API.
        """
        self.id = id
        self.sdk_token = sdk_token

    def check_api_connection(self) -> bool:
        """Check whether the backend API is accessible and is able to process requests.

        Returns:
            `True`, if the backend API responds with status code 200, otherwise returns `False`.
        """
        res = RequestHandler.check_api_connection(self)
        return res == 200

    def location(self):
        """Get the location information of this device.

        Returns:
            `DeviceLocation` object
        """
        return DeviceLocation.get(self)

    def network_profile(self):
        """Get the network profile of this device.

        Returns:
            `DeviceLocation` object
        """
        return NetworkProfile.get(self)

    def apply(self, configuration) -> None:
        """Apply a configuration change to this device.

        Args:
            configuration: An network configuration object, such as a NetworkProfile.
        """
        configuration.apply(self)
