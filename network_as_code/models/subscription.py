from typing import List
from .resource import Model, Collection


class Subscription(Model):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    @property
    def imsi(self):
        return self.attrs.get("imsi")

    @property
    def msisdn(self):
        return self.attrs.get("msisdn")

    async def get_location(self) -> dict:
        """Get the last reported location of the subscriber.

        Returns:
            A `dict` containing various information about the latest reported location.
        """
        res = await self.api.subscriptions.get_subscriber_location(self.id)
        return res.get("locationInfo")

    async def get_bandwidth(self) -> str:
        """Get the bandwidth identifier for the subscriber.

        Returns:
            Currently active bandwidth configuration name.
        """
        res = await self.api.subscriptions.get_subscriber_bandwidth(self.id)
        return res.get("serviceTier")

    async def set_bandwidth(self, name: str) -> str:
        """Update the bandwidth identifier for the subscriber.

        Args:
            name (str): Desired bandwidth configuration name.

        Returns:
            Currently active bandwidth configuration name.
        """
        res = await self.api.subscriptions.set_subscriber_bandwidth(self.id, name)
        return res.get("serviceTier")

    async def get_custom_bandwidth(self):
        """Get the bandwidth (uplink and downlink) limits for the subscriber.

        Returns:
            A `tuple` of currently set custom upload and download limits.
        """
        res = await self.api.subscriptions.get_subscriber_custom_bandwidth(self.id)
        return res.get("upload"), res.get("download")

    async def set_custom_bandwidth(self, up: int, down: int):
        """Update the bandwidth (uplink and downlink) of the subscriber.

        Args:
            up (int): The new upload (uplink) limit.
            down (int): The new download (downlink) limit.

        Returns:
            A `tuple` of currently set custom upload and download limits.
        """
        res = await self.api.subscriptions.set_subscriber_custom_bandwidth(
            self.id, up, down
        )
        return res.get("upload"), res.get("download")


class SubscriptionCollection(Collection):
    model = Subscription

    async def get(self, id) -> Subscription:
        """Get a subscription by its external ID.

        Args:
            id (str): External ID of the subscription.

        Returns:
            A :py:class:`Subscription` object.
        """
        # TODO: Value checking here.
        res = await self.api.subscriptions.get_subscription(id)
        return self.prepare_model(res)

    async def list(self) -> List[Subscription]:
        # TODO: Implement me!
        raise NotImplementedError

    async def create(
        self,
        id: str,
        imsi: str,
        msisdn: str,
        testmode: bool = True,
    ) -> Subscription:
        """Create a new subscription. A subscription is typically tied to a mobile device.

        **Note!** At the moment it's only possible to create testmode subscriptions.

        Args:
            id (str): External ID of the subscription. Email-like.
            imsi (str): Phone-number like number with 14 to 16 digits.
            msisdn (str): Phone-number like number with 10 to 14 digits.
            testmode (bool): Whether to create a simulated or real subscription.

        Returns:
            A :py:class:`Subscription` object.
        """
        # TODO: Value checking here.
        res = await self.api.subscriptions.create_subscription(id, imsi, msisdn)
        return self.prepare_model(res)

    async def delete(self, id: str, testmode: bool = True) -> bool:
        """Delete a subscription. A subscription is typically tied to a device.

        #### Note! Only test-mode subscriptions can be deleted!

        Args:
            id (str): External ID of the subscription. Email-like.
            testmode (bool): Whether to create a simulated or real subscription.
        """
        # TODO: Value checking here.
        return await self.api.subscriptions.delete_subscription(id)
