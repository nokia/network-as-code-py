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
