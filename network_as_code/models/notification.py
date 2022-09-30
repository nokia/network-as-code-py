from .resource import Model, Collection


class Notification(Model):
    @property
    def uuid(self):
        return self.attrs["uuid"]

    async def get_websocket_channel(self):
        return await self.api.notifications.get_websocket_channel(self.uuid)

    async def poll(self):
        return await self.api.notifications.poll_channel(self.uuid)


class NotificationCollection(Collection):
    model = Notification

    def get(self, id: str) -> Notification:
        return self.prepare_model({"uuid": id})

    async def create(self) -> Notification:
        res = await self.api.notifications.create_notification_channel()
        uuid = res["subscription_id"]

        return self.prepare_model({"uuid": uuid})

    async def delete(self, id: str):  # testmode: bool = True
        return await self.api.notifications.delete_notification_channel(id)
