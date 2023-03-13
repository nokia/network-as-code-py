from typing import List
import websockets.client as ws
from . import Endpoint


class NotificationsAPI(Endpoint):
    """A client for handling Notification API calls"""

    def get_websocket_channel(self, uuid: str):
        """Open a notification channel over websocket"""
        base_dir_override = "ws://nwac.atg.dynamic.nsn-net.net/nwac/v4"
        return ws.connect(
            f"{base_dir_override}/notifier/notifications/ws/{uuid}",
            ping_timeout=None,
        )

    async def poll_channel(self, uuid: str) -> List[dict]:
        """Poll a notification channel and return list of all notifications in the queue"""
        res = await self.client.get(f"/notifier/notifications/poll/{uuid}")
        return self.client.result(res, json=True)

    async def create_notification_channel(self) -> dict:
        """Poll a notification channel and return list of all notifications in the queue"""
        res = await self.client.post(f"/notifier/callback-setup")
        return self.client.result(res, json=True)

    async def delete_notification_channel(self, uuid: str):
        """Poll a notification channel and return list of all notifications in the queue"""
        res = await self.client.delete(f"/notifier/callback-delete/{uuid}")
        return self.client.result(res, json=True)