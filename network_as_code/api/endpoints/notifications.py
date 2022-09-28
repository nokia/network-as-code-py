
import websockets

from .endpoint import AsyncEndpoint

class NotificationsAPI(AsyncEndpoint):
    """A client for handling Notification API calls"""

    async def get_websocket_channel(self, uuid: str) -> websockets.WebSocketClientProtocol:
        """Open a notification channel over websocket"""

        base_dir_override = "ws://nwac.atg.dynamic.nsn-net.net/nwac/v4"

        return await websockets.connect(f"{base_dir_override}/notifier/notifications/ws/{uuid}", ping_timeout=None)

    def poll_channel(self, uuid: str):
        """Poll a notification channel and return list of all notifications in the queue"""
        res: Response = self.request("GET", f"/notifier/notifications/poll/{uuid}")

        return self._result(res, json=True)

    def create_notification_channel(self):
        """Poll a notification channel and return list of all notifications in the queue"""
        res: Response = self.request("POST", f"/notifier/callback-setup")

        return self._result(res, json=True)

    def delete_notification_channel(self, uuid: str):
        """Poll a notification channel and return list of all notifications in the queue"""
        res: Response = self.request("DELETE", f"/notifier/callback-delete/{uuid}")

        return self._result(res, json=True)
