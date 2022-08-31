from .resource import Model, Collection


class Subscription(Model):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.

    Args:
        id (str): External ID of the subscription. Follows email address conventions.
    """

    def __repr__(self) -> str:
        return (
            f"Subscription(attrs={repr(self.attrs)}, "
            f"client={repr(self.client)}, "
            f"collection={repr(self.collection)})"
        )

    @property
    def imsi(self):
        return self.attrs.get("imsi")

    @property
    def msisdn(self):
        return self.attrs.get("msisdn")

    def get_location(self) -> dict:
        """Get the last reported location of the subscriber.

        Returns:
            A `dict` containing various information about the latest reported location.
        """
        res = self.client.api.get_subscriber_location(self.id)
        return res.get("locationInfo")

    def get_bandwidth(self) -> str:
        """Get the bandwidth identifier for the subscriber.

        Returns:
            Currently active bandwidth configuration name.
        """
        res = self.client.api.get_subscriber_bandwidth(self.id)
        return res.get("bandwidth")

    def set_bandwidth(self, name: str) -> str:
        """Update the bandwidth identifier for the subscriber.

        Args:
            name (str): Desired bandwidth configuration name.

        Returns:
            Currently active bandwidth configuration name.
        """
        res = self.client.api.set_subscriber_bandwidth(self.id, name)
        return res.get("bandwidth")

    def get_custom_bandwidth(self):
        """Get the bandwidth (uplink and downlink) limits for the subscriber.

        Returns:
            A `tuple` of currently set custom upload and download limits.
        """
        res = self.client.api.get_subscriber_custom_bandwidth(self.id)
        return res.get("upload"), res.get("download")

    def set_custom_bandwidth(self, up: int, down: int):
        """Update the bandwidth (uplink and downlink) of the subscriber.

        Args:
            up (int): The new upload (uplink) limit.
            down (int): The new download (downlink) limit.

        Returns:
            A `tuple` of currently set custom upload and download limits.
        """
        res = self.client.api.set_subscriber_custom_bandwidth(self.id, up, down)
        return res.get("upload"), res.get("download")


class SubscriptionCollection(Collection):
    model = Subscription

    def get(self, id):
        """Get a subscription by its external ID.

        Args:
            id (str): External ID of the subscription.

        Returns:
            A :py:class:`Subscription` object.

        Raises:
            :py:class:`network_as_code.errors.NotFound`
                If the subscription does not exist.
            :py:class:`network_as_code.errors.APIError`
                If the server returns an error.
        """
        # TODO: Value checking here.
        res = self.client.api.get_subscription(id)
        return self.prepare_model(res)

    def list(self):
        # TODO: Implement me!
        raise NotImplementedError

    def create(
        self,
        id: str,
        imsi: str,
        msisdn: str,
        testmode: bool = True,
    ) -> Subscription:
        """Create a new subscription. A subscription is typically tied to a device.

        #### Note! At the moment it's only possible to create testmode subscriptions.

        Args:
            id (str): External ID of the subscription. Email-like.
            imsi (str): Phone-number like number with 14 to 16 digits.
            msisdn (str): Phone-number like number with 10 to 14 digits.
            testmode (bool): Whether to create a simulated or real subscription.

        Returns:
            A :py:class:`Subscription` object.

        Raises:
            :py:class:`network_as_code.errors.NotFound`
                If the subscription does not exist.
            :py:class:`network_/as_code.errors.APIError`
                If the server returns an error.
        """
        # TODO: Value checking here.
        res = self.client.api.create_subscription(id, imsi, msisdn)
        return self.prepare_model(res)
