from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import APIClient


class Endpoint:
    """The base class for API endpoints which implement some subset of the API.

    This class ensures that the subclass will have an API Client.

    NOTE: If you need to re-implement the __init__ method in an
    Endpoint subclass remember to call `super().__init__(client=client)`.
    """

    def __init__(self, client: "APIClient") -> None:
        self.client = client
