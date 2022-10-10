from typing import List
from uuid import UUID
from pydantic import BaseModel, PrivateAttr
from ..api import APIClient


class Notification(BaseModel):
    pass
    # TODO: What are the fields of a Notification object?


class NotificationChannel(BaseModel):
    _api: APIClient = PrivateAttr()
    uuid: UUID

    @property
    def _uuid(self):
        """A string representation of the channel's UUID"""
        return str(self.uuid)

    @property
    def websocket(self):
        """Opens a websocket connection to the remote notification channel

        Example: TODO: Finish this example...
        ```python
        async with channel.websocket as sock:
            sock.recv()
        ```
        """
        # TODO: Is returning a websocket too low-level? Can we abstract it?
        return self._api.notifications.get_websocket_channel(self._uuid)

    async def poll(self) -> List[Notification]:
        """Retrieve a list of all notifications that are currently in this channel's queue

        Returns:
            A list of `Notification` objects or an empty list if no new notifications
        """
        data = await self._api.notifications.poll_channel(self._uuid)
        return [Notification(**d) for d in data]

    async def close(self) -> None:
        """Closes the remote channel.

        No new messages can be read from this channel after this operation.
        """
        await self._api.notifications.delete_notification_channel(self._uuid)
