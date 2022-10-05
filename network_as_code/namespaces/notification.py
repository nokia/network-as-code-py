from typing import List
from .namespace import Namespace


class Notifications(Namespace):
    async def get_websocket_channel(self):
        return await self.api.notifications.get_websocket_channel(self.uuid)

    async def poll(self):
        return await self.api.notifications.poll_channel(self.uuid)

    def get(self, id: str) -> Notifications:
        return self.prepare_model({"uuid": id})

    def list(self) -> List[Notifications]:
        # TODO: Implement me!
        raise NotImplementedError

    async def create(self, attrs=None) -> Notifications:
        res = await self.api.notifications.create_notification_channel()
        uuid = res["subscription_id"]

        return self.prepare_model({"uuid": uuid})

    async def delete(self, id: str):  # testmode: bool = True
        return await self.api.notifications.delete_notification_channel(id)
