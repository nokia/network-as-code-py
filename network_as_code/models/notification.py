from .resource import Model, Collection


class Notification(Model):
    def __init__(self, uuid, api=None):
        self.uuid = uuid
        self.api = api

    async def get_websocket_channel(self):
        return await self.api.notifications.get_websocket_channel(self.uuid)

    def poll(self):
        return self.api.notifications.poll_channel(self.uuid)

class NotificationCollection(Collection):
    model = Notification
    
    def get(self, id) -> Notification:
        return Notification(id)
    
    def create(
        self,
    ) -> Notification:

        res = self.api.notifications.create_notification_channel()

        uuid = res["subscription_id"]

        return Notification(uuid, api=self.api)

    def delete(
        self,
        id: str,
        #testmode: bool = True,
    ):

        res = self.api.notifications.delete_notification_channel(id)
