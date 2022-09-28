from .resource import Model, Collection


class Notification(Model):
    def __init__(self, uuid, client=None):
        self.uuid = uuid
        self.client = client

    async def get_websocket_channel(self):
        return await self.client.api.get_websocket_channel(self.uuid)

    def poll(self):
        return self.client.api.poll_channel(self.uuid)

class NotificationCollection(Collection):
    model = Notification
    
    def get(self, id) -> Notification:
        return Notification(id)
    
    def create(
        self,
    ) -> Notification:

        res = self.client.api.create_notification_channel()

        uuid = res["subscription_id"]

        return Notification(uuid, client=self.client)

    def delete(
        self,
        id: str,
        #testmode: bool = True,
    ):

        res = self.client.api.delete_notification_channel(id)
