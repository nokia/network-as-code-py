class NaCError(Exception):
    """Network as Code base exception."""

    # This class can define common processing functionality
    # for the exceptions of this library.
    # E.g. https://docs.python-requests.org/en/master/_modules/requests/exceptions/


class ApiError(NaCError):
    """Network as Code API error."""


class GatewayConnectionError(NaCError):
    """Error for when a connection to the SDK gateway can't be established."""
