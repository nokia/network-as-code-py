from abc import ABC
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from network_as_code.api import APIClient


class Namespace(ABC):
    """A base class for representing a single resource instance."""

    def __init__(self, api: "APIClient"):
        # An APIClient object which provides access to the Network as Code API.
        self.api = api
