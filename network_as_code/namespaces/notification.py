from typing import List
from uuid import UUID
from . import Namespace
from ..models import NotificationChannel


class Notifications(Namespace):
    async def get_channel(self, uuid: "UUID|str") -> NotificationChannel:
        """Creates a NotificationChannel instance based on the given UUID.

        Returns:
            A new NotificationChannel instance
        """
        _uuid = UUID(uuid) if isinstance(uuid, str) else uuid
        return NotificationChannel(api=self.api, uuid=_uuid)

    def list_channels(self) -> List[NotificationChannel]:
        """Fetch a list of available Notification channels from the API.

        Returns:
            A list of NotificationChannel instances
            or an empty list if no channels are available.
        """
        # TODO: Implement me!
        raise NotImplementedError

    async def new_channel(self) -> NotificationChannel:
        """Create a new Notification channel in the backend API.

        NOTE: For testing purposes only!

        Returns:
            A new NotificationChannel instance representing the new channel
        """
        data = await self.api.notifications.create_notification_channel()
        return NotificationChannel(api=self.api, uuid=data["subscription_id"])

    async def delete(self, uuid: "UUID|str"):
        """Delete (close) a remote notification channel."""
        return await self.api.notifications.delete_notification_channel(str(uuid))
