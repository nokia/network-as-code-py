from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import APIClient, AsyncAPIClient


class Endpoint:
    def __init__(self, client: "APIClient") -> None:
        self.client = client


class AsyncEndpoint:
    def __init__(self, client: "AsyncAPIClient") -> None:
        self.client = client
