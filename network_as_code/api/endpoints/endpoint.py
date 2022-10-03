from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import APIClient


class Endpoint:
    def __init__(self, client: "APIClient") -> None:
        self.client = client
